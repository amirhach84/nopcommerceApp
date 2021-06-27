import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.SearchProductPage import SearchProduct
from pageObjects.AddproductPage import AddProduct
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchProductByProductName_007:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_searchProductByProductName(self,setup):
        self.logger.info("************* Test_SearchProductByProductName_007 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Open the Products screen **********")

        self.addprod = AddProduct(self.driver)
        self.addprod.clickOnCatalogMenu()
        self.addprod.clickOnProductMenuItem()

        self.logger.info("******* Starting Search Product By Product Name **********")

        searchprod = SearchProduct(self.driver)
        searchprod.setSearchProductName("Apple MacBook Pro 13-inch")
        searchprod.clickSearchProd()
        time.sleep(5)
        status = searchprod.searchByProductName("Apple MacBook Pro 13-inch")
        assert True == status

        self.logger.info("******* Starting Edit Product **********")

        # Change the name of the product
        searchprod.clickEditProd()
        time.sleep(3)
        #searchprod.clickExpandProdInf()
        time.sleep(3)
        self.addprod.clearProductName()
        self.addprod.setProductName("New Version Of Apple MacBook Pro 13-inch")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnSave()
        time.sleep(3)
        searchprod.setSearchProductName("New Version Of Apple MacBook Pro 13-inch")
        searchprod.clickSearchProd()
        time.sleep(5)
        status = searchprod.searchByProductName("New Version Of Apple MacBook Pro 13-inch")
        assert True == status

        # Change the product name again back to the original name
        searchprod.clickEditProd()
        #searchprod.clickExpandProdInf()
        time.sleep(3)
        self.addprod.clearProductName()
        self.addprod.setProductName("Apple MacBook Pro 13-inch")
        time.sleep(3)
        self.addcust.clickOnSave()
        searchprod.clickSearchProd()
        time.sleep(5)
        status = searchprod.searchByProductName("Apple MacBook Pro 13-inch")
        assert True == status

        self.driver.close()
        self.logger.info("***************  TC_SearchProductByProductName_007 Finished  *********** ")