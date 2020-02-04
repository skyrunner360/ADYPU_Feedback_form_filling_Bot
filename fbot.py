from selenium import webdriver
from time import sleep
from secrets import *

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
        sleep(2)
        #send signin data
        email_id = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_id.send_keys(email)
        #click on next button
        sleep(2)
        next_btn1 = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next_btn1.click()
        #enter Password
        sleep(2)
        passwd_field = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        passwd_field.send_keys(passwd)
        #click on next button
        next_btn2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        next_btn2.click()
        sleep(5)
        #PAGE 1
        #fill form email id
        sleep(2)
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
        sleep(2)
        course_btn = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        course_btn.click()
        #click on semester button
        sem_btn = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        sem_btn.click()
        #click on subject name
        sub_name = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[7]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        sub_name.click()
        #click on faculty name
        fac_name = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        fac_name.click()
        #click on Q1
        rb1 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div')

        rb1.click()
        a=10
        choice=5 #NOTE - change the value of 5 to adjust score to be given in each question
            #Note You cannot change the score to be given individually
        while True:
             try:
                rb2 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div['+str(a)+']/div/div[2]/div/span/div/div['+str(choice)+']/label/div/div[1]/div/div[3]/div')
                rb2.click()
                a+=1
             except Exception:
                 cmnt_box = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[27]/div/div[2]/div/div[1]/div/div[1]/input')
                 cmnt_box.send_keys(cmnt1)
                 break

        next_btn3 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div')
        next_btn3.click()
        sleep(5)
        #PAGE 2
        sleep(2)
        rb3 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb3.click()
        rb4 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb4.click()
        #start clicking on radio buttons
        b=5
        while True:
            try:
                rb5 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div['+str(b)+']/div/div[2]/div/span/div/div['+str(choice)+']/label/div/div[1]/div/div[3]/div')
                rb5.click()
                b+=1
            except Exception:
                cmnt_box2 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[23]/div/div[2]/div/div[1]/div/div[1]/input')
                cmnt_box2.send_keys(cmnt2)
                break
        next_btn4 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]')
        next_btn4.click()
        sleep(5)
        #PAGE 3
        sleep(2)
        rb6 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb6.click()
        rb7 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb7.click()
        #start clicking on radio buttons
        sleep(2)
        c=5
        while True:
            try:
                rb8 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div['+str(c)+']/div/div[2]/div/span/div/div['+str(choice)+']/label/div/div[1]/div')
                rb8.click()
                c+=1
            except Exception:
                cmnt_box3 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[23]/div/div[2]/div/div[1]/div/div[1]/input')
                cmnt_box3.send_keys(cmnt3)
                break
        next_btn4 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]')
        next_btn4.click()
        sleep(2)
        #PAGE 4
        sleep(2)
        rb6 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb6.click()
        rb7 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb7.click()
        # start clicking on radio buttons
        sleep(2)
        c = 5
        while True:
            try:
                rb8 = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div/div/div[2]/div[' + str(c) + ']/div/div[2]/div/span/div/div[' + str(
                        choice) + ']/label/div/div[1]/div')
                rb8.click()
                c += 1
            except Exception:
                cmnt_box3 = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div/div/div[2]/div[23]/div/div[2]/div/div[1]/div/div[1]/input')
                cmnt_box3.send_keys(cmnt4)
                break
        next_btn4 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]')
        next_btn4.click()
        sleep(2)
        #PAGE 5
        sleep(2)
        rb6 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb6.click()
        rb7 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb7.click()
        # start clicking on radio buttons
        sleep(2)
        c = 5
        while True:
            try:
                rb8 = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div/div/div[2]/div[' + str(c) + ']/div/div[2]/div/span/div/div[' + str(
                        choice) + ']/label/div/div[1]/div')
                rb8.click()
                c += 1
            except Exception:
                cmnt_box3 = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div/div/div[2]/div[23]/div/div[2]/div/div[1]/div/div[1]/input')
                cmnt_box3.send_keys(cmnt5)
                break
        next_btn4 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]')
        next_btn4.click()
        sleep(2)
        #PAGE 6
        sleep(2)
        rb6 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb6.click()
        rb7 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb7.click()
        # start clicking on radio buttons
        sleep(2)
        c = 5
        while True:
            try:
                rb8 = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div/div/div[2]/div[' + str(c) + ']/div/div[2]/div/span/div/div[' + str(
                        choice) + ']/label/div/div[1]/div')
                rb8.click()
                c += 1
            except Exception:
                cmnt_box3 = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div/div/div[2]/div[23]/div/div[2]/div/div[1]/div/div[1]/input')
                cmnt_box3.send_keys(cmnt6)
                break
        next_btn4 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]')
        next_btn4.click()
        sleep(2)
        #PAGE 7
        sleep(2)
        rb6 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb6.click()
        rb7 = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        rb7.click()
        # start clicking on radio buttons
        sleep(2)
        c = 5
        while True:
            try:
                rb8 = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div/div/div[2]/div[' + str(c) + ']/div/div[2]/div/span/div/div[' + str(
                        choice) + ']/label/div/div[1]/div')
                rb8.click()
                c += 1
            except Exception:
                cmnt_box3 = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div/div/div[2]/div[23]/div/div[2]/div/div[1]/div/div[1]/input')
                cmnt_box3.send_keys(cmnt7)
                break
        next_btn4 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]')
        next_btn4.click()
        sleep(2)

bot = fbot()
bot.feedback()







