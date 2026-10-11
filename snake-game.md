Snake Game: Minimum Moves to Reach the Apple (Hard)

You are simulating the classic Snake game on a grid with R rows and C columns. Cells are identified as (r, c) with 0 <= r < R and 0 <= c < C.

The snake is a sequence of L distinct cells body[0], body[1], ..., body[L-1], where body[0] is the head and every pair of consecutive cells is adjacent (shares an edge). A single apple is located at cell apple = (ar, ac), guaranteed not to lie on the snake.

Movement rules. On each move you choose one of four directions (up, down, left, right) and the game advances one tick:

The new head cell h' is the current head shifted one cell in the chosen direction.
If h' is the apple cell, the snake eats and grows: h' is prepended and the tail stays in place (length becomes L + 1).
Otherwise, h' is prepended and the tail cell body[L-1] is vacated on the same tick (length unchanged).
A move is legal only if h' is inside the grid and does not collide with the body as it exists after the tail update: h' must not equal any of body[0..L-2]. Moving into the current tail cell body[L-1] is legal on a non-eating move, because the tail vacates that cell during the same tick.
The snake cannot pass through walls or through itself, and moves exactly one cell per tick.

Task. Return the minimum number of moves for the snake's head to reach the apple cell (the move on which the head enters the apple counts), or -1 if the apple can never be reached.

The function receives R, C, body (a list of [r, c] cells, head first), and apple ([ar, ac]).

Examples
Example 1
Input
(2, 3, [[0, 0]], [1, 2])
Output
3
Notes
A length-1 snake starting at (0,0) reaches apple (1,2) in 3 moves, e.g. right, right, down.
Example 2
Input
(3, 3, [[0, 2], [0, 1], [0, 0]], [2, 0])
Output
4
Notes
Head goes down to (1,2), down to (2,2), left to (2,1), left to (2,0)=apple; the body follows, vacating one tail cell per tick.
Constraints
2 <= R, C <= 10
1 <= L <= min(8, R * C - 1)
The initial body cells are distinct, consecutive cells are adjacent (share an edge), and the apple is not on the body.
The head only ever moves one cell per tick, in one of the four cardinal directions.

Signature
def solution(R: int, C: int, body: list[list[int]], apple: list[int]) -> int:
Sample call
solution(2, 3, [[0, 0]], [1, 2])

from collections import deque

def solution(R, C, body, apple):
    # R rows, C cols. body: list of [r, c] cells, head first. apple: [ar, ac].
    # Return the minimum number of moves for the head to reach the apple, or -1.
    pass