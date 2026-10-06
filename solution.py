def dedupe_and_sort_trades(trades):
    seen = set()
    unique = []

    for trade in trades:
        trade_id = trade["trade_id"]
        if trade_id in seen:
            continue
        seen.add(trade_id)
        unique.append(trade)

    unique.sort(key=lambda trade: (trade["ts"], trade["symbol"], trade["trade_id"]))
    return unique
