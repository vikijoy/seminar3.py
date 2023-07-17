import itertools

# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
# *Код должен расширяться на любое большее количество друзей.
friends = input().split()  # формируем список друзей
data = {}


for friend in friends:  # заполняем словарь data ключами - именами друзей и значениями - кортежами с вводимыми данными.
    data.setdefault(friend, tuple(input().split()))


def all_things(dic: dict) -> str:
    """Функция для возвращения строки, со всеми вещами"""
    result = ''
    for tup in dic.values():
        for j in tup:
            result += j + ' '
    return f'All friends took these: {result}'


def uniq_things(doc: dict) -> str:
    """Функция для возвращения строки, с уникальными вещами"""
    lst = []
    for tup in doc.values():
        for k in tup:
            lst.append(k)
    return f'Unique items are: {set(lst)}'


def except_things(d: dict, name: str):
    """Функция для печати строк с вещами, которых нет у переданного имени"""
    for key, value in d.items():
        if key != name:
            print(f'{key} взял с собой {value}')
        else:
            print(f' И всех этих вещей нет у человека по имени {name}')


print(all_things(data))
print(uniq_things(data))
except_things(data, 'name')

# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
lst = [1, 2, 3, 4, 1, 3, 5, 5, 2, 1, 4, 12, 27, 666, 144]
d = {}
for i in lst:
    d[i] = d.get(i, 0) + 1
for key, value in d.items():
    if value > 1:
        print(key, end=' ')

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.
text = '''В этой статье мы рассмотрели Метод setdefault словаря Python, его синтаксис, основное
       использование и практические приложения. Мы также сравнили его с методом get,
       выделив ключевые различия между ними.Метод setdefault является полезным инструментом
       для инициализации значений в словаре при работе с ключами, которые могут присутствовать
       или отсутствовать, что делает его ценным дополнением к вашему набору инструментов Python. 
       Много раз при работе со строками Python у нас возникает проблема, при которой нам нужно удалить
       определенные символы из строк. Это может найти применение при предварительной обработке данных в 
       области науки о данных, а также в повседневном программировании. Давайте обсудим определенные 
       способы, которыми мы можем выполнить эту задачу, используя Python. Для создания контента YaGPT 
       использует различные источники информации интернет, книги, журналы, газеты и другие источники. 
       Также добавляет в свою базу знаний ту информацию, которую предоставляет пользователь. Помощник 
       может помочь написать сценарий, составить обращение в государственные органы, предложит план 
       действий для той или иной ситуации. По утверждению самого помощника на его основе можно создать 
       локальную базу знаний для создания персонализированных ответов на вопросы и запросы, для хранения 
       заметок, списков задач, напоминаний и других вещей, которые могут помочь в повседневной жизни. 
       Помощник может ошибаться в фактах и фантазировать, однако по мере обучения нейросети будет выдавать 
       всё более точные ответы. Ожидается, что голосовой помощник будет внедрен в поисковик Яндекс-браузера 
       уже есть аналогичное решение у MS Windows, где поисковый движок Bing является основным браузерным 
       движком нейросети ChatGPT по умолчанию. YandexGPT обучали на суперкомпьютерах Яндекса в два этапа. 
       На первом этапе нейросети скормили большое количество наиболее полезных общедоступных текстов отобранных
        с помощью поисковых моделей Яндекса. На втором этапе точно не ясно но по всей видимости обучали на 
        качественных примерах уже готовых ответов на вопросы. Для этих целей был задействован краудсорсинг Яндекса,
         а также команда AI тренеров специалистов широкого круга гуманитарных профессий нанятых компанией Яндекс 
         для обучения нейросети. Кроме того, нейросеть училась придумывать новые факты и события, основываясь на 
         контексте и знаниях о мире по всей видимости это будет отдельная опция по аналогии с реализацией ChatGPT 
         в браузере Edge. 5 июня 2023 года в пресс-службе Яндекса сообщили, что нейросеть научилась запоминать контекст
          беседы и задавать уточняющие вопросы. 15 июня 2023 года Яндекс добавил языковую модель YandexGPT в свой 
          сервис генерации изображений Шедеврум. Теперь пользователи приложения могут в ответ на текстовый запрос 
          получить не только картинку, но и содержательный пост.19 июня 2023 года нейросеть YandexGPT стала доступна 
          бизнесу для создания умных помощников и чат ботов, а также генерирования и структурирования текстовой 
          информации. В рамках бета-тестирования, которое начнётся в июле, примет участие ограниченное число компаний,
           которые смогут использовать технологию в двух режимах: YandexGPTPlayground и YandexGPT API.27 июня 2023 года 
           в Яндексе сообщили, что нейросеть научилась составлять краткое содержание статей. Функция находится в тестовом
            режиме и работает пока только на русскоязычных текстах объёмом до 30 000 тыс. знаков.'''
modified_text = map(lambda x: x.strip(',') or x.lower().strip('.'), text.split())
words = {}
for word in modified_text:
    words[word] = words.get(word, 0) + 1
sorted_words = {key: value for key, value in sorted(words.items(), key=lambda item: item[1], reverse=True)}
print(*list(itertools.islice(sorted_words.keys(), 10)))

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть
# один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
def max_weight_count(weight: int) -> list:
    mass = weight * 1000
    result = []
    things = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300, 'термос': 1000, 'аптечка': 200,
              'куртка': 600, 'бинокль': 400, 'удочка': 1200, 'салфетки': 40, 'бутерброды': 820, 'палатка': 5500,
              'спальный мешок': 2250, 'жвачка': 10}
    modified_things = dict(sorted(things.items(), key=lambda x: -x[1]))
    for thing, vess in modified_things.items():
        if vess < mass:
            result.append(thing)
            mass -= vess
    return result


num = int(input('Put your weight in grams\n'))
print(max_weight_count(num))