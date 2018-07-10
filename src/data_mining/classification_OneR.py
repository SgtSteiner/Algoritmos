from collections import defaultdict
from operator import itemgetter
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split



def train_feature_value(x, y_true, feature_index, value):
    class_counts = defaultdict(int)

    for sample, y in zip(x, y_true):
        if sample[feature_index] == value:
            class_counts[y] += 1

    sorted_class_counts = sorted(class_counts.items(), key=itemgetter(1), reverse=True)
    most_frequent_class = sorted_class_counts[0][0]

    incorrect_predictions = [class_count for class_value, class_count
                             in class_counts.items()
                             if class_value != most_frequent_class]
    error = sum(incorrect_predictions)

    return most_frequent_class, error


def train_on_feature(x, y_true, feature_index):
    values = set(x[:, feature_index])
    predictors = {}
    errors = []

    for current_value in values:
        most_frequent_class, error = train_feature_value(x, y_true, feature_index, current_value)
        predictors[current_value] = most_frequent_class
        errors.append(error)

    total_error = sum(errors)
    return predictors, total_error


def predict(x_test, model):
    variable = model['variable']
    predictor = model['predictor']
    y_predicted = np.array([predictor[int(sample[variable])] for sample in x_test])
    return y_predicted


dataset = load_iris()
x = dataset.data
y = dataset.target

attribute_means = x.mean(axis=0)
x_d = np.array(x >= attribute_means, dtype='int')

xd_train, xd_test, y_train, y_test = train_test_split(x_d, y, random_state=14)

all_predictors = {}
errors = {}

for feature_index in range(xd_train.shape[1]):
    predictors, total_error = train_on_feature(xd_train, y_train, feature_index)
    all_predictors[feature_index] = predictors
    errors[feature_index] = total_error

best_feature, best_error = sorted(errors.items(), key=itemgetter(1))[0]
model = {'feature': best_feature, 'predictor': all_predictors[best_feature][0]}

y_predicted = predict(xd_test, model)
accuracy = np.mean(y_predicted == y_test) * 100
print("The test accuracy is {:.1f}%".format(accuracy))
