# Energy-Consumption-Predictor

An intelligent machine learning model that predicts energy consumption based on building type, square footage, occupancy, appliances usage, temperature, and day of the week. Ideal for facility managers, energy analysts, and sustainability researchers.

### Project Overview

The Energy Consumption Predictor is a regression-based ML project that estimates the energy usage of buildings using real-world features. It leverages user input to make accurate predictions, enabling better energy planning and sustainability efforts.

### Features Used

| Feature               | Description                                                                          |
| --------------------- | ------------------------------------------------------------------------------------ |
| `Building Type`       | Categorical feature specifying the type of building (e.g., Residential, Commercial). |
| `Square Footage`      | Total area of the building in square feet.                                           |
| `Number of Occupants` | Total number of people regularly occupying the building.                             |
| `Appliances Used`     | Count of energy-consuming appliances installed.                                      |
| `Average Temperature` | Average outdoor temperature in °C.                                                   |
| `Day of Week`         | Categorical value indicating the day (Monday to Sunday).                             |
| `Energy Consumption`  | **Target Variable** – Measured in kWh (kilowatt-hours).                              |

### Technologies Used

Python 

Pandas / NumPy

Matplotlib / Seaborn

Scikit-learn (Linear/StandardScaler)

Flask (if you have a web app interface)

HTML/CSS (for frontend form)

### Future Improvements

Incorporate time-series data (hourly/daily usage)

Use XGBoost or Random Forest for better accuracy

Deploy on cloud (e.g., AWS, Render, Heroku)

