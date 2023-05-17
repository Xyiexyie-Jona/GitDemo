import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Firstname is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getStatus().click()

        homepage.getSubmit().click()
        message = homepage.getSucessMessage().text

        print(getData["firstname"], message)
        print(getData["firstname"], message)
        #adshajsd
        #ahdsakd
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param

