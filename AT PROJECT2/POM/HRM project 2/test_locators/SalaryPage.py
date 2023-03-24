from selenium.webdriver.common.by import By

class Salary:
    click_salary_xpath = "//*[contains(text(),'Salary')]"
    click_Add_xpath = "//div/div[2]/div/div/button[@type='button']"
    input_salarycomponent_xpath = "//label[text()='Salary Component']/parent::div/following-sibling::div/input"
    dropdown_paygrade_xpath = "//form/div/div/div[2]/div/div[2]"
    select_paygrade_xpath = "//*[contains(text(),'Grade 2')]"
    dropdown_payfrequency_xpath = "//form/div/div/div[3]/div/div[2]"
    select_frequency_xpath = "//*[contains(text(),'Monthly')]"
    dropdown_currency_xpath = "//form/div/div/div[4]/div/div[2]"
    select_currency_xpath = "//*[contains(text(),'United States Dollar')]"
    txtbox_amount_xpath = "//form/div[1]/div/div[5]/div/div[2]/input"
    txtbox_comments_xpath = "//textarea"
    chekbox_directdeposit_xpath = "//form/div[3]/div/label/span"
    input_accountnumber_xpath = "//form/div[4]/div[1]/div[1]/div/div[2]/input"
    drpdown_accounttype_xpath = "//form/div[4]/div[1]/div[2]/div/div[2]/div/div"
    select_type_xpath = "//*[contains(text(),'Savings')]"
    input_routingnumber_xpath = "//form/div[4]/div[2]/div[1]/div/div[2]/input"
    input_amount_xpath = "//form/div[4]/div[2]/div[2]/div/div[2]/input"
    btn_save_xpath = "//*[text()=' Save ']"
    box_visible_xpath = "//form/div[4][@class='oxd-form-row']"
    msg_successfullysaved_xpath = "//*[text()='Successfully Saved']"

    def __init__(self, driver):
        self.driver =  driver

    def GotoSalary(self):
        self.driver.find_element(By.XPATH, self.click_salary_xpath).click()

    def ClickAdd(self):
        self.driver.find_element(By.XPATH, self.click_Add_xpath).click()

    def SalaryComponent(self,salarycomponent):
        self.driver.find_element(By.XPATH, self.input_salarycomponent_xpath).send_keys(salarycomponent)

    def PayGrade(self):
        self.driver.find_element(By.XPATH, self.dropdown_paygrade_xpath).click()
        self.driver.find_element(By.XPATH, self.select_paygrade_xpath).click()

    def PayFrequency(self):
        self.driver.find_element(By.XPATH, self.dropdown_payfrequency_xpath).click()
        self.driver.find_element(By.XPATH, self.select_frequency_xpath).click()

    def Currency(self):
        self.driver.find_element(By.XPATH, self.dropdown_currency_xpath).click()
        self.driver.find_element(By.XPATH, self.select_currency_xpath).click()

    def Amount(self, amount):
        self.driver.find_element(By.XPATH, self.txtbox_amount_xpath).send_keys(amount)

    def Comments(self, comments):
        self.driver.find_element(By.XPATH, self.txtbox_comments_xpath).send_keys(comments)

    def DirectDeposit(self):
        self.driver.find_element(By.XPATH, self.chekbox_directdeposit_xpath).click()

    def Visiblefields(self):
        try:
            return self.driver.find_element(By.XPATH, self.box_visible_xpath).is_displayed()
        except:
            return False

    def AccountNumber(self, accnumber):
        self.driver.find_element(By.XPATH, self.input_accountnumber_xpath).send_keys(accnumber)

    def AccountType(self):
        self.driver.find_element(By.XPATH, self.drpdown_accounttype_xpath).click()
        self.driver.find_element(By.XPATH, self.select_type_xpath).click()

    def RoutingNumber(self, routing):
        self.driver.find_element(By.XPATH, self.input_routingnumber_xpath).send_keys(routing)

    def DepositAmount(self, depamount):
        self.driver.find_element(By.XPATH, self.input_amount_xpath).send_keys(depamount)

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def ValidateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_successfullysaved_xpath).is_displayed()
        except:
            return False