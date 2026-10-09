# Turning the Interview Script into a Real Library or API

## Working assumptions

The interview code is correct, small, in-memory, single-threaded, and a few hundred lines long. The goal is not to rewrite the logic from scratch; it is to turn a working prototype into something other engineers can depend on safely.

The key shift is this:

- A script is optimized for solving one task in one process.
- A library is optimized for clear contracts, correctness, and safe reuse.
- An API is optimized for reliability, observability, and stable external behavior.

The best path is to make the core game rules explicit, separate the domain logic from transport concerns, and define the public contract before adding any new features.

---

## 1) Define the contract first

The first thing to do is stop thinking in terms of "a convenient script" and start thinking in terms of a public specification.

Ask and answer these questions clearly:

- What is a board?
- What is a move?
- What is a legal move?
- What counts as a win?
- What happens on invalid input?
- Does a move return a new board, or mutate the current one?
- Is the engine meant to be stateful or functional?
- Is the game one-off or does it support a sequence of turns?

For a library, the contract should be explicit enough that another engineer can use it without reading the whole implementation.

Concrete examples of contracts to lock down:

- Board dimensions are fixed at width x height, or configurable.
- Column indexes are 0-based or 1-based.
- Moves are applied only to the bottom of a column, and pieces are pushed upward within that column.
- A move is invalid if the column is out of range or already full.
- A winner is detected only after a move is applied.
- Winner detection explicitly checks horizontal and vertical runs of length k.

Why this matters:

- If the contract is unclear, every caller will guess differently.
- A library is only as trustworthy as its public semantics.
- Many bugs in real systems are not logic bugs; they are contract misunderstandings.

---

## 2) Separate the domain model from the implementation details

Right now the code probably mixes:

- board representation
- move rules
- win detection
- input validation
- maybe console/debug output
- maybe test code

That is fine for a prototype, but not for a library.

I would split the code into a few clear layers:

- Domain model
  - Board
  - Player / color
  - Move
  - Position
  - Game status / result

- Rules engine
  - apply_move(board, column, player)
  - is_valid_move(board, column)
  - detect_winner(board, last_move, k)

- Validation layer
  - validates shape, player identity, move arguments, board state

- Public interfaces
  - a library-facing API with typed inputs and outputs
  - an optional service-facing API if the code is later exposed over HTTP

Why this matters:

- A library should be easier to reason about than the original script.
- Clear separation reduces accidental coupling.
- It makes testing and future changes much safer.

---

## 3) Make the state and mutations explicit

The single biggest design decision is whether the engine mutates state in place or returns a new state.

For a reusable library, I would strongly prefer a clear and explicit model:

- either a pure function style
  - apply_move(board, move) -> new_board
- or a stateful object with well-defined mutation semantics
  - game.apply_move(column, player) -> GameResult

A pure or explicitly functional style is often easier to reason about and safer to test.

I would also define exactly what is returned after a move:

- success / failure
- updated board
- winner status
- winning line or cells
- next player
- error details if invalid

A single return object is usually better than relying on side effects or hidden global state.

Why this matters:

- Hidden mutation is hard to test and easy to misuse.
- In-process consumers need reliable, deterministic behavior.
- API clients need data they can interpret without reading internals.

---

## 4) Establish invariants and validation rules

The interview implementation likely assumes all inputs are well-formed because the test harness gives it valid data. A library cannot assume that.

I would define invariants such as:

- board dimensions are positive
- column index is within bounds
- move is not attempted on a full column
- player value is one of the supported colors
- the win check is performed only on valid states
- no illegal board shapes are accepted

Then I would enforce them consistently.

For a library, it is usually better to fail fast with explicit exceptions or structured error results.

Examples:

- InvalidColumnError
- BoardFullError
- InvalidPlayerError
- GameAlreadyFinishedError

Why this matters:

- Many production failures come from invalid assumptions, not from the main logic itself.
- Clear validation tells callers how to fix their usage.
- It creates a stable boundary between a valid engine and bad inputs.

---

## 5) Model the public API around the business semantics, not the implementation

The code is a game engine, so the public API should describe game operations in domain language, not low-level array operations.

Good contract examples:

- create_board(rows, columns)
- apply_move(board, column, player)
- get_winner(board, k)
- is_game_over(board, k)
- get_valid_moves(board)

If this becomes a library, I would keep the public surface small and intentional.

I would also decide whether the library should expose:

- raw board arrays
- high-level move objects
- immutable board states
- serialized representations for persistence or API use

The more core the concept, the more important it is to keep the contract stable.

Why this matters:

- A good public API limits surprises.
- Engineers can reason about it without depending on implementation details.
- It makes future versioning feasible.

---

## 6) Add tests to define the contract, not just the implementation

The interview solution passes the interviewer's tests. That is not enough for a library.

I would add tests for:

