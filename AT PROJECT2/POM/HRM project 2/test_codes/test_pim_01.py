from test_locators.LoginPage import Login
from test_locators.AdminPage import Admin
from utilities.readproperties import ReadConfig
from utilities import customlogger


class Test_Menu:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()
    excepted_result = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard',
                       'Directory', 'Maintenance', 'Buzz']

    def testcase_pim_01(self, setup):
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
        
        self.genealogizing.setusername("sachin")
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


        self.actual_result = self.adminpageobj.menu_element()
        if self.actual_result == self.excepted_result:
            assert True
        else:
            assert False
        self.logger.info("******** validated below menu tabs are presented in Admin page  ********")


        for item in self.excepted_result:
            self.adminpageobj.search_box(item.lower())
            if self.adminpageobj.result() == item:
                assert True
            else:
                assert False
            self.implicity_wait(5)
            self.adminpageobj.clear()
        self.logger.info("********* search bar lower case search all menu tabs displayed successfully  ********")

        for item in self.excepted_result:
            self.adminpageobj.search_box(item.upper())
            if self.adminpageobj.result() == item:
                assert True
            else:
                assert False
            self.implicity_wait(5)
            self.adminpageobj.clear()
        self.logger.info("********* search bar upper case search all menu tabs displayed successfully  ********")
        self.driver.close()
        self.logger.info("******** test_pim_01 will be completed successfully ********")
