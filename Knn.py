from sklearn.neighbors import KNeighborsClassifier

x = [
    [150,50],
    [160,60],
    [170,70],
    [180,80],
    [190,90]
]
y = [0,0,1,1,1]

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(x,y)
height = float(input("enter Height of a person:"))
weight = float(input("enter weight of a person:"))
new_sample = [[height,weight]]

predicted_class = knn.predict(new_sample)

print(f"predicted class for {new_sample[0]} is:","tall" if predicted_class[0] == 1 else "short")