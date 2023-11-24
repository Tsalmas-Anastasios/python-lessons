'''  Κώδικας που χρειάζεται περισσότερα iterations
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("winequality-white.csv", sep=";")

df_features = df.drop(columns='quality')

df_label = df['quality']


 
X_train, X_test, y_train, y_test = train_test_split(df_features, df_label, test_size=0.20)


logisticRegression = LogisticRegression()
logisticRegression.fit(X_train, y_train)

logisticRegression.score(X_test, y_test)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler  # Import the StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.tree import plot_tree

# Load the dataset
df = pd.read_csv("winequality-white.csv", sep=";")

# Prepare the features and labels
df_features = df.drop(columns='quality')
df_label = df['quality']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df_features, df_label, test_size=0.20)

# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Create and train the logistic regression model
logisticRegression = LogisticRegression(max_iter=1000)
logisticRegression.fit(X_train, y_train)

# Predict the probability for the first sample in the test set
predicted_prob = logisticRegression.predict_proba(X_test[:1])  # Use array slicing instead of .iloc

# Print the predicted probabilities
#print("Predicted Probabilities for the First Sample:")
#print(predicted_prob)
print(y_test.iloc[:1])

from sklearn import svm
 
SVM = svm.SVC()
SVM.fit(X_train, y_train)
# Και η βαθμολογία που έλαβε:
 
svm_score = SVM.score(X_test, y_test)
print(svm_score)


from sklearn.linear_model import SGDClassifier

SGD = SGDClassifier()
SGD.fit(X_train, y_train)
# Και η βαθμολογία που λαμβάνουμε είναι:
sgd_score = SGD.score(X_test, y_test)
print(sgd_score)
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

# Φόρτωση του dataset
df = pd.read_csv("winequality-white.csv", sep=";")

# Προετοιμασία χαρακτηριστικών κι ετικετών
df_features = df.drop(columns='quality')
df_label = df['quality']

# Διαχωρισμός δεδομένων για εκπαιδευση και τεστ
X_train, X_test, y_train, y_test = train_test_split(df_features, df_label, test_size=0.20)

# Επαυξηση των δεδομένων με το StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Δημιουργία ταξινοξητικού δένδρου αποφάσεων
decisionTree = DecisionTreeClassifier()
decisionTree.fit(X_train, y_train)

# Γράφημα δένδρου
plt.figure(figsize=(16, 8))

# Εμφάνιση του γραφήματος με διασαφήνιση των παραμέτρων
plot_tree(decisionTree,
          filled=True,
          rounded=True)

# Display the plot
plt.show()
