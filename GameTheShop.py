import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GameTheShop : 
	def __init__(self):
		webOptions = webdriver.ChromeOptions()
		webOptions.add_argument("start-maximized")
		webOptions.add_argument("disable-infobars")

		self.driver = webdriver.Chrome(executable_path=r"/pathtothechromedriver",options=options)

	def login(self,email,password,url):
		self.driver.get(url)
		login_email = self.driver.find_element_by_xpath("//div[@class='cls-txtbx-otrdiv']/input[@type='text' and @value='E-mail']")
		login_email.send_keys(email)
		login_password = self.driver.find_element_by_xpath("//div[@class='cls-txtbx-otrdiv']/input[@type='password']")
		login_password.send_keys(password)
		signin = self.driver.find_element_by_xpath("//input[@type='submit' and contains(@id,'btnSubmit')]")
		signin.click()

	def add_to_cart(self,url):
		time.sleep(1)
		self.driver.get(url)

		addToCart = false

		while not addToCart:
			try:
				addToCartButton = self.driver.find_element_by_xpath("//div[(.)='ADD TO CART']")
                addToCartButton.click()
                addToCart = True
            except:
                self.driver.refresh()
        time.sleep(1)
		
	def checkout(self, mobile):
		go_to_cart = self.driver.find_element_by_xpath("//span[@class='headerCartC']")
		go_to_cart.click()
		time.sleep(1)
		proceedToCheckout = self.driver.find_element_by_xpath("//a[contains(@id,'clsProcChkout') and contains((.),'Proceed to')]")
		proceedToCheckout.click()
		#time.sleep(0.5)
		cont1 = self.driver.find_element_by_xpath("//input[@id='btnLoggedinContinue']")
		cont1.click()
		#time.sleep(0.5)
		shipping = self.driver.find_element_by_xpath("(//div[(.)='SHIP MY ORDER TO THIS ADDRESS'])[1]")
		shipping.click()
		#time.sleep(0.5)
		cont2 = self.driver.find_element_by_xpath("//input[@name='btnShippingContinue']")
		cont2.click()
		#time.sleep(0.5)
		proceedToPayment = self.driver.find_element_by_xpath("//input[@id='btnProceedToPayment']")
		proceedToPayment.click()
		#time.sleep(0.5)
		payButton = self.driver.find_element_by_xpath("//input[@id='btnPayPaytm']")
		payButton.click()
		#time.sleep(0.5)
		paytmMobile = self.driver.find_element_by_xpath("//input[@id='inp']")
		paytmMobile.send_keys(mobile)
		proceed = self.driver.find_element_by_xpath("//button/span/span[(.)='Proceed']")
		proceed.click()

if __name__=="__main__":
    autoBuyBot = GameTheShop()

    email = ""
    password = ""
    mobile = ""

    autoBuyBot.login("https://www.gamestheshop.com/sign-in",email,password)

    autoBuyBot.add_to_cart("https://www.gamestheshop.com/PlayStation-5-Console/5112")

    #use this for disc edition : https://www.gamestheshop.com/PlayStation-5-Console/5111

    autoBuyBot.checkout(mobile)