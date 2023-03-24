from test_locators.LoginPage import Login
from test_locators.AdddNewEmployeePage import AddNewEmployee
from test_locators.EmployeelistPage import Employeelist
from test_locators.Personaldetails import personaldetails
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_Add_personaldetails:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def testcase_pim_05(self, setup):
        self.logger.info("******** Test_Add_personaldetails is Started *********")
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

        self.personaldetailsobj = personaldetails(self.driver)
        self.personaldetailsobj.AddNickname("sachin")
        self.personaldetailsobj.AddOtherid("14310")
        self.personaldetailsobj.AddDrivingLicense("TN8344422936094")
        self.personaldetailsobj.LicenseExpdate("2030-04-24")
        self.personaldetailsobj.Addssnnumber("23456")
        self.personaldetailsobj.Addsinnumber("98765")
        self.personaldetailsobj.Nationality()
        self.personaldetailsobj.MaritialStatus()
        self.personaldetailsobj.Dateofbirth("2000-07-14")
        self.personaldetailsobj.Gender()
        self.personaldetailsobj.MilitaryService("No")
        self.personaldetailsobj.PersonalDetailsSave()
        self.personaldetailsobj.BloodType()
        self.personaldetailsobj.CustomFieldSave()
        self.logger.info("******** All Details are filled successfully in personal details ********")

        self.validateSuccess = self.personaldetailsobj.ValidateConformation()

        if self.validateSuccess == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False
        self.logger.info("******** Validated filled details are presented *********")

        self.logger.info("******** test_pim_05 will be completed successfully ********")
