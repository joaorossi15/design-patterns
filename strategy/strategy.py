from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from pred import show_predictions

class ModelTrainingStrategy():
    def train(self, X_train, y_train):
        pass

class LogisticRegressionStrategy(ModelTrainingStrategy):
    def train(self, X_train, y_train):
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)
        return model

class RandomForestStrategy(ModelTrainingStrategy):
    def train(self, X_train, y_train):
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        return model

class SVMStrategy(ModelTrainingStrategy):
    def train(self, X_train, y_train):
        model = SVC()
        model.fit(X_train, y_train)
        return model

class ModelTrainer:
    def __init__(self, strategy: ModelTrainingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ModelTrainingStrategy):
        self._strategy = strategy

    def train_model(self, X_train, y_train):
        return self._strategy.train(X_train, y_train)

if __name__ == "__main__":
    digits = load_digits()
    X_train, X_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.3, random_state=42
    )

    trainer = ModelTrainer(LogisticRegressionStrategy())
    model_lr = trainer.train_model(X_train, y_train)
    preds = model_lr.predict(X_test)
    print(f"lr accuracy: {accuracy_score(y_test, preds):.2f}")
    print()

    trainer.set_strategy(RandomForestStrategy())
    model_rf = trainer.train_model(X_train, y_train)
    preds = model_rf.predict(X_test)
    print(f"rf accuracy: {accuracy_score(y_test, preds):.2f}")
    print()

    trainer.set_strategy(SVMStrategy())
    model_svm = trainer.train_model(X_train, y_train)
    preds = model_svm.predict(X_test)
    print(f"svm accuracy: {accuracy_score(y_test, preds):.2f}")
    print()

    models = [model_lr, model_rf, model_svm]
    show_predictions(models, X_test, y_test)
