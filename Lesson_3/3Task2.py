Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.   
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Введите год рождения: '))
city = input('Введите город: ')
email = input('Введите email: ')
telephone = input('Введите телефон: ')
def my_func (name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])

print(f"Фамилия - {surname}; Имя - {name}; Год - {year}; Город - {city}; Почта - {email}; Телефон - {telephone}")
input()