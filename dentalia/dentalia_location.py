from playwright.sync_api import sync_playwright
import time
import json
import re

data = []
with open('dentalia.json', 'r') as file:
        data = json.load(file)


with sync_playwright() as plays:
    browser = plays.firefox.launch(headless=False, slow_mo=50)
    page = browser.new_page()

    for i in range(len(data)):
        url = data[i]['location']

        page.goto(url)
        page.wait_for_timeout(5000)
        link = page.url
        page.wait_for_timeout(300)
        reg = ['!1d(-?\d+(?:\.\d+)?)!2d(-?\d+(?:\.\d+))', '!3d(-?\d+(?:\.\d+)?)!4d(-?\d+(?:\.\d+))']
        
        match = re.search(reg[0], link)
        if match:
            pass
        else:
            match = re.search(reg[1], link)
        text = match[0]

        if text[:3] == '!1d':
            temp = text.split('!2d')
            new_text = [temp[1], temp[0][3:]]
        elif text[:3] == '!3d':
            temp = text.split('!4d')
            new_text = [temp[0][3:], temp[1]]

        data[i]['location'] = new_text

with open('dentalia_with_location.json', 'w', encoding='utf-8') as file:
    json.dump(data, file,  indent=2, ensure_ascii=False)