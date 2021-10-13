import pause
import pyautogui
from datetime import datetime


def post():
    pass


def get_date() -> datetime:
    data: str = pyautogui.prompt("Enter date in 'YYYY:MM:DD:hh:mm' format")
    time: list = data.split(":")
    if len(time) != 5:
        pyautogui.alert("Please input date correctly")
        get_date()
    return datetime(
        time[0],  # year
        time[1],  # month
        time[2],  # day
        time[3],  # hour
        time[4],  # minute
    )


def init():
    pause.until(get_date())
    post()
