import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class City:
    def __init__(self, city, state, data):
        self.city = city
        self.state = state
        self.df = data[(data['RegionName'] == self.city) \
                       & (data['State'] == self.state)]
        self.price_arr = self.df.iloc[:, 8:].values.flatten()
        

    def most_recent_price(self):
        recent_time = self.df.columns[-1]
        recent_price = self.price_arr[-1]
        return {recent_time: f'${recent_price:,.0f}'}


    def linearity_score(self, plot = False):
        # Prepare data 
        y = self.price_arr[~np.isnan(self.price_arr)]
        X = (np.arange(len(y)) + 1).reshape(-1, 1)

        # Fit a linear regression model to the data
        model = LinearRegression()
        model.fit(X, y)

        # Predict the values for the input data
        y_pred = model.predict(X)

        # Get R2 score
        r2 = round(model.score(X, y), 2)

        # Plot the data and the fitted line
        if plot:
            plt.scatter(X, y, color="b")
            plt.plot(X, y_pred, color="k")
            plt.title(f'R2 Score for {self.city}, {self.state}: {r2}')
            plt.xlabel("Time")
            plt.ylabel("Price")
            plt.show()

        return r2
    