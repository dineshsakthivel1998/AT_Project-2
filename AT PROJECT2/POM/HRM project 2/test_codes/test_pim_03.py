from test_locators.LoginPage import Login
from test_locators.AdddNewEmployeePage import AddNewEmployee
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_AddNewEmployee:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()
    excepted_result = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard',
                       'Directory', 'Maintenance', 'Buzz']
    def testcase_pim_03(self, setup):
        self.logger.info("******** Test_AddNewEmployee is Started *********")
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

        self.AddEmployeepageobj = AddNewEmployee(self.driver)
        self.AddEmployeepageobj.GoTOPIM()
        self.logger.info("******** Go to pimpage *********")

        self.actual_result = self.AddEmployeepageobj.menu_element()
        if self.actual_result == self.excepted_result:
            assert True
        else:
            assert False
        self.logger.info("******** validated below menu tabs are presented in Admin page  ********")

        self.AddEmployeepageobj.ClickAdd()
        self.AddEmployeepageobj.FirstName("Ramesh")
        self.AddEmployeepageobj.LastName("kumar")
        self.AddEmployeepageobj.CreateLogin()
        self.AddEmployeepageobj.Username("ueyed qiwhb")
        self.AddEmployeepageobj.Enabled()
        self.AddEmployeepageobj.Password("Qwerty@123")
        self.AddEmployeepageobj.Confirmpassword("Qwerty@123")
        self.AddEmployeepageobj.ClickSave()
        self.implicity_wait(10)
        self.logger.info("******** Add new employee successfully *********")

        self.validateemployee = self.AddEmployeepageobj.ValidateEmployeeList()
        if self.validateemployee == True:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

        self.logger.info("******** validated the employeelist page will displayed *********")

        self.logger.info("********* test_case_03 will be completed successfully ********")
