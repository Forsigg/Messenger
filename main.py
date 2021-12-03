from user import User

if __name__ == '__main__':

    user = User()

    command = input('Добро пожаловать!\nПожалуйста, введите команду: ').lower()
    if command == 'войти':
        user.log_in()
    elif command == 'зарегистрироваться':
        user.register()

