# tictactoe

Experimenting with the 
[MENACE](https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine)
algorithm.


## Install

    python -m pip install .


## Start

    python cli.py

Key map for human player:

     q | w | e
    ---+---+---
     a | s | d
    ---+---+---
     z | x | c


## Tests

    python -m unittest discover -s tests


## representative field

A field is stored as a nine characters string.

A given field is translated to its representative field by finding all
equivalent fields through rotating and flipping.
Those eight equivalents are then sorted, and the first one is used as the
representative field.

Rotating and flipping operations are coded in `tools.OPERATIONS`.


## Decision model

See values of decision model ("beads" and "boxes") in `decision_model.yaml`.
Values are stored between games.
