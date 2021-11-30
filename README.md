# 2048-Game Ather2021
2048 is a popular single player sliding tile puzzle video game. This is an implementation of the game in Python.

General Plan/Flow Chart:

  Initialize ---------> Take input from     ----------> Merge tiles 
    Grid                the user for the                    |
                        direction to merge                  |
                        tiles                               |
                              ^                             |
                              |          No                 |         Yes
                              +------------------------ Game over? --------> Print Result 
