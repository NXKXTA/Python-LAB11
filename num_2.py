def string_reverse(stroka):
    final_str = ""
    steck = list()
    for char in stroka:
        steck.append(char)
    for element in range(len(stroka)):
        final_str += steck.pop()
    return final_str


user_inp = input("Введите строку: ")
reverse_stroka = string_reverse(user_inp)
print(f"Реверс строки: {reverse_stroka}")
