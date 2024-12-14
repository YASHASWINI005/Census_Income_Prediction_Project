from flask import Flask, render_template, request
from flask_cors import CORS
import pandas as pd
import joblib
import sys

# Add the folder containing your custom module to sys.path
sys.path.append(r'D:\AIP Project\database')
from storage_predictions import store_in_excel  # Custom module for storing predictions

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})

# Load the trained model pipeline
model_pipeline = joblib.load("logistic_pipeline.pkl")

# Define the training column order (same as used in your model)
training_columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education.num', 'marital.status',
    'occupation', 'relationship', 'race', 'sex', 'capital.gain', 'capital.loss', 'hours.per.week','native.country'
]

@app.route('/')
def index():
    return render_template('index.html', prediction=None, error=None, form_data={})

@app.route('/predict', methods=['POST'])
def predict():
    action = request.form.get('action', 'add')  # Default action is 'add'

    if action == 'clear':
        # Clear form and prediction data
        return render_template('index.html', prediction=None, error=None, form_data={}, cleared=True)

    try:
        # Extract form inputs and validate for missing values
        input_data = {
            'age':int(request.form.get('age')),
            'workclass': request.form.get('workclass'),
            'fnlwgt': int(request.form.get('fnlwgt')),
            'education': request.form.get('education'),
            'education.num': int(request.form.get('education.num')),
            'marital.status': request.form.get('marital.status'),
            'occupation': request.form.get('occupation'),
            'relationship': request.form.get('relationship'),
            'race': request.form.get('race'),
            'sex': request.form.get('sex'),
            'capital.gain': int(request.form.get('capital.gain')),
            'capital.loss':int(request.form.get('capital.loss')),
            'hours.per.week':int(request.form.get('hours.per.week')),
            'native.country': request.form.get('native.country')
        }

        # Debugging: Print the order of input_data received
        print("Received input data in form:", input_data)

        # Check for missing values
        missing_keys = [key for key, value in input_data.items() if value in [None, '']]
        if missing_keys:
            raise ValueError(f"Missing value for: {', '.join(missing_keys)}")

        # Convert to DataFrame and reorder columns to match the model's expected order
        input_df = pd.DataFrame([input_data])[training_columns]

        # Debugging: Print the reordered input data
        print("Reordered input data for model:", input_df)

        # Predict using the trained model pipeline
        prediction = model_pipeline.predict(input_df)
        income_class = '>50K' if prediction[0] == 1 else '<=50K'

        # Store prediction results
        store_in_excel(input_data, income_class)

        # Render prediction result and retain form data
        return render_template('index.html', prediction=income_class, error=None, form_data=input_data,cleared=False)

    except ValueError as ve:
        # Handle missing value error
        return render_template('index.html', error=f"Error during prediction: {str(ve)}", prediction=None, form_data=request.form,cleared=False)

    except Exception as e:
        # Handle other errors
        return render_template('index.html', error=f"Error during prediction: {str(e)}", prediction=None, form_data=request.form,cleared=False)

if __name__ == '__main__':
    app.run(debug=True, port=5001)



