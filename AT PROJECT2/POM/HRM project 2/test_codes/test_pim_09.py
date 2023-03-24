from test_locators.LoginPage import Login
from test_locators.AdddNewEmployeePage import AddNewEmployee
from test_locators.EmployeelistPage import Employeelist
from test_locators.JobPage import Job
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_Add_Job:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def testcase_pim_09(self, setup):
        self.logger.info("******** Test_Add_Job is Started *********")
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

        self.jobpageobj = Job(self.driver)
        self.jobpageobj.GotoJob()
        self.logger.info("******** going to Job tab ********")
        self.jobpageobj.Joindate("2020-02-08")
        self.jobpageobj.JobTitle()
        self.jobpageobj.JobCategory()
        self.jobpageobj.SubUnit()
        self.jobpageobj.Location()
        self.jobpageobj.EmployeeStatus()

        self.jobpageobj.Contract()
        self.logger.info("******** click contract toggle ********")
        self.jobpageobj.ContractStart("2020-02-08")
        self.jobpageobj.ContractEnd("2022-02-07")
        self.jobpageobj.savecontract()
        self.logger.info("******** fill all the details in job and click save ********")

        self.validateSuccess = self.jobpageobj.ValidateConformation()
        if self.validateSuccess == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False
        self.logger.info("******** Validated filled details are presented *********")

        self.logger.info("******** test_pim_09 will be completed successfully ********")
