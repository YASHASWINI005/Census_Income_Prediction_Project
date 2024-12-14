'''import pandas as pd
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained pipeline
pipeline = joblib.load("logistic_pipeline.pkl")

# List the features in the same order they were used during training
training_columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education.num', 'marital.status',
    'occupation', 'relationship', 'race', 'sex', 'capital.gain', 'capital.loss',
    'hours.per.week', 'native.country'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        input_data = request.get_json(force=True)
        
        # Convert the input data to a DataFrame
        input_df = pd.DataFrame(input_data, index=[0])
        
        # Ensure the input data has the same columns as the training data
        # Reorder the columns to match the model's expected feature order
        input_df = input_df[training_columns]  # Reorder columns

        # Handle missing values (fill with the most frequent value, like in training)
        for col in ['workclass', 'occupation', 'native.country']:
            input_df[col] = input_df[col].fillna(input_df[col].mode()[0])

        # Use the pipeline to process the input data (apply encoding and scaling)
        transformed_input = pipeline.named_steps['encoder'].transform(input_df)
        transformed_input = pipeline.named_steps['scaler'].transform(transformed_input)

        # Make prediction using the model
        prediction = pipeline.named_steps['model'].predict(transformed_input)
        
        # Map prediction to a human-readable label
        result = {
            'prediction': int(prediction[0]),
            'income_class': '>50K' if prediction[0] == 1 else '<=50K'
        }
        return jsonify(result)
    
    except Exception as e:
        # Handle any exceptions and return a meaningful error message
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
'''




