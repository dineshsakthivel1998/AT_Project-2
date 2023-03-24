import time

from selenium.webdriver.common.by import By

class AddNewEmployee:
    click_pim_xpath = "//span[text()='PIM']"
    menu_xpath = "//ul[@class='oxd-main-menu']/li/a/span"
    actual_result = []
    click_addemp_xpath = "//button[normalize-space()='Add']"
    input_firstname_xpath = "//input[@name='firstName']"
    input_lastname_xpath = "//input[@name='lastName']"
    btn_createlogin_xpath = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    input_username_xpath = "//form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input"
    click_Enabled_xpath = "//label[text()='Enabled']"
    input_password_xpath = "//div/div[1]/div/div[2]/input[@type='password']"
    input_confmpassword_xpath = "//div/div[2]/div/div[2]/input[@type='password']"
    click_savebtn_xpath = "//button[@type='submit']"
    txt_emplyeelist_xpath = "//*[contains(text(),'Employee List')]"

    def __init__(self, driver):
        self.driver = driver

    def GoTOPIM(self):
        self.driver.find_element(By.XPATH, self.click_pim_xpath).click()

    def menu_element(self):
        menu_elements = self.driver.find_elements(By.XPATH, self.menu_xpath)
        for item in menu_elements:
            self.actual_result.append(item.text)
        return self.actual_result

    def ClickAdd(self):
        self.driver.find_element(By.XPATH, self.click_addemp_xpath).click()

    def FirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).send_keys(firstname)

    def LastName(self, lastname):
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).send_keys(lastname)

    def CreateLogin(self):
        self.driver.find_element(By.XPATH, self.btn_createlogin_xpath).click()

    def Username(self, username):
        self.driver.find_element(By.XPATH, self.input_username_xpath).send_keys(username)

    def Enabled(self):
        self.driver.find_element(By.XPATH, self.click_Enabled_xpath).click()

    def Password(self, password):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(password)

    def Confirmpassword(self, confirmpassword):
        self.driver.find_element(By.XPATH, self.input_confmpassword_xpath).send_keys(confirmpassword)

    def ClickSave(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.click_savebtn_xpath).click()

    def ValidateEmployeeList(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_emplyeelist_xpath).is_displayed()
        except:
            return False
