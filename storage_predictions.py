import os
import pandas as pd
from openpyxl import load_workbook

def store_in_excel(input_data, prediction, file_path='D:\\AIP Project\\database\\predictions.xlsx'):
    try:
        # Convert specific fields to numbers where required
        numeric_fields = ['age', 'fnlwgt', 'education.num', 'capital.gain', 'capital.loss', 'hours.per.week']
        for field in numeric_fields:
            if field in input_data:
                input_data[field] = pd.to_numeric(input_data[field], errors='coerce')

        # Add prediction to data
        data = {**input_data, 'Prediction': '>50K' if prediction == 1 else '<=50K'}
        df = pd.DataFrame([data])

        # Ensure the directory for the file exists
        folder_path = os.path.dirname(file_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Save or append data to the Excel file
        if not os.path.exists(file_path):
            df.to_excel(file_path, index=False, engine='openpyxl')
        else:
            with pd.ExcelWriter(file_path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                start_row = writer.sheets['Sheet1'].max_row
                df.to_excel(writer, index=False, startrow=start_row, header=False)

        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error in storing Excel data: {e}")
        raise
