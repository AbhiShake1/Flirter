import requests
from bs4 import BeautifulSoup


def get_current_temperature() -> str:
    # the method will get called at the end after the temperature variable is defined
    def get_message() -> str:
        temp = int(temperature.strip("°C"))
        if -30 < temp < 0:
            return "It's freezing cold. I want to spend some time with you around a fireplace !"
        if 0 < temp < 15:
            return "It's cold. Coffee !?"
        if 15 < temp < 30:
            return "Should we go for a date today !?"
        return "Damn, it's hot out there. Chilled beer !?"

    # url from where we need to scrape the temperature
    r = requests.get("https://www.google.com/search?q=current+temperature")
    # need to install lxml via pip which also works with broken html unlike html.parser
    data = BeautifulSoup(r.text, "lxml")
    # find method only returns the first result
    temperature = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
    location = data.find("div", class_="BNeawe s3v9rd AP7Wnd lRVwie").text.strip("Current temperature")
    return f"The current temperature in {location} is {temperature}\n{get_message()}"
