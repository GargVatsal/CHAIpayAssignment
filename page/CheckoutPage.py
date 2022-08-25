import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CheckoutPage:

    payTitleLocator = (By.XPATH, "//h4[@id='forpaypalandsavedcards']")
    amountLocator = (By.XPATH, "//span[@class='totalAmountCount']")
    payOptionLocator = (By.XPATH, "//a[@Id='walletlang']")
    payOptionBtnLocator = (By.XPATH, "//input[@id='OMISE-OMISE_PAYNOW']")
    payNowBtnLocator = (By.XPATH, "//button[@id='PayNowButtonWeb']")

    def __init__(self, log):
        self.log = log

    def checkUrl(self, driver):
        try:
            # Validating the checkout page has opened or not
            wait = WebDriverWait(driver, 2)
            wait.until(expected_conditions.visibility_of_element_located(CheckoutPage.payTitleLocator))
            payTitle = driver.find_element(*CheckoutPage.payTitleLocator).text
            assert payTitle == 'Payment Options', 'Unable to Load Checkout page'

        except AssertionError or Exception as e:
            pytest.fail(e)

    def checkAmount(self, driver, amount):
        try:
            # Validating the amount on checkout page
            checkoutPageAmount = driver.find_element(*CheckoutPage.amountLocator).text
            if '\xa0' in checkoutPageAmount:
                checkoutPageAmount = checkoutPageAmount.replace('\xa0', ' ')
            assert checkoutPageAmount == amount, self.log.error('Amount Value is not SGD 100.00 on checkout page')
            self.log.info('Checkout page amount is - %s', checkoutPageAmount)

        except AssertionError or Exception as e:
            pytest.fail(e)

    def selectPaymentOptions(self, driver):
        try:
            payOption = driver.find_element(*CheckoutPage.payOptionLocator)
            payOption.click()
            self.log.info('%s payment option is expanded', payOption.text)
            driver.find_element(*CheckoutPage.payOptionBtnLocator).click()
            self.log.info('%s radio button is selected', payOption.text)


        except AssertionError or Exception as e:
            pytest.fail(e)

    def payNow(self, driver, amount):
        try:
            payButton = driver.find_element(*CheckoutPage.payNowBtnLocator)
            if '\xa0' in payButton.text:
                payButton = payButton.text.replace('\xa0', ' ')
            assert amount in payButton.text, self.log.error('Amount Value is not 100.00 for paynow button on checkout '
                                                            'page')
            self.log.info('Amount in payButton is - %s', amount)
            payButton.click()
            self.log.info('Paybutton is clicked')

        except AssertionError or Exception as e:
            pytest.fail(e)
