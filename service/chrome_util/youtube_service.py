from selenium import webdriver


class YoutubeService:
    driver = webdriver.Chrome("chromedriver.exe")

    def open_youtube(self):
        self.driver.get("youtube.com")
