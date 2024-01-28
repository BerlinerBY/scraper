import urllib.request
from parsel import Selector
import json 


from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    file_object = open("example.txt", "w")
    browser = pw.firefox.launch(headless=False)
    page = browser.new_page()

    # go to url
    page.goto('https://dentalia.com/clinica/', timeout=0)
    # get HTML
    file_object.write(page.content())
    file_object.close()


    #parse wsite with Playwright and get HTML
    file_object = open("example.txt", "r")
    data = file_object.read()

    sel = Selector(data)

    basic = "/html/body/div[2]/section/div/div[2]/div/section[3]/div/div/div/div/div/div/div[1]"
    #class="jet-listing-grid__items grid-col-desk-1 grid-col-tablet-1 grid-col-mobile-1 jet-listing-grid--330"
    #sel.xpath(f"name({basic}/*[node()])").get()

    """first div is enumeration variable of items""" 
    #path_to_item = "/div[30]/div/div/section/div/div[2]/div/section/div"
    #class="elementor-container elementor-column-gap-default"

    path_to_name = "/div[1]/div/div[1]/div/h3/text()"
    path_to_address = '/div[1]/div/div[2]/div/div/div/div/text()'
    path_to_location = '/div[2]/div/div[1]/div/div/a/@href' #add regex
    path_to_phone = '/div[1]/div/div[3]/div/div/div/div/text()'
    #numbers = [elem.strip() for elem in tex1[tex1.index(":") + 2: -1].split("\n")]

    path_to_working_hours = '/div[1]/div/div[4]/div/div/div/div/text()'
    #hours = [elem.strip() for elem in tex1[tex1.index(":") + 2: -1].split("\n")]


    arr = []
    for i in range(1, int(float(sel.xpath(f"count({basic}/div)").get())) + 1):
        path = f"{basic}/div[{i}]/div/div/section/div/div[2]/div/section/div"
        object_1 = dict()
        object_1["name"] = sel.xpath(f"{path}{path_to_name}").get()
        object_1["address"] = sel.xpath(f"{path}{path_to_address}").get()
        object_1["location"] = sel.xpath(f"{path}{path_to_location}").get()
        numbers = sel.xpath(f"{path}{path_to_phone}").get()
        object_1["phone"] = [elem.strip() for elem in numbers[numbers.index(":") + 2:].split("\n")]
        hours = sel.xpath(f"{path}{path_to_working_hours}").get()
        object_1["working_hours"] = [elem.strip() for elem in hours[hours.index(":") + 2: -1].split("\n")]
        arr.append(object_1)


    with open('dentalia.json', 'w', encoding='utf-8') as file:
        json.dump(arr, file,  indent=2, ensure_ascii=False)

    file_object.close()
