import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class GamblerRuinDTMC:
    def __init__(self, N, p):
        self.N = N
        self.p = p
        self.q = 1 - p
        self.states = list(range(N + 1))
        self.P = self._build_transition_matrix()

    def _build_transition_matrix(self):
        P = np.zeros((self.N + 1, self.N + 1))
        for i in range(1, self.N):
            P[i][i + 1] = self.p
            P[i][i - 1] = self.q
        P[0][0] = 1.0  # absorbing at 0
        P[self.N][self.N] = 1.0  # absorbing at N
        return P

    def simulate(self, start, steps):
        state = start
        path = [state]
        for _ in range(steps):
            if state == 0 or state == self.N:
                break
            state = np.random.choice(self.states, p=self.P[state])
            path.append(state)
        return path

    def plot_chain(self):
        G = nx.DiGraph()
        for i in range(self.N + 1):
            for j in range(self.N + 1):
                if self.P[i][j] > 0:
                    G.add_edge(i, j, weight=round(self.P[i][j], 2))

        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Gambler's Ruin DTMC Transition Graph")
        plt.show()

    def steady_state(self):
        eigvals, eigvecs = np.linalg.eig(self.P.T)
        stat_dist = np.array(eigvecs[:, np.isclose(eigvals, 1)])
        stat_dist = stat_dist[:,0]
        stat_dist = stat_dist / stat_dist.sum()
        return stat_dist.real

    def ruin_probability(self, start):
        # Exact probability that gambler reaches 0 before N
        if self.p == self.q:
            return (self.N - start) / self.N
        else:
            r = self.q / self.p
            return (1 - r**start) / (1 - r**self.N)

# -------------------------------
# Example usage:
model = GamblerRuinDTMC(N=10, p=0.4)
path = model.simulate(start=5, steps=100)
print("Simulated path:", path)
print("Ruin probability from $5:", model.ruin_probability(start=5))
model.plot_chain()
