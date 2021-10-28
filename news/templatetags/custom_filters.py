from django import template


register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int):  # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')  #  в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку


CENSORED = ['физика', 'это', 'устройство,']


@register.filter(name='censor')
def censor(value):
    text = value.split()
    for word in text:
        if word.lower() in CENSORED:
            value = value.replace(word, '****')
    return value

# from django import template
#
# censor = ['физика', 'это', 'устройство,']
# register = template.Library()
#
#
# @register.filter(name='block_words')
# def block_words(value):
#     News_text = value.split()
#     for words in News_text:
#         if words.lower() in censor:
#             value = value.replace(words, '********')
#     return value
