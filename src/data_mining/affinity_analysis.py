import numpy as np
from collections import defaultdict
from operator import itemgetter


def print_rule(premise, conclusion, support, confidence, features):
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print("Regla: Si una persona compra {0} también comprará {1}".format(premise_name, conclusion_name))
    print(" - Support: {0}".format(support[(premise, conclusion)]))
    print(" - Confidence: {0:.3f}".format(confidence[(premise, conclusion)]))


if __name__ == "__main__":
    dataset_filename = "datasets\\affinity_dataset.txt"
    x = np.loadtxt(dataset_filename)

    valid_rules = defaultdict(int)
    invalid_rules = defaultdict(int)
    num_occurances = defaultdict(int)

    features = ["pan", "leche", "queso", "manzanas", "plátanos"]

    for sample in x:
        for premise in range(len(features)):
            if sample[premise] == 0:
                continue
            num_occurances[premise] += 1
            for conclusion in range(len(features)):
                if premise == conclusion:
                    continue
                if sample[conclusion] == 1:
                    valid_rules[(premise, conclusion)] += 1
                else:
                    invalid_rules[(premise, conclusion)] += 1

    support = valid_rules
    confidence = defaultdict(float)
    for premise, conclusion in valid_rules.keys():
        rule = (premise, conclusion)
        confidence[rule] = valid_rules[rule] / num_occurances[premise]

    print("Número de compras realizadas: {}".format(len(x)))
    print()

    sorted_support = sorted(support.items(), key=itemgetter(1), reverse=True)
    for index in range(5):
        print("\nRegla nº{0}".format(index + 1))
        premise, conclusion = sorted_support[index][0]
        print_rule(premise, conclusion, support, confidence, features)

    sorted_confidence = sorted(confidence.items(), key=itemgetter(1), reverse=True)
    for index in range(5):
        print("\nRegla nº{0}".format(index + 1))
        premise, conclusion = sorted_confidence[index][0]
        print_rule(premise, conclusion, support, confidence, features)