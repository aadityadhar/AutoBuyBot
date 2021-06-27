import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RelianceDigital :
	def __init__(self):
		webOptions = webdriver.ChromeOptions()
		webOptions.add_argument("start-maximized")
		webOptions.add_argument("disable-infobars")

		self.driver = webdriver.Chrome(executable_path=r"/pathtothechromedriver",options=options)

	def login(self,email,password,url):
		self.driver.get(url)
		login_email = self.driver.find_element_by_xpath("//input[@id='email']")
		login_email.send_keys(email)
		login_password = self.driver.find_element_by_xpath("//input[@id='pass']")
		login_password.send_keys(password)
		loginButton = self.driver.find_element_by_xpath("//button/span[(.)='Continue']")
		loginButton.click()
		time.sleep(1)

	def loginGoogle(self,url):
		self.driver.get(url)
		window_before = self.driver.window_handles[0]
		loginViaGoogle = self.driver.find_element_by_xpath("//button/span[contains((.),'Google')]")
		loginViaGoogle.click()
		window_after = self.driver.window_handles[1]
		self.driver.switch_to.window(window_after)
		emailLink = self.driver.find_element_by_xpath("//div[(.)='aaditya.dhar@gmail.com']")
		emailLink.click()
		self.driver.switch_to(window_before)

	def addToCart(self,url):
		self.driver.get(url)

		addToCart = false

		while not addToCart:
			try:
				addToCartButton = self.driver.find_element_by_xpath("//button/span[(.)='ADD TO CART']")
                addToCartButton.click()
                addToCart = True
            except:
                self.driver.refresh()
        time.sleep(0.5)

    def checkout(self,url,upi):
    	self.driver.get(url)
    	proceedToCheckout = self.driver.find_element_by_xpath("//div[(.)='Have a Coupon?']/../../../preceding-sibling::div/button[contains((.),'CHECKOUT')]")
    	proceedToCheckout.click()
    	selectAddress = self.driver.find_element_by_xpath("//button/span[(.)='Deliver here']")
    	selectAddress.click()
    	try:
    		mobileConfirmation = self.driver.find_element_by_xpath("//button/span[(.)='Ok, Got it']")
    		mobileConfirmation.click()
    	except:
    		print("Mobile confirmation not asked!!")
    	proceedToPayment = self.driver.find_element_by_xpath("//button[@id='btn-ptp-w']/span[(.)='Proceed To Payment']")
    	proceedToCheckout.click()
    	time.sleep(1)
    	upiCheck = self.driver.find_element_by_xpath("//div[(.)='UPI']/preceding-sibling::span")
    	upiCheck.click()
    	terms = self.driver.find_element_by_xpath("(//span[@class='checkBox__checkmark'])[2]")
    	terms.click()
    	payButton = self.driver.find_element_by_xpath("(//span[@class='checkBox__checkmark']/../../../../following-sibling::div/button/span[contains((.),'PAY RS. ')])[3]")
    	payButton.click()
    	upiAddress = self.driver.find_element_by_xpath("//input[@id='vpAddress']")
    	upiAddress.send_keys(upi)
    	makePayment = self.driver.find_element_by_xpath("//button[(.)='Make Payment ']")
    	makePayment.click()

if __name__=="__main__":
    autoBuyBot = RelianceDigital()

    email = ""
    password = ""
    upi = ""

    autoBuyBot.login("https://www.reliancedigital.in/signin",email,password)

    #Uncomment this and comment the line above if you want to login via google
    #autoBuyBot.loginGoogle("https://www.reliancedigital.in/signin")

    autoBuyBot.add_to_cart("https://www.reliancedigital.in/sony-cfi-1008b01r-playstation-5-digital-edition-console-with-dualsense-wireless-controller-3d-audio-technology/p/491936181")

    #use this for disc edition : 

    autoBuyBot.checkout("https://www.reliancedigital.in/cart",upi)