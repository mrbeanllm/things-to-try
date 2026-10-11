Code Editor with Block Shrink and Expand (Code Folding) (Medium)

Implement the core of a code editor (like VS Code) that supports code folding: collapsing ("shrink") and restoring ("expand") indentation-based blocks of code.

Indentation (leading spaces, always a multiple of 4) defines block structure, as in Python. Line i is a block header if the line immediately after it has strictly greater indentation. The block owned by a header is the run of consecutive following lines with strictly greater indentation (it ends at the first line whose indentation is <= the header's). Blocks may nest, and each header keeps its own collapsed/expanded state. A line is visible if and only if none of the headers whose blocks contain it are collapsed.

render() format
render() returns the currently visible lines, one string each, as:

<display_number> <marker><line content>
display_number: 1-based index over visible lines only (hidden lines consume no number).
marker: "+ " if the line is a block header, otherwise the empty string.
line content: the original text, including leading indentation.
Operations (display numbers, not file line numbers)
shrink(d): if the visible line at display number d is a block header, mark it collapsed (its block's lines become hidden; the header stays visible). No-op if it is not a header or is already collapsed.
expand(d): if the visible line at d is a collapsed header, expand it. Its block's lines become visible except those still hidden by a nested header that remains collapsed.
Function adaptation (what you implement here)
This stateful editor is exposed as a single function so it can be graded by replay:

solution(lines, operations) -> list of render outputs
lines: the source lines the editor is initialized with.
operations: a sequence of operations applied in order, each one of:
["render"] — append the current render() output to the result,
["shrink", d] — collapse the header at display number d,
["expand", d] — expand the collapsed header at display number d.
Return the list of render() outputs (a list of lists of strings), one entry per ["render"] operation, in the order they occur. A shrink/expand uses the display numbering of the current (most recent) render state.
Example
Initialized with:

a = 1
for i in range(10):
    print(i)
    print(i ** 2)
b = 10
render() returns:

1 a = 1
2 + for i in range(10):
3     print(i)
4     print(i ** 2)
5 b = 10
After shrink(2), render() returns:

1 a = 1
2 + for i in range(10):
3 b = 10
The for-loop body (original lines 3-4) is hidden and b = 10 is renumbered to 3. expand(2) restores the original output.

Examples
Example 1
Input
(['a = 1', 'for i in range(10):', ' print(i)', ' print(i ** 2)', 'b = 10'], [['render'], ['shrink', 2], ['render'], ['expand', 2], ['render']])
Output
[['1 a = 1', '2 + for i in range(10):', '3 print(i)', '4 print(i ** 2)', '5 b = 10'], ['1 a = 1', '2 + for i in range(10):', '3 b = 10'], ['1 a = 1', '2 + for i in range(10):', '3 print(i)', '4 print(i ** 2)', '5 b = 10']]
Notes
Canonical example: render, shrink the for-loop, render (body hidden + renumbered), expand, render (restored).
Example 2
Input
(['def f():', ' for i in x:', ' a = 1', ' b = 2', ' c = 3', 'd = 4'], [['render'], ['shrink', 2], ['render'], ['shrink', 1], ['render'], ['expand', 1], ['render']])
Output
[['1 + def f():', '2 + for i in x:', '3 a = 1', '4 b = 2', '5 c = 3', '6 d = 4'], ['1 + def f():', '2 + for i in x:', '3 c = 3', '4 d = 4'], ['1 + def f():', '2 d = 4'], ['1 + def f():', '2 + for i in x:', '3 c = 3', '4 d = 4']]
Notes
Nested blocks: collapse inner for-loop, collapse outer def, expand outer while inner stays collapsed.
Constraints
1 <= number of lines <= 10^4; each line has at most 200 characters.
Indentation is spaces only, always a multiple of 4; the first line has indentation 0.
A line's indentation is at most one level (4 spaces) deeper than the previous line.
Up to 10^4 total shrink / expand / render operations.
Every shrink/expand receives a display number d that is valid for the current render state (1 <= d <= number of visible lines).
Sample call
solution(['a = 1', 'for i in range(10):', '    print(i)', '    print(i ** 2)', 'b = 10'], [['render'], ['shrink', 2], ['render'], ['expand', 2], ['render']])

from typing import List

def solution(lines: List[str], operations: List[list]) -> List[List[str]]:
    """
    Replay code-folding operations on an editor and return each render() output.

    lines:      source lines the editor is initialized with.
    operations: each is ["render"], ["shrink", d], or ["expand", d] (d is a
                1-based DISPLAY number in the current render state).
    Returns:    one render() output (list of strings) per ["render"] operation.

    Notes:
      - Line i is a block header iff line i+1 has strictly greater indentation.
      - render() line format: f"{display_number} {'+ ' if header else ''}{line}".
      - A line is visible iff no header whose block contains it is collapsed.
    """
    # TODO: implement
    pass