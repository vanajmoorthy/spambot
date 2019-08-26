`from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the person/group you want to message: ')
message = input('Enter your message: ')
count = int(input('Enter number of times you want to send this message: '))

input('Enter a random key after scanning the QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

message_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    message_box.send_keys(message)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
