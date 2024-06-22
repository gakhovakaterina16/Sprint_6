from selenium.webdriver.common.by import By

class OrderPage:
    # Локаторы полей ввода
    name_field = (By.CSS_SELECTOR, '.Order_Form__17u6u input[placeholder="* Имя"]')
    surname_field = (By.CSS_SELECTOR, '.Order_Form__17u6u input[placeholder="* Фамилия"]')
    address_field = (By.CSS_SELECTOR, '.Order_Form__17u6u input[placeholder="* Адрес: куда привезти заказ"]')
    station_field = (By.CSS_SELECTOR, '.Order_Form__17u6u input[placeholder="* Станция метро"]')
    phone_number_field = (By.CSS_SELECTOR, '.Order_Form__17u6u input[placeholder="* Телефон: на него позвонит курьер"]')
    
    # Локаторы кнопок и других элементов
    next_button = (By.CSS_SELECTOR, '.Order_Form__17u6u button')

    # Пример локатора для поля ввода даты, если он использует DatePicker
    date_field = (By.CSS_SELECTOR, '.Order_Form__17u6u input[type="date"]')

    # Локаторы полей ввода и элементов формы
    delivery_date_field = (By.CSS_SELECTOR, '.Order_MixedDatePicker__3qiay input[type="text"]')
    rental_period_dropdown = (By.CSS_SELECTOR, '.Dropdown-placeholder')
    color_black_checkbox = (By.XPATH, '//label[text()="чёрный жемчуг"]/input')
    color_grey_checkbox = (By.XPATH, '//label[text()="серая безысходность"]/input')
    courier_comment_field = (By.CSS_SELECTOR, '.Order_Form17u6u .Input_Input1iN_Z')
    
    # Локаторы кнопок
    back_button = (By.XPATH, '//button[text()="Назад"]')
    order_button = (By.XPATH, '//button[text()="Заказать"]')
    
    # Локатор для надписи "Заказ оформлен"
    order_confirmation_text = (By.CSS_SELECTOR, '.Order_ModalHeader__3FDaJ')

    # Конструктор класса
    def init(self, driver):
        self.driver = driver

    # Пример метода для взаимодействия с элементами на странице заказа
    def enter_name(self, name):
        name_input = self.driver.find_element(*self.name_field)
        name_input.send_keys(name)

    def enter_surname(self, surname):
        surname_input = self.driver.find_element(*self.surname_field)
        surname_input.send_keys(surname)

    def enter_address(self, address):
        address_input = self.driver.find_element(*self.address_field)
        address_input.send_keys(address)

    def enter_station(self, station):
        station_input = self.driver.find_element(*self.station_field)
        station_input.send_keys(station)

    def enter_phone_number(self, phone_number):
        phone_number_input = self.driver.find_element(*self.phone_number_field)
        phone_number_input.send_keys(phone_number)

    def click_next_button(self):
        next_button = self.driver.find_element(*self.next_button)
        next_button.click()

    def click_back_button(self):
        back_button = self.driver.find_element(*self.back_button)
        back_button.click()

    def click_order_button(self):
        order_button = self.driver.find_element(*self.order_button)
        order_button.click()

    def get_order_confirmation_text(self):
        order_confirmation = self.driver.find_element(*self.order_confirmation_text)
        return order_confirmation.text
    