# Canonical Order Sort

You are given a list of trade execution records from an upstream feed. The records may arrive out of order. Each trade record is a dictionary with the fields:
- `trade_id` (string, unique)
- `symbol` (string)
- `ts` (integer timestamp in milliseconds)
- `price` (integer)
- `qty` (integer)
- `side` ("B" or "S")

Return the records sorted into a deterministic canonical order:
1. increasing `ts`
2. increasing `symbol` lexicographically
3. increasing `trade_id` lexicographically

## Example 1

Input:
```python
[
  {'trade_id': 'T3', 'symbol': 'MSFT', 'ts': 1002, 'price': 330, 'qty': 5, 'side': 'S'},
  {'trade_id': 'T1', 'symbol': 'AAPL', 'ts': 1000, 'price': 150, 'qty': 10, 'side': 'B'},
  {'trade_id': 'T2', 'symbol': 'AAPL', 'ts': 1001, 'price': 151, 'qty': 3, 'side': 'S'}
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
  {'trade_id': 'T2', 'symbol': 'MSFT', 'ts': 1000, 'price': 330, 'qty': 2, 'side': 'B'},
  {'trade_id': 'T1', 'symbol': 'AAPL', 'ts': 1000, 'price': 150, 'qty': 1, 'side': 'S'},
  {'trade_id': 'T3', 'symbol': 'AAPL', 'ts': 1000, 'price': 151, 'qty': 1, 'side': 'B'}
]
```

Output:
```python
[
  {'trade_id': 'T1', 'symbol': 'AAPL', 'ts': 1000, 'price': 150, 'qty': 1, 'side': 'S'},
  {'trade_id': 'T3', 'symbol': 'AAPL', 'ts': 1000, 'price': 151, 'qty': 1, 'side': 'B'},
  {'trade_id': 'T2', 'symbol': 'MSFT', 'ts': 1000, 'price': 330, 'qty': 2, 'side': 'B'}
]
```

## Constraints

- 0 <= len(trades) <= 200000
- `trade_id` values are unique
- `qty` > 0 for every trade
- `side` is either "B" or "S"
- Timestamps and prices fit in standard integer ranges

Write a function that takes a list of records and returns them in canonical order.