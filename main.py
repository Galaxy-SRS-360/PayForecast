# Import necessary libraries
import pickle  # For loading the machine learning model and scaler
from flask import Flask, render_template, request, jsonify  # For creating a web application, handling HTTP requests, and JSON responses

# Create a Flask web application instance
myapp=Flask(__name__, static_folder='assets', static_url_path='/assets')
# Paths to the saved model and scaler
model_path = "byteStream/SRS_Model.pkl"
sc_path = "byteStream/scDump.pkl"

# Load the machine learning model and scaler using pickle
model = pickle.load(open(model_path, "rb"))  # Load the machine learning model
sc = pickle.load(open(sc_path, "rb"))  # Load the scaler for data transformation

# Route for the home page
@myapp.route('/')
def index():
    return render_template("index.html")

# Route for the Salary Predictor page
@myapp.route('/Salary_Predictor', methods=['POST', 'GET'])
def Salary_Predictor():
    try:
        # Retrieve the user input for years of experience
        int_features = [int(x) for x in request.form.values()]
        
        # Transform the input data using the loaded scaler
        sc_data = sc.transform([int_features])
        
        # Predict the salary using the loaded machine learning model
        prediction = model.predict(sc_data)
        
        # Round the prediction to get a whole number salary
        salary = round(prediction.tolist()[0], 2)
        
        # Render the template with the predicted salary
        return render_template("SalaryPredicted/index.html", salary_text=f"Employee Salary should be: {salary}/-")
    except Exception as e:
        # Print detailed error message for debugging
        print(f"Error occurred: {e}")
        return "An error occurred while processing the request."

# Route for API endpoint to predict salary
@myapp.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        # Get JSON data from the request
        data = request.get_json(force=True)
        
        # Transform the input data using the loaded scaler
        sc_data = sc.transform([list(data.values())])
        
        # Predict the salary using the loaded machine learning model
        prediction = model.predict(sc_data)
        
        # Get the output prediction
        output = prediction[0]
        
        # Return the prediction as JSON response
        return jsonify(output)
    except Exception as e:
        # Print detailed error message for debugging
        print(f"API Error occurred: {e}")
        return "An error occurred while processing the API request."

# Main entry point of the application
if __name__ == '__main__':
    # Run the Flask web application on localhost:8000 in debug mode
    myapp.run(debug=True, port=8000)
