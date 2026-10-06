# Canonical Order Sort - Part 2

You are given a list of trade execution records from an upstream feed. The records may arrive out of order and the upstream feed may replay the same trade more than once. Each trade record is a dictionary with the fields:
- `trade_id` (string)
- `symbol` (string)
- `ts` (integer timestamp in milliseconds)
- `price` (integer)
- `qty` (integer)
- `side` ("B" or "S")

Treat any later record with a `trade_id` that has already appeared as a duplicate replay and ignore it. Keep only the first occurrence of each `trade_id`, then return the remaining records in canonical order:
1. increasing `ts`
2. increasing `symbol` lexicographically
3. increasing `trade_id` lexicographically

## Example 1

Input:
```python
[
  {'trade_id': 'T2', 'symbol': 'AAPL', 'ts': 1001, 'price': 151, 'qty': 3, 'side': 'S'},
  {'trade_id': 'T1', 'symbol': 'AAPL', 'ts': 1000, 'price': 150, 'qty': 10, 'side': 'B'},
  {'trade_id': 'T2', 'symbol': 'AAPL', 'ts': 1001, 'price': 151, 'qty': 3, 'side': 'S'},
  {'trade_id': 'T3', 'symbol': 'MSFT', 'ts': 1002, 'price': 330, 'qty': 5, 'side': 'S'}
]
```

Output:
```python
[
  {'trade_id': 'T1', 'symbol': 'AAPL', 'ts': 1000, 'price': 150, 'qty': 10, 'side': 'B'},
  {'trade_id': 'T2', 'symbol': 'AAPL', 'ts': 1001, 'price': 151, 'qty': 3, 'side': 'S'},
  {'trade_id': 'T3', 'symbol': 'MSFT', 'ts': 1002, 'price': 330, 'qty': 5, 'side': 'S'}
]
```

## Example 2

Input:
```python
[
  {'trade_id': 'T1', 'symbol': 'MSFT', 'ts': 1005, 'price': 330, 'qty': 4, 'side': 'B'},
  {'trade_id': 'T2', 'symbol': 'AAPL', 'ts': 1000, 'price': 150, 'qty': 1, 'side': 'S'},
  {'trade_id': 'T1', 'symbol': 'AAPL', 'ts': 999, 'price': 100, 'qty': 9, 'side': 'S'},
  {'trade_id': 'T3', 'symbol': 'GOOG', 'ts': 1001, 'price': 2800, 'qty': 2, 'side': 'B'}
]
```

Output:
```python
[
  {'trade_id': 'T2', 'symbol': 'AAPL', 'ts': 1000, 'price': 150, 'qty': 1, 'side': 'S'},
  {'trade_id': 'T3', 'symbol': 'GOOG', 'ts': 1001, 'price': 2800, 'qty': 2, 'side': 'B'},
  {'trade_id': 'T1', 'symbol': 'MSFT', 'ts': 1005, 'price': 330, 'qty': 4, 'side': 'B'}
]
```

## Constraints

- 0 <= len(trades) <= 200000
- `qty` > 0 for every trade
- `side` is either "B" or "S"
- Duplicate `trade_id` values should be treated as replays
- If multiple records share a `trade_id`, keep the first one from the input and ignore the rest

Write a function that takes a list of records, removes duplicate replays, and returns the remaining records in canonical order.
