my_int = 7
my_float = 3,8
my_str = "Меня зовут Влад"
my_list = ['a', '8']
my_tuple = ('b', '6')
my_dict = {'город': 'Санкт-Петербург', 'страна': 'Россия'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')