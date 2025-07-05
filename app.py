from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        building_type = request.form['Building_Type']
        square_footage = float(request.form['Square_Footage'])
        num_occupants = int(request.form['Number_of_Occupants'])
        appliances_used = int(request.form['Appliances_Used'])
        avg_temp = float(request.form['Average_Temperature'])
        day_of_week = request.form['Day_of_Week']

        # Encode building type
        building_type_encoded = {
            'Residential': 0,
            'Commercial': 1,
            'Industrial': 2
        }.get(building_type, 0)

        # Encode day of week as weekday/weekend
        weekend_days = {'Saturday', 'Sunday'}
        day_encoded = 1 if day_of_week in weekend_days else 0

        # Scale only square footage
        scaled_sqft = scaler.transform([[square_footage]])[0][0]

        # Prepare final input in correct order
        final_input = np.array([
            building_type_encoded,
            scaled_sqft,
            num_occupants,
            appliances_used,
            avg_temp,
            day_encoded
        ]).reshape(1, -1)

        # Predict and format
        prediction = float(model.predict(final_input)[0])

        return f"<h2 style='text-align:center;'>Predicted Energy Consumption: {prediction:.2f} kWh</h2>"

    except Exception as e:
        return f"<h2 style='color:red;text-align:center;'>❌ Error during prediction: {str(e)}</h2>"

if __name__ == '__main__':
    app.run(debug=True)