## Model Deployment using Flask

This folder contains a Flask application to deploy a trained machine learning model.

## Files
- **app.py** – Flask application  
- **final_model.pkl** – Trained model  
- **requirements.txt** – Required libraries  

## Steps to Run
1. Install dependencies  
    ```bash
    pip install -r requirements.txt
    ```
2. Run the Flask app  
    ```bash
    python app.py
    ```
3. Access the application at `http://
localhost:5000`


## API
- **POST /predict**  
Sends input data and returns a prediction.

## Output
- Predictions are saved in `prediction_logs.txt`.
- Each entry includes a timestamp.
- This confirms the API is working.

## Folder Structure
```
/Model_Deployment
│── app.py
│── final_model.pkl
│── requirements.txt
```