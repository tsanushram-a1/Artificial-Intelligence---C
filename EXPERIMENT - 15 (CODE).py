from sklearn.tree import DecisionTreeClassifier
X = [[1], [2], [3], [4], [5], [6]]

y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=0)

model.fit(X, y)

hours = [[4]]
result = model.predict(hours)

if result[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")

