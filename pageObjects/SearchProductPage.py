class SearchProduct():
    # Search product Page
    btnSearchProd_id = "search-products"

    txtSearchProductName_xpath = "//input[@id='SearchProductName']"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='products-grid']"
    tableRows_xpath = "//table[@id='products-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='products-grid']//tbody/tr/td"

    btnEdit_xpath = "//a[contains(text(),'Edit')]"
    btnExpandProdInf_xpath = "//div[@id='product-info']//i[contains(@class,'fa-plus')]"

    def __init__(self, driver):
        self.driver = driver

    def setSearchProductName(self,pname):
        self.driver.find_element_by_xpath(self.txtSearchProductName_xpath).send_keys(pname)

    def clickSearchProd(self):
        self.driver.find_element_by_id(self.btnSearchProd_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchByProductName(self,pname):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
          table = self.driver.find_element_by_xpath(self.table_xpath)
          pname_table = table.find_element_by_xpath("//table[@id='products-grid']/tbody/tr["+str(r)+"]/td[3]").text
          if pname_table == pname:
              flag = True
              break
        return flag

    def clickEditProd(self):
        self.driver.find_element_by_xpath(self.btnEdit_xpath).click()

    def clickExpandProdInf(self):
        self.driver.find_element_by_xpath(self.btnExpandProdInf_xpath).click()