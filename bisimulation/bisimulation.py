import itertools

import numpy as np

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

import seaborn as sns

import networkx as nx

import rustworkx as rx



from bispy import compute_maximum_bisimulation, Algorithms
from llist import dllist
from rustworkx.visualization import mpl_draw
from bispy.saha.saha import saha as saha_algorithm
from bispy.utilities.graph_normalization import (
    check_normal_integer_graph,
    convert_to_integer_graph,
    back_to_original,
)
from bispy.utilities.graph_decorator import decorate_nx_graph, to_tuple_list
from bispy.paige_tarjan.paige_tarjan import paige_tarjan_qblocks

from typing import Union, List, Dict, Any, Tuple
from bispy.utilities.graph_entities import _QBlock, _Vertex




from typing import Dict, Tuple, Any, List

from bispy.saha.saha_partition import saha_algorithm

from typing import Iterable, List, Tuple, Dict, Union
from itertools import islice
from llist import dllist
from bispy.utilities.graph_entities import _QBlock as _Block, _Vertex, _XBlock
from bispy.utilities.graph_decorator import decorate_nx_graph
from bispy.paige_tarjan.paige_tarjan import paige_tarjan_qblocks
from bispy.utilities.graph_normalization import (
    check_normal_integer_graph,
    convert_to_integer_graph,
    back_to_original,
)
from bispy.utilities.graph_entities import _XBlock
from bispy.dovier_piazza_policriti.ranked_partition import RankedPartition


from llist import dllist, dllistnode
from typing import List, Dict, Any, Tuple, Iterable
import networkx as nx

from bispy.utilities.graph_entities import (
    _Vertex,
    _XBlock,
    _QBlock,
    _Count,
)
from bispy.paige_tarjan.compound_xblocks_container import (
    CompoundXBlocksContainer,
)
from bispy.utilities.graph_decorator import (
    decorate_nx_graph,
    preprocess_initial_partition,
    to_tuple_list,
)
from bispy.utilities.graph_normalization import (
    check_normal_integer_graph,
    convert_to_integer_graph,
    back_to_original,
)
# Erstellen der zufälligen Di.Graphen

def generate_random_digraph(node_counts: list[int], sparsity: list[float], one_divided_samplerate: int):
    # Generate a random binary adjacency matrix for a digraph with the given sparsity
    adj_matrix_factory = lambda n, s, samples: np.random.choice([0, 1], size=(n, n, samples), p=[s, 1 - s])
    graph_factory = lambda adj_matrix: nx.from_numpy_array(adj_matrix, create_using = nx.DiGraph)
    
    possible_graphs = [adj_matrix_factory(n, s, n**2//one_divided_samplerate) for n, s in itertools.product(node_counts, sparsity)]
    graphs = [[graph_factory(adj_matrix[:,:,i]) for i in range(adj_matrix.shape[2])] for adj_matrix in possible_graphs]
    
    return graphs


# Beispiel: Verwendung der Funktion
node_counts = [10, 20]  # Beispiel: Anzahl der Knoten
sparsity = [0.2, 0.5]   # Beispiel: Dichte
one_divided_samplerate = 10  # Beispiel: Stichprobengröße

# Generieren von Graphen
generated_graphs = generate_random_digraph(node_counts, sparsity, one_divided_samplerate)


# Bestimmen der größten Bisimulation
for graph_list in generated_graphs:
    for graph in graph_list:
        bisimulation_result = compute_maximum_bisimulation(graph)
def graph_factory(adj_matrix):
    return nx.from_numpy_array(adj_matrix, create_using=nx.DiGraph)
print(results_df.head())
# Korrelation zwischen Parametern berechnen
corr_mat = results_df.corr().stack().reset_index(name="correlation")

# Visualisierung der Korrelationsmatrix
sns.set_theme(style="whitegrid")
g = sns.relplot(
    data=corr_mat,
    x="level_0", y="level_1", hue="correlation", size="correlation",
    palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
    height=10, sizes=(50, 250), size_norm=(-.2, .8),
)

# Einstellen des Diagramms
g.set(xlabel="", ylabel="", aspect="equal")
g.despine(left=True, bottom=True)
g.ax.margins(.02)
for label in g.ax.get_xticklabels():
    label.set_rotation(90)
# Erstellen der Korrelationsmatrix

# Erstellen eines leeren DataFrames
results_df = pd.DataFrame(columns=["Node_Count", "Sparsity", "Bisimulation_Size"])

# Durchlaufen der generierten Graphen und Berechnung der Bisimulation
for node_count_idx, node_count in enumerate(node_counts):
    for sparsity_idx, sparsity_value in enumerate(sparsity):
        for graph in generated_graphs[node_count_idx][sparsity_idx]:
            # Überprüfen Sie, ob der Graph ein nx.DiGraph ist
            if isinstance(graph, nx.DiGraph):
                try:
                    bisimulation_result = compute_maximum_bisimulation(graph)
                    bisimulation_size = len(bisimulation_result)  # Größe der Äquivalenzklassen
                    results_df = results_df.append({"Node_Count": node_count, "Sparsity": sparsity_value, "Bisimulation_Size": bisimulation_size}, ignore_index=True)
                except Exception as e:
                    print(f"Ein Fehler ist aufgetreten: {e}")
            else:
                print("Der Graph ist nicht vom Typ nx.DiGraph")


# Weiterverarbeitung des DataFrames für die Darstellung

corr_mat = results_df.corr().stack().reset_index(name="correlation")

# Visualisierung der Korrelationsmatrix
sns.set_theme(style="whitegrid")
g = sns.relplot(
    data=corr_mat,
    x="level_0", y="level_1", hue="correlation", size="correlation",
    palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
    height=10, sizes=(50, 250), size_norm=(-.2, .8),
)

# Tweak the figure to finalize
g.set(xlabel="", ylabel="", aspect="equal")
g.despine(left=True, bottom=True)
g.ax.margins(.02)
for label in g.ax.get_xticklabels():
    label.set_rotation(90)


sns.set_theme(style="whitegrid")

# Load the brain networks dataset, select subset, and collapse the multi-index
df = compute_maximum_bisimulation

used_networks = [generated_graphs]

used_columns = (df.columns.get_level_values("network").astype(int).isin(used_networks))

df = df.loc[:, used_columns]

df.columns = df.columns.map("-".join)

# Compute a correlation matrix and convert to long-form
corr_mat = df.corr().stack().reset_index(name="correlation")

# Draw each cell as a scatter point with varying size and color
g = sns.relplot(
    data=corr_mat,
    x="level_0", y="level_1", hue="correlation", size="correlation",
    palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
    height=10, sizes=(50, 250), size_norm=(-.2, .8),
)

# Tweak the figure to finalize
g.set(xlabel="", ylabel="", aspect="equal")
g.despine(left=True, bottom=True)
g.ax.margins(.02)
for label in g.ax.get_xticklabels():
    label.set_rotation(90)
