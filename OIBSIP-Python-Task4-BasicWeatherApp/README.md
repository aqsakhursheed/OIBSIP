# Basic Weather App (Beginner)

## Project Description

This is a **Python-based Basic Weather Application** developed as part of my **Python Programming internship at Oasis Infobyte**.

The program fetches and displays real-time weather information for a user-specified city. It integrates with a live weather API to retrieve up-to-date data including current temperature, humidity levels, weather conditions, and wind speed. It also includes comprehensive input validation and error handling to ensure seamless user interaction via the command line.

## Features

- **Real-time Weather Data** — Fetches live weather updates for any user-specified city globally.
- **Dual Temperature Units** — Displays current temperature in both Celsius (°C) and Fahrenheit (°F).
- **Comprehensive Metrics** — Provides humidity percentage (%), weather condition description, and wind speed.
- **Robust Error Handling** — Handles invalid city names, non-existent locations, and API communication issues gracefully without crashing.
- **Input Validation** — Prevents empty inputs and prompts the user for valid city names.
- **Continuous Execution Loop** — Allows users to look up multiple cities continuously or exit whenever they want.

## Technologies Used

- **Python**
- **requests** — Used to send HTTP requests and interact with the external live Weather API.
- **JSON** — Used to parse and extract structured weather metrics from the API's JSON response.

## How It Works

1. The program greets the user and prompts for a city name.
2. The user's input is validated to ensure it is not blank.
3. An HTTP GET request is sent to the Weather API endpoint with the requested city name and authentication key.
4. The API processes the request and returns the weather data in JSON format.
5. The program parses the JSON response to extract key weather variables such as temperature, humidity, weather condition, and wind speed.
6. The formatted weather details are displayed neatly on the command line interface.
7. If an invalid city name or network issue occurs, an appropriate error message is shown.
8. The user can search for another city or type `exit` to close the application.

## Project Purpose

The purpose of this project was to strengthen my understanding of **Python programming, RESTful API integration using HTTP requests, JSON parsing, dictionary manipulation, error handling, input validation, and command-line application loops**.

## Internship

**Organization:** Oasis Infobyte

**Track:** Python Programming

**Project:** Basic Weather App (Beginner)