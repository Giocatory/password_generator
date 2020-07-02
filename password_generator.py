import random

num_for_close_loop = 1
while num_for_close_loop:

    number_for_length_password = int(input('Сколько символов нужно для вашего пароля?: '))
    print('Обычный пароль: ')


    def password_generator(count_char=8):
        char_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                      'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Q', 'W', 'E', 'R', 'T', 'Y',
                      'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
                      'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        password = []
        for char in range(count_char):
            password.append(random.choice(char_array))
        return "".join(password)


    print(password_generator(number_for_length_password))  # 10 chars password
    print("\nСложный пароль:")

    def strong_password_generator(count_char=8):
        char_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                      'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Q', 'W', 'E', 'R', 'T', 'Y',
                      'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
                      'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@',
                      '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ':', ';', '"', '?',
                      '<', '>', '?', '/']
        password = []
        for char in range(count_char):
            password.append(random.choice(char_array))
        return "".join(password)


    print(f"{strong_password_generator(number_for_length_password)}")  # 10 chars password
    choice = input('Продолжить? (y/n): ')

    if choice == "n":
        num_for_close_loop = 0
