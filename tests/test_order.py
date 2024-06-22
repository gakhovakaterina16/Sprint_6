import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import RentalFlowData

@pytest.mark.usefixtures("setup_class")
class TestRentalFlow:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.main_page = MainPage(cls.driver)
        cls.order_page = OrderPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.feature("Rental Flow")
    @pytest.mark.parametrize("data", [RentalFlowData.test_data_1, RentalFlowData.test_data_2])
    @allure.story("Positive Scenario")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_rental_flow(self, data):
        with allure.step("Click on the order button on the main page"):
            self.main_page.click_order_button()

        with allure.step("Fill in the order form"):
            self.order_page.fill_order_form(data)

        with allure.step("Submit the order"):
            self.order_page.submit_order()

        with allure.step("Verify order confirmation"):
            assert self.order_page.is_order_confirmation_displayed(), "Order confirmation modal not displayed"

        with allure.step("Navigate back to main page"):
            self.order_page.navigate_to_main_page()

        with allure.step("Verify redirection to main page"):
            assert self.main_page.is_logo_visible(), "Logo not visible, failed to navigate to main page"