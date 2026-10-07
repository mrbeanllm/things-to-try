# Bottom-Insertion Connect Game: Detect the First k-in-a-Row Winner

## Problem

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

## Example 1

```python
k = 3
moves = [["B", 0], ["R", 5], ["B", 1], ["R", 5], ["B", 2]]
# Output: [5, ["B"]]
```

After move 5, row 0 holds B in columns 0, 1, 2 — three in a row. Column 5 holds only two R pieces (not enough for k=3).

## Example 2

```python
k = 3
moves = [["R", -1], ["B", -1], ["R", 0], ["B", 0], ["R", 1], ["B", 1]]
# Output: [6, ["B", "R"]]
```

Each B move pushes the R piece in that column up to row 1. After move 6, row 0 has B in columns -1, 0, 1 and row 1 has R in columns -1, 0, 1 — both complete a run of 3 simultaneously.

## Example 3

```python
k = 3
moves = [["B", 0], ["R", 0], ["B", 0]]
# Output: [-1, []]
```

All three land in column 0; bottom-to-top it reads B, R, B, so no run of 3 exists anywhere.

## Constraints

- 1 <= k <= 50
- 1 <= len(moves) <= 5000
- -10^6 <= column <= 10^6 (the board is unbounded — do not assume a fixed width)
- player is always "B" or "R"

## Notes

- Horizontal (single-row) and vertical (single-column) runs count.
- Diagonals do not count.

## Suggested approach

Use a sparse representation of the board per column:

- Store the stack of pieces in each column as a list or dict mapping row to player.
- For each move, determine the new height of the column and update the column state.
- Check only the affected row(s) and column for possible winning runs.
- Since a move can only affect one column and at most one row value pattern, the board can be checked efficiently without scanning the full board.
- For each player, detect if there are k consecutive occupied cells in the same row or same column after the update.

## Python template

```python
def winner_for_k_in_a_row(k, moves):
    # TODO: implement
    pass
```

## Example test cases

```python
assert winner_for_k_in_a_row(3, [["B", 0], ["R", 5], ["B", 1], ["R", 5], ["B", 2]]) == [5, ["B"]]
assert winner_for_k_in_a_row(3, [["R", -1], ["B", -1], ["R", 0], ["B", 0], ["R", 1], ["B", 1]]) == [6, ["B", "R"]]
assert winner_for_k_in_a_row(3, [["B", 0], ["R", 0], ["B", 0]]) == [-1, []]
```
