import os
import sys

users_data = {}

class Message:
    def __init__ (self, text, datetime, user):
        self.text = text
        self.time = datetime
        self.user = user

    def send(self):
        pass


class User():
    def __init__(self):
        self.is_log_in = False
        self.is_register()
        self.log_in()

    def wrapper(self):
        os.system('CLS')
        print ('----------')

    def log_in(self):
        self.wrapper()
        while self.is_log_in == False:
            print ("Пожалуйста, введите данные для идентификации пользователя.")
            temp_login = input('Логин: ')
            temp_pass = input('Пароль: ')

            if temp_login not in users_data:
                print('Такого пользователя не существует. Желаете зарегистрироваться?')
                if input().lower() == 'да':
                    return self.register()
                else:
                    sys.exit()
            if temp_pass != self.password:
                print("Неправильно введен пароль. Попробуйте снова")
            else:
                self.is_log_in = True
                return print(f"Приветствуем, {self.login}!")

    def is_register(self):
        print('Вы уже зарегистрированы? ')
        status = input()
        if status.lower() == 'да':
            self.log_in()
        else:
            self.register()

    def register(self):
        self.wrapper()
        print ('Для регистрации, пожалуйста, введите следующие данные: ')
        self.login = input('Логин: ')
        while True:
            temp_pass = input('Пароль: ')
            conf_temp_pass = input('Повторите пароль: ')
            if temp_pass != conf_temp_pass:
                print ('Пароли не совпадают. Попробуйте снова.')
            else:
                self.password = temp_pass
                break
        print (f'Привет, {self.login}!')
        users_data[self.login] = [self.password,]


if __name__ == '__main__':
    user_test = User()
    print (users_data)