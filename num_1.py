def pal_check(string, mod_2):
    for _ in range(len(string)):
        del_el = string.pop()
        if not del_el == s[int(len(s) / 2 + i + mod_2)]:
            print("Не палиндром")
            exit()


s = list(input("Введите слово для проверки на палиндром: "))
heap = list()

if len(s) < 3:
    print("В слове меньше 3 букв")
    exit()

for i in range(int(len(s) / 2)):
    heap.append(s[i])
even = len(s) % 2

pal_check(heap, even)
print("Палиндром")
