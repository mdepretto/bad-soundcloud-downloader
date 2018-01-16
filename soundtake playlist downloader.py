#! python3
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pyautogui
import os

#the url i'm going to be using
playlistURL = "https://soundtake.net/#https://soundcloud.com/user-106042152/sets/likes"

#the download path
downloadPath = 'D:\\Music\\soundcloud'

#accumulator for div tag
divTag = 2

#boolean for pressing down once
isDown = False

#instantiates the webdriver and chooses firefox
driver = webdriver.Firefox()

#ublock origin addon, if you don't have the extension, comment out this line.
#also, good luck trying to find this son of a bitch. 
driver.install_addon("C:\\Users\\dave2\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\10t5gwzv.default\\extensions\\uBlock0@raymondhill.net.xpi")

#goto my playlist download link on soundtake
driver.get(playlistURL)

#might not need this...
#give it time to load
time.sleep(2)

#some shit to change the download directory
#clicks the 3 bars for options
pyautogui.moveTo(1258,54)
pyautogui.click()
time.sleep(1)

#clicks options
pyautogui.moveTo(1124,344)
pyautogui.click()
time.sleep(1)

#types download to search for the path
pyautogui.typewrite('download')
pyautogui.moveTo(893,251)
time.sleep(1)

#click "browse"
pyautogui.click()
pyautogui.moveTo(734,42)
time.sleep(1)

#enter path for download
pyautogui.typewrite(downloadPath)
time.sleep(1)
pyautogui.moveTo(1175,1000)
pyautogui.click()


#clicks the download button
#/html/body/div[3]/div/div[10]/div[2]/div[ONLY THIS TAG CHANGES]/div[2]/div[4]/a
#and this is where it gets bad
while divTag <= 232:
    driver.find_element_by_xpath('/html/body/div[3]/div/div[10]/div[2]/div[' + str(divTag) + ']/div[2]/div[4]/a').click()
    print("clicked download")

    #self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    driver.switch_to.active_element

    #see if save alert pops up immediately, but doesn't work like it should but doesn't work without it...
    try:
        time.sleep(3)
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        
    except TimeoutException:
        print("")


    try:
        if divTag < 8:
            print("waiting 5 seconds")
            time.sleep(5)
            #move mouse to skip button
            pyautogui.moveTo(1189,103)
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
        
        #click on downloader form if no skip button
        pyautogui.moveTo(650,302)
        pyautogui.click()

        #checks if "open with" or "save" is selected in a bad manner
        if isDown == False:
            pyautogui.press('down')
            isDown = True

        time.sleep(1)
        #should select save
        pyautogui.press('enter')
        print("accepting download number: " + str(divTag))
        time.sleep(2)

        if divTag < 10:
            print('close tab')
            #pressing ctrl+w will close the adf.ly tab
            pyautogui.keyDown('ctrl')
            pyautogui.press('w')
            pyautogui.keyUp('ctrl')
    except TimeoutException:
        print("wtf2")


    #increment divTag
    divTag += 1
	
	
#
#
#part 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
#the downloads will contain [soundtake.net] in every song, this removes it from the mp3
fileList = os.listdir( downloadPath )

for file in fileList:
    if "[soundtake.net]" in file:
        #replace text with nothing (delete it)
        newName = file.replace( "[soundtake.net]" , "")
        print(newName + "\n")
		
		#rename replace this file in this folder with this file to this folder. 
        os.rename(os.path.join(fileList, file), os.path.join(fileList, newName))

#there will usually be a space left so i'm removing that, too
for file in os.listdir("D:\\Music\\soundcloud\\rafa"):
        #k is the position of the first space going in reverse (last space)
        k = file.rfind(" ")
        #newName1 becomes the file name but the last space replaced by nothing
        #err, idk actually
        newName1 = file[:k] + "" + file[k+1:]
        print(newName1 + "\n")
        os.rename(os.path.join(fileList, file), os.path.join(fileList, newName1))
        
