from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    btnCheck = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    # btnCheck = (By.XPATH, "//a[@class ='nav-link btn btn-primary']")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def btnCheckOut(self):
        return self.driver.find_element(*CheckoutPage.btnCheck)

    def checkOutItems(self):
        # self.driver.find_element(*CheckoutPage.checkout).click()
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
