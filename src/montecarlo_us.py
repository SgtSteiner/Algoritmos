import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def draw_histogram(ar):
    plt.hist(ar, bins=50, alpha=1, edgecolor='black', linewidth=1)
    plt.axvline(np.percentile(ar, 5), color='r', linestyle='dashed', linewidth=2)
    plt.axvline(np.percentile(ar, 95), color='r', linestyle='dashed', linewidth=2)
    # plt.grid(True)
    plt.show()
    plt.clf()


def montecarlo(initial_us, initial_projects):
    user_stories = initial_us
    projects = initial_projects
    results = []

    for _ in range(projects):
        acum = 0
        sprints = 0
        while acum < user_stories:
            sprints += 1
            acum += random.randint(1, 6)
        results.append(sprints)

    hist = Counter(results)
    for sprint, percentage in sorted([(key, hist[key]/initial_projects) for key in hist]):
        print("{}\t{:>7.3%}".format(sprint, percentage))

    print("Media = {0:.0f}".format(np.mean(results)))
    print(" 5% quantile = {0:.0f}".format(np.percentile(results, 5)))
    print("95% quantile = {0:.0f}".format(np.percentile(results, 95)))

    return results


if __name__ == '__main__':
    USER_STORIES = 30   # Number of user stories per project
    PROJECTS = 50000   # Number of projects to be executed

    draw_histogram(montecarlo(USER_STORIES, PROJECTS))
