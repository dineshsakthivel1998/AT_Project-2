import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Admin:
    clik_admin_xpath = "//span[text()='Admin']"
    menu_xpath = "//ul[@class='oxd-main-menu']/li/a/span"
    actual_result = []
    search_box_xpath = "//input[@placeholder='Search']"
    result_input_xpath = "//ul[@class='oxd-main-menu']/li/a/span"

    click_usermanagement_xpath ="//span[contains(text(),'User Management ')]"
    click_users_xpath = "//*[contains(text(),'Users')]"
    dropdown_userrole_xpath ="//form/div/div/div[2]//div[text()='-- Select --']"
    validate_drpdownadmin_xpath = "//*[contains(text(),'Admin')]"
    validate_drpdowness_xpath ="//*[contains(text(),'ESS')]"
    dropdown_status_xpath ="//form/div/div/div[4]//div[text()='-- Select --']"
    validate_enabled_xpath = "//*[contains(text(),'Enabled')]"
    validate_disabled_xpath = "//*[contains(text(),'Disabled')]"


    def __init__(self, driver):
        self.driver = driver

    def GoToAdmin(self):
        self.driver.find_element(By.XPATH, self.clik_admin_xpath).click()

    def menu_element(self):
        menu_elements = self.driver.find_elements(By.XPATH, self.menu_xpath)
        for item in menu_elements:
            self.actual_result.append(item.text)
        return self.actual_result

    def search_box(self, item):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(item)

    def result(self):
        return self.driver.find_element(By.XPATH, self.result_input_xpath).text

    def clear(self):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)


    def ClickUserManagement(self):
        self.driver.find_element(By.XPATH, self.click_usermanagement_xpath).click()

    def ClickUsers(self):
        self.driver.find_element(By.XPATH, self.click_users_xpath).click()

    def ValidateDropdownAdmin(self):
        self.driver.find_element(By.XPATH, self.dropdown_userrole_xpath).click()
        time.sleep(3)
        try:
            return self.driver.find_element(By.XPATH, self.validate_drpdownadmin_xpath).is_displayed()
        except:
            return False


    def ValidateDropdownESS(self):
        try:
            return self.driver.find_element(By.XPATH, self.validate_drpdowness_xpath).is_displayed()
        except:
            return False

    def ValidateEnabled(self):
        self.driver.find_element(By.XPATH, self.dropdown_status_xpath).click()
        try:
            return self.driver.find_element(By.XPATH, self.validate_enabled_xpath).is_displayed()
        except:
            return False

    def ValidateDisabled(self):
        try:
            return self.driver.find_element(By.XPATH, self.validate_disabled_xpath).is_displayed()
        except:
            return False