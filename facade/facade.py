import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split


class DataGenerator:
    def generate_data(self, n_samples=100, n_features=1, noise=10):
        X, y = make_regression(n_samples=n_samples, 
                              n_features=n_features, 
                              noise=noise, 
                              random_state=42)
        return X, y
    
    def split_data(self, X, y, test_size=0.2):
        return train_test_split(X, y, test_size=test_size, random_state=42)



class LinearRegressionModel:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def train(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        costs = []

        for i in range(self.iterations):
            y_pred = np.dot(X, self.weights) + self.bias

            # gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred-y))
            db = (1/n_samples) * np.sum(y_pred - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            cost = (1/(2*n_samples)) * np.sum((y_pred - y)**2)
            costs.append(cost)

        return {"weights": self.weights, "bias": self.bias, "costs": costs}

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


class Visualizer:
    def visualize_results(self, X_train, y_train, X_test, y_test, y_pred_train, y_pred_test, costs, model):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
        ax1.scatter(X_train, y_train, color='blue', label='Training data')
        ax1.scatter(X_test, y_test, color='green', label='Testing data')
        
        X_line = np.concatenate([X_train, X_test])
        X_line = np.sort(X_line, axis=0)
        y_line = model.predict(X_line)
        
        ax1.plot(X_line, y_line, color='red', linewidth=2, label='Regression line')
        ax1.set_title('Linear Regression Fit')
        ax1.set_xlabel('X')
        ax1.set_ylabel('y')
        ax1.legend()
        
        ax2.plot(range(len(costs)), costs)
        ax2.set_title('Cost History During Training')
        ax2.set_xlabel('Iterations')
        ax2.set_ylabel('Cost')
        
        plt.tight_layout()
        plt.show()


class MLFacade:
    def __init__(self) -> None:
        self.data_generator = DataGenerator()
        self.model = LinearRegressionModel(learning_rate=.01, iterations=1000)
        self.visualizer = Visualizer()

    def train_model(self):
        X, y = self.data_generator.generate_data(n_samples=50, noise=2)
        X_train, X_test, y_train, y_test = self.data_generator.split_data(X, y)

        results = self.model.train(X_train, y_train)
        y_pred_train = self.model.predict(X_train)
        y_pred_test = self.model.predict(X_test)

        self.visualizer.visualize_results(X_train, y_train, X_test, y_test, y_pred_train, y_pred_test, results["costs"], self.model)



if __name__ == "__main__":
    ml_facade = MLFacade()
    ml_facade.train_model()
        
