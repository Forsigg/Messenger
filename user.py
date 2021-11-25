import os
import sys
from data.datausersmanager import USERS_DATA


class User():
    def __init__(self):
        self.is_log_in = False
        self.is_register()

    def wrapper(self):
        os.system('CLS')
        print ('----------')

    def log_in(self):
        self.wrapper()
        while self.is_log_in == False:
            print ("Пожалуйста, введите данные для идентификации пользователя.")
            temp_login = input('Логин: ')
            temp_pass = input('Пароль: ')

            if USERS_DATA.user_in_base(temp_login) == False:
                print('Такого пользователя не существует. Желаете зарегистрироваться?')
                if input().lower() == 'да':
                    return self.register()
                else:
                    sys.exit()
            if USERS_DATA.is_right_password(temp_login, temp_pass) == False:
                print("Неправильно введен пароль. Попробуйте снова")
            else:
                self.is_log_in = True
                return print(f"Приветствуем, {temp_login.title()}!")

    def is_register(self):
        print('Вы уже зарегистрированы? ')
        command = input()
        if command.lower() == 'да':
            self.log_in()
        elif command.lower() == 'нет':
            self.register()
        else:
            sys.exit()

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
                break
        print (f'Привет, {self.login.title()}!')
        USERS_DATA.add_one(self.login, temp_pass)

if __name__ == '__main__':
    user_test = User()

