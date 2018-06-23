import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


class Montecarlo:
    def __init__(self, us_low, us_high, initial_projects):
        self.user_stories_low = us_low
        self.user_stories_high = us_high
        self.projects = initial_projects
        self.results = []
        self.hist = {}

    def run(self, min_throughput=1, max_throughput=6):
        for _ in range(self.projects):
            acum = 0
            sprints = 0
            user_stories = random.randint(self.user_stories_low, self.user_stories_high)
            while acum < user_stories:
                sprints += 1
                acum += random.randint(min_throughput, max_throughput)
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
        plt.suptitle("Método Montecarlo")
        plt.xlabel("Nº de sprints")
        # plt.grid(True)
        plt.show()
        plt.clf()

    def draw_bar(self):
        plt.bar(self.hist.keys(), [value/self.projects for value in self.hist.values()])
        plt.axvline(np.percentile(self.results, 85), color='r', linestyle='dashed', linewidth=2, label="85%")
        # plt.text(np.mean(self.results), max(self.hist.values())/self.projects + 0.01, "Media", fontsize=10, horizontalalignment='center', verticalalignment='center')
        plt.suptitle("Método Montecarlo")
        plt.title("Probabilidad de finalizar entre {0} y {1} HU tras {2:,} iteraciones".format(
            self.user_stories_low, self.user_stories_high, self.projects).replace(",", ".")
        )
        plt.ylabel("Probabilidad")
        plt.xlabel("Nº de sprints")
        plt.show()
        plt.clf()


if __name__ == '__main__':
    USER_STORIES_LOW_ESTIMATED = 20   # Number of user stories to be completed (low bound)
    USER_STORIES_HIGH_ESTIMATED = 30  # Number of user stories to be completed (high bound)
    PROJECTS = 500000   # Number of projects to be executed

    THROUGHPUT_LOW_BOUND = 1   # Lowest throughput estimate
    THROUGHPUT_HIGH_BOUND = 5  # Higuest throughput estimate

    mc = Montecarlo(USER_STORIES_LOW_ESTIMATED, USER_STORIES_HIGH_ESTIMATED, PROJECTS)
    mc.run(THROUGHPUT_LOW_BOUND, THROUGHPUT_HIGH_BOUND)
    mc.print_results()
    # mc.draw_histogram()
    mc.draw_bar()
