2048-Game Ather2021

2048 is a popular single player sliding tile puzzle video game. This is an implementation of the game in Python.

General Plan/Flow Chart:

  Initialize ---------> Take input from     ----------> Merge tiles and randomly
    Grid                the user for the                fill an empty tile with
                        direction to merge              a value of 2 or 4.
                        tiles                                 |
                              ^                               |
                              |             No                v         Yes
                              +-------------------------- Game over? ---------> Print Result

- The game can be extended for 8x8 grid by changing the GRID_SIZE variable in the Grid class.
- Similarly, WIN_SCORE can be changed to 4096 to make the winning number as 4096 instead of 2048. 
