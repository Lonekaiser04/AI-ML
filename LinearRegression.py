from sklearn.linear_model import LinearRegression

x = [[1],[2],[3],[4]]

y = [20,40,60,80]

model = LinearRegression()

model.fit(x,y)

hours = float(input("Enter how many hours do you study:"))

new_sample = [[hours]]
predic_Class= model.predict(new_sample)

print(f"Based on my prediction i thick you will get :{predic_Class} marks")