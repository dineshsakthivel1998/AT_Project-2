from selenium.webdriver.common.by import By

class Dependency :
    click_dependent_xpath = "//*[contains(text(),'Dependents')]"
    click_add_xpath = "//div[2]/div[1]/div/button[text()=' Add ']"
    txtbox_name_xpath = "//label[text()='Name']/parent::div/following-sibling::div/input"
    dropdown_relationship_xpath = "//*[contains(text(),'Select')]"
    click_child_xpath = "//*[contains(text(),'Child')]"
    datepic_dob_xpath = "//input[@placeholder='yyyy-mm-dd']"
    btn_save_xpath = "//button[text()=' Save ']"
    msg_successfullysaved_xpath = "//*[text()='Successfully Saved']"


    def __init__(self, driver):
        self.driver = driver

    def ClickDependent(self):
        self.driver.find_element(By.XPATH, self.click_dependent_xpath).click()

    def ClickAdd(self):
        self.driver.find_element(By.XPATH, self.click_add_xpath).click()

    def Name(self, name):
        self.driver.find_element(By.XPATH, self.txtbox_name_xpath).send_keys(name)

    def Relationship(self):
        self.driver.find_element(By.XPATH, self.dropdown_relationship_xpath).click()
        self.driver.find_element(By.XPATH, self.click_child_xpath).click()

    def DateOfBirth(self, DOB):
        self.driver.find_element(By.XPATH, self.datepic_dob_xpath).send_keys(DOB)

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def ValidateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_successfullysaved_xpath).is_displayed()
        except:
            return False