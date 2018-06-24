import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime, timedelta


class Montecarlo:
    def __init__(self, us_low, us_high, simulation_max, start_date, throughput_unit):
        self.user_stories_low = us_low
        self.user_stories_high = us_high
        self.simulation_max = simulation_max
        self.star_date = start_date
        self.throughput_unit = throughput_unit
        self.results = []
        self.hist = {}

    def run(self, min_throughput=1, max_throughput=6):
        for _ in range(self.simulation_max):
            acum = 0
            weeks = 0
            user_stories = random.randint(self.user_stories_low, self.user_stories_high)
            while acum < user_stories:
                weeks += 1
                acum += random.randint(min_throughput, max_throughput)
            self.results.append(weeks)

        self.hist = Counter(self.results)

    def print_results(self):
        print("Duración %Prob.")
        print("======== ======")
        for weeks, percentage in sorted([(key, self.hist[key] / self.simulation_max) for key in self.hist]):
            print("{0:^8.0f} {1:>6.2%}".format(weeks, percentage))

        print("\nMedia = {0:.0f}\n".format(np.mean(self.results)))

    def print_quantile(self):
        print("%Prob. Duración   Fecha")
        print("====== ======== ==========")
        for quan in range(100, -5, -5):
            quand_date = self.star_date + timedelta(
                days=round(np.percentile(self.results, quan)) * self.throughput_unit * 7
            )
            print("{0:>5}% {1:^8.0f} {2}".format(
                quan, np.percentile(self.results, quan), quand_date.strftime("%d-%m-%Y")
            ))

    def draw_histogram(self):
        plt.hist(self.results, bins=len(self.hist), alpha=1, edgecolor='black', linewidth=1)
        plt.axvline(np.percentile(self.results, 85), color='r', linestyle='dashed', linewidth=2, label="Percentil 85")
        plt.suptitle("Método Montecarlo")
        plt.title("Frecuencia de finalizar entre {0} y {1} HU tras {2:,} iteraciones".format(
            self.user_stories_low, self.user_stories_high, self.simulation_max).replace(",", ".")
                  )
        plt.ylabel("Frecuencia")
        plt.xlabel("Duración en {0} semanas".format(self.throughput_unit))
        plt.legend()
        # plt.show()

    def draw_bar(self):
        plt.bar(self.hist.keys(), [value / self.simulation_max for value in self.hist.values()])
        plt.axvline(np.percentile(self.results, 85), color='r', linestyle='dashed', linewidth=2, label="Percentil 85")
        plt.suptitle("Método Montecarlo")
        plt.title("Probabilidad de finalizar entre {0} y {1} HU tras {2:,} iteraciones".format(
            self.user_stories_low, self.user_stories_high, self.simulation_max).replace(",", ".")
        )
        plt.ylabel("Probabilidad")
        plt.xlabel("Duración en {0} semanas".format(self.throughput_unit))
        plt.legend()
        # plt.show()


if __name__ == '__main__':
    USER_STORIES_LOW_ESTIMATED = 30   # Number of user stories to be completed (low bound)
    USER_STORIES_HIGH_ESTIMATED = 30  # Number of user stories to be completed (high bound)
    SIMULATION_MAX = 5000   # Number of projects to be executed

    THROUGHPUT_LOW_BOUND = 1   # Lowest throughput estimate
    THROUGHPUT_HIGH_BOUND = 5  # Higuest throughput estimate

    THROUGHPUT_UNIT = 1        # Throughput/Velocity per weeks or per sprint

    START_DATE = datetime.now()  # First day of the forecast

    mc = Montecarlo(USER_STORIES_LOW_ESTIMATED, USER_STORIES_HIGH_ESTIMATED, SIMULATION_MAX, START_DATE, THROUGHPUT_UNIT)
    mc.run(THROUGHPUT_LOW_BOUND, THROUGHPUT_HIGH_BOUND)
    mc.print_results()
    mc.print_quantile()

    # Show the graphs
    plt.subplot(1, 2, 1)
    mc.draw_histogram()
    plt.subplot(1, 2, 2)
    mc.draw_bar()
    plt.show()
