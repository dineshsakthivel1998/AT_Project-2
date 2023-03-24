from test_locators.LoginPage import Login
from test_locators.AdddNewEmployeePage import AddNewEmployee
from test_locators.EmployeelistPage import Employeelist
from test_locators.Emergencycontact import EmergencyContact
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_Add_EmergencyContact:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def testcase_pim_07(self, setup):
        self.logger.info("******** Test_Add_EmergencyContacts is Started *********")
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

        self.emergencyobj = EmergencyContact(self.driver)
        self.emergencyobj.ClickEmergencyContacts()
        self.logger.info("******** going to emergency contacts tab ********")
        self.emergencyobj.ClickADD()
        self.emergencyobj.Name("virat")
        self.emergencyobj.Relationship("brother")
        self.emergencyobj.HomeTelephone("8765432234")
        self.emergencyobj.Mobile("8654345677")
        self.emergencyobj.WorkTelephone("2345676665450")
        self.emergencyobj.ClickSave()
        self.logger.info("******** Fill all details and click save ********")

        self.validateSuccess = self.emergencyobj.ValidateConformation()
        if self.validateSuccess == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False
        self.logger.info("******** Validated filled details are presented *********")

        self.logger.info("******** test_pim_07 will be completed successfully ********")
