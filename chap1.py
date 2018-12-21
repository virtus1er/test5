from sklearn import load_iris

iris_dataset = load_iris()

print(iris_dataset)
#
# print("Keys of iris_dataset:\n", iris_dataset.keys())

print(iris_dataset['DESCR'][:193] + "\n...")

print("Target names:", iris_dataset['target_names'])