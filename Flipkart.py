import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Flipkart : 
	def __init__(self):
		webOptions = webdriver.ChromeOptions()
		webOptions.add_argument("start-maximized")
		webOptions.add_argument("disable-infobars")

		self.driver = webdriver.Chrome(executable_path=r"/pathtothechromedriver",options=options)


	def login(self,url,email,password):
		self.driver.get(url)
        login = self.driver.find_element_by_xpath("//a[(.)='Login']")
        login.click()
        time.sleep(2)
        #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"")))
        login_email = self.driver.find_element_by_xpath("//span[contains(.,'Enter Email/Mobile number')]//preceding::input[1]")
        login_email.send_keys(email)
        login_password = self.driver.find_element_by_xpath("//span[contains(.,'Enter Password')]//preceding::input[1]")
        login_password.send_keys(password)
        loginButton = self.driver.find_element_by_xpath("//button[@type='submit']//span[contains(.,'Login')]")
        loginButton.click()

	def buy_now(self):
		time.sleep(1)

		buyNow = false

		while not buyNow:
			try:
				buyNowButton = self.driver.find_element_by_xpath("//button[contains((.),'BUY NOW')]")
                buyNowButton.click()
                buyNow = True
            except:
                self.driver.refresh()
        time.sleep(1)


    def completePayment(self):
    	cont = self.driver.find_element_by_xpath("//button[(.)='CONTINUE']")
    	cont.click()
    	time.sleep(1)
    	paymentMode = self.driver.find_element_by_xpath("//div[contains((.),'Google Pay UPI') and contains((.),'aaditya.dhar-1@okaxis')]/../../../label/input")
    	paymentMode.click()
    	#cvvEntry = self.driver,find_element_by_xpath("//input[@type='radio']/../../../../following-sibling::div//span[(.)='ending in 2444']/../../../../../../../following-sibling::div//input[@type='password']")
    	#cvvEntry.send_keys(cvv)
    	continueButton = self.driver.find_element_by_xpath("//div[contains((.),'Google Pay UPI') and contains((.),'aaditya.dhar-1@okaxis')]/div/button[(.)='Continue']")
    	continueButton.click()
    	time.sleep(60)


if __name__=="__main__":
    autoBuyBot = Flipkart()

    email = ""
    password = ""

    autoBuyBot.login("https://www.flipkart.com/sony-playstation-5-cfi-1008b01r-825-gb-astro-s-playroom/p/itm8bf74f8d0b890",email,password)

    #use this for disc : https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa

    autoBuyBot.buy_now()

    autoBuyBot.completePayment()