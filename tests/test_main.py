import pytest

from page.PaymentPage import PaymentPage
from page.CheckoutPage import CheckoutPage
from page.FinalPaymentPage import FinalPaymentPage
from utilities.baseClass import BaseClass


@pytest.mark.usefixtures('setup')
class Test:

    amount = 'SGD 100.00'
    log = BaseClass().log_method()
    paymentPage = PaymentPage(log)
    checkoutPage = CheckoutPage(log)
    finalPaymentPage = FinalPaymentPage(log)

# Payment page tests
    def test_paymentPageAmount(self):
        self.paymentPage.amountField(self.driver)

    def test_paymentPageFullName(self):
        self.paymentPage.fullNameField('VG', self.driver)

    def test_paymentPageEmail(self):
        self.paymentPage.emailField('test@mail.com', self.driver)

    def test_paymentPagePhone(self):
        self.paymentPage.phNumberField('1234567890', self.driver)

    def test_paymentPagePayBtn(self):
        self.paymentPage.clickPayButton(self.driver)

# checkout page tests
    def test_checkoutPageCheckPage(self):
        self.checkoutPage.checkUrl(self.driver)

    def test_checkoutPageCheckAmount(self):
        self.checkoutPage.checkAmount(self.driver, Test.amount)

    def test_checkoutPageSelectPayment(self):
        self.checkoutPage.selectPaymentOptions(self.driver)

    def test_checkoutPagePayNow(self):
        self.checkoutPage.payNow(self.driver, Test.amount)

# Payment page tests
    def test_finalPaymentPageCheckUrl(self):
        self.finalPaymentPage.checkUrl(self.driver)

    def test_finalPaymentPageCheckAmount(self):
        self.finalPaymentPage.checkAmount(self.driver, Test.amount)
