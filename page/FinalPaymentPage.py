import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class FinalPaymentPage:

    amountLocator = (By.XPATH, "//h3[@id='amount-elem']")
    pageHeadingLocator = (By.XPATH, "//span[@id='heading-text']")

    def __init__(self, log):
        self.log = log

    def checkUrl(self, driver):
        try:
            # Validating the final payment page
            wait = WebDriverWait(driver, 5)
            wait.until(expected_conditions.visibility_of_element_located(FinalPaymentPage.pageHeadingLocator))
            pageHeading = driver.find_element(*FinalPaymentPage.pageHeadingLocator).text
            assert pageHeading == 'Pay with QR code via', self.log.error('Unable to Load FinalPayment page')
            self.log.info('Final Payment Page is Loaded')

        except AssertionError or Exception as e:
            pytest.fail(e)

    def checkAmount(self, driver, amount):
        try:
            # Validating the amount on final payment Page
            finalPageAmount = driver.find_element(*FinalPaymentPage.amountLocator).text
            if '\xa0' in finalPageAmount:
                finalPageAmount = finalPageAmount.replace('\xa0', ' ')
            assert finalPageAmount == amount,  self.log.error('Amount Value is not SGD 100.00 on Final page')
            self.log.info('Final page amount is - %s', finalPageAmount)

        except AssertionError or Exception as e:
            pytest.fail(e)
