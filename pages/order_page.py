from selenium.webdriver.common.by import By

class OrderPage:
    # локатор поля для ввода имени
    name_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/input']
    # локатор поля для ввода фамилии
    surname_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/input']
    # локатор поля для ввода адреса
    address_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/input']   
    # локатор поля для ввода станции метро
    station_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/input']
    # локатор поля для ввода телефонного номера
    phone_number_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[5]/input']
    # локатор кнопки далее
    then_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button']
    # локатор поля для ввода даты
    date_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/input']                                        
    


    # конструктор класса
    def __init__(self, driver):
        self.driver = driver
