import pyttsx3
import datetime
import wikipedia
import webbrowser
import requests
import json
from youtubesearchpython import VideosSearch
import openai  

# Set your OpenAI API key
openai.api_key = ""  # Replace with your actual API key

# OpenWeatherMap API key (replace with your own)
openweathermap_api_key = ""

# News API key (replace with your own)
news_api_key = ""

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak('Hello Nikoloz, I wish you a happy day, ')
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    print(Time)
    speak(f" Georgian time is {Time}")

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def get_weather_forecast(location):
    try:
        # Make a request to the OpenWeatherMap API
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": location,
            "appid": openweathermap_api_key,
            "units": "metric",
        }
        response = requests.get(url, params=params)
        data = response.json()

        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            forecast = f"The weather in {location} is {weather_description}. " \
                       f"The temperature is {temperature}°C, humidity is {humidity}%, " \
                       f" and wind speed is {wind_speed} m/s."
            print(forecast)
            speak(forecast)
        else:
            speak("Sorry, I couldn't fetch the weather forecast for that location.")

    except Exception as e:
        print("An error occurred:", str(e))
        speak("An error occurred while fetching the weather forecast.")

def suggest_weather_categories():
    try:
        # Suggest weather-related categories from Wikipedia
        suggested_categories = wikipedia.search("Weather categories")

        if suggested_categories:
            speak("Here are some suggested weather-related categories on Wikipedia:")
            for category in suggested_categories[:5]:
                print(category)
                speak(category)
        else:
            speak("Sorry, I couldn't find any weather-related categories on Wikipedia at the moment.")

    except Exception as e:
        print("An error occurred:", str(e))
        speak("An error occurred while suggesting weather-related categories.")

# Function to fetch news from the last 24 hours
def get_news():
    try:
        # Define the news source and API endpoint
        news_source = "your-news-source"
        news_url = f"https://newsapi.org/v2/everything"
        params = {
            "apiKey": news_api_key,
            "q": "latest news",
            "from": (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            "to": datetime.datetime.now().strftime('%Y-%m-%d'),
            "sortBy": "publishedAt",
            "pageSize": 5,
            "language": "en",
        }

        response = requests.get(news_url, params=params)
        data = response.json()

        if data["status"] == "ok" and data["totalResults"] > 0:
            articles = data["articles"]
            speak("Here are some of the latest news headlines from the last 24 hours:")
            for i, article in enumerate(articles):
                title = article["title"]
                description = article["description"]
                print(f"{i + 1}. {title}: {description}")
                speak(f"{i + 1}. {title}: {description}")
        else:
            speak("Sorry, I couldn't fetch the latest news at the moment.")

    except Exception as e:
        print("An error occurred:", str(e))
        speak("An error occurred while fetching the latest news.")

# Function to interact with the GPT-3 model
def ask_gpt3(question):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=50,
        )

        # Extract and return the generated response
        generated_text = response.choices[0].text
        return generated_text

    except Exception as e:
        print("An error occurred while querying GPT-3:", str(e))
        return "Sorry, I encountered an error while processing your request."

# Function to play a song from YouTube
def play_song(song_name):
    try:
        # Search for the song on YouTube
        query = f"{song_name}"
        videos_search = VideosSearch(query)
        results = videos_search.result()

        # Limit the number of results to 1
        results = results["result"][:1]

        if results:
            # Get the first video's URL
            video_url = results[0]["link"]
            speak(f"Playing {song_name} on YouTube.")
            webbrowser.open(video_url)
        else:
            speak(f"Sorry, I couldn't find {song_name} on YouTube.")

    except Exception as e:
        print("An error occurred while playing the song:", str(e))
        speak("An error occurred while playing the song.")

def main():
    time()
    speak("How can I assist you today? Please choose one of the following options: Wikipedia, Weather, News, Play a Song, or Ask a Question to GPT-3.")

    choice = input("Enter your choice (Wikipedia/Weather/News/Song/GPT3): ").strip().lower()

    if choice == "wikipedia":
        speak("Please enter your question.")
        query = input("Your question: ")

        try:
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("It seems there are multiple results for your query. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I couldn't find any information about that topic on Wikipedia.")

        except Exception as e:
            print("An error occurred:", str(e))
            speak("An error occurred while processing your request.")

    elif choice == "weather":
        speak("Please enter the location for the weather forecast.")
        location = input("Location: ")
        get_weather_forecast(location)

    elif choice == "news":
        get_news()

    elif choice == "song":
        speak("Please enter the song you want to play.")
        song_name = input("Enter the song: ")
        play_song(song_name)

    elif choice == "gpt3":
        speak("Please enter your question for GPT-3.")
        question = input("Your question: ")
        gpt3_response = ask_gpt3(question)
        speak(gpt3_response)

    else:
        speak("Sorry, I didn't understand your choice. Please choose either Wikipedia, Weather, News, Play a Song, or Ask a Question to GPT-3.")

if __name__ == "__main__":
    main()

