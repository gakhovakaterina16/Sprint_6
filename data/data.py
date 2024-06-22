from selenium.webdriver.common.by import By

class FAQData:
    questions_answers = [
        {
            "question_locator": (By.XPATH, '//*[@id="accordion__heading-8"]/text()'),
            "answer_locator": (By.XPATH, '//*[@id="accordion__panel-8"]/p/text()'),
            "expected_answer": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        },
        {
            "question_locator": (By.XPATH, '//*[@id="accordion__heading-9"]/text()'),
            "answer_locator": (By.XPATH, '//*[@id="accordion__panel-9"]/p/text()'),
            "expected_answer": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        },
        {
            "question_locator": (By.XPATH, '//*[@id="accordion__heading-10"]/text()'),
            "answer_locator": (By.XPATH, '//*[@id="accordion__panel-10"]/p/text()'),
            "expected_answer": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру."
        },
        {
            "question_locator": (By.XPATH, '//*[@id="accordion__heading-11"]/text()'),
            "answer_locator": (By.XPATH, '//*[@id="accordion__panel-11"]/p/text()'),
            "expected_answer": "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        },
        {
            "question_locator": (By.XPATH, '//*[@id="accordion__heading-12"]/text()'),
            "answer_locator": (By.XPATH, '//*[@id="accordion__panel-12"]/p/text()'),
            "expected_answer": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        },
        {
            "question_locator": (By.XPATH, '//*[@id="accordion__heading-13"]/text()'),
            "answer_locator": (By.XPATH, '//*[@id="accordion__panel-13"]/p/text()'),
            "expected_answer": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        },
        {
            "question_locator": (By.XPATH, '//*[@id="accordion__heading-14"]/text()'),
            "answer_locator": (By.XPATH, '//*[@id="accordion__panel-14"]/p/text()'),
            "expected_answer": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        },
        {
            "question_locator": (By.XPATH, '//*[@id="accordion__heading-15"]/text()'),
            "answer_locator": (By.XPATH, '//*[@id="accordion__panel-15"]/p/text()'),
            "expected_answer": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        }
    ]

class RentalFlowData:
    # Наборы данных для теста test_order
    test_data_1 = {
        "name": "Иван",
        "surname": "Иванов",
        "address": "ул. Пушкина, д. Колотушкина",
        "metro_station": "Пушкинская",
        "phone_number": "+79123456789",
        "delivery_date": "15.07.2024",
        "rental_period": "3 дня",
        "color_checkbox": "чёрный жемчуг"
    }

    test_data_2 = {
        "name": "Мария",
        "surname": "Сидорова",
        "address": "ул. Лермонтова, д. Белгородская",
        "metro_station": "Лермонтовская",
        "phone_number": "+79234567890",
        "delivery_date": "20.07.2024",
        "rental_period": "5 дней",
        "color_checkbox": "серая безысходность"
    }    
    