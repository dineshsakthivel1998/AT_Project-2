from selenium.webdriver.common.by import By

class TaxExemptions:
    click_taxexemptions_xpath = "//*[contains(text(),'Tax Exemptions')]"
    dropdown_FITstatus_xpath = "//form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"
    select_FITstatus_xpath = "//*[contains(text(),'Single')]"
    txtbox_FITexemption_xpath = "//form/div/div/div[2]/div/div[2]/input"
    dropdown_state_xpath = "//form/div[2]//div[1]/div/div[2]/div/div/div[1]"
    select_state_xpath = "//*[contains(text(),'New York')]"
    dropdown_SITstatus_xpath = "//form/div[2]//div[2]/div/div[2]/div/div/div[1]"
    select_SITstatus_xpath = "//*[contains(text(),'Single')]"
    txtbox_SITexemption_xpath = "//form/div[2]//div[3]/div/div[2]/input"
    dropdown_unemploymentstate_xpath = "//form/div[2]//div[4]/div/div[2]/div/div/div[1]"
    select_unemploymentstate_xpath = "//*[contains(text(),'Texas')]"
    dropdown_workstate_xpath = "//form/div[2]//div[5]/div/div[2]/div/div/div[1]"
    select_workstate_xpath = "//*[contains(text(),'California')]"
    btn_save_xpath = "//button[@type='submit']"
    msg_successfullysaved_xpath = "//*[text()='Successfully Updated']"

    def __init__(self, driver):
        self.driver = driver


    def GotoTaxExemptions(self):
        self.driver.find_element(By.XPATH, self.click_taxexemptions_xpath).click()

    def FITstatus(self):
        self.driver.find_element(By.XPATH, self.dropdown_FITstatus_xpath).click()
        self.driver.find_element(By.XPATH, self.select_FITstatus_xpath).click()

    def FITexemptions(self, exemptions):
        self.driver.find_element(By.XPATH, self.txtbox_FITexemption_xpath).send_keys(exemptions)

    def State(self):
        self.driver.find_element(By.XPATH, self.dropdown_state_xpath).click()
        self.driver.find_element(By.XPATH, self.select_state_xpath).click()

    def SITstatus(self):
        self.driver.find_element(By.XPATH, self.dropdown_SITstatus_xpath).click()
        self.driver.find_element(By.XPATH, self.select_SITstatus_xpath).click()

    def SITexemption(self, exemption):
        self.driver.find_element(By.XPATH, self.txtbox_SITexemption_xpath).send_keys(exemption)

    def UnEmploymentState(self):
        self.driver.find_element(By.XPATH, self.dropdown_unemploymentstate_xpath).click()
        self.driver.find_element(By.XPATH, self.select_unemploymentstate_xpath).click()

    def WorkState(self):
        self.driver.find_element(By.XPATH, self.dropdown_workstate_xpath).click()
        self.driver.find_element(By.XPATH, self.select_workstate_xpath).click()

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def ValidateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_successfullysaved_xpath).is_displayed()
        except:
            return False