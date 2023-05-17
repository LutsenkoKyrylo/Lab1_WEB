import requests #Імпортуємо бібліотеку requests
e = input("Введіть вираз для обчислення: ") #Введення виразу з клавіатури
url = "https://api.mathjs.org/v4/?expr=" + e #Створення URL

try:
    res = requests.get(url)  #HTTP-запит до API
    if res.status_code == 200:  #Перевірка відповіді HTTP-запиту
        r = res.text #Отримання результату
        print("Результат:", r) #Виведення результату
    else:
        print("Помилка під час виконання запиту:", res.status_code) #Якщо сталася помилка, виведення повідомлення про помилку
except requests.RequestException as e:
    print("Помилка під час виконання запиту:", str(e))