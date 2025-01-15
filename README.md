## Objective
The goal of this project is to develop a network representation that links microorganisms with the compounds they can potentially produce. The network should help visualize which microorganisms are capable of synthesizing specific compounds. This exercise evaluates the ability to research, design, and implement a Python-based solution for microbial compound production analysis.

## Project Overview
In this project, we focus on microorganisms involved in **C1/C2 metabolism** (prokaryotic bacteria) and identify compounds they can potentially produce. The network will be represented graphically using Python, where:
- **Nodes** will represent microorganisms and compounds.
- **Edges** will indicate the relationship, i.e., a microorganism can produce a given compound.

## Research and Identification
1. A list of potential microorganisms involved in C1/C2 metabolism has been compiled.
2. Candidate compounds these microorganisms can potentially produce are identified, focusing on those with feasible laboratory testing potential.

### Explanation:
- **matplotlib** is used for plotting the graph.
- **networkx** is the library for creating and managing the network graph (nodes, edges, and visualization).
- **pandas** is used to read data from CSV files and handle the input data for microorganisms, compounds, and edges.

Make sure to include the `requirements.txt` file along with the `README.md` in your GitHub repository to allow others to easily set up the environment.
Users can install the required dependencies by running the following command:
pip install -r requirements.txt



