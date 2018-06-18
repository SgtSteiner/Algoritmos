import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


class Montecarlo:
    def __init__(self, initial_features, initial_projects):
        self.features = initial_features
        self.projects = initial_projects
        self.results = []
        self.hist = {}

    def run(self):
        for _ in range(self.projects):
            acum = 0
            sprints = 0
            while acum < self.features:
                sprints += 1
                acum += random.randint(1, 6)
            self.results.append(sprints)

        self.hist = Counter(self.results)

    def print_results(self):
        for sprints, percentage in sorted([(key, self.hist[key] / self.projects) for key in self.hist]):
            print("{}\t{:>7.3%}".format(sprints, percentage))

        print("Media = {0:.0f}".format(np.mean(self.results)))
        print("85% quantile = {0:.0f}".format(np.percentile(self.results, 85)))

    def draw_histogram(self):
        plt.hist(self.results, bins=len(self.hist), alpha=1, edgecolor='black', linewidth=1)
        plt.axvline(np.percentile(self.results, 85), color='r', linestyle='dashed', linewidth=2)
        plt.xlabel("Nº sprints")
        # plt.grid(True)
        plt.show()
        plt.clf()

    def draw_bar(self):
        plt.bar(self.hist.keys(), [value/self.projects for value in self.hist.values()])
        plt.suptitle("Método Montecarlo")
        plt.title("Probabilidad de finalizar {0} features tras {1:,} iteraciones".format(
            self.features, self.projects).replace(",", ".")
        )
        plt.ylabel("Probabilidad")
        plt.xlabel("Nº de sprints")
        plt.show()
        plt.clf()


if __name__ == '__main__':
    USER_STORIES = 30   # Number of user stories per project
    PROJECTS = 500000   # Number of projects to be executed

    mc = Montecarlo(USER_STORIES, PROJECTS)
    mc.run()
    mc.print_results()
    # mc.draw_histogram()
    mc.draw_bar()
