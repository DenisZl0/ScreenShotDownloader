#!/usr/local/bin/python3.8
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
import random
import time
from sys import platform

start_time = time.time()


def sys_check():
    if platform == "linux" or platform == "linux2":
        linux()
    elif platform == "win32":
        windows()


def random_sequence():
    sequence = 'abcdefghijklmnopqrstuvwxyz1234567890'
    rsequence = random.choices(sequence, k=6)
    r = ''.join(rsequence)
    return r


def linux():
    num_of_pics = int(input('How many pictures do you want: '))

    dir = input('Enter directory for images (use the full path) or press enter for default: ')
    if dir == '':
        if os.path.isdir('/home/' + str(os.environ['USER']) + '/Pictures/LightShotIsBad'):
            dir = '/home/' + str(os.environ['USER']) + '/Pictures/LightShotIsBad'
        else:
            os.mkdir('/home/' + str(os.environ['USER']) + '/Pictures/LightShotIsBad')
            dir = '/home/' + str(os.environ['USER']) + '/Pictures/LightShotIsBad'
    else:
        dir = dir

    # Parsing the links

    i = 1
    while i <= num_of_pics:
        rs = random_sequence()

        url1 = 'https://prnt.sc/' + rs
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3', }

        source = requests.get(url1, headers=user_agent).text

        soup = BeautifulSoup(source, 'lxml')

        img = soup.find('img')['src']

        if img.find("https://") == -1:
            i -= 1
        else:
            print('№' + str([i]) + ' ' + img + ' ' + url1)

        # Downloading the images from the links

        url = img

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3', }

        try:

            l = url.split('.')
            type = str(l[3]).upper()

            name = rs
            response = requests.get(url, headers=headers, stream=True)
            im = Image.open(BytesIO(response.content))
            os.chdir(dir)
            try:
                im.save(dir + '/' + name, type)
            except KeyError:
                im.save(dir + '/' + name, "JPEG")

            if type == 'PNG':
                os.rename(rs, rs + '.png')
                i += 1
            elif type == 'JPEG':
                os.rename(rs, rs + '.jpeg')
                i += 1
            elif type == 'JPG':
                os.rename(rs, rs + '.jpg')
                i += 1
            else:
                i += 1
                continue

        except requests.exceptions.MissingSchema:
             i += 1
             continue

    print(f" Downloaded {num_of_pics} pictures in {int(time.time() - start_time)} seconds")


def windows():
    num_of_pics = int(input('How many pictures do you want: '))

    dir = input('Enter directory for images (use the full path) or press enter for default: ')
    if dir == '':
        if os.path.isdir('C:\\Users\\' + str(os.getlogin()) + '\\Pictures\LightShotIsBad'):
            dir = 'C:\\Users\\' + str(os.getlogin()) + '\\Pictures\LightShotIsBad'
        else:
            os.mkdir('C:\\Users\\' + str(os.getlogin()) + '\\Pictures\LightShotIsBad')
            dir = 'C:\\Users\\' + str(os.getlogin()) + '\\Pictures\LightShotIsBad'
    else:
        dir = dir

    # Parsing the links

    i = 1
    while i <= num_of_pics:
        rs = random_sequence()

        url1 = 'https://prnt.sc/' + rs
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3', }

        source = requests.get(url1, headers=user_agent).text

        soup = BeautifulSoup(source, 'lxml')

        img = soup.find('img')['src']

        if img.find("https://") == -1:
            i -= 1
        else:
            print('№' + str([i]) + ' ' + img + ' ' + url1)

        # Downloading the images from the links

        url = img

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3', }

        try:

            l = url.split('.')
            type = str(l[3]).upper()

            name = rs
            response = requests.get(url, headers=headers, stream=True)
            im = Image.open(BytesIO(response.content))
            os.chdir(dir)
            try:
                im.save(name, type)
            except KeyError:
                im.save(name, "JPEG")
            if type == 'PNG':
                os.rename(rs, rs + '.png')
                i += 1
            elif type == 'JPEG':
                os.rename(rs, rs + '.jpeg')
                i += 1
            elif type == 'JPG':
                os.rename(rs, rs + '.jpg')
                i += 1
            else:
                i += 1
                continue

        except requests.exceptions.MissingSchema:
            i += 1
            continue
    print(f" Downloaded {num_of_pics} pictures in {int(time.time() - start_time)} seconds")


if __name__ == '__main__':
    sys_check()
