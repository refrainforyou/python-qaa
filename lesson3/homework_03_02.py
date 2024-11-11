adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print(adwentures_of_tom_sawer)
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print('\n', adwentures_of_tom_sawer, sep='')

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print('\n', adwentures_of_tom_sawer, sep='')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_split = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer_split)
print('\n', adwentures_of_tom_sawer, sep='')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('зустрічається літера "h":', adwentures_of_tom_sawer.count('h'))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count = 0
for latter in adwentures_of_tom_sawer:
    if latter.isupper():
        count += 1
print('method 1:', count)

words = adwentures_of_tom_sawer.split()
capitalized_words = [word for word in words if word.istitle()]
count_2 = len(capitalized_words)
print('method 2:', count_2)



# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
find_tom = []
for index, word in enumerate(words):
    if word == 'Tom':
        find_tom.append(index)
print('method 1:', find_tom[1])

find_tom_2 = [index for index, word in enumerate(words) if word == 'Tom']
print('method 2:', find_tom_2[1])


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentences in adwentures_of_tom_sawer_sentences:
    if sentences.startswith("By the time"):
        print(True)
    else:
        print(False)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print('Кількість слів останнього речення:', len((adwentures_of_tom_sawer_sentences[-1]).split()))
