
# Plant Irrigation Model API

This project provides a RESTful API for making predictions using a pre-trained LightGBM model to assist with plant irrigation decisions. The API is built with FastAPI and serves predictions based on environmental and soil features.

## Features

- **/predict** endpoint for model inference
- Input validation using Pydantic schemas
- Loads a LightGBM model from a pickle file
- Error handling for invalid input and model issues

## Project Structure

```
plant-irrigation-model/
├── app/
│   ├── model_handler.py
│   └── schema.py
├── model/
│   └── lgbm_model.pkl
├── main.py
├── requirements.txt
├── test.py
└── .gitignore
```

## Requirements

- Python 3.8+
- See requirements.txt for dependencies

## Setup

1. **Clone the repository**  
   ```sh
   git clone <repo-url>
   cd plant-irrigation-model
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python -m venv myvenv
   source myvenv/Scripts/activate  # On Windows
   # or
   source myvenv/bin/activate      # On Unix/Mac
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Ensure the model file exists**  
   Place your trained `lgbm_model.pkl` in the model directory.

## Running the API

Start the FastAPI server with Uvicorn:

```sh
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Usage

### POST `/predict`

**Request Body:**
```json
{
  "features": {
    "Temperature": 27.0,
    "Soil_Humidity": 60.0,
    "Time": 14.0,
    "Soil_Moisture": 0,
    "rainfall": 0.5,
    "Air_temperature_C": 26.5,
    "Wind_speed_Kmh": 5.0,
    "Air_humidity_": 50.0,
    "Pressure_KPa": 101.3
  }
}
```

**Response:**
```json
{
  "prediction": 1.0
}
```

## Testing

You can test the deployed API using test.py:

```sh
python test.py
```


