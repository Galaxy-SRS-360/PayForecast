# Salary Predictor ML Project with Flask

This project demonstrates how machine learning models can be deployed on production using Flask API. The project includes a trained machine learning model to predict employee salaries based on training data.

## Prerequisites

Ensure you have the following libraries installed:
- Scikit Learn
- Pandas (for Machine Learning Model)
- Flask (for API)

## Project Structure

- **model.pkl:** Contains the trained machine learning model for salary prediction.
- **main.py:** Implements Flask APIs to receive employee details through GUI or API calls, computes the predicted value based on the model, and returns it.
- **templates:** Folder containing the HTML template to allow users to enter employee details and display the predicted employee salary.
- **assets:** Folder containing static files such as CSS stylesheets and images.

## Running the Project

1. Create the machine learning model by running the following command:
    ```bash
    python model.jpynb
    ```
   This creates a serialized version of the model into `model.pkl`.

2. Start the Flask API using the following command:
    ```bash
    python main.py
    ```
   By default, Flask will run on port 5000.

3. Navigate to [http://localhost:8000](http://localhost:8000) to access the application. Enter valid numerical values in the input boxes and click "Predict" to view the predicted salary.

4. To send direct POST requests to the Flask API using Python's `requests` module, run the following command:
    ```bash
    python request.py
    ```

## API Endpoints

- **POST `/Salary_Predictor`:** Predicts salary based on input data. Expects form data with employee details.
- **POST `/predict_api`:** API endpoint to predict salary. Expects JSON data with employee details.

## File Descriptions

- **model.pkl:** Serialized machine learning model.
- **main.py:** Flask application containing API endpoints and logic for predicting salary.
- **templates/index.html:** HTML template for the user interface.
- **assets/salarystyle.css:** CSS styles for the user interface.

Feel free to customize this `README.md` file and the code according to your project requirements.
