from test_locators.LoginPage import Login
from test_locators.AdddNewEmployeePage import AddNewEmployee
from test_locators.EmployeelistPage import Employeelist
from test_locators.Contactdetails import ContactDetails
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_Add_Contactdetails:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def testcase_pim_06(self, setup):
        self.logger.info("******** Test_Add_Contact_details is Started *********")
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

        self.contactdetailsobj = ContactDetails(self.driver)
        self.contactdetailsobj.GotoContactDetails()
        self.implicity_wait(5)
        self.contactdetailsobj.Street1("24,NavaIndia")
        self.contactdetailsobj.Street2("peelamedu")
        self.contactdetailsobj.City("Coimbatore")
        self.contactdetailsobj.State("TamilNadu")
        self.contactdetailsobj.Zipcode("641028")
        self.contactdetailsobj.Country()
        self.logger.info("******** Address Details filled successfully ********")
        self.contactdetailsobj.Home("042-345678")
        self.contactdetailsobj.Mobile("9876543210")
        self.contactdetailsobj.Work("0123456789")
        self.logger.info("******** Telephone details filled successfully ********")
        self.contactdetailsobj.WorkEmail("eyrt1234@osohrm.com")
        self.contactdetailsobj.OtherEmail("euehn09876@gmail.com")
        self.implicity_wait(5)
        self.contactdetailsobj.ClickSave()
        self.logger.info("******** Email details filled successfully ********")
        self.implicity_wait(5)
        self.validateSuccess = self.contactdetailsobj.ValidateConformation()

        if self.validateSuccess == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False
        self.logger.info("******** Validated filled details are presented *********")

        self.logger.info("******** test_pim_06 will be completed successfully ********")

