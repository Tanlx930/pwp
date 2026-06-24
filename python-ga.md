# Python — Genetic Algorithm Optimizer for Hospital PPE Supplier Distribution

> A Python genetic-algorithm solution for optimizing distribution of personal-protective-equipment (PPE) from suppliers to hospitals.

![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![Algorithm](https://img.shields.io/badge/Algorithm-Genetic-9C27B0)
![Domain](https://img.shields.io/badge/Domain-Optimization-blueviolet)
![License](https://img.shields.io/badge/license-Academic-blue)

---

## Overview

This project applies a **genetic algorithm (GA)** to a real-world optimization problem: distributing PPE supplies from a set of suppliers to a network of hospitals while respecting capacity, demand, and cost constraints. The GA evolves candidate distribution plans across generations, using crossover and mutation to converge on near-optimal allocations.

---

## Module / Course

- **Module Code:** AAPP015-4-1-PWP
- **Course:** Python Programming
- **Institution:** Asia Pacific University
- **Project Type:** Group Assignment

---

## Problem Statement

Given:
- A list of **PPE suppliers** (each with a capacity and unit cost).
- A list of **hospitals** (each with a demand profile and priority).
- A **distribution constraint** matrix.

Find: an allocation of supplier → hospital quantities that **minimizes total cost** while satisfying all demand constraints.

---

## Genetic Algorithm Design

| Component | Implementation |
|---|---|
| **Chromosome** | A 2D matrix of allocations: rows = suppliers, columns = hospitals. |
| **Fitness function** | Weighted sum of total cost + penalty for unmet demand. |
| **Selection** | Tournament selection (k=3). |
| **Crossover** | Single-point or uniform crossover (configurable). |
| **Mutation** | Random reallocation between two cells (low rate). |
| **Termination** | Max generations OR fitness plateau. |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Core libraries | `random`, `numpy` (if used), built-in I/O |
| Data | Plain-text input files (`hospital.txt`, `ppe.txt`, `suppliers.txt`, `distribution.txt`) |
| Output | Console + flowchart visualization |

---

## Project Structure

```
python-ga/
├── GA_G20.py              # Main genetic algorithm
├── Python Code_G20.py     # Supporting / driver script
├── hospital.txt           # Hospital data
├── ppe.txt                # PPE types & demand
├── suppliers.txt          # Supplier capacity & cost
├── distribution.txt       # Constraints
├── db.txt                 # Combined dataset
├── Flowchart.png          # Algorithm flowchart
└── Pesudocode.docx        # Pseudocode walkthrough
```

---

## Getting Started

```bash
# 1. Ensure Python 3.x
python --version

# 2. Run the genetic algorithm
python GA_G20.py
```

The script reads the data files from the working directory and prints the best solution found along with convergence statistics.

---

## Sample Output

```
Generation 1   | Best Fitness: 245.32
Generation 50  | Best Fitness: 198.71
Generation 100 | Best Fitness: 178.42
...
Final allocation matrix:
    H1   H2   H3   H4
S1  120   80   0    50
S2  0     100  150  60
S3  ...
```

---

## Screenshots

> _Add screenshots of GA convergence plot, console output, and final solution matrix._

---

## Documentation

- `Python Documentation _G4.pdf` — full report
- `Python Presentation_G4.mp4` — demo presentation
- `Flowchart.png` — algorithm flowchart
- `Pesudocode.docx` — pseudocode

---

## License

Academic project. Source provided for portfolio reference; not for commercial reuse.
