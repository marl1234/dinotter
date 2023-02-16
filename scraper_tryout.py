from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import pandas as pd

# # Path to location of TOR browser's Firefox binary
# # For VM:
# binary = FirefoxBinary('/home/dinotter/Downloads/tor-browser/firefox')

# For local run:
binary = FirefoxBinary('/Applications/Tor Browser.app/Contents/MacOS/firefox')

# Set up driver and open TOR browser
driver = webdriver.Firefox(firefox_binary=binary)

# Click connect button after five seconds
time.sleep(5)
driver.find_element("id", "connectButton").click()

# # Define url
# url = 'https://www.google.com'
#
# # Go to url
# time.sleep(5)
# driver.get(url)

# url WeTheNorth
url_north = 'http://hn2paw7zaahbikbejiv6h22zwtijlam65y2c77xj2ypbilm2xs4bnbid.onion/index.php'

# Go to url
time.sleep(5)
driver.get(url_north)

# Find element by class name
# Class name of images on TOR: col-1search-img
#driver.find_element_by_class_name("col-1search-img")

# Close windows and end driver session
time.sleep(20)
driver.quit()