from test_locators.LoginPage import Login
from test_locators.AdddNewEmployeePage import AddNewEmployee
from test_locators.EmployeelistPage import Employeelist
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_Validate_Employeelistpage:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()
    expected_result = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration', 'Job',
                       'Salary', 'Tax Exemptions', 'Report-to', 'Qualifications', 'Memberships']

    def testcase_pim_04(self, setup):
        self.logger.info("******** Test_Validate_Employeelistpage is Started *********")
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
        self.employeelistobj.Clicksearch()
        self.logger.info("******** Click Search button ********")
        self.employeelistobj.Clickeditbutton()
        self.logger.info("******** Click edit button ********")


        self.actual_result = self.employeelistobj.tab_element()
        if self.actual_result == self.expected_result:
            assert True
        else:
            assert False
        self.logger.info("******** the tabs are presented in tha employee list page ********")
        self.driver.close()
        self.logger.info("******** test_pim_04 will be completed successfully ********")

