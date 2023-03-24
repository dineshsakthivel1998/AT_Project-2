from test_locators.LoginPage import Login
from test_locators.AdddNewEmployeePage import AddNewEmployee
from test_locators.EmployeelistPage import Employeelist
from test_locators.TaxExemptionpage import TaxExemptions
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_Tax_Exemptions:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def testcase_pim_13(self, setup):
        self.logger.info("******** Test_Tax Exemptions is Started *********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.loginpageobj = Login(self.driver)
        
        self.loginpageobj.setusername(self.username)
        self.loginpageobj.setpassword("invalid password")
        self.loginpageobj.clickloginbutton()
        self.logger.info("******** Enter wrong password to login ******** ")
        self.implicity_wait(5)
        
        self.loginpageobj.setusername("sachin")
        self.loginpageobj.setpassword(self.password)
        self.loginpageobj.clickloginbutton()
        self.logger.info("******** Enter Wrong Username Login ********")
        self.implicity_wait(5)
        
        self.loginpageobj.setusername("826hse")
        self.loginpageobj.setpassword("nu230oej")
        self.loginpageobj.clickloginbutton()
        self.logger.info("******** Enter Wrong Username and password login ********")
        self.implicity_wait(5)

        self.loginpageobj.setusername(self.username)
        self.loginpageobj.setpassword(self.password)
        self.loginpageobj.clickloginbutton()
        self.logger.info("******** Login Successfully *********")

        self.AddEmployeepage = AddNewEmployee(self.driver)
        self.AddEmployeepage.GoTOPIM()
        self.logger.info("******** Go to pimpage *********")

        self.employeelistobj = Employeelist(self.driver)
        self.employeelistobj.EnterEmployeeName("Ramesh kumar")
        self.logger.info("******** Enter Employee Name ********")
        self.employeelistobj.Currentandpastemployees()
        self.logger.info("******** Click current and past employees ********")
        self.employeelistobj.Clicksearch()
        self.logger.info("******** Click Search button ********")
        self.employeelistobj.Clickeditbutton()
        self.logger.info("******** Click edit button ********")

        self.taxexemptionobj = TaxExemptions(self.driver)
        self.taxexemptionobj.GotoTaxExemptions()
        self.implicity_wait(5)
        self.logger.info("******** going to tax exemption tab  ********")
        self.taxexemptionobj.FITstatus()
        self.taxexemptionobj.FITexemptions("10")
        self.taxexemptionobj.State()
        self.taxexemptionobj.SITstatus()
        self.taxexemptionobj.SITexemption("10")
        self.taxexemptionobj.UnEmploymentState()
        self.taxexemptionobj.WorkState()
        self.taxexemptionobj.ClickSave()
        self.logger.info("******** fill all details in tax exemptions tab and click save  ********")

        self.validateSuccess = self.taxexemptionobj.ValidateConformation()
        if self.validateSuccess == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False
        self.logger.info("******** Validated filled details are presented *********")


        self.logger.info("******** test_pim_13 will be completed successfully ********")
