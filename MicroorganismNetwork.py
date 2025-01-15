import matplotlib
matplotlib.use('TkAgg')  # Change backend for interactive plotting
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Load data from CSV files
microorganisms_file = "microorganisms.csv"
compounds_file = "compounds.csv"
edges_file = "edges.csv"

# Load microorganisms
microorganisms_df = pd.read_csv(microorganisms_file)
microorganisms = microorganisms_df["Microorganism"].tolist()

# Load compounds
compounds_df = pd.read_csv(compounds_file)
compounds = compounds_df["Compound"].tolist()

# Load edges
edges_df = pd.read_csv(edges_file)
edges = [tuple(x) for x in edges_df.values]

# Step 2: Create the network
def create_network():
    G = nx.DiGraph()  # Directed graph to show relationships

    # Add nodes
    G.add_nodes_from(microorganisms, node_type='microorganism')
    G.add_nodes_from(compounds, node_type='compound')

    # Add edges
    G.add_edges_from(edges)

    return G

# Step 3: Visualize the network
def visualize_network(G):
    plt.figure(figsize=(12, 8))

    # Define positions for the nodes
    pos = nx.spring_layout(G, seed=42)

    # Draw microorganism nodes
    nx.draw_networkx_nodes(G, pos, nodelist=microorganisms, node_color='skyblue', node_size=800, label='Microorganisms')

    # Draw compound nodes
    nx.draw_networkx_nodes(G, pos, nodelist=compounds, node_color='lightgreen', node_size=800, label='Compounds')

    # Draw edges (arrows representing relationships)
    nx.draw_networkx_edges(G, pos, edgelist=edges, arrows=True, width=2, edge_color='gray')

    # Draw labels for nodes
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

    # Add custom legend
    handles, labels = plt.gca().get_legend_handles_labels()
    handles += [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='skyblue', markersize=10, label='Microorganisms'),
                plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', markersize=10, label='Compounds')]
    labels += ['Microorganisms', 'Compounds']
    plt.legend(handles, labels, loc='upper left')

    # Display the graph
    plt.title("Microorganism-Compound Network")
    plt.show()

# Step 4: Execute the script
if __name__ == "__main__":
    network = create_network()
    visualize_network(network)

