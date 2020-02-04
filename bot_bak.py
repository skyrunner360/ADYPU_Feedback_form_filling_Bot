from selenium import webdriver
from time import sleep
from secrets import link,email,name,urn,cmnt,passwd

class fbot():
    def __init__(self):
        #open web browser (chrome)
        self.driver = webdriver.Chrome()
    def feedback (self):
        #open feedback form link
        self.driver.get(link)
        sleep(2)
        #click on sign in button
        signin_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span')
        signin_btn.click()
        #send signin data
        email_id = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_id.send_keys(email)
        #click on next button
        next_btn1 = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next_btn1.click()
        #enter Password
        passwd_field = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        passwd_field.send_keys(passwd)
        #click on next button
        next_btn2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        next_btn2.click()
        #fill form email id
        form_email = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input')
        form_email.send_keys(email)
        #Click on university name
        uni_name = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        uni_name.click()
        #fill Student Name
        std_name = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input')
        std_name.send_keys(name)
        #fill urn field
        urn_field = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input')
        urn_field.send_keys(urn)
        #click on course Button
        course_btn = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div/div')
        course_btn.click()
        #click on semester button
        sem_btn = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        sem_btn.click()
        #click on subject name
        sub_name = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[7]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        sub_name.click()
        #click on faculty name
        fac_name = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        fac_name.click()
        #click on Q1
        rb1 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div')

        rb1.click()














