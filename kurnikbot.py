#!/usr/bin/env python

## This is a chess playing bot for kurnik site
## It uses pystockfish module to handle communication with
## powerful open-source Stockfish engine
## Requires following additional Python modules (can be installed via pip):
## - pyperclip (for clipboard handling)
## - pgn (for pgn parsing)
## - chess (for game state representation)
## - pymouse (for mouse events)
## - pykeyboard (for keyboard events)
## You need stockfish accessible via 'stockfish' from shell:
## michal3141@ubuntu:~/python/bot$ stockfish 
## Stockfish 270915 by Tord Romstad, Marco Costalba and Joona Kiiski

import sys
import time
import pyperclip
import pgn
from chess import Bitboard
from pymouse import PyMouse
from pykeyboard import PyKeyboard, PyKeyboardEvent
from pystockfish import Engine

class Player(object):
    WHITE = 0
    BLACK = 1

# Set here whatever kurnik login you are using
me = sys.argv[1]

# Stockfish engine itself
stock = Engine()

# Mouse and Keyboard
m = PyMouse()
k = PyKeyboard()

# Sleep time when moving (between mouse clicks)
SLEEP_TIME_MOVING = 0.1

# Sleep time to get focus on PGN window (when copying)
SLEEP_TIME_PGN = 0.2

# Constants representing board position and size (see docs for details)
# You can customize it to adjust to your game window position and size
XSTART = 280
YSTART = 180
DX = DY = 70

# Numbers from 1 to 9
DIGITS = [str(x) for x in range(1, 10)]

# Click on particular square sq with mouse
def _move(sq, side):
    row = sq[0]
    col = sq[1]
    if side == Player.WHITE:
        i = ord(row) - ord('a')
        j = 8 - int(col)
    elif side == Player.BLACK:
        i = 7 + ord('a') - ord(row) 
        j = int(col) - 1
    m.click(XSTART + i*DX, YSTART + j*DY)

# Click PGN button to get pgn
def _click_pgn():
    m.click(907, 515)
    time.sleep(SLEEP_TIME_PGN)
    m.click(907, 515)

# Click randomly :) to get outside PGN popup
def _click_outside_pgn():
    m.click(XSTART, YSTART)

# Copy content of PGN popup to clipboard (for game state)
def _copy_to_clipboard():
    k.press_key('Control_L')
    k.press_key('a')
    k.press_key('c')
    k.release_key('Control_L')
    k.release_key('a')
    k.release_key('c')

# Getting current game situation
def get_pgn():
    _click_pgn()
    _copy_to_clipboard()
    _click_outside_pgn() 
    return pyperclip.paste()

# Make move
def make_move(move, side):
    sq1 = move[0:2]
    sq2 = move[2:4]
    print 'Executing move: %s -> %s' % (sq1, sq2)
    _move(sq1, side)
    time.sleep(SLEEP_TIME_MOVING)
    _move(sq2, side)

# Listening to keyboard events
class ClickKeyEventListener(PyKeyboardEvent):
    def tap(self, keycode, character, press):
        # If 'n' is pressed then next move is played by allmighty SF
        if character == 'n' and press:
            print '---------------------------'
            try:
                pgn_text = get_pgn()
                game = pgn.loads(pgn_text)[0]
                if game.white == me: side = Player.WHITE
                else: side = Player.BLACK 
            except:
                print 'Issue with PGN:', pgn_text
                return

            print 'Moves: ', game.moves

            board = Bitboard()
            for move in game.moves:
                if move != '*':
                    board.push_san(move)

            fen_pos = board.fen()
            print 'FEN: ', fen_pos

            ## Set fen position to stockfish, find the best move

            stock.setposition_fen(fen_pos)
            move_dict = stock.bestmove()
            print 'move_dict: ', move_dict

            move = move_dict['move']

            ## Try to play the best move
            try:
                make_move(move, side)
            except:
                print 'Problem playing move!'

        # By pressing number from 1-9 you can set how long SF could possibly
        # think on a particular move (in seconds)
        elif character in DIGITS and press:
            print 'pressed: ', character
            stock.movetime = int(character) * 1000

def main():
    key_listener = ClickKeyEventListener()
    key_listener.start()
    while True:
        time.sleep(100)

if __name__ == '__main__':
    main()