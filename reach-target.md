Reach a Target Using Each Number At Most Once (Hard)

You are given an array of integers nums and an integer target. Decide whether you can build an arithmetic expression that evaluates to exactly target, under the following rules:

Each element of nums may be used at most once. Elements with equal values count as separate elements. You do not have to use every element, but you must use at least one.
The numbers you pick may be arranged in any order and combined with the binary operators +, -, *, /, with any parenthesization.
Division is exact mathematical (rational) division: intermediate results may be non-integer fractions. Division by zero is not allowed at any step.
No unary minus, and no concatenating digits of different numbers (e.g. you may not glue 1 and 2 into 12).
An expression consisting of a single picked number (no operators) is allowed, so if some element already equals target, the answer is true.
Return true if target is reachable, otherwise false. Equality must be exact (rational arithmetic), not approximate floating-point equality.

Example 1

Input:  nums = [1, 2, 3, 4], target = 24
Output: true
Pick 2, 3, 4 (leaving 1 unused): 2 * 3 * 4 = 24.

Example 2

Input:  nums = [3, 3, 8, 8], target = 24
Output: true
8 / (3 - 8 / 3) = 8 / (1/3) = 24. Intermediate values are fractions, so exact rational arithmetic matters.

Example 3

Input:  nums = [2, 5], target = 9
Output: false
All reachable values are 2, 5, 7, -3, 3, 10, 2/5, 5/2 — none equals 9.

Constraints

1 <= nums.length <= 5
0 <= nums[i] <= 100
-10^4 <= target <= 10^4
Examples
Example 1
Input
([1, 2, 3, 4], 24)
Output
True
Notes
Pick 2,3,4 (leave 1 unused): 2*3*4 = 24.
Example 2
Input
([3, 3, 8, 8], 24)
Output
True
Notes
8 / (3 - 8/3) = 8 / (1/3) = 24 — requires exact fraction arithmetic.
Constraints
1 <= nums.length <= 5
0 <= nums[i] <= 100
-10^4 <= target <= 10^4
Each element may be used at most once; at least one must be used.
Operators: +, -, *, / with any parenthesization; no unary minus, no digit concatenation.
Division is exact rational division; division by zero is forbidden at every step.
Equality with target must be exact (rational), not floating-point.

Signature
def solution(nums: list[int], target: int) -> bool:
Sample call
solution([1, 2, 3, 4], 24)

def solution(nums, target):
    # nums: List[int], target: int -> return bool
    # Use exact rational arithmetic (fractions.Fraction) so that
    # intermediate fractions like 8/3 are handled without rounding.
    pass