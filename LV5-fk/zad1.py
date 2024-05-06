import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn . metrics import accuracy_score
from sklearn . metrics import confusion_matrix , ConfusionMatrixDisplay, classification_report
from sklearn . linear_model import LogisticRegression
from matplotlib.colors import ListedColormap


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#a
X_train_tsposed = np.transpose(X_train)
X_test_tsposed = np.transpose(X_test)
plt.scatter(x = X_train_tsposed[0], y = X_train_tsposed[1], s = 30, c = y_train, cmap = 'viridis', label = 'Training')
plt.scatter(x = X_test_tsposed[0], y = X_test_tsposed[1], s = 30, c = y_test, marker = 'x', cmap = 'viridis', label = 'Test')
plt.legend()
plt.colorbar()
plt.xlabel('x1')
plt.ylabel('x2')

#b
LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)

#c
t0 = LogRegression_model.intercept_[0]
t1, t2 = LogRegression_model.coef_.T
plt.figure()
plt.scatter(x = X_train_tsposed[0], y = X_train_tsposed[1], s = 30, c = y_train, cmap = 'viridis', label = 'Training')
plt.colorbar()
plt.xlabel('x1')
plt.ylabel('x2')
decision_values = - ((t0 / t2) + X_train_tsposed[0] * (t1 / t2))
plt.plot(X_train_tsposed[0], decision_values)

#d
y_testp = LogRegression_model.predict(X_test)
cm = confusion_matrix(y_test, y_testp)
disp = ConfusionMatrixDisplay ( confusion_matrix (y_test , y_testp))
disp.plot ()
print(classification_report(y_test, y_testp))

#e
plt.figure()
true = np.where(y_test == y_testp)
false = np.where(y_test != y_testp)
plt.scatter(x = X_test_tsposed[0, true], y = X_test_tsposed[1, true], s = 30, c = 'green')
plt.scatter(x = X_test_tsposed[0, false], y = X_test_tsposed[1, false], s = 30, c = 'black')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()