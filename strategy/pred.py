import matplotlib.pyplot as plt
import random

def show_predictions(models, X_test, y_test, index=None):
    if index is None:
        index = random.randint(0, len(X_test) - 1)

    image = X_test[index].reshape(8, 8)  
    true_label = y_test[index]

    model_names = ['Logistic Regression', 'Random Forest', 'SVM']
    predictions = []
    for model in models:
        pred = model.predict([X_test[index]])[0]
        predictions.append(pred)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(image, cmap='gray')
    ax.axis('off')

    ax.set_title(f"True Label: {true_label}", fontsize=16)

    full_text = "\n".join([f"{name}: {pred}" for name, pred in zip(model_names, predictions)])
    plt.figtext(0.5, 0.01, full_text, wrap=True, horizontalalignment='center', fontsize=12, backgroundcolor='white')

    plt.show()

