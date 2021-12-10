#make the necessary imports
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#function to send attachments to a list of contacts
def send_attachments():

    #the list of contacts and groups to which we want to send the attachments
    targets = ["Contact A", "Contact B", "Group A", "Group B"]

    #path of the attachment to be sent
    attachment_path = "/dir1/subdir1/image_name.jpg"

    #type of the attachment: img/doc
    attachment_type = "img"
    for target in targets:

        #finding the search bar for searching the name of the contact/group and clicking it
        driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"][@dir="ltr"]').click()

        #wait for the action to be completed
        time.sleep(3)

        #typing the name of the contact/group to which the attachment is to be sent
        driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"][@dir="ltr"]').send_keys(target)

        #wait for the search results to appear
        time.sleep(3)

        #finding the correct chat in the search results and clicking it
        driver.find_element_by_xpath('//span[@title="{}"][@dir="auto"][@class="_1hI5g _1XH7x _1VzZY"]'.format(target)).click()

        #wait for the chat to open
        time.sleep(3)

        #finding the "send attachment" button and clicking it
        driver.find_element_by_xpath('//div[@title="Attach"]').click()

        #finding and sending keys to the correct attachment button based on the type of the attachment
        if attachment_type == "img":
            driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(attachment_path)
        if attachment_type == "doc":
            driver.find_element_by_xpath('//input[@type = "file"] [@accept="*"] [@multiple=""][@style="display: none;"]').send_keys(attachment_path)

        #wait for the attachment preview to appear
        time.sleep(3)

        #finding and clicking the send button
        driver.find_element_by_xpath('//div[@role="button"][@tabindex="0"][@class="q2PP6 _3Git-"]').click()

        #wait for the next screen to load before moving on to the next contact
        time.sleep(3)

def send_messages():
    targets = ["Contact A", "Group A", "Group B"]
    common_msg = "Hi {}! It's been a long time since we last met! Let's get a cup of coffee sometime."
    for target in targets:

        #finding the search bar for searching the name of the contact/group and clicking it
        driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"][@dir="ltr"]').click()

        #wait for the action to be completed
        time.sleep(3)

        #typing the name of the contact/group to which the attachment is to be sent
        driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"][@dir="ltr"]').send_keys(target)

        #wait for the search results to appear
        time.sleep(3)

        #finding the correct chat in the search results and clicking it
        driver.find_element_by_xpath('//span[@title="{}"][@dir="auto"][@class="_1hI5g _1XH7x _1VzZY"]'.format(target)).click()

        #wait for the chat to open
        time.sleep(3)

        #finding the input box and sending keys to it in the form of the common message
        driver.find_element_by_xpath('//div[@class = "_1awRl copyable-text selectable-text"] [@contenteditable="true"] [@data-tab="6"] [@dir="ltr"] [@spellcheck="true"]').send_keys(common_msg.format(target))

        #wait for the action to complete
        time.sleep(3)

        #finding and clicking the send button
        driver.find_element_by_xpath('//div[@class="_3qpzV"]').click()

        #wait for the next screen to load before moving on to the next contact
        time.sleep(3)

#save the path of chromedriver that you installed on your system in a variable
chrome_driver_path = "/dir2/subdir2/chromedriver"

#create an instance of chrome browser on your system using chromedriver
driver = webdriver.Chrome(chrome_driver_path)

#if you wish to use Firefox instead of Chrome, install geckodriver on your system and then uncomment the following line
#make sure that you have added the path of geckodriver in your PATH environment variable before running this script
#if you do not know how to add paths into PATH, then Google it, you will get decent tutorials on that
#driver = webdriver.Firefox()

#open whatsapp web
driver.get("https://web.whatsapp.com/")

#wait for the webpage to load and scan the QR code
time.sleep(10)

#function calls
send_messages()
send_attachments()
