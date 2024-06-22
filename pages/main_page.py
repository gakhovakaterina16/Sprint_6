from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    first_important_question = (By.XPATH, '//*[@id="accordion__heading-8"]/text()')
    second_important_question = (By.XPATH, '//*[@id="accordion__heading-9"]/text()')
    third_important_question = (By.XPATH, '//*[@id="accordion__heading-10"]/text()')
    fourth_important_question = (By.XPATH, '//*[@id="accordion__heading-11"]/text()')
    fifth_important_question = (By.XPATH, '//*[@id="accordion__heading-12"]/text()')
    sixth_important_question = (By.XPATH, '//*[@id="accordion__heading-13"]/text()')
    seventh_important_question = (By.XPATH, '//*[@id="accordion__heading-14"]/text()')
    eighth_important_question = (By.XPATH, '//*[@id="accordion__heading-15"]/text()')

    first_important_answer = (By.XPATH, '//*[@id="accordion__panel-8"]/p/text()')
    second_important_answer = (By.XPATH, '//*[@id="accordion__panel-9"]/p/text()')
    third_important_answer = (By.XPATH, '//*[@id="accordion__panel-10"]/p/text()')
    fourth_important_answer = (By.XPATH, '//*[@id="accordion__panel-11"]/p/text()')
    fifth_important_answer = (By.XPATH, '//*[@id="accordion__panel-12"]/p/text()')
    sixth_important_answer = (By.XPATH, '//*[@id="accordion__panel-13"]/p/text()')
    seventh_important_answer = (By.XPATH, '//*[@id="accordion__panel-14"]/p/text()')
    eighth_important_answer = (By.XPATH, '//*[@id="accordion__panel-15"]/p/text()')

    order_first_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/button[1]')
    order_second_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div[2]/div[5]/button')

    def init(self, driver):
        super().init(driver)

    def click_first_order_button(self):
        self.click(self.order_first_button)

    def click_second_order_button(self):
        self.click(self.order_second_button)

    def click_question(self, question_locator):
        self.click(question_locator)

    def get_answer_text(self, answer_locator):
        element = self.find_element(answer_locator)
        return element.text

    def click_and_get_answer(self, question_locator, answer_locator):
        self.click_question(question_locator)
        return self.get_answer_text(answer_locator)
