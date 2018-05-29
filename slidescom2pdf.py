#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import time
import getpass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config import *

def get_slides_ss(uname, email, passwd, deck_name, ss_dir):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(*SLIDE_SIZE)

    driver.get('https://slides.com/users/sign_in')
    driver.find_element_by_id('user_email').send_keys(email)
    driver.find_element_by_id('user_password').send_keys(passwd)
    driver.find_element_by_name('button').click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'picture')))
    driver.get('https://slides.com/{}/{}/live#/'.format(uname, deck_name))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//footer/button')))
    time.sleep(2)
    driver.find_element_by_xpath('//footer/button').click()

    ss_idx = 0
    while True:
        time.sleep(2)
        ss_fname = '{}{:04d}.png'.format(SCREENSHOT_BASENAME, ss_idx)
        driver.save_screenshot(os.path.join(ss_dir, ss_fname))
        right_arrow = driver.find_element_by_xpath('//button[2]')
        down_arrow = driver.find_element_by_xpath('//button[4]')
        if 'enabled' in down_arrow.get_attribute('class'):
            down_arrow.find_element_by_xpath('.//div').click()
            print('Wrote: {}'.format(ss_fname))
            ss_idx += 1
            continue
        elif 'enabled' in right_arrow.get_attribute('class'):
            right_arrow.find_element_by_xpath('.//div').click()
            print('Wrote: {}'.format(ss_fname))
            ss_idx += 1
            continue
        else:
            break
    return ss_idx

def make_ss_dir(ss_dir):
    if os.path.isdir(ss_dir):
        old_files = glob.glob(os.path.join(ss_dir, '*'))
        for old_file in old_files:
            if os.path.isfile(old_file):
                os.remove(old_file)
    else:
        os.makedirs(ss_dir)

def main():
    for info in INPUT_INFO.values():
        if len(info['value']) == 0:
            info['value'] = input(info['phrase'])
    passwd = getpass.getpass('your password: ')

    info = INPUT_INFO
    make_ss_dir(info['ss_dir']['value'])
    num_ss = get_slides_ss(
            info['uname']['value'], info['email']['value'],
            passwd, info['deck_name']['value'], info['ss_dir']['value'])

    ss_fname = os.path.join(
            info['ss_dir']['value'], '{}*.png'.format(SCREENSHOT_BASENAME))
    os.system('convert {} ./{}'.format(ss_fname, info['pdf_fname']['value']))

if __name__ == '__main__':
    main()
