from selenium.webdriver.common.by import By

class personaldetails :
    txtname_nickname_xpath = "//label[text()='Nickname']/parent::div/following-sibling::div/input"
    txtbox_otherid_xpath = "//div[2]/div[1]/div[2]/div[1]/div[2]/input"
    txtbox_drivinglicense_xpath = "//div[2]/div[2]/div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    datepic_licenseexpdate_xpath = "//div[2]/div/div[2]/div/div/input[@placeholder='yyyy-mm-dd']"
    txtbox_ssnnumber_xpath = "//div[2]/div[3]/div[1]/div[1]/div[2]/input"
    txtbox_sinnumber_xpath = "//div[2]/div[3]/div[2]/div[1]/div[2]/input"
    dropdown_nationality_xpath = "//form/div[3]/div/div[1]//div[text()='-- Select --']"
    select_nationality_xpath = "//*[contains(text(),'Indian')]"
    dropdown_maritialstatus_xpath = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    select_single_xpath = "//*[contains(text(),'Single')]"
    select_married_xpath = "//*[contains(text(),'Married')]"
    datepic_DOB_xpath = "//div[3]//input[@placeholder='yyyy-mm-dd']"
    radiobtn_gender_xpath = "//label[text()='Male']"
    txtbox_militaryser_xpath = "//label[text()='Military Service']/parent::div/following-sibling::div/input"
    personaldetails_savebtn_xpath = "//div[5]/button[@type='submit']"
    dropdown_bloodtype_xpath = "//form/div[1]/div/div[1]//div[text()='-- Select --']"
    select_bloodtype_xpath = "//*[contains(text(),'B+')]"
    customfield_savebtn_xpath = "//div[2]/button[@type='submit']"
    msg_successfullysaved_xpath = "//*[text()='Successfully Updated']"


    def __init__(self, driver):
        self.driver = driver

    def AddNickname(self, nickname):
        self.driver.find_element(By.XPATH, self.txtname_nickname_xpath).send_keys(nickname)

    def AddOtherid(self, otherid):
        self.driver.find_element(By.XPATH, self.txtbox_otherid_xpath).send_keys(otherid)

    def AddDrivingLicense(self, drivinglicense):
        self.driver.find_element(By.XPATH, self.txtbox_drivinglicense_xpath).send_keys(drivinglicense)

    def LicenseExpdate(self, licenseexpdate):
        self.driver.find_element(By.XPATH, self.datepic_licenseexpdate_xpath).send_keys(licenseexpdate)

    def Addssnnumber(self, ssnnumber):
        self.driver.find_element(By.XPATH, self.txtbox_ssnnumber_xpath).send_keys(ssnnumber)

    def Addsinnumber(self, sinnumber):
        self.driver.find_element(By.XPATH, self.txtbox_sinnumber_xpath).send_keys(sinnumber)

    def Nationality(self):
        self.driver.find_element(By.XPATH, self.dropdown_nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.select_nationality_xpath).click()

    def MaritialStatus(self):
        self.driver.find_element(By.XPATH, self.dropdown_maritialstatus_xpath).click()
        self.driver.find_element(By.XPATH, self.select_single_xpath).click()

    def Dateofbirth(self, dob):
        self.driver.find_element(By.XPATH, self.datepic_DOB_xpath).send_keys(dob)

    def Gender(self):
        self.driver.find_element(By.XPATH, self.radiobtn_gender_xpath).click()

    def MilitaryService(self, militartservice):
        self.driver.find_element(By.XPATH, self.txtbox_militaryser_xpath).send_keys(militartservice)

    def PersonalDetailsSave(self):
        self.driver.find_element(By.XPATH, self.personaldetails_savebtn_xpath).click()

    def BloodType(self):
        self.driver.find_element(By.XPATH, self.dropdown_bloodtype_xpath).click()
        self.driver.find_element(By.XPATH, self.select_bloodtype_xpath).click()

    def CustomFieldSave(self):
        self.driver.find_element(By.XPATH, self.customfield_savebtn_xpath).click()

    def ValidateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_successfullysaved_xpath).is_displayed()
        except:
            return False