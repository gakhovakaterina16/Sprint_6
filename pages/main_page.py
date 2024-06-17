from selenium.webdriver.common.by import By

class MainPage:
    # локатор поля "Сколько это стоит? И как оплатить?"
    first_important_question = [By.XPATH, '//*[@id="accordion__heading-8"]/text()']    
    # локатор поля "Хочу сразу несколько самокатов! Так можно?"
    second_important_question = [By.XPATH, '//*[@id="accordion__heading-9"]/text()']
    # локатор поля "Как рассчитывается время аренды?"
    third_important_question = [By.XPATH, '//*[@id="accordion__heading-10"]/text()']    
    # локатор поля "Можно ли заказать самокат прямо на сегодня?"
    fourth_important_question = [By.XPATH, '//*[@id="accordion__heading-11"]/text()']    
    # локатор поля "Можно ли продлить заказ или вернуть самокат раньше?"
    fifth_important_question = [By.XPATH, '//*[@id="accordion__heading-12"]/text()']  
    # локатор поля "Вы привозите зарядку вместе с самокатом?"
    sixth_important_question = [By.XPATH, '//*[@id="accordion__heading-13"]/text()'] 
    # локатор поля "Можно ли отменить заказ?"
    seventh_important_question = [By.XPATH, '//*[@id="accordion__heading-14"]/text()']  
    # локатор поля "Я жизу за МКАДом, привезёте?"
    eighth_important_question = [By.XPATH, '//*[@id="accordion__heading-15"]/text()'] 

    # локатор поля ответа на первый вопрос
    first_important_answer = [By.XPATH, '//*[@id="accordion__panel-8"]/p/text()']
    # локатор поля ответа на второй вопрос
    second_important_answer = [By.XPATH, '//*[@id="accordion__panel-9"]/p/text()']
    # локатор поля ответа на третий вопрос
    third_important_answer = [By.XPATH, '//*[@id="accordion__panel-10"]/p/text()']
    # локатор поля ответа на четвёртый вопрос
    fourth_important_answer = [By.XPATH, '//*[@id="accordion__panel-11"]/p/text()']
    # локатор поля ответа на пятый вопрос
    fifth_important_answer = [By.XPATH, '//*[@id="accordion__panel-12"]/p/text()']
    # локатор поля ответа на шестой вопрос
    sixth_important_answer = [By.XPATH, '//*[@id="accordion__panel-13"]/p/text()']
    # локатор поля ответа на седьмой вопрос
    seventh_important_answer = [By.XPATH, '//*[@id="accordion__panel-14"]/p/text()'] 
    # локатор поля ответа на восьмой вопрос
    eighth_important_answer = [By.XPATH, '//*[@id="accordion__panel-15"]/p/text()'] 

    # локатор первой кнопки "Заказать"
    order_first_button = [By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/button[1]']
    # локатор второй кнопки "Заказать"
    order_second_button = [By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div[2]/div[5]/button']         


    # конструктор класса
    def __init__(self, driver):
        self.driver = driver
