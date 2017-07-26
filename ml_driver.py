import pandas as pd
import numpy as np
from aggregate_funcs import *
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score, log_loss
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression


titanic_data=load_titanic_data()

titanic_data=aggregate_one(titanic_data)

classifiers = [
    KNeighborsClassifier(3),
    SVC(probability=True),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
	AdaBoostClassifier(),
    GradientBoostingClassifier(),
    GaussianNB(),
    LinearDiscriminantAnalysis(),
    QuadraticDiscriminantAnalysis(),
    LogisticRegression()]


X=titanic_data.drop('Survived', axis=1).as_matrix()
y=titanic_data["Survived"].as_matrix()

sss=StratifiedShuffleSplit(n_splits=10, test_size=0.1, random_state=0)
scores=np.array([])
for classifier in classifiers:
    classifier_score=np.array([])
    for train_index, test_index in sss.split(X,y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        classifier.fit(X_train, y_train)
        classifier_score=np.append(classifier_score, classifier.score(X_test, y_test))
    scores=np.append(scores, classifier_score.mean())
print scores
    





