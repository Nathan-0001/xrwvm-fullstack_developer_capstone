"""Django REST Framework API views"""
# Uncomment the imports below before you add the function code
import os
import requests
from dotenv import load_dotenv


load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    """Do a GET request to the
    specified endpoint with optional parameters"""
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print(f"GET from {request_url} ")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        # If any error occurs
        print("Network exception occurred")


# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    """Does sentiment analysis of the input text
    using the sentiment analyzer microservice"""
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# Add code for posting review
def post_review(data_dict):
    """Does a POST request to the
    specified endpoint with a review in JSON format"""
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
