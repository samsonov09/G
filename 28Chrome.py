import webbrowser
import time

# number of visiting webpages in google chrome = 28 times


url = 'https://yahoo.com'
url2 = 'https://www.paypal.com'
url3 = 'https://dlptest.com'

chrome = 'open -a /Applications/Google\ Chrome.app %s'

webbrowser.get(chrome).open_new(url2)

webbrowser.get(chrome).open_new(url3)

time.sleep(1)

webbrowser.get(chrome).open_new(url)

webbrowser.get(chrome).open_new(url2)

time.sleep(2)

webbrowser.get(chrome).open_new(url3)

webbrowser.get(chrome).open_new(url2)

time.sleep(1)

webbrowser.get(chrome).open_new(url3)

webbrowser.get(chrome).open_new(url)

time.sleep(1)

webbrowser.get(chrome).open_new(url2)

webbrowser.get(chrome).open_new(url)

time.sleep(1)

webbrowser.get(chrome).open_new(url2)

webbrowser.get(chrome).open_new(url3)

time.sleep(1)

webbrowser.get(chrome).open_new(url)

webbrowser.get(chrome).open_new(url2)

time.sleep(2)

webbrowser.get(chrome).open_new(url3)

webbrowser.get(chrome).open_new(url2)

time.sleep(1)

webbrowser.get(chrome).open_new(url3)

webbrowser.get(chrome).open_new(url)

time.sleep(1)

webbrowser.get(chrome).open_new(url2)

webbrowser.get(chrome).open_new(url)

time.sleep(1)

webbrowser.get(chrome).open_new(url2)

webbrowser.get(chrome).open_new(url3)

time.sleep(1)

webbrowser.get(chrome).open_new(url)

webbrowser.get(chrome).open_new(url2)

webbrowser.get(chrome).open_new(url)

webbrowser.get(chrome).open_new(url3)

webbrowser.get(chrome).open_new(url)

webbrowser.get(chrome).open_new(url3)

print("all done, number of visiting webpages in google chrome = 28 times")