- valid move application
- invalid column usage
- full-column rejection
- winner detection in rows
- winner detection in columns
- no false positives on nearly-winning patterns
- repeated play across multiple turns
- edge-case board sizes
- board initialization and invariants

I would also write tests around the library contract itself:

- what happens on invalid input
- what is returned on success
- what is returned on game end
- whether the engine mutates or returns a new board

Why this matters:

- Tests become the specification.
- If a future change breaks semantics, the contract catches it.
- This is the difference between "code that works" and "code that can be trusted".

---

## 7) Add versioning and compatibility planning

Once other engineers depend on it, the most important thing is not speed; it is stability.

I would define:

- semantic versioning
- compatibility guarantees for the public API
- deprecation policy for old entry points
- changelog and migration notes

Examples:

- v1.0: initial public contract
- v1.1: add helper methods without breaking current ones
- v2.0: breaking changes only if absolutely necessary

Why this matters:

- Library users need confidence that upgrades do not silently break behavior.
- APIs are long-lived contracts, not disposable scripts.

---

## 8) If it becomes an API, move the transport concerns out of the core engine

This is where a lot of code goes wrong: the core engine is correct, but the network layer changes how people use it.

For an API, the engine should stay separate from the HTTP layer.

I would split it into:

- core game logic package
- API request/response schemas
- authentication and authorization layer
- rate limiting and request validation
- storage of match state (if needed)
- metrics and logs

Concrete API design points:

- Request includes game id, player, column, maybe match state
- Response includes success/failure, updated board, status, winner, error code
- API contract is versioned, not just code
- Validation happens before business logic
- No raw internal objects are exposed directly

Why this matters:

- The network boundary is a very different failure surface than an in-process library.
- A correct engine can still be unusable if the API contract is weak or inconsistent.
- This separation also allows you to support multiple clients without changing the core logic.

---

## 9) Add observability and operational safety

A library can be used incorrectly, but an API must be diagnosable.

I would add:

- structured logs for move attempts and outcomes
- metrics for valid vs invalid moves
- timing for winner checks and game operations
- health checks if served over HTTP
- retry-safe semantics where appropriate
- explicit error codes for bad inputs vs internal errors

For example, a client should not see a generic internal error when they send an invalid column index; that should be a specific validation error.

Why this matters:

- When engineers depend on your code, they need to understand failure modes.
- A deterministic, observable contract is far more maintainable than a silent one.

---

## 10) Decide what is public and what is internal

This is a crucial library design principle.

Public:

- Board API
- move application behavior
- winner detection semantics
- supported input types
- error contracts

Internal:

- helper functions that are only useful to the engine
- data layout choices
- temporary optimization code
- debugging or profiling helpers

A library should expose the minimum necessary surface area and keep the rest private.

Why this matters:

- It reduces accidental coupling.
- It allows refactoring without breaking downstream users.
- It gives you room to improve the internals while keeping the contract stable.

---

## 11) Think about the long-term shape of the product

This is the part the interview probably wants you to notice: the code works now, but a reusable product needs more than logic.

I would ask:

- Is this only for one game, or do we need variants with different rules?
- Can we support different board sizes or win lengths?
- Do we need serialization for saving games?
- Will another team use this in a UI, automated agent, or backend service?
- Do we need concurrency or multiple simultaneous games?

At that point, the design should support expansion without forcing major rewrites.

Why this matters:

- The library can start as a simple engine, but it should not be architected as a one-off.
- Good library design anticipates reuse and growth.

---

## 12) The practical sequence I would follow

Here is the concrete order I would take it in:

1. Write the public contract
   - Define input/output behavior.
   - Make assumptions explicit.

2. Identify the domain model
   - Board, move, result, player, state, error types.

3. Extract the core engine
   - No side effects, no global mutable state, no script-specific convenience code.

4. Add validation and exception types
   - Fail fast and clearly.

5. Separate engine from transport
   - Library first; API second.

6. Add comprehensive tests for contract behavior
   - Not just happy paths.

7. Add docs and examples
   - So other engineers can use it without reading the code.

8. Version the public interface
   - Make compatibility expectations explicit.

9. Add API exposure only after the core is stable
   - Do not expose business logic over HTTP before it has a clean contract.

10. Add observability and operational protections
   - Logs, metrics, error taxonomy, health checks.

---

## Bottom line

The interview code is good because it is logically correct. The transition to a library or API is not about making it more clever; it is about making it safer, clearer, and more stable for other people to depend on.

The most important changes are:

- define the contract clearly
- separate core logic from network concerns
- enforce validation and explicit errors
- make mutation behavior explicit
- test the contract, not just the sample cases
- version the public interface
- design for reuse, not just local correctness

That is what turns a working interview script into something a team can actually trust.

---

## Short summary in one sentence

I would turn the script into a contract-first, validated, testable game engine with a small public surface and explicit semantics, then layer an API on top only after that core contract is stable and durable.

