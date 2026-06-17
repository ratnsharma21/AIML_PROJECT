# Python Scientific Calculator

This folder contains a desktop Scientific Calculator GUI application built using Python's `tkinter` library for the graphical interface and the `math` module for scientific computations.

---

## Features

1.  **Basic Operations**: Addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
2.  **Parentheses Support**: Multi-layered bracket evaluations `(` and `)`.
3.  **Trigonometric Functions**: Sine (`sin`), Cosine (`cos`), and Tangent (`tan`) operations.
4.  **Angle Modes**: Interactive toggle between **DEG** (Degrees) and **RAD** (Radians) angle modes.
5.  **Conversions**: Instant conversion options for `deg→rad` and `rad→deg`.
6.  **Advanced Calculations**: Square root (`sqrt`) calculations.
7.  **Constants**: Input insertion for $\pi$ (Pi).
8.  **Usability**: Backspace (`⌫`) button for correcting entries and Clear (`C`) for resetting the expression.

---

## GUI Specifications
*   **Dimensions**: $400 \times 550$ pixels.
*   **Theme**: Dark mode interface with a modern color scheme (charcoal, orange highlight for operators, red for controls, and white display).

---

## Execution Output Snapshot

```text
+--------------------------------------+
| DEG                                  |
|                             (30+60)  |
+--------------------------------------+
| [C]   [⌫]   [(]   [)]   [DEG/RAD]    |
| [sin] [cos] [tan] [d→r] [r→d]        |
| [7]   [8]   [9]   [/]   [sqrt]       |
| [4]   [5]   [6]   [*]   [^]          |
| [1]   [2]   [3]   [-]   [π]          |
| [0]   [.]   [+]   [=]                |
+--------------------------------------+
```
*Note: Clicking 'sin' after inputting 90 in DEG mode evaluates to 1.0.*
