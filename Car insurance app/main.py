from fastapi import FastAPI, HTTPException, Path
from schema import PredictionResult
from load_models import load_model
import pandas as pd

try:
    features = pd.read_csv('data_car_insurance.csv')
except FileNotFoundError:
    raise RuntimeError("CSV file not found.Please check the file path")

try:
    model = load_model()
except Exception as e:
    raise RuntimeError(f'Failed to load model: {str(e)}')


app = FastAPI()

@app.get("/car/insurance/predictions/{policy_id}", response_model=PredictionResult,
         summary="Get insurance prediction", description="Returns insurance risk prediction for specified policy ID")
def prediction_by_ID(policy_id: str = Path(..., title="Policy ID", description="ID from your dataset like ID00001, ID00002 etc.")):

    try:
        record = features[features['policy_id'] == policy_id]
        if record.empty:
            raise HTTPException(status_code=404, detail='Policy ID not found')

        data = ['policy_tenure', 'age_of_car', 'age_of_policyholder',
            'population_density', 'make', 'displacement', 'cylinder', 'gear_box',
            'turning_radius', 'ncap_rating', 'fuel_type_Diesel', 'fuel_type_Petrol',
             'transmission_type_Manual', 'steering_type_Manual', 'steering_type_Power',
            'is_power_door_locks_Yes', 'is_day_night_rear_view_mirror_Yes', 'safety_features_count',
            'comfort_features_count', 'volume']

        input_data = record[data]

        prediction = model.predict(input_data)[0]

        try:
            probability = model.predict_proba(input_data)[0][1]
        except AttributeError:
            probability = None

        prediction_str = ''
        if prediction==0:
            prediction_str = 'Низкий риск страхового случая'
        elif prediction==1:
            prediction_str = 'Высокий риск страхового случая'


        probability_str = f'Вероятность принадлежать к классу риска: {probability * 100:.2f}%'

        return PredictionResult(id=policy_id, prediction=prediction_str, probability=probability_str)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# uvicorn app.main:app --reload