# ==========================================================
# EXPLAINABLE AI REASONING ENGINE
# Integrates CO1 to CO6
# ==========================================================

import heapq

# ==========================================================
# CO1 - RULE BASED KNOWLEDGE REPRESENTATION
# ==========================================================

class RuleEngine:

    def __init__(self):
        self.rules = []

    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))

    def infer(self, facts):
        explanations = []

        changed = True

        while changed:
            changed = False

            for condition, conclusion in self.rules:

                if condition in facts and conclusion not in facts:
                    facts.add(conclusion)

                    explanations.append(
                        f"Rule Applied: '{condition}' → '{conclusion}'"
                    )

                    changed = True

        return facts, explanations


# ==========================================================
# CO2 - A* SEARCH
# ==========================================================

class AStarSearch:

    def __init__(self):

        self.graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'D': 2},
            'C': {'D': 1},
            'D': {}
        }

        self.heuristic = {
            'A': 3,
            'B': 2,
            'C': 1,
            'D': 0
        }

    def search(self, start, goal):

        pq = [(0, start, [])]
        visited = set()
        trace = []

        while pq:

            cost, node, path = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)

            path = path + [node]

            trace.append(f"Expanded Node: {node}")

            if node == goal:
                return path, trace

            for neigh, edge_cost in self.graph[node].items():

                f = cost + edge_cost + self.heuristic[neigh]

                heapq.heappush(
                    pq,
                    (f, neigh, path)
                )

        return None, trace


# ==========================================================
# CO3 - CSP USING MRV
# ==========================================================

class CSP_MRV:

    def __init__(self):

        self.variables = {
            'A': [1, 2, 3],
            'B': [1, 2, 3],
            'C': [1, 2, 3]
        }

        self.assignment = {}

    def is_valid(self, value):
        return value not in self.assignment.values()

    def select_mrv(self):

        unassigned = [
            v for v in self.variables
            if v not in self.assignment
        ]

        return min(
            unassigned,
            key=lambda x: len(self.variables[x])
        )

    def backtrack(self):

        if len(self.assignment) == len(self.variables):
            return True

        var = self.select_mrv()

        for value in self.variables[var]:

            if self.is_valid(value):

                self.assignment[var] = value

                if self.backtrack():
                    return True

                del self.assignment[var]

        return False

    def solve(self):
        self.backtrack()
        return self.assignment


# ==========================================================
# CO4 - MINIMAX
# ==========================================================

class Minimax:

    def __init__(self):

        self.tree = {
            'A': ['B', 'C'],
            'B': [3, 5],
            'C': [2, 9]
        }

        self.trace = []

    def minimax(self, node, maximizing):

        if isinstance(node, int):
            return node

        children = self.tree[node]

        if maximizing:

            values = [
                self.minimax(child, False)
                for child in children
            ]

            best = max(values)

            self.trace.append(
                f"MAX at {node} chooses {best}"
            )

            return best

        else:

            values = [
                self.minimax(child, True)
                for child in children
            ]

            best = min(values)

            self.trace.append(
                f"MIN at {node} chooses {best}"
            )

            return best

    def solve(self):

        result = self.minimax('A', True)

        return result, self.trace


# ==========================================================
# CO5 - BAYESIAN REASONING
# ==========================================================

class BayesianReasoner:

    def calculate(self):

        prior = 0.01
        likelihood = 0.95
        evidence = 0.05

        posterior = (
            likelihood * prior
        ) / evidence

        explanation = f"""
Prior Probability      = {prior}
Likelihood             = {likelihood}
Evidence               = {evidence}
Posterior Probability  = {round(posterior,4)}
"""

        return posterior, explanation


# ==========================================================
# CO6 - HYBRID EXPLAINABLE AI REASONING ENGINE
# ==========================================================

class ExplainableAIEngine:

    def __init__(self):

        self.trace = []

    def run(self):

        print("\n==============================")
        print(" EXPLAINABLE AI REASONING ")
        print("==============================")

        # -----------------------------------
        # CO1 Rule Based Reasoning
        # -----------------------------------

        print("\n[CO1] Rule-Based Reasoning")

        rule_engine = RuleEngine()

        rule_engine.add_rule(
            "rainy",
            "carry_umbrella"
        )

        rule_engine.add_rule(
            "carry_umbrella",
            "stay_dry"
        )

        facts = {"rainy"}

        facts, rule_trace = rule_engine.infer(facts)

        print("Facts:", facts)

        self.trace.extend(rule_trace)

        # -----------------------------------
        # CO2 A* Search
        # -----------------------------------

        print("\n[CO2] A* Search")

        astar = AStarSearch()

        path, astar_trace = astar.search(
            'A',
            'D'
        )

        print("Optimal Path:", path)

        self.trace.extend(astar_trace)

        # -----------------------------------
        # CO3 CSP MRV
        # -----------------------------------

        print("\n[CO3] CSP with MRV")

        csp = CSP_MRV()

        solution = csp.solve()

        print("Assignment:", solution)

        self.trace.append(
            f"CSP Solution Found: {solution}"
        )

        # -----------------------------------
        # CO4 Minimax
        # -----------------------------------

        print("\n[CO4] Minimax Decision")

        game = Minimax()

        utility, game_trace = game.solve()

        print("Utility Value:", utility)

        self.trace.extend(game_trace)

        # -----------------------------------
        # CO5 Bayesian Reasoning
        # -----------------------------------

        print("\n[CO5] Bayesian Inference")

        bayes = BayesianReasoner()

        posterior, bayes_exp = bayes.calculate()

        print(
            "Posterior Probability:",
            round(posterior, 4)
        )

        self.trace.append(
            f"Bayesian Confidence = {round(posterior,4)}"
        )

        # -----------------------------------
        # FINAL DECISION
        # -----------------------------------

        decision = (
            "Carry Umbrella"
            if posterior > 0.1
            else "No Action"
        )

        self.trace.append(
            f"Final Decision = {decision}"
        )

        # -----------------------------------
        # EXPLANATION TRACE
        # -----------------------------------

        print("\n==============================")
        print(" EXPLANATION TRACE ")
        print("==============================")

        for step in self.trace:
            print("•", step)

        print("\nFinal Decision:", decision)
        print("Confidence:", round(posterior, 4))


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    engine = ExplainableAIEngine()

    engine.run()