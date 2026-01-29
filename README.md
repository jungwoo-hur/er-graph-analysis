# Experimental Analysis of Graph Algorithms on Random Networks

This project experimentally evaluates key graph algorithms on
random graph models to study structural properties of real-world networks.

The focus is on measuring **diameter**, **clustering coefficient**, and
**degree distribution** under controlled random graph generation.

---

## Overview
Many real-world systems (social networks, communication networks, biological networks)
can be modeled as graphs with characteristic structural properties.
This project analyzes such properties by implementing and testing
graph algorithms on randomly generated graphs.

The following algorithms are implemented and evaluated:
- Graph diameter estimation
- Clustering coefficient computation
- Degree distribution analysis

Experiments are conducted on **Erdos–Renyi random graphs** to observe
how these metrics scale with graph size.

---

## Graph Model
This project uses **Erdos–Renyi random graphs** `G(n, p)`, where:
- `n` is the number of vertices
- `p = 2 (ln n) / n`


This choice ensures the graph is connected with high probability,
allowing meaningful analysis of diameter and clustering behavior.

---

## Implemented Algorithms

### 1. Diameter Estimation
Approximates the length of the longest shortest path in the graph.
The algorithm balances accuracy and computational feasibility
for large graphs.

### 2. Clustering Coefficient
Computes the ratio:

`(3 × number of triangles) / (number of length-2 paths)`

This metric captures the tendency of nodes to form tightly connected groups
and measures the level of local clustering in the graph.

### 3. Degree Distribution
Counts the number of vertices for each possible degree,
revealing the connectivity pattern of the graph.

---

## Experimental Setup
- Graph sizes tested: multiple values of `n`
- Multiple random graph instances generated per size
- Results averaged to reduce randomness effects
- All experiments were conducted using the same random seed policy
  to ensure reproducibility.
- Independent random seeds were used across trials to reduce bias.

---



