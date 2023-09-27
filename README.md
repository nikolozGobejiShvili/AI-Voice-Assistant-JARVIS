# AI Voice Assistant JARVIS

![AI Voice Assistant JARVIS](assistant.jpg)

AI Voice Assistant JARVIS is a Python script (`jarvis.py`) that implements a voice-controlled assistant capable of performing various tasks using voice commands. JARVIS can interact with several APIs and services to provide information, play music, and generate text responses using OpenAI's GPT-3.

## Features

- **Time and Greeting:** JARVIS greets the user and provides the current time when activated.

- **Google Search:** It can perform a Google search based on user input.

- **Weather Forecast:** JARVIS can fetch the weather forecast for a specified location using the OpenWeatherMap API.

- **News:** Users can get the latest news by category, including sports, business, and technology, using the News API.

- **Song Playback:** JARVIS can search for and play songs from YouTube based on user requests.

- **GPT-3 Interaction:** Users can ask questions, and JARVIS interacts with the GPT-3 language model to generate responses.

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3.x:** You'll need Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

- **Required Python Packages:** Install the required Python packages using `pip`:

    ```bash
    pip install pyttsx3 wikipedia webbrowser requests youtubesearchpython openai speech_recognition
    ```

- **API Keys:** Obtain API keys for the following services:

    - OpenAI GPT-3 API key (Replace `"your-openai-api-key"` with your actual key).
    - OpenWeatherMap API key (Replace `"your-openweathermap-api-key"` with your actual key).
    - News API key (Replace `"your-news-api-key"` with your actual key).

## Usage

Run AI Voice Assistant JARVIS using the following command:

```bash
python jarvis.py
