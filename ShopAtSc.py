import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopAtSC :
	def __init__(self):
		webOptions = webdriver.ChromeOptions()
		webOptions.add_argument("start-maximized")
		webOptions.add_argument("disable-infobars")

		self.driver = webdriver.Chrome(executable_path=r"/pathtothechromedriver",options=options)

	def login(self,email,password,url):
		self.driver.get(url)
		login_email = self.driver.find_element_by_xpath("//input[@id='customer_email']")
		login_email.send_keys(email)
		login_password = self.driver.find_element_by_xpath("//input[@id='customer_password']")
		login_password.send_keys(password)
		loginButton = self.driver.find_element_by_xpath("//div[@class='form-group']/input[@type='submit' and @value='Login']")
		loginButton.click()
		time.sleep(1)

	def add_to_cart(self,url,pincode):
		self.driver.get(url)
		pincodeInput = self.driver.find_element_by_xpath("//input[@id='pincode_input']")
		pincodeInput.send_keys(pincode)
		checkDelivery = self.driver.find_element_by_xpath("//span[@id='check-delivery-submit' and (.)='Check']")
		checkDelivery.click()

		addToCart = false

		while not addToCart:
			try:
				addToCartButton = self.driver.find_element_by_xpath("//span[(.)='This PIN code is serviceable.']/../../../../../../../../following-sibling::div/input[@id='product-add-to-cart']")
                addToCartButton.click()
                addToCart = True
            except:
                self.driver.refresh()
        time.sleep(0.5)

    def checkout(self,upiID):
    	viewCart = self.driver.find_element_by_xpath("//a[contains((.),'View Cart')]")
    	viewCart.click()
    	time.sleep(1)
    	proceedToCheckout = self.driver.find_element_by_xpath("//input[@id='checkout_button']")
    	proceedToCheckout.click()
    	time.sleep(1)
    	continueToShipping = self.driver.find_element_by_xpath("//button[@id='continue_button']/span[(.)='Continue to shipping']")
    	continueToShipping.click()
    	time.sleep(0.5)
    	continueToPayment = self.driver.find_element_by_xpath("//button[@id='continue_button']/span[(.)='Continue to payment']")
    	continueToPayment.click()
    	time.sleep(0.5)
    	completeOrder = self.driver.find_element_by_xpath("//div[contains(@class,'shown')]/button[@id='continue_button']/span[(.)='Complete order']")
    	completeOrder.click()
    	paymentCheck = self.driver.find_element_by_xpath("//button/div/div/div[(.)='Wallet - PhonePe']")
    	paymentCheck.click()
    	window_before = self.driver.window_handles[0]
    	payButton = self.driver.find_element_by_xpath("//div[@id='footer']/span[contains((.),'Pay ₹')]")
    	payButton.click()
    	window_after = self.driver.window_handles[1]
    	self.driver.switch_to.window(window_after)
    	upiInput = self.driver.find_element_by_xpath("//input[@id='vpaInput' and @placeholder='username@upi']")
    	upiInput.send_keys(upiID)
    	verifyUpi = self.driver.find_element_by_xpath("//a[(.)='VERIFY']")
    	verifyUpi.click()
    	pay = self.driver.find_element_by_xpath("//button[(.)='Pay']")
    	pay.click()


if __name__=="__main__":
    autoBuyBot = ShopAtSC()

    email = ""
    password = ""
    pincode = ""
    upiID = ""

    autoBuyBot.login("https://shopatsc.com/account/login",email,password)

    autoBuyBot.add_to_cart("https://shopatsc.com/products/playstation5-digital-edition",pincode)

    #use this for disc edition : 

    autoBuyBot.checkout(upiID)