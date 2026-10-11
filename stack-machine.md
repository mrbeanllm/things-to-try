Stack Machine Interpreter with Typed Int and String Values (Easy)

You are building an interpreter for a simple stack machine. The machine has a single persistent stack, and every value on it is exactly one of two primitive types: an integer (e.g. 7) or a string (e.g. "7"). The integer 7 and the string "7" are different values and must never be conflated.

The program is given as a list of textual instructions in execution order. Implement solution(program) that executes them and returns the list of values printed by each POP_AND_PRINT, in order (as strings, one per printed value). The four instruction kinds are:

PUSH v — push value v. If v is written in double quotes (e.g. PUSH "7") it is a string (the quotes are delimiters, not part of the value); otherwise (e.g. PUSH 7) it is an integer. The type is fixed at parse time.
POP — remove and discard the top value.
POP_AND_PRINT — remove the top value and emit it. An integer is emitted in decimal form; a string is emitted as its raw characters (no quotes).
ADD — pop the top two values and push the combined result. If both are integers, push their integer sum. If at least one is a string, convert any integer operand to its decimal string and push the concatenation, with the deeper (earlier-pushed) value first, followed by the value that was on top.
Return the printed values as a list of strings (empty list if nothing is printed).

Examples
Example 1
Input
(['PUSH 7', 'PUSH 7', 'ADD', 'POP_AND_PRINT', 'PUSH 7', 'PUSH "7"', 'ADD', 'POP_AND_PRINT', 'PUSH "ab"', 'PUSH "cd"', 'ADD', 'POP_AND_PRINT'],)
Output
['14', '77', 'abcd']
Notes
7+7 is int+int -> 14. 7+"7" involves a string, so 7 becomes "7" and concatenation gives "77". "ab"+"cd" concatenates to "abcd" with the earlier-pushed "ab" first.
Example 2
Input
(['PUSH "x"', 'PUSH 5', 'ADD', 'POP_AND_PRINT'],)
Output
['x5']
Notes
Deeper value is the string "x", top is int 5. At least one is a string, so 5 becomes "5" and the deeper value comes first: "x" + "5" = "x5".
Constraints
1 <= number of instructions <= 10^5.
Integer operands and all intermediate integer sums fit in a signed 64-bit integer.
String operands consist of printable ASCII characters, may be empty, and may contain digit characters (a string of digits is still a string).
The total length of all string values ever created during execution does not exceed 10^6 characters.
The program is valid: POP and POP_AND_PRINT are only issued on a non-empty stack, and ADD only when the stack holds at least two values.

Signature
def solution(program: list[str]) -> list[str]:
Sample call
solution(['PUSH 7', 'PUSH 7', 'ADD', 'POP_AND_PRINT', 'PUSH 7', 'PUSH "7"', 'ADD', 'POP_AND_PRINT', 'PUSH "ab"', 'PUSH "cd"', 'ADD', 'POP_AND_PRINT'])

def solution(program):
    # program: list of instruction strings, e.g.
    #   ['PUSH 7', 'PUSH "7"', 'ADD', 'POP_AND_PRINT']
    # return: list of strings printed by each POP_AND_PRINT, in order
    # TODO: implement
    pass