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

import matplotlib.pyplot as plt

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

#Here we built the graph from the Stanford Encyclopedia by hand to test the bisimulation algo. 
#We immediately noticed that the equivalence classes differed from the specification in the script. 
#Prof. Moss (University of Indiana) has already written about this, I have attached the e-mail at the very end. 


graph = nx.DiGraph()

graph.add_node("1")
graph.add_node("2a")
graph.add_node("2b")
graph.add_node("2c")
graph.add_node("3a")
graph.add_node("3b")
graph.add_node("3c")
graph.add_node("3d")


graph.add_edge("1", "2b")
graph.add_edge("1", "3c")
graph.add_edge("1", "3b")
graph.add_edge("1", "2c")
graph.add_edge("2a", "2c")
graph.add_edge("2a", "3a")
graph.add_edge("2b", "2a")
graph.add_edge("2b", "3b")
graph.add_edge("2c", "2b")
graph.add_edge("2c", "3c")

# Here your function is used, which outputs the following 
compute_maximum_bisimulation(graph)
# ...
[(2a,2b,2c),(3a,3b,3c,1)]

# We concluded that this means 2 eq.-classes but Prof. Moss says, there needs to be three: 



#Hello Professor Moss,

#I have recently studied the anti-foundation axiom and came across your Stanford encyclopedia article. To gain a deeper understanding off bisimulations and quotient graphs I attempted to reproduce the bisimulation from the article using an open source implementation of the algorithm (https://joss.theoj.org/papers/10.21105/joss.03519). However the generated bisimulation only has two equivalence classes. (https://github.com/BigMo0208/bispy-test)

#Is the bisimulation used in non well-founded set theory different to the bisimulations from graph/automata theory?


#As a self taught mathematician any clarification or insight you could provide on this topic would greatly help me develop a deeper understanding of Your theory and its applications.
#I thank You in advance for your time and valuable insights. Your work has deeply inspired me and I look forward to learning more about it.


#Dear Moritz Ackermann,

#The bisimulation used in non well-founded set theory is basically the same as the bisimulation from graph/automata theory: one takes a set T (usually a transitive set), and turns it into a graph by the definition 

 #  x --> y  if and only if y is an element of x

#Then one applies the definition of bisimulation from graphs/automata.

#I haven't looked at your github link, but I have an idea that could clarify things for you.  There is a difference between a bisimulation and the largest bisimulation. Perhaps this is old news to you, but the largest bisumulation on a given graph is the union of all the bisumulations on it.  But there are many bisimulations on a given graph – for example, the empty relation would be one.  My guess is that the implementation that you were using computed the largest one (since this is the main one of interest in practice).   

#Does this help?

 #     Larry Moss

