import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    distance = np.sqrt(np.sum((x1-x2)**2))
    return distance
class KNN:
    def _init_(self, k=3):
        self.k = k
    def fit():
        self.x_train = x
        self.y_train = y
    
    def predict (self, x):
        predictions = [self._predict(x) for x in x]
        return predictions

    def _predict(self, x): 
        # compute the distance
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        # get the closet k
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labes = [self.y_train[i] for i in k_indices]

        # majority voye
        most_common = counter(k_nearest_labes).most_common()
        return most_common [0] [0] 
    
# USING ALGORITHM   
# Returns list of counts of all instances "times occured, Name of list" 
# clf = KNN (k=5)
# from KNN import KNN
# clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)
# print(predictions)
# Accuracy Test
# acc = np.sum(predictions == y_test) /len(y_test)
# print(acc)