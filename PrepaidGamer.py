import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PrepaidGamer :
	def __init__(self):
		webOptions = webdriver.ChromeOptions()
		webOptions.add_argument("start-maximized")
		webOptions.add_argument("disable-infobars")

		self.driver = webdriver.Chrome(executable_path=r"/pathtothechromedriver",options=options)

	def login(self,email,password,url):
		self.driver.get(url)
		login_email = self.driver.find_element_by_xpath("//input[@id='username']")
		login_email.send_keys(email)
		login_password = self.driver.find_element_by_xpath("//input[@id='passsword']")
		login_password.send_keys(password)
		loginButton = self.driver.find_element_by_xpath("//button[(.)='Log in']")
		loginButton.click()
		time.sleep(1)

	def addToCart(self,url):
		self.driver.get(url)

		addToCart = false

		while not addToCart:
			try:
				addToCartButton = self.driver.find_element_by_xpath("//button[(.)='Add to cart']")
                addToCartButton.click()
                addToCart = True
            except:
                self.driver.refresh()
        time.sleep(0.5)

    def checkout(self,upi):
    	proceedToCheckout = self.driver.find_element_by_xpath("//a[contains(@class,'checkout') and contains((.),'Proceed to checkout')]")
    	proceedToCheckout.click()
    	time.sleep(1)
    	upiCheck = self.driver.find_element_by_xpath("//input[@id='payment_method_wc-upi']")
    	upiCheck.click()
    	time.sleep(0.5)
    	upiAddress = self.driver.find_element_by_xpath("//input[@id='upiwc-address']")
    	upiAddress.send_keys(upi)
    	payButton = self.driver.find_element_by_xpath("//button[(.)='Place Order']")
    	payButton.click()
    	
if __name__=="__main__":
    autoBuyBot = RelianceDigital()

    email = ""
    password = ""
    upi = ""

    autoBuyBot.login("https://prepaidgamercard.com/my-account/",email,password)

    autoBuyBot.add_to_cart("https://prepaidgamercard.com/product/playstation-5-digital-edition-ps5/")

    #use this for disc edition : 

    autoBuyBot.checkout(upi)