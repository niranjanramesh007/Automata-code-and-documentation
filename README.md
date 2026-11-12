# Formal Language Theory & Automata Implementation

This repository holds the formal design specifications, programmatic state machine implementations, and visualization configurations for three fundamental deterministic systems.

---

## 1. System Formalizations

### System 1: Password Verification DFA
Verifies a strict structural layout: **exactly 1 uppercase letter**, followed by **exactly 2 lowercase letters**, followed by **exactly 1 digit** (e.g., `Abc1`).
- **Formal Definition**:
  - $Q = \{ q_0, q_1, q_2, q_3, q_4, q_{dead} \}$
  - $\Sigma = \text{All printable characters}$
  - $q_0 = q_0$
  - $F = \{ q_4 \}$
  - $\delta$ Transitions:
    - $\delta(q_0, [A-Z]) = q_1$
    - $\delta(q_1, [a-z]) = q_2$
    - $\delta(q_2, [a-z]) = q_3$
    - $\delta(q_3, [0-9]) = q_4$
    - Any off-sequence path drops to $q_{dead}$.

### System 2: Email Format Validator DFA
Checks strings structured as `[alphanumeric]^+ @ [alphanumeric]^+ . com`.
- **Formal Definition**:
  - $Q = \{ q_0, q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_{dead} \}$
  - $q_0 = q_0$
  - $F = \{ q_7 \}$
  - $\delta$ Transitions:
    - $\delta(q_0, [a-zA-Z0-9]) = q_1$
    - $\delta(q_1, [a-zA-Z0-9]) = q_1$; $\delta(q_1, @) = q_2$
    - $\delta(q_2, [a-zA-Z0-9]) = q_3$
    - $\delta(q_3, [a-zA-Z0-9]) = q_3$; $\delta(q_3, .) = q_4$
    - $\delta(q_4, 'c') = q_5$; $\delta(q_5, 'o') = q_6$; $\delta(q_6, 'm') = q_7$
    - Out-of-alphabet or invalid transitions dump to $q_{dead}$.

### System 3: ATM PIN Verification State Machine
Models security locking behavior with a maximum of three attempts.
- **Formal Definition**:
  - $Q = \{ q_{start}, q_{att2}, q_{att3}, q_{unlocked}, q_{blocked} \}$
  - $\Sigma = \{ \text{'correct'}, \text{'incorrect'} \}$
  - $q_0 = q_{start}$
  - $F = \{ q_{unlocked} \}$
  - $\delta$ Transitions:
    - $\delta(q_{start}, \text{'correct'}) = q_{unlocked}$; $\delta(q_{start}, \text{'incorrect'}) = q_{att2}$
    - $\delta(q_{att2}, \text{'correct'}) = q_{unlocked}$; $\delta(q_{att2}, \text{'incorrect'}) = q_{att3}$
    - $\delta(q_{att3}, \text{'correct'}) = q_{unlocked}$; $\delta(q_{att3}, \text{'incorrect'}) = q_{blocked}$

---

## 2. Comparative Analysis Table

| Criteria / Property | Password DFA (System 1) | Email DFA (System 2) | ATM Security Machine (System 3) |
| :--- | :--- | :--- | :--- |
| **State Complexity** | 6 states (including $q_{dead}$) | 9 states (including $q_{dead}$) | 5 logical operational states |
| **Determinism (DFA)** | Yes (Deterministic) | Yes (Deterministic) | Yes (Deterministic) |
| **Transition Dynamics** | Linear structural progression | Self-loops & terminal word-matching | Multi-tiered linear progression with paths to terminal configurations |
| **Memory / Tracking** | Strictly tracks current character index | Arbitrary length matching with character lookahead | Sequence length state tracking (up to 3 input steps) |
| **Terminal Outlets** | Invariant terminal reject ($q_{dead}$) | Invariant terminal reject ($q_{dead}$) | Absorbing permanent states (`Blocked` / `Unlocked`) |