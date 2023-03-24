import time

from selenium.webdriver.common.by import By

class Employeelist :
    txtbox_empname_xpath = "//form/div/div/div[1]//input[@placeholder='Type for hints...']"
    dropdown_empname_xpath = "//*[contains(text(),'Ramesh kumar')]"
    dropdown_include_xpath = "//*[text()='Current Employees Only']"
    select_include_xpath = "//*[text()='Current and Past Employees']"
    btn_search_xpath = "//button[@type='submit']"
    btn_editemp_xpath = "//button/i[@class ='oxd-icon bi-pencil-fill']"
    tabs_xpath = "//div[@role='tab']"
    actual_result = []


    def __init__(self, driver):
        self.driver = driver

    def EnterEmployeeName(self, employeename):
        self.driver.find_element(By.XPATH, self.txtbox_empname_xpath).send_keys(employeename)
        time.sleep(3)

    def Currentandpastemployees(self):
        self.driver.find_element(By.XPATH, self.dropdown_include_xpath).click()
        self.driver.find_element(By.XPATH, self.select_include_xpath).click()

    def Clicksearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def Clickeditbutton(self):
        self.driver.find_element(By.XPATH, self.btn_editemp_xpath).click()


    def tab_element(self):
        tab_elements = self.driver.find_elements(By.XPATH, self.tabs_xpath)
        for item in tab_elements:
            self.actual_result.append(item.text)
        return self.actual_result
