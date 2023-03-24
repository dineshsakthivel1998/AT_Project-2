from test_locators.LoginPage import Login
from test_locators.AdddNewEmployeePage import AddNewEmployee
from test_locators.EmployeelistPage import Employeelist
from test_locators.SalaryPage import Salary
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_Salary:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def testcase_pim_12(self, setup):
        self.logger.info("******** Test_Salary is Started *********")
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

        self.salarypageobj = Salary(self.driver)
        self.salarypageobj.GotoSalary()
        self.logger.info("******** going to Salary tab ********")
        self.salarypageobj.ClickAdd()
        self.salarypageobj.SalaryComponent("fixed component")
        self.salarypageobj.PayGrade()
        self.salarypageobj.PayFrequency()
        self.salarypageobj.Currency()
        self.salarypageobj.Amount("45000")
        self.salarypageobj.Comments("salary is good")
        self.implicity_wait(5)
        self.salarypageobj.DirectDeposit()
        self.visible = self.salarypageobj.Visiblefields()
        if self.visible == True:
            assert True

        else:
            assert False

        self.logger.info("******** click Direct deposit toggle ********")
        self.salarypageobj.AccountNumber("123456789000")
        self.salarypageobj.AccountType()
        self.salarypageobj.RoutingNumber("56432")
        self.salarypageobj.DepositAmount("30000")
        self.salarypageobj.ClickSave()
        self.logger.info("******** fill all details in salary tab and click save  ********")

        self.validateSuccess = self.salarypageobj.ValidateConformation()
        if self.validateSuccess == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False
        self.logger.info("******** Validated filled details are presented *********")

        self.logger.info("******** test_pim_12 will be completed successfully ********")
