Merge Two Insertion Diffs in Linear Time (Medium)

A text-editing system represents changes to a document as insertion diffs. An insertion diff is a set of (position, value) pairs, where each pair means: after this diff is applied, the element value sits at index position of the resulting document. All elements of the pre-diff document keep their relative order and fill the remaining indices from left to right.

Formally, applying a diff D to a sequence S produces a sequence T of length len(S) + len(D):

For every pair (p, v) in D, T[p] = v.
The elements of S, in their original order, occupy the remaining indices of T in increasing index order.
For example, applying {0: "A", 3: "B"} to ["z", "z", "z"] yields ["A", "z", "z", "B", "z"].

Now suppose two diffs are applied one after the other:

diff_one is applied to the original document.
diff_two is then applied to the result of step 1 — so its positions refer to indices of the final document.
Continuing with the original document ["z", "z", "z"]: diff_one = {0: "A", 3: "B"} produces ["A", "z", "z", "B", "z"], and diff_two = {0: "C", 4: "D"} then produces ["C", "A", "z", "z", "D", "B", "z"].

Write merge_diffs(diff_one, diff_two) returning a single diff equivalent to applying diff_one followed by diff_two. For the example, the merged diff is [(0, "C"), (1, "A"), (4, "D"), (5, "B")]: applying it directly to ["z", "z", "z"] yields the same final document in one step.

The document itself is never given and may be enormous, so you cannot materialize it. Your function must run in O(n + m) time, where n = len(diff_one) and m = len(diff_two) — not proportional to the document length or to the largest position value.

Input: each diff is a list of (position, value) pairs sorted by increasing position; positions within one diff are distinct non-negative integers; values are opaque non-empty strings. Both diffs are valid for their (unseen) document.

Output: the merged diff as a list of (position, value) pairs sorted by increasing position; its size is exactly n + m.

Example 1
Input
([(0, 'A'), (3, 'B')], [(0, 'C'), (4, 'D')])
Output
[(0, 'C'), (1, 'A'), (4, 'D'), (5, 'B')]
Notes
The worked example. C takes final index 0, pushing A (was at T1 index 0) to 1; D takes index 4; B (was at T1 index 3) lands at 3 + 2 = 5.
Example 2
Input
([(1, 'P')], [(1, 'Q')])
Output
[(1, 'Q'), (2, 'P')]
Notes
Position collision. On doc ['a','b'], diff_one gives ['a','P','b']; diff_two's index 1 is absolute, so Q takes index 1 and P is pushed to index 2 (1 + d, d=1).
Constraints
0 <= n, m <= 2 * 10^5 (n = len(diff_one), m = len(diff_two))
0 <= position <= 10^9
Positions within a single diff are distinct; each diff is sorted by increasing position
Values are opaque non-empty strings
Required time complexity: O(n + m) — you may not materialize the document
Sample call
merge_diffs([(0, 'A'), (3, 'B')], [(0, 'C'), (4, 'D')])
def merge_diffs(diff_one, diff_two):
    # diff_one, diff_two: List[Tuple[int, str]] sorted by increasing position.
    # Return the merged diff as List[Tuple[int, str]] sorted by increasing position.
    # Must run in O(n + m); do NOT reconstruct the document.
    pass