# FlaskWeatherApp
Dynamic list of cities and related weather data using open_weather_map API
![Flask Weather GIF](weatherapp.gif)

## Features

- Add a city to your personal list to monitor its weather.
- View weather data including current temperature and weather description.
- Delete individual cities from your list.
- Option to clear all data.
- User-friendly interface.

## Requirements

- Python 3.6+
- Flask
- SQLAlchemy
- SQLite3
- requests

## Installation & Setup

1. Clone the repository: 
    ```
    git clone https://github.com/Simon-zps/FlaskWeatherApp.git
    ```
2. Navigate to the cloned repository: 
    ```
    cd repository
    ```
3. Install the necessary requirements: 
    ```
    pip install -r requirements.txt
    ```
4. Replace `credentials.secret_key` with your Flask secret key.
5. Replace `appid` in the OpenWeatherMap API URL with your OpenWeatherMap API key.
6. Run the application: 
    ```
    python main.py
    ```
7. Visit `localhost:5000` on your web browser to start using the app.

## Usage

1. Enter the name of the city you want to monitor in the input field.
2. Click "Submit" to add the city to your list.
3. If the city is found and not already in your list, it will be added to your list. If the city is not found or already in your list, an appropriate message will be displayed.
4. The weather data for each city in your list will be displayed on the home page.
5. Click "Delete" next to a city to remove it from your list.
6. To delete all cities from your list, manually navigate to the "/cleardata"