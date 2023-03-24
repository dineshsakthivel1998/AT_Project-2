import time

from selenium.webdriver.common.by import By

class Job:
    click_job_xpath = "//*[contains(text(),'Job')]"
    datepic_join_xpath = "//*[@placeholder='yyyy-mm-dd' ]"
    dropdown_title_xpath = "//form/div[1]/div/div[2]/div/div[2]/div/div[1]"
    select_qaengineer_xpath = "//*[contains(text(),'QA Engineer')]"
    dropdown_category_xpath = "//form/div[1]/div/div[4]/div/div[2]/div/div[1]"
    select_professionals_xpath = "//*[contains(text(),'Professionals')]"
    dropdown_subunit_xpath = "//form/div[1]/div/div[5]/div/div[2]/div/div[1]"
    select_QA_xpath = "//*[contains(text(),'Quality Assurance')]"
    dropdown_location_xpath = "//form/div[1]/div/div[6]/div/div[2]/div/div[1]"
    select_location_xpath = "//*[contains(text(),'Texas R&D')]"
    dropdown_empstatus_xpath = "//form/div[1]/div/div[7]/div/div[2]/div/div[1]"
    select_status_xpath = "//*[contains(text(),'Full-Time Permanent')]"
    toggle_contract_xpath = "//label/span"
    contract_start_xpath = "//form/div[3]/div/div[1]/div/div[2]/div/div/input"
    contract_end_xpath = "//form/div[3]/div/div[2]/div/div[2]/div/div/input"
    btn_save_xpath = "//button[text()=' Save ']"
    btn_terminate_xpath = "//button[text()=' Terminate Employment ']"
    terminate_date_xpath = "//form/div[1]/div/div[2]/div/div/input"
    terminate_reason_xpath = "//form/div[2]/div/div[2]/div/div/div[text()='-- Select --']"
    select_reason_xpath = "//*[contains(text(),'Resigned')]"
    terminate_save_xpath = "//form/div[4]/button[2]"
    terminate_date_show = "//p[@class='oxd-text oxd-text--p orangehrm-terminate-date']"
    btn_active_xpath = "//div/div[2]/div[2]/div/button"
    msg_successfullysaved_xpath = "//*[text()='Successfully Updated']"

    def __init__(self, driver):
        self.driver = driver

    def GotoJob(self):
        self.driver.find_element(By.XPATH, self.click_job_xpath).click()

    def Joindate(self, date):
        self.driver.find_element(By.XPATH, self.datepic_join_xpath).send_keys(date)

    def JobTitle(self):
        self.driver.find_element(By.XPATH, self.dropdown_title_xpath).click()
        self.driver.find_element(By.XPATH, self.select_qaengineer_xpath).click()

    def JobCategory(self):
        self.driver.find_element(By.XPATH, self.dropdown_category_xpath).click()
        self.driver.find_element(By.XPATH, self.select_professionals_xpath).click()

    def SubUnit(self):
        self.driver.find_element(By.XPATH, self.dropdown_subunit_xpath).click()
        self.driver.find_element(By.XPATH, self.select_QA_xpath).click()

    def Location(self):
        self.driver.find_element(By.XPATH, self.dropdown_location_xpath).click()
        self.driver.find_element(By.XPATH, self.select_location_xpath).click()

    def EmployeeStatus(self):
        self.driver.find_element(By.XPATH, self.dropdown_empstatus_xpath).click()
        self.driver.find_element(By.XPATH, self.select_status_xpath).click()


    def Contract(self):
        self.driver.find_element(By.XPATH, self.toggle_contract_xpath).click()


    def ContractStart(self, start):
        self.driver.find_element(By.XPATH, self.contract_start_xpath).send_keys(start)

    def ContractEnd(self, End):
        self.driver.find_element(By.XPATH, self.contract_end_xpath).send_keys(End)

    def savecontract(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def ValidateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_successfullysaved_xpath).is_displayed()
        except:
            return False

    def TerminateEmployee(self):
        self.driver.find_element(By.XPATH, self.btn_terminate_xpath).click()

    def TerminateDate(self, terminate):
        self.driver.find_element(By.XPATH, self.terminate_date_xpath).send_keys(terminate)

    def TerminateReason(self):
        self.driver.find_element(By.XPATH, self.terminate_reason_xpath).click()
        self.driver.find_element(By.XPATH, self.select_reason_xpath).click()
        time.sleep(3)

    def SaveTerminate(self):
        self.driver.find_element(By.XPATH, self.terminate_save_xpath).click()

    def ClickActive(self):
        self.driver.find_element(By.XPATH, self.btn_active_xpath).click()


    def Date(self):
        try:
            return self.driver.find_element(By.XPATH, self.terminate_date_show).is_displayed()
        except:
            return False

    def ActivateEmployment(self):
        try:
            return self.driver.find_element(By.XPATH, self.btn_active_xpath).is_displayed()
        except:
            return False

    def TerminateEmployment(self):
        try:
            return self.driver.find_element(By.XPATH, self.btn_terminate_xpath).is_displayed()
        except:
            return False