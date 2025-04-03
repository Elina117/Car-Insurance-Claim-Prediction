import pickle

def load_model():
    # Получаем путь к модели
    model_path = "models/LightGB_model.pkl"

    # Открываем файл с моделью для чтения
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    # Проверяем, что модель имеет необходимые методы
    if not hasattr(model, 'predict') or not hasattr(model, 'predict_proba'):
        raise AttributeError("Модель должна содержать методы 'predict' и 'predict_proba'.")

    return model