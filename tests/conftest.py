import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope='class')
def setup(request):
    service_obj = Service('C:\\Users\\HP\\Documents\\python\\selenium_automation\\edgeWebDriver\\msedgedriver.exe')
    driver = webdriver.Edge(service=service_obj)
    driver.get('https://www.stage-page.chaiport.io/2AZX3ENuQMlYlNBlXfr7dcI5ngS')
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()









