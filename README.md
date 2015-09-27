# kurnikbot
Chess playing bot for http://www.kurnik.pl/szachy/ using Stockfish engine written in Python 2.
Created and tested for Linux/Ubuntu.

This is a chess playing bot for kurnik site. It is not meant for faint-hearted.
You probably need to modify code to adjust it to your setup (screen resolution, 
playing window position, connection lags and jitter...).
It uses pystockfish module to handle communication with
powerful open-source Stockfish engine
Requires following additional Python modules (can be installed via pip):
- pyperclip (for clipboard handling)
- pgn (for pgn parsing)
- chess (for game state representation)
- pymouse (for mouse events)
- pykeyboard (for keyboard events)

You need stockfish accessible via 'stockfish' command from shell:

    michal3141@ubuntu:~/python/bot$ stockfish 
    Stockfish 270915 by Tord Romstad, Marco Costalba and Joona Kiiski

Usage:

    ./kurnikbot.py <your_nickname_on_kurnik>
    
Bot works by clicking on PGN button to get pgn listing of the game.
Then copying PGN to clipboard and interpreting it to get FEN from the current board position.
The position where to click is hardcoded (also for executing mouse clicks when moving pieces...)
This means that you need to do some adjustments in code (e.g. positions).
If your internet connection is as laggy as mine then you probably need to modify some sleep constants to make it work.

My kurnik setup when using this bot (note that PGN button has to be there. Also coordinates has to be adjusted in code):

![](https://github.com/michal3141/kurnikbot/blob/master/images/bot_description.png)
