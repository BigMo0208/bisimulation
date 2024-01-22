# 1. Überprüfen der Anzahl der Knoten und Kanten
print("Anzahl der Knoten im Originalgraphen:", original_graph.num_nodes())
print("Anzahl der Knoten im Quotientengraphen:", quotienten_graph.num_nodes())
print("Anzahl der Kanten im Originalgraphen:", original_graph.num_edges())
print("Anzahl der Kanten im Quotientengraphen:", quotienten_graph.num_edges())

# 2. Überprüfen spezifischer Kanten (dies hängt von Ihrem spezifischen Graphen ab)
# Beispiel: Überprüfen, ob eine Kante zwischen zwei bestimmten Knotengruppen existiert
# Hinweis: Sie müssen die Gruppenkennungen entsprechend Ihrem Graphen anpassen
gruppe1 = frozenset({node_a})  # Beispiel für die Gruppenkennung
gruppe2 = frozenset({node_b})  # Beispiel für die Gruppenkennung
kante_existiert = any(quotienten_graph.has_edge(gruppen_zu_knoten[gruppe1], gruppen_zu_knoten[gruppe2]) for gruppe1, gruppe2 in quotienten_graph.edge_list())
print("Kante zwischen Gruppe1 und Gruppe2 existiert:", kante_existiert)

# 3. Prüfen der Knoteneigenschaften (dies ist abhängig von der Struktur Ihres Graphen)
# Beispiel: Überprüfen, ob ein Knoten die korrekte Gruppe von bisimilären Knoten repräsentiert
# Hinweis: Sie müssen die Gruppenkennungen entsprechend Ihrem Graphen anpassen
knoten_repraesentiert_gruppe = frozenset({node_a, node_b}) in [data for _, data in quotienten_graph.nodes()]
print("Knoten repräsentiert die korrekte Gruppe bisimilärer Knoten:", knoten_repraesentiert_gruppe)
