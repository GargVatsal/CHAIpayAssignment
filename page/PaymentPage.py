import pytest
from selenium.webdriver.common.by import By


class PaymentPage:

    payAmountLocator = (By.XPATH, "//input[@name='amount']")
    fullNameLocator = (By.XPATH, "//input[@name='fullName']")
    emailLocator = (By.XPATH, "//input[@name='email']")
    flagLocator = (By.XPATH, "//div[@class='selected-flag']")
    countryFlagLocator = (By.XPATH, "//ul//li[@data-country-code='in']")
    phCodeLocator = (By.CSS_SELECTOR, "input[placeholder='Phone Number']")
    phNoLocator = (By.CSS_SELECTOR, "input[placeholder='Phone Number']")
    payButtonLocator = (By.CSS_SELECTOR, "button.MuiButton-root")

    def __init__(self, log):
        self.log = log

    def amountField(self, driver):
        # Validating the amount present is Editable or not
        try:
            paymentPageAmount = driver.find_element(*PaymentPage.payAmountLocator)
            assert paymentPageAmount.get_attribute('disabled'), self.log.critical('Amount is editable on Payment Page')
            self.log.info('Payment Page Amount is not editable')
        except AssertionError or Exception as e:
            pytest.fail(e)

    def fullNameField(self, name, driver):
        try:
            driver.find_element(*PaymentPage.fullNameLocator).send_keys(name)
            self.log.info('Name Entered is - %s', name)
        except AssertionError or Exception as e:
            pytest.fail(e)

    def emailField(self, mail, driver):
        try:
            driver.find_element(*PaymentPage.emailLocator).send_keys(mail)
            self.log.info('Email Entered is - %s', mail)
        except AssertionError or Exception as e:
            pytest.fail(e)

    def phNumberField(self, number, driver):
        try:
            driver.find_element(*PaymentPage.flagLocator).click()
            self.log.info('Flag Button is clicked')
            driver.find_element(*PaymentPage.countryFlagLocator).click()
            self.log.info('Phone Country code dropdown is selected')
            # Validating if selected country code is proper or not
            phCode = driver.find_element(*PaymentPage.phCodeLocator).get_attribute('value')
            assert phCode == '+91', self.log.error('Phone country code is not +91 on Payment Page')
            self.log.info('%s code is selected', phCode)
            driver.find_element(*PaymentPage.phNoLocator).send_keys(number)
            self.log.info('Phone Number - %s is entered', number)
        except AssertionError or Exception as e:
            pytest.fail(e)

    def clickPayButton(self, driver):
        try:
            driver.find_element(*PaymentPage.payButtonLocator).click()
            self.log.info('Pay button is clicked on Payment page')
        except AssertionError or Exception as e:
            pytest.fail(e)
