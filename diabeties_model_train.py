import pandas as pd
import joblib as jb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import SMOTE

#load dataset
df = pd.read_csv("Datasets\diabetes.csv")

x= df.drop("Outcome",axis=1)
y = df["Outcome"]


#without smote
x_train, x_test, y_train, y_test  = train_test_split(x,y,test_size= 0.2, random_state= 42)

#train decision tree
model = DecisionTreeClassifier(criterion= 'gini', max_depth=4,random_state=42)
model.fit(x_train,y_train)


#using smote

# x_train, x_test, y_train, y_test  = train_test_split(x,y,test_size= 0.3, random_state= 42,stratify=y)

# smote = SMOTE(random_state=42)
# x_train_resampled ,y_train_resampled = smote.fit_resample(x_train,y_train)
# #train decision tree
# model = DecisionTreeClassifier(criterion= 'gini', max_depth=5,random_state=42)
# model.fit(x_train_resampled,y_train_resampled)


#evaluate
y_pred = model.predict(x_test)
print(f"Accuracy:{accuracy_score(y_test,y_pred)*100:}%")

#save model
jb.dump(model,"models\decisiontree_model.pkl")
print("Model saved as decisiontree_model.pkl ")
