from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print('Program Started')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome(options=options)
web.get('https://docs.google.com/forms/d/e/1FAIpQLSegLlcZZQRu9LUSwUMGzPM2U9o4dIF0Gu_v5daRTQz61NP85Q/viewform')
web.maximize_window()

time.sleep(2)

NAME = "Your Name Here"
namePath = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
namePath.send_keys(NAME)

print("Filled Name Successfully")

USN = "Your USN here"
usnPath = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
usnPath.send_keys(USN)

print("Filled USN Successfully")

Submit = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
Submit.click()

print("Clicked Submit button")

time.sleep(3)

get_confirmation_div_text = web.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[3]")
print("Printing Confirmation Text: ")
print(get_confirmation_div_text.text)

if((get_confirmation_div_text.text) == 'Your response has been recorded.'):
    print('Form filled successfully.')
else:
    print('Automation failed. Fill manually.')