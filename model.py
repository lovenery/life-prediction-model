import os.path as path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pickle

# Read CSV
df = pd.read_csv(path.join(path.dirname(__file__), './data/result.csv'))

# Plot
# import matplotlib.pyplot as plt
# df.hist()
# plt.show()

# Split
feature_column_name = ['county', 'sex', 'cause']
label_column_name = ['age']
X = df[feature_column_name].as_matrix()
y = df[label_column_name].as_matrix()
y = y.ravel() # y.ravel() or y.flatten() or y.reshape(y.shape[0],)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=0)

# Model
rfc = RandomForestClassifier(n_estimators=10, n_jobs=2)
rfc.fit(X_train, y_train)

# Test
# print "Accuracy = %0.3f" % accuracy_score(y_test, rfc.predict(X_test))
# print classification_report(y_test, rfc.predict(X_test))
# print rfc.predict([[1, 1, 37]]) # 2
# for i in range(1, 42):
#     print i, rfc.predict([[1, 1, i]])

# Output
output_file = path.join(path.dirname(__file__), './web/rfc.pkl')
pickle.dump(rfc, open(output_file, "wb"))
