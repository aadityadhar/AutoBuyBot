import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Amazon : 
	def __init__(self):
		webOptions = webdriver.ChromeOptions()
		webOptions.add_argument("start-maximized")
		webOptions.add_argument("disable-infobars")

		self.driver = webdriver.Chrome(executable_path=r"/pathtothechromedriver",options=options)


	def login(self,url,email,password):
		self.driver.get(url)
		login_email = self.driver.find_element_by_xpath("//input[@id='ap_email']")
		login_email.send_keys(email)
		cont = self.driver.find_element_by_xpath("//input[@id='continue']")
		cont.click()
		login_password = self.driver.find_element_by_xpath("//input[@id='ap_password']")
		login_password.send_keys(password)
		signin = self.driver.find_element_by_xpath("//input[@id='signInSubmit']")
		signin.click()


	def buy_now(self,url):
		time.sleep(1)
		self.driver.get(url)

		buyNow = false

		while not buyNow:
			try:
				buyNowButton = self.driver.find_element_by_xpath("//input[@id='buy-now-button']")
                buyNowButton.click()
                buyNow = True
            except:
                self.driver.refresh()
        time.sleep(1)


    def completePayment(self,cvv):
    	paymentMode = self.driver.find_element_by_xpath("//input[@type='radio']/../../../../following-sibling::div//span[(.)='ending in 2444']")
    	paymentMode.click()
    	cvvEntry = self.driver,find_element_by_xpath("//input[@type='radio']/../../../../following-sibling::div//span[(.)='ending in 2444']/../../../../../../../following-sibling::div//input[@type='password']")
    	cvvEntry.send_keys(cvv)
    	continueButton = self.driver.find_element_by_xpath("(//div/span/span/input[@type='submit'])[2]")
    	continueButton.click()
    	time.sleep(3)
    	placeOrder = self.driver.find_element_by_xpath("//span[@id='placeYourOrder']/span/input[@title='Place Your Order and Pay' and @type='submit']")
    	placeOrder.click()

    	#need to add notifications to the user somehow


if __name__=="__main__":
    autoBuyBot = Amazon()

    email = ""
    password = ""
    cvv = ""

    autoBuyBot.login("https://www.amazon.in/gp/sign-in.html",email,password)

    autoBuyBot.buy_now("https://www.amazon.in/Sony-CFI-1008B01R-PlayStation-Digital-Edition/dp/B08FVRQ7BZ")

    #use this for disc edition : https://www.amazon.in/Sony-CFI-1008A01R-PlayStation-5-console/dp/B08FV5GC28
    #use this for bundle1 : https://www.amazon.in/PS5TM-Digital-DualSenseTM-charging-station/dp/B08NTVHTPT

    autoBuyBot.completePayment(cvv)