# Finite Automata for Real-Time Validation

**Course:** 21CSC301T Formal Language and Automata, CLA-2, Assessment Task 2  
**Student:** Niranjan R (RA2411026050070), B.Tech AIML 'A', III year  
**Faculty:** Dr. C. Gunasundari, SRM IST Tiruchirappalli  

This repository contains the design, mathematical formalisms, and programmatic execution models for three deterministic finite automata (DFA) representing daily input-validation tasks.

---

## 1. Application Automaton & Live States Summary

| # | Application | Automaton Type | Input Alphabet ($\Sigma$) | Final/Accepting States | Dead/Trap States | Total States |
|:-:| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Password Policy** | DFA | ASCII Characters | $\{q_4\}$ | $q_{dead}$ | 6 |
| 2 | **E-mail Format** | DFA | Alphanumeric, `@`, `.`, `c`, `o`, `m` | $\{q_7\}$ | $q_{dead}$ | 9 |
| 3 | **ATM PIN Verification** | State Machine | $\{	ext{correct}, 	ext{incorrect}\}$ | $\{q_{unlocked}\}$ | None (absorbing $q_{blocked}$) | 5 |

---

## 2. Run It

To execute the verification engines locally, clone this repository and run the state machine simulation script:

```bash
# Run the state machines and execute integrated validation test suites
python task2_automata.py
```

---

## 3. ATM PIN Verification

### System Design
This system models security threshold logic allowing a user a maximum of **three verification attempts** before permanently locking the system.

<img width="768" height="302" alt="atm_dfa" src="https://github.com/user-attachments/assets/ab2d32b0-b2a2-4530-adb8-5046fbf7a2a2" />


### Theoretical Explanation
* **States ($Q$):**
  * $q_{start}$ / $q_{att1}$: Waiting for the initial PIN input attempt.
  * $q_{att2}$: Second attempt state after 1 incorrect input.
  * $q_{att3}$: Third and final attempt state after 2 incorrect inputs.
  * $q_{unlocked}$: Accepting state representing validated access. It is an absorbing terminal state.
  * $q_{blocked}$: Terminal state indicating that the security threshold has been exceeded and the account is frozen.
* **Transition Security Logic:** This is not a simple regular expression evaluator; it acts as a contextual threshold counter tracking consecutive failures.

---

## 4. Password Policy Verification

### System Design
Validates that an entry strictly matches the criteria: **exactly 1 uppercase letter**, followed by **exactly 2 lowercase letters**, followed by **exactly 1 digit** (e.g., `Abc1`).

<img width="768" height="285" alt="password_dfa" src="https://github.com/user-attachments/assets/fcc9f90f-0d29-433f-ae2e-a9831132692d" />

### Theoretical Explanation
* **States ($Q$):**
  * $q_0$: Initial state, waiting for a capital letter.
  * $q_1$: Successfully parsed 1 uppercase letter.
  * $q_2$: Successfully parsed 1 uppercase and 1 lowercase letter.
  * $q_3$: Successfully parsed 1 uppercase and 2 lowercase letters.
  * $q_4$: Target accepting state (exactly 1 uppercase, 2 lowercase, 1 digit).
  * $q_{dead}$: Sinks any invalid characters or length violations.

---

## 5. E-mail Format Validator

### System Design
Matches valid format strings conforming to the grammar structure: `[alphanumeric]^+ @ [alphanumeric]^+ . com`.

<img width="960" height="312" alt="email_dfa" src="https://github.com/user-attachments/assets/03da929b-0608-43a5-bae8-b50d954eb431" />

### Theoretical Explanation
* **State Breakdown:**
  * $q_0 
ightarrow q_1$: Matches the initial non-empty username segment.
  * $q_1 
ightarrow q_2$: Transitioned by the mandatory `@` symbol.
  * $q_2 
ightarrow q_3$: Matches the domain prefix segment.
  * $q_3 
ightarrow q_4$: Instigated by the domain dot (`.`).
  * $q_4 
ightarrow q_5 
ightarrow q_6 
ightarrow q_7$: Sequentially verifies the fixed top-level extension string `'c'-'o'-'m'` to reach the accepting state.

---

## 6. Syntax vs. Semantics in Input Validation

In language theory and software compilers, validators evaluate inputs at different layers:
* **Syntax (Structural Grammar):** Focuses solely on whether the input follows the structural rules of the language. For example, verifying that an email matches the structure `user@domain.com` or that a password consists of `[A-Z][a-z][a-z][0-9]`. This layout-level evaluation is perfectly processed by Regular Expressions and Deterministic Finite Automata (DFA).
* **Semantics (Meaning & Contextual Validity):** Evaluates if a syntactically correct input makes sense in context. For example, `nonexistent_user@invalid_domain.com` is **syntactically valid** (it passes the DFA check), but **semantically invalid** if that domain does not exist or the mailbox is inactive. Evaluating semantics typically requires external context lookup, databases, or runtime checks that go beyond the capabilities of simple regular language machines.

---

## 7. Layout & State Transitions Comparison

Our three models represent different architectural state styles:

* **Linear Path Layout (System 1 & 2):** Characters must arrive in a strict chronological sequence. Deviations from the transition pattern permanently dump the process into an absorbing error state ($q_{dead}$).
* **Self-Loop Dynamic Layout (System 2):** Integrates loops on states $q_1$ and $q_3$ to process variable-length strings of alphanumeric inputs.
* **Sequential Counter State Layout (System 3):** Simulates contextual history tracking. Rather than reading characters, it evaluates transactional events (`correct`/`incorrect`) to scale through successive threat levels before permanently landing in a terminal lock state.
