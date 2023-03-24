from selenium.webdriver.common.by import By

class ContactDetails:
    click_contactdetails_xpath = "//*[contains(text(),'Contact Details')]"
    txtbox_street1_xpath ="//*[text()='Street 1']/parent::div/following-sibling::div/input"
    txtbox_street2_xpath ="//*[text()='Street 2']/parent::div/following-sibling::div/input"
    txtbox_city_xpath = "//*[text()='City']/parent::div/following-sibling::div/input"
    txtbox_state_xpath ="//*[text()='State/Province']/parent::div/following-sibling::div/input"
    txtbox_zipcode_xpath ="//*[text()='Zip/Postal Code']/parent::div/following-sibling::div/input"
    drpdown_country_xpath = "//*[contains(text(),'Select')]"
    click_india_xpath = "//*[contains(text(),'India')]"
    txtbox_home_xpath ="//*[text()='Home']/parent::div/following-sibling::div/input"
    txtbox_mobile_xpath = "//*[text()='Mobile']/parent::div/following-sibling::div/input"
    txtbox_work_xpath =  "//*[text()='Work']/parent::div/following-sibling::div/input"
    txtbox_workemail_xpath = "//*[text()='Work Email']/parent::div/following-sibling::div/input"
    txtbox_otheremail_xpath = "//*[text()='Other Email']/parent::div/following-sibling::div/input"
    btn_save_xpath = "//button[@type='submit']"
    msg_successfullysaved_xpath = "//*[text()='Successfully Updated']"

    def __init__(self,driver):
        self.driver = driver

    def GotoContactDetails(self):
        self.driver.find_element(By.XPATH, self.click_contactdetails_xpath).click()

    def Street1(self, street1):
        self.driver.find_element(By.XPATH, self.txtbox_street1_xpath).send_keys(street1)

    def Street2(self, street2):
        self.driver.find_element(By.XPATH, self.txtbox_street2_xpath).send_keys(street2)

    def City(self, city):
        self.driver.find_element(By.XPATH, self.txtbox_city_xpath).send_keys(city)

    def State(self, state):
        self.driver.find_element(By.XPATH, self.txtbox_state_xpath).send_keys(state)

    def Zipcode(self, zipcode):
        self.driver.find_element(By.XPATH, self.txtbox_zipcode_xpath).send_keys(zipcode)

    def Country(self):
        self.driver.find_element(By.XPATH, self.drpdown_country_xpath).click()
        self.driver.find_element(By.XPATH, self.click_india_xpath).click()

    def Home(self, home):
        self.driver.find_element(By.XPATH, self.txtbox_home_xpath).send_keys(home)

    def Mobile(self, mobile):
        self.driver.find_element(By.XPATH, self.txtbox_mobile_xpath).send_keys(mobile)

    def Work(self, work):
        self.driver.find_element(By.XPATH, self.txtbox_work_xpath).send_keys(work)

    def WorkEmail(self, email ):
        self.driver.find_element(By.XPATH, self.txtbox_workemail_xpath).send_keys(email)

    def OtherEmail(self, otherEmail):
        self.driver.find_element(By.XPATH, self.txtbox_otheremail_xpath).send_keys(otherEmail)

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def ValidateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_successfullysaved_xpath).is_displayed()
        except:
            return False