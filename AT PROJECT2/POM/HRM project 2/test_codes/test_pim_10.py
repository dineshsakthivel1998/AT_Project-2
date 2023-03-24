from test_locators.LoginPage import Login
from test_locators.AdddNewEmployeePage import AddNewEmployee
from test_locators.EmployeelistPage import Employeelist
from test_locators.JobPage import Job
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_Employee_Terminate:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def testcase_pim_10(self, setup):
        self.logger.info("******** Test_Employee_terminate is Started *********")
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

        self.jobpageobj = Job(self.driver)
        self.jobpageobj.GotoJob()
        self.logger.info("******** going to job tab ********")
        self.jobpageobj.TerminateEmployee()
        self.logger.info("******** click terminate employement ********")
        self.jobpageobj.TerminateDate("2022-10-10")
        self.jobpageobj.TerminateReason()
        self.jobpageobj.SaveTerminate()
        self.implicity_wait(5)
        self.logger.info("******** fill the date and reason and click save ********")

        self.showdate = self.jobpageobj.Date()
        if self.showdate == True:
            assert True

        else:
            assert False
        self.logger.info("******** validate the terminate date will be displayed in page  ********")

        self.showActive = self.jobpageobj.ActivateEmployment()
        if self.showActive == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False
        self.logger.info("******** validate Active employement is displayed ********")

        self.logger.info("******** test_pim_10 will be completed successfully ********")
