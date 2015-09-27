# kurnikbot
Chess playing bot for http://www.kurnik.pl/szachy/ using Stockfish engine written in Python 2.
Created and tested for Linux/Ubuntu.

This is a chess playing bot for kurnik site
It uses pystockfish module to handle communication with
powerful open-source Stockfish engine
Requires following additional Python modules (can be installed via pip):
- pyperclip (for clipboard handling)
- pgn (for pgn parsing)
- chess (for game state representation)
- pymouse (for mouse events)
- pykeyboard (for keyboard events)
You need stockfish accessible via 'stockfish' from shell:
  michal3141@ubuntu:~/python/bot$ stockfish 
  Stockfish 270915 by Tord Romstad, Marco Costalba and Joona Kiiski
