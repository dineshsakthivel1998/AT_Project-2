from test_locators.LoginPage import Login
from test_locators.AdminPage import Admin
from utilities.readproperties import ReadConfig
from utilities import customlogger


class Test_Admin:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()
    excepted_result = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard',
                       'Directory', 'Maintenance', 'Buzz']

    def testcase_pim_02(self, setup):
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

        self.adminpageobj = Admin(self.driver)
        self.adminpageobj.GoToAdmin()
        self.implicity_wait(5)
        self.logger.info("******** Go to Admin page ********")

        # self.actual_result = self.adminpageobj.menu_element()
        # if self.actual_result == self.excepted_result:
        #     assert True
        # else:
        #     assert False
        # self.logger.info("******** validated below menu tabs  is displayed in Admin page ********")

        self.adminpageobj.ClickUserManagement()
        self.adminpageobj.ClickUsers()
        self.logger.info("******** click Users successfully ********")

        self.Admin =self.adminpageobj.ValidateDropdownAdmin()
        if self.Admin == True:
            assert True
        else:
            assert False
        self.logger.info("******** Validated Admin will displayed under userrole dropdown ********")

        self.ESS =self.adminpageobj.ValidateDropdownESS()
        if self.ESS == True:
            assert True
        else:
            assert False
        self.logger.info("******** Validated ESS will displayed under userrole dropdown ********")

        self.Enabled =self.adminpageobj.ValidateEnabled()
        if self.Enabled == True:
            assert True
        else:
            assert False
        self.logger.info("******** Validated Enabled will displayed under status dropdown ********")

        self.Disabled =self.adminpageobj.ValidateDisabled()
        if self.Disabled == True:
            assert True
        else:
            assert False
        self.logger.info("******** Validated Disabled will displayed under status dropdown ********")
        self.driver.close()
        self.logger.info("******** test_pim_02 will be completed successfully ********")
