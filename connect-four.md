Part 1: Initialize a Bottom Push-Up Connect Four Board (Easy)

Create the initial state for a Connect Four variant where discs are inserted at the bottom of a column and push existing discs upward. Use row index 0 as the bottom/insertion row, and row index R-1 as the top/ejection row. For this standalone problem, return a textual snapshot of the initialized board and bookkeeping. Passing rows=0 and cols=0 requests the default 6 x 7 board. If dimensions are invalid, return ['INVALID_DIMENSIONS']. Also report whether a connect-four line is geometrically possible on the board.

Example 1
Input
(0, 0)
Output
['rows=6', 'cols=7', 'orientation=bottom_index_0_top_index_R-1', 'heights=0,0,0,0,0,0,0', 'filled=0', 'can_connect_four=true', '.......', '.......', '.......', '.......', '.......', '.......']
Notes
The default 6 x 7 empty board is created.
Example 2
Input
(3, 3)
Output
['rows=3', 'cols=3', 'orientation=bottom_index_0_top_index_R-1', 'heights=0,0,0', 'filled=0', 'can_connect_four=false', '...', '...', '...']
Notes
A 3 x 3 board cannot contain four cells in any direction.
Constraints
0 <= rows, cols <= 200
rows=0 and cols=0 means use the default 6 x 7 board
After default handling, rows and cols must both be positive
Internal row orientation must treat row 0 as the bottom insertion row
Signature
def solution(rows: int, cols: int) -> list[str]:
Sample call
solution(0, 0)

Part 2: Drop a Disc with Bottom Push-Up Semantics (Medium)

Simulate disc drops in the bottom push-up Connect Four variant. A valid drop inserts the player's disc into the bottom cell of the chosen column and shifts existing discs in that column upward by one row. If the column is full, the old top disc is ejected permanently. Player X always moves first, and valid moves must alternate X, O, X, O. Rejected moves must not mutate the board or advance the turn.

Example 1
Input
(4, 3, ['X 1', 'O 1', 'X 1'])
Output
['OK:ejected=.', 'OK:ejected=.', 'OK:ejected=.', 'TURN:O', 'HEIGHTS:0,3,0', 'FILLED:3', '...', '.X.', '.O.', '.X.']
Notes
All three discs are inserted at the bottom of column 1, pushing previous discs upward.
Example 2
Input
(2, 1, ['X 0', 'O 0', 'X 0'])
Output
['OK:ejected=.', 'OK:ejected=.', 'OK:ejected=X', 'TURN:O', 'HEIGHTS:2', 'FILLED:2', 'O', 'X']
Notes
The third drop is into a full column and ejects the old top X.
Constraints
1 <= rows, cols <= 200
0 <= len(moves) <= 1000
Players are represented by 'X' and 'O'
A rejected move performs no mutation and does not advance the turn
This part does not perform win detection; it only simulates drops
Signature
def solution(rows: int, cols: int, moves: list[str]) -> list[str]:
Sample call
solution(4, 3, ['X 1', 'O 1', 'X 1'])

Part 3: Detect Wins After Bottom Push-Up Drops (Medium)

Simulate bottom push-up drops and report winners after each valid move. A win is four equal discs horizontally, vertically, or diagonally. Unlike standard Connect Four, checking only around the newly inserted bottom cell is not sufficient because every disc in the affected column may move upward. For this problem, use a full-board scan after each valid move.

Example 1
Input
(4, 5, ['X 0', 'O 4', 'X 1', 'O 4', 'X 2', 'O 4', 'X 3'])
Output
['OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:X']
Notes
X completes a horizontal bottom-row connect four.
Example 2
Input
(4, 6, ['X 1', 'O 4', 'X 1', 'O 5', 'X 2', 'O 2', 'X 3', 'O 4', 'X 3', 'O 5', 'X 0', 'O 0'])
Output
['OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:-', 'OK:X']
Notes
The final O drop in column 0 pushes an X upward, creating an X horizontal win that is not through the newly placed O.
Constraints
1 <= rows, cols <= 100
0 <= len(moves) <= 1000
Players are 'X' and 'O'
A rejected move performs no mutation and does not advance the turn
A board with both rows < 4 and cols < 4 can never contain a connect-four line
Signature
def solution(rows: int, cols: int, moves: list[str]) -> list[str]:
Sample call
solution(4, 5, ['X 0', 'O 4', 'X 1', 'O 4', 'X 2', 'O 4', 'X 3'])

Part 4: Undo and Redo Bottom Push-Up Drops (Hard)

Support drop, undo, and redo operations for the bottom push-up Connect Four variant. Each successful drop must be recorded as a command containing enough information to invert it exactly, including whether the column was full and which disc, if any, was ejected. Undo reverses the most recent successful drop. Redo reapplies the most recently undone drop. A new successful drop after an undo clears the redo history.

Example 1
Input
(3, 2, ['drop X 0', 'drop O 1', 'undo', 'redo'])
Output
['OK:ejected=.', 'OK:ejected=.', 'UNDO_OK', 'REDO_OK:ejected=.', 'TURN:X', 'HEIGHTS:1,1', 'FILLED:2', '..', '..', 'XO']
Notes
Undo removes O from column 1; redo restores the same drop.
Example 2
Input
(2, 1, ['drop X 0', 'drop O 0', 'drop X 0', 'undo'])
Output
['OK:ejected=.', 'OK:ejected=.', 'OK:ejected=X', 'UNDO_OK', 'TURN:X', 'HEIGHTS:2', 'FILLED:2', 'X', 'O']
Notes
Undo of a full-column drop restores the ejected X to the top.
Constraints
1 <= rows, cols <= 100
0 <= len(operations) <= 1000
Players are 'X' and 'O', with X moving first
Rejected drops do not mutate state, advance turn, or clear redo history
A new successful drop after one or more undos clears the redo stack
Signature
def solution(rows: int, cols: int, operations: list[str]) -> list[str]:
Sample call
solution(3, 2, ['drop X 0', 'drop O 1', 'undo', 'redo'])