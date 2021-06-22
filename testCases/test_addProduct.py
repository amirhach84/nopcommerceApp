import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.AddproductPage import AddProduct
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_AddProduct:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_addProduct(self, setup):
        self.logger.info("************* Test_004_Addproduct **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Product Test **********")

        self.addprod = AddProduct(self.driver)
        self.addprod.clickOnCatalogMenu()
        self.addprod.clickOnProductMenuItem()

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing product info **********")

        self.addprod.setProductName("New Product")
        self.addprod.setShortDescription("This is a new product")

        self.addcust.clickOnSave()

        self.msg = self.driver.find_element_by_xpath("//div[contains(@class,'alert-success')]")

        if self.msg is not None:
            assert True
            self.logger.info("********* Add product Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addProduct_scr.png")  # Screenshot
            self.logger.error("********* Add product Test Failed ************")
            assert False

        self.addprod.clickOnDeleteSelected()
        self.addprod.clickOnDeleteConfirmation()

        self.driver.close()
        self.logger.info("******* Ending Add product test **********")