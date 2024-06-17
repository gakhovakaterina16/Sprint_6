import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage

@pytest.mark.usefixtures("setup_class")
class TestImportantQuestions:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.page = MainPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.feature("Important Questions")
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        (MainPage.first_important_question, MainPage.first_important_answer, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (MainPage.second_important_question, MainPage.second_important_answer, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (MainPage.third_important_question, MainPage.third_important_answer, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру."),
        (MainPage.fourth_important_question, MainPage.fourth_important_answer, "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (MainPage.fifth_important_question, MainPage.fifth_important_answer, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (MainPage.sixth_important_question, MainPage.sixth_important_answer, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (MainPage.seventh_important_question, MainPage.seventh_important_answer, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (MainPage.eighth_important_question, MainPage.eighth_important_answer, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    @allure.story("Check answers for important questions")
    @allure.severity(allure.severity_level.NORMAL)
    def test_important_questions(self, question_locator, answer_locator, expected_answer):
        with allure.step("Click on the question element"):
            question_element = self.driver.find_element(*question_locator)
            question_element.click()
        
        with allure.step("Retrieve and validate the answer"):
            answer_element = self.driver.find_element(*answer_locator)
            answer_text = answer_element.text
            allure.attach(answer_text, name="Answer Text", attachment_type=allure.attachment_type.TEXT)
        
        assert answer_text == expected_answer, f"Expected '{expected_answer}', but got '{answer_text}'"
