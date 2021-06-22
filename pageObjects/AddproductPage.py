import time
from selenium.webdriver.support.ui import Select
from pageObjects.AddcustomerPage import AddCustomer

class AddProduct:
    # Add product Page
    lnkCatalog_menu_xpath = "//a[@href='#']//p[contains(text(),'Catalog')]"
    lnkProduct_menu_xpath = "//a[@href='/Admin/Product/List']//p[contains(text(),'Products')]"
    txtProductName_xpath = "//input[@id='Name']"
    txtShortDescription_xpath = "//textarea[@id='ShortDescription']"
    btnDeleteSelected_xpath = "//button[@id='delete-selected']"
    btnDeleteConfirmation_xpath = "//button[@id='delete-selected-action-confirmation-submit-button']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCatalogMenu(self):
        self.driver.find_element_by_xpath(self.lnkCatalog_menu_xpath).click()

    def clickOnProductMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkProduct_menu_xpath).click()

    def setProductName(self,pname):
        self.driver.find_element_by_xpath(self.txtProductName_xpath).send_keys(pname)

    def setShortDescription(self,shortDesc):
        self.driver.find_element_by_xpath(self.txtShortDescription_xpath).send_keys(shortDesc)

    def clickOnDeleteSelected(self):
        self.driver.find_element_by_xpath(self.btnDeleteSelected_xpath).click()

    def clickOnDeleteConfirmation(self):
        self.driver.find_element_by_xpath(self.btnDeleteConfirmation_xpath).click()