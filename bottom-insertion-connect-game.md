# Bottom-Insertion Connect Game: Detect the First k-in-a-Row Winner

Two players, B and R, take turns dropping pieces onto a board covering the upper half-plane of an integer grid. Columns are indexed by arbitrary integers (..., -2, -1, 0, 1, 2, ...); rows are indexed 0, 1, 2, ... upward from the bottom.

A move (player, column) is applied as follows:

- If the chosen column is empty, the new piece is placed at row 0 (the bottom cell).
- If the column already contains pieces, every piece in that column is pushed up by one row, and the new piece is placed at row 0.
- Pieces never move sideways, and a move never affects any other column.

Process the moves one at a time. After a move, a player wins if the board contains k consecutive occupied cells in a single row or a single column that all hold that player's pieces. Diagonals do not count. Because a move shifts an entire column upward, a single move can complete winning lines for both players at once.

Return [m, winners] for the first winning move — m is the 1-based move index and winners is the alphabetically sorted list of players holding a winning line at that moment (["B"], ["R"], or ["B", "R"]). If nobody wins after all moves, return [-1, []].

## Input

- k — required run length.
- moves — list of [player, column] pairs in play order; player is "B" or "R", column is an integer.

## Output

A pair [m, winners] as described, or [-1, []].

## Examples

### Example 1
k = 3
moves = [["B", 0], ["R", 5], ["B", 1], ["R", 5], ["B", 2]]
Output: [5, ["B"]]

### Example 2
k = 3
moves = [["R", -1], ["B", -1], ["R", 0], ["B", 0], ["R", 1], ["B", 1]]
Output: [6, ["B", "R"]]

### Example 3
k = 3
moves = [["B", 0], ["R", 0], ["B", 0]]
Output: [-1, []]

## Constraints

- 1 <= k <= 50
- 1 <= len(moves) <= 5000
- -10^6 <= column <= 10^6 (the board is unbounded — do not assume a fixed width)
- player is always "B" or "R"
