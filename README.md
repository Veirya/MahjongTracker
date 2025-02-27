App made to help me track starting and ending hands for Riichi Mahjong so I can find out if I really was unlucky or if I could have played better. Made for Python 3.12 with Tkinter for graphics. Run mahjongtracker.py from the root of the repository.

v0.5 Supports loading/reloading hands from a JSON, saving to JSON, and adding new hand information. These hands are displayed in the window, but a lot of the readibility/labelling is missing, not all info is displayed, and horizontal scrolling isn't implemented at all.

Hand input follows the MPSZ format. Spaces can be used to separate calls and drawn tile from the rest of the hand. 'b1' is used for unrevealed tiles. Order is preserved, that is, no 
**_Input fields:_**
**Final Hand:** Hand you had at the end of the round.
**Dealt Hand:** Hand you were dealt at the beginning of the round.
**Revealed Dora:** Dora revealed by the end of the round.
**Accepts/Waits:** Tiles you were looking for to complete or advance your hand at the end of the round.
**Shanten:** Shanten of the hand at the end of the round.
**Yaku:** Yaku the targeted hand would have been worth.
**Won?:** Did you win the round?
**Furiten?:** Where you in furiten?
**Ron/Tsumo?:** (If you won) Was the winning call Ron or Tsumo? (Free-text field)
**Where?:** Where was the tile(s) you were looking for? (Wall, Dead Wall, Other \[Player's hand\])
**# Left:** # of tiles left in the wall.
