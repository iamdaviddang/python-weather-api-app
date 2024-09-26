
# Python Weather API App

This is a simple command-line weather application built using Python. It fetches current weather data for a given city using the OpenWeatherMap API.

## Features

- Fetches current weather data (temperature, humidity, weather description) for any city.
- Displays data in a user-friendly format directly in the terminal.
- Utilizes the OpenWeatherMap API for real-time weather information.
- Can be extended or integrated into a larger application.

## Prerequisites

To run this project locally, you will need:

- Python 3.6 or higher
- An API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/iamdaviddang/python-weather-api-app.git
   cd python-weather-api-app
   ```

2. **Install dependencies**:

   It's recommended to create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:

   Get your API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up). 

   Then, create a `.env` file in the root directory and add your API key as follows:

   ```bash
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Usage

1. **Run the application**:

   To fetch the weather for a city, run the following command:

   ```bash
   python app.py
   ```

2. **Enter the city name**:

   The app will prompt you to enter the city name, and then display the current weather information.

## Example

Here’s an example of how the output looks like:

```
Enter city name: London
Weather in London:
Temperature: 15°C
Humidity: 80%
Weather description: clear sky
```

## Future Enhancements

- Add support for fetching forecasts (next 5 days).
- Add a graphical user interface (GUI).
- Improve error handling (e.g., invalid city names, API key issues).
  
## Contributing

Feel free to contribute by submitting a pull request or opening an issue for discussion.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
