import datetime
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from getpass import getpass

loop = 1
date = datetime.datetime.now()
sundate = date.strftime("%B %d, %Y")
email = 'cac.cdo@gmail.com'
password = 'Emm4nu37'
description = "For your giving, you may send it to our church bank account: Security Bank City Alliance Church 0231-022229-001 " \
              "\nAll music used is for church purposes only. No copyright infringement intended. All rights reserved to its rightful owners."

print(
    "\tCAC Title Generator v2.1\nTo start, enter the necessary information below.\n*IF SPEAKER IS PTR. NANO, YOU CAN LEAVE THE SPEAKER FIELD BLANK*")
print(
    "\nType 1 for Ptr. Nano\nType 2 for Ptr. Roanne\nType 3 for Ptr. Mobida\nFor other speakers, type the full name of the Speaker")


def main():
    while (loop == 1):
        speaker = input("\nSpeaker: ")

        if speaker == 'exit':
            break

        switcher = {
            '1': 'Rev. Lorenzo Nano Jr.',
            '2': 'Ptr. Roanne Vergara',
            '3': 'Ptr. Jun Mobida',
            'fb': fb()
        }

        sermon_title = input("Sermon Title: ")
        print("Title:")
        print(
            f"CAC CDO  Sunday Online Worship  | {sundate} | {sermon_title} | Speaker: {switcher.get(speaker, speaker)}")
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio\OBS Studio (64bit).lnk")
        print(description)
        print('\n**Opening Facebook**')

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get('https://www.facebook.com/')

            username_box = driver.find_element('id', 'email')
            username_box.send_keys(email)

            password_box = driver.find_element('id', 'pass')
            password_box.send_keys(password)

            login_btn = driver.find_element(By.NAME, 'login')
            login_btn.click()

            time.sleep(7)
            driver.get('https://www.facebook.com/live/producer/1056138658352397/?entry_point=feedx_sprouts/')

            try:
                fb_title = driver.find_element(By.ID, 'jsc_c_1z' or 'jsc_c_25' or 'jsc_c_26' or 'jsc_c_32')
            except:
                print("Element not found")
        except:
            print('Error Occured')


def fb():
    print('**Opening Facebook**')

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.facebook.com/')

        username_box = driver.find_element('id', 'email')
        username_box.send_keys(email)

        password_box = driver.find_element('id', 'pass')
        password_box.send_keys(password)

        login_btn = driver.find_element(By.NAME, 'login')
        login_btn.click()

        time.sleep(7)
        driver.get('https://www.facebook.com/live/producer/1056138658352397/?entry_point=feedx_sprouts/')
    except:
        print('Error Occured')


if __name__ == "__main__":
    main()
