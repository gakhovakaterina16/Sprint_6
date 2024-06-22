import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from data.data import FAQData

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
    @pytest.mark.parametrize("data", FAQData.questions_answers)
    @allure.story("Check answers for important questions")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify that the answer for each important question is correct")
    def test_important_questions(self, data):
        question_locator = data["question_locator"]
        answer_locator = data["answer_locator"]
        expected_answer = data["expected_answer"]

        with allure.step("Click on the question element"):
            self.page.click_question(question_locator)
        
        with allure.step("Retrieve and validate the answer"):
            answer_text = self.page.get_answer_text(answer_locator)
            allure.attach(answer_text, name="Answer Text", attachment_type=allure.attachment_type.TEXT)
        
        assert answer_text == expected_answer, f"Expected '{expected_answer}', but got '{answer_text}'"
