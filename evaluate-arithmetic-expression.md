# Evaluate a String Arithmetic Expression

## Problem

Evaluate a string arithmetic expression whose literals are positive integers and whose binary operators are +, -, *, and /. Return its integer value if every evaluated subexpression has a strictly positive integer result. If any literal, operand, or intermediate result fails that rule, return Boolean false for the whole expression; later operations cannot make that subexpression valid.

## Supplied Decomposition Helper

Assume a helper `split(s)` is provided for expressions in this task. It decomposes an expression at its outermost operation and returns either:
- A one-element tuple containing a literal expression: `(literal,)`
- A three-element tuple: `(left_expression, operator, right_expression)`

The returned operand expressions may themselves need evaluation.

### Examples of split()

```python
split("3 / 5")           # -> ("3", "/", "5")
split("5")               # -> ("5",)
split("(10 / 2) / 5")    # -> ("(10 / 2)", "/", "5")
```

The helper determines the decomposition of a valid input expression. This task does not ask you to implement a parser. The source does not specify the helper's behavior for malformed expressions or every unparenthesized operator combination.

## Arithmetic and Output Rules

1. **Literals**: A literal must be a positive integer after permitted surrounding whitespace and enclosing parentheses are removed. Zero is invalid.

2. **Addition and Multiplication**: Use exact integer arithmetic.

3. **Subtraction**: Invalid if its result is zero or negative.

4. **Division**: Invalid if:
   - The divisor is zero, OR
   - The dividend is not exactly divisible by the divisor (do not round or truncate a fractional quotient).

5. **Return Value**: Return the final positive integer, or Boolean `false` when any subexpression is invalid.

## Examples

### Example 1
```python
expression = "(3 + (3 * 5)) / 2"
# Evaluation: (3 + 15) / 2 = 18 / 2 = 9
result = 9
```

### Example 2
```python
expression = "((3 - 5) + 12) / 2"
# (3 - 5) = -2, which is invalid (not strictly positive)
result = False
```

### Example 3
```python
expression = "8 / 12"
# 8 / 12 is not exact (no integer quotient)
result = False
```

### Example 4
```python
expression = "3 - 3"
# 3 - 3 = 0, which is invalid (must be strictly positive)
result = False
```

## Key Points

- All subexpressions must evaluate to strictly positive integers.
- Zero is considered invalid.
- Negative results are invalid.
- Fractional division results are invalid.
- The evaluation must be recursive: each operand is itself an expression that must be valid.
- Once a subexpression fails validation, the entire expression is invalid.

## Python Template

```python
def evaluate_expression(expression, split):
    """
    Evaluate an arithmetic expression with validation.
    
    Args:
        expression: A string containing the arithmetic expression
        split: A helper function that decomposes expressions
        
    Returns:
        int: The evaluated result if all subexpressions are strictly positive
        False: If any subexpression is invalid
    """
    # TODO: implement
    pass
```

## Test Cases

```python
# Assuming split is provided
assert evaluate_expression("(3 + (3 * 5)) / 2", split) == 9
assert evaluate_expression("((3 - 5) + 12) / 2", split) == False
assert evaluate_expression("8 / 12", split) == False
assert evaluate_expression("3 - 3", split) == False
assert evaluate_expression("5", split) == 5
assert evaluate_expression("10 + 5", split) == 15
assert evaluate_expression("10 - 5", split) == 5
assert evaluate_expression("10 * 3", split) == 30
assert evaluate_expression("20 / 4", split) == 5
```

## Algorithm Approach

1. Use the provided `split()` helper to decompose the expression.
2. If the result is a single-element tuple, parse it as a literal:
   - Remove whitespace and parentheses
   - Verify it's a positive integer
   - Return the integer or `False` if invalid
3. If the result is a three-element tuple:
   - Recursively evaluate the left operand
   - Recursively evaluate the right operand
   - If either is `False`, return `False`
   - Apply the operator to the two results
   - Validate the operation according to the rules above
   - Return the result or `False` if invalid
