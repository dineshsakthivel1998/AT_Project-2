from selenium.webdriver.common.by import By

class Login:
    txt_username_xpath = "//input[@name='username']"
    txt_password_xpath = "//input[@name='password']"
    btn_loginbutton_xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def setusername (self,username):
        self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys(username)

    def setpassword (self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def clickloginbutton (self):
        self.driver.find_element(By.XPATH, self.btn_loginbutton_xpath).click()

