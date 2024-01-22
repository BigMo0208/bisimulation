import rustworkx as rx

def ueberpruefe_uebergaenge(graph, start, ziel, bisimulationsrelation):
    for nachbar in graph.neighbors(start):
        bisimilar_found = False
        for ziel_nachbar in graph.neighbors(ziel):
            if (nachbar, ziel_nachbar) in bisimulationsrelation or nachbar == ziel_nachbar:
                bisimilar_found = True
                break
        if not bisimilar_found:
            return False
    return True

def ist_bisimilar(graph, node1, node2, bisimulationsrelation):
    if (node1, node2) in bisimulationsrelation or (node2, node1) in bisimulationsrelation:
        return True

    if not ueberpruefe_uebergaenge(graph, node1, node2, bisimulationsrelation):
        return False

    if not ueberpruefe_uebergaenge(graph, node2, node1, bisimulationsrelation):
        return False

    bisimulationsrelation.add((node1, node2))
    bisimulationsrelation.add((node2, node1))
    return True

def finde_bisimulationsrelation(graph):
    bisimulationsrelation = set()

    for node1 in graph.node_indices():
        for node2 in graph.node_indices():
            if node1 != node2:
                ist_bisimilar(graph, node1, node2, bisimulationsrelation)

    return bisimulationsrelation

def erstelle_quotientengraph(original_graph, bisimulationsrelation):
    quotienten_graph = rx.PyDiGraph()
    gruppen_zu_knoten = {}

    for node in original_graph.node_indices():
        gruppe = frozenset({n for n, m in bisimulationsrelation if n == node or m == node})
        if not gruppe:
            gruppe = frozenset({node})
        if gruppe not in gruppen_zu_knoten:
            neuer_knoten = quotienten_graph.add_node(gruppe)
            gruppen_zu_knoten[gruppe] = neuer_knoten

    for node1 in original_graph.node_indices():
        gruppe1 = frozenset({n for n, m in bisimulationsrelation if n == node1 or m == node1})
        for node2 in original_graph.neighbors(node1):
            gruppe2 = frozenset({n for n, m in bisimulationsrelation if n == node2 or m == node2})
            if gruppe1 != gruppe2:
                quotienten_graph.add_edge(gruppen_zu_knoten[gruppe1], gruppen_zu_knoten[gruppe2], None)

    return quotienten_graph

# Erstellen und Befüllen des Originalgraphen
original_graph = rx.PyDiGraph()
node_a = original_graph.add_node("A")
node_b = original_graph.add_node("B")
original_graph.add_edge(node_a, node_b, None)  # Kante von A nach B

# Finden der Bisimulationsrelation und Erstellen des Quotientengraphen
bisimulationsrelation = finde_bisimulationsrelation(original_graph)
quotienten_graph = erstelle_quotientengraph(original_graph, bisimulationsrelation)

# Ausgabe der Anzahl der Knoten und Kanten im Quotientengraphen
print("Anzahl der Knoten im Quotientengraphen:", quotienten_graph.num_nodes())
print("Anzahl der Kanten im Quotientengraphen:", quotienten_graph.num_edges())
