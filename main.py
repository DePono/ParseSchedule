import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from bs4 import BeautifulSoup
import pandas as pd


def saveHTML(i):
    link = f'https://www.samgups.ru/raspisanie/sessiya/2022-2023/perviy-semestr/HTML/{i}.html'
    driver.get(link)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(3)
    pyautogui.hotkey('enter')


for i in range(1, 158):
    saveHTML(i)

data = []
group = []
headers = ['Дата', '1 пара', '2 пара', '3 пара', '4 пара', '5 пара', '6 пара', '7 пара']
mydata = pd.DataFrame(columns=headers)
for i in range(1, 158):
    try:
        with open(f'HTML/{i}.htm', encoding='utf-8') as file:
            source = file.read()
            soup = BeautifulSoup(source, 'lxml')
            p = soup.select_one('p')
            nameOfGroup = p.find_all('font')[1]

        with open(f'HTML/{i}.htm', encoding='utf-8') as file:
            source = file.read()
            soup = BeautifulSoup(source, 'lxml')
            table1 = soup.find('table')

        for j in table1.find_all('tr')[2:]:
            row_data = j.find_all('td')
            print(row_data)
            row = [i.text for i in row_data]
            length = len(mydata)
            mydata.loc[length] = row
            group.append(nameOfGroup.text)
    except:
        pass
mydata['Группа'] = group
mydata.to_excel('1.xlsx', index=False)
