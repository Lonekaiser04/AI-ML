from sklearn.neighbors import KNeighborsClassifier

X = [
    [140,40],
    [150,50],
    [150,55],
    [153,58],
    [155,60],
    [160,50],
    [170,60],
    [175,65],
    [180,70],
    [180,75]
]

y = [1,1,0,0,0,1,1,0,1,1]

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X,y)

height = float(input("enter Height of a person:"))
weight = float(input("enter weight of a person:"))
new_sample = [[height,weight]]

pred_class = knn.predict(new_sample)

print(f"predicted class for {new_sample} is :","boy" if pred_class == 1 else "girl")


