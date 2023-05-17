import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("Getting all the Products Title")
        products = checkoutpage.getCardTitle()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            print(productName)
            log.info(productName)
            if productName == "Blackberry":
                checkoutpage.getCardFooter().click()

        checkoutpage.btnCheckOut().click()
        confirmpage = checkoutpage.checkOutItems()
        log.info("Entering country name Ind")
        self.driver.find_element(By.ID, "country").send_keys("Ind")
        self.verifyLinkPresence("India")
        # wait = WebDriverWait(self.driver, 15)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from app is " + successText)
        assert "Success! Thank you!" in successText


#  just note: py.test --browser_name firefox
