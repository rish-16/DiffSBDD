import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

ratios = []
for i in range(5000):
    nnodes = random.randint(11, 200)
    nedges = random.randint(4, 10)
    a, b = np.random.uniform(), np.random.uniform()

    try:
        graph_choices = [
            nx.complete_graph(nnodes),
            nx.stochastic_block_model([nnodes//2, nnodes//2], [[a, b], [b, a]]),
            nx.lollipop_graph(nnodes, nnodes//2),
            nx.barabasi_albert_graph(nnodes, nedges),
            nx.stochastic_block_model([nnodes//2, nnodes//2], [[b, a], [a, b]]),
            nx.erdos_renyi_graph(nnodes, p=np.random.uniform())
        ]

        G = random.choice(graph_choices)
        diam_G = nx.diameter(G)
        apg_G = nx.average_shortest_path_length(G,)

        ratio = diam_G / apg_G
        ratios.append(ratio)
    except Exception as e:
        print (e, G)

plt.hist(ratios, bins=25, color="orange")
plt.grid()
plt.xlabel("diam(G) / apg(G)")
plt.ylabel("Frequency")
plt.show()

plt.hist(ratios, bins=15, color="blue")
plt.grid()
plt.xlabel("diam(G) / apg(G)")
plt.ylabel("Frequency")
plt.show()

plt.hist(ratios, bins=10, color="green")
plt.grid()
plt.xlabel("diam(G) / apg(G)")
plt.ylabel("Frequency")
plt.show()