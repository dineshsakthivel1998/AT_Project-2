from selenium.webdriver.common.by import By

class EmergencyContact :
    click_emergencycontact_xpath = "//*[contains(text(),'Emergency Contacts')]"
    click_add_xpath = "//div[2]/div[1]/div/button[text()=' Add ']"
    txtbox_name_xpath = "//label[text()='Name']/parent::div/following-sibling::div/input"
    txtbox_relationship_xpath = "//label[text()='Relationship']/parent::div/following-sibling::div/input"
    txtbox_telephone_xpath = "//label[text()='Home Telephone']/parent::div/following-sibling::div/input"
    txtxbox_mobile_xpath = "//label[text()='Mobile']/parent::div/following-sibling::div/input"
    txtbox_worktelephone_xpath = "//label[text()='Work Telephone']/parent::div/following-sibling::div/input"
    btn_save_xpath = "//button[text()=' Save ']"
    msg_successfullysaved_xpath = "//*[text()='Successfully Saved']"

    def __init__(self, driver):
        self.driver = driver

    def ClickEmergencyContacts(self):
        self.driver.find_element(By.XPATH, self.click_emergencycontact_xpath).click()

    def ClickADD(self):
        self.driver.find_element(By.XPATH, self.click_add_xpath).click()

    def Name(self, name):
        self.driver.find_element(By.XPATH, self.txtbox_name_xpath).send_keys(name)

    def Relationship(self, relationship):
        self.driver.find_element(By.XPATH, self.txtbox_relationship_xpath).send_keys(relationship)

    def HomeTelephone(self, hometelephone):
        self.driver.find_element(By.XPATH, self.txtbox_telephone_xpath).send_keys(hometelephone)

    def Mobile(self, mobile):
        self.driver.find_element(By.XPATH, self.txtxbox_mobile_xpath).send_keys(mobile)

    def WorkTelephone(self, worktelephone):
        self.driver.find_element(By.XPATH, self.txtbox_worktelephone_xpath).send_keys(worktelephone)

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def ValidateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_successfullysaved_xpath).is_displayed()
        except:
            return False