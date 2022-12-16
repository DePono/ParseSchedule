from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
import pyautogui
import time
def saveHTML(i):
    link = f'https://www.samgups.ru/raspisanie/sessiya/2022-2023/perviy-semestr/HTML/{i}.html'
    driver.get(link)
    time.sleep(3)
    pyautogui.hotkey('ctrl','s')
    time.sleep(3)
    pyautogui.hotkey('enter')
for i in range(1,158):
    saveHTML(i)