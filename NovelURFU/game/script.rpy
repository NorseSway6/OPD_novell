define m = Character('[name]', color='#fafafa', image='[skin]')
define n = Character(None, kind=nvl)
define h = Character('Herceg', color='#fafafa')
define d = Character('Дмитрий', color='#fafafa')
define k = Character('King', color='#fafafa')
define di = Character('Диана', color='#fafafa')
define ki = Character('Кирилл', color='#fafafa')
define e = Character('Екатерина', color='#fafafa')
define a = Character('Алина', color='#fafafa')
define o = Character('Олег', color='#fafafa')
define t = Character('Команда', color='#fafafa')
define memory1 = False
define memory2 = False
$ skin = ''
$ gender = 0


### Сделать "аватар" к репликам (+- сделан)
### Поиграться с окончаниями, что бы для женищины не делать отдельную историю. Можно с помощью бибилиотеки
### Решить что то со склонением имен
### Сделать hide winodw ии подобная хрень

init:
    $ main_character = Position(xalign = 0.2, yalign = 0.8)
    $ secondary_character = Position(xalign = 0.85, yalign = 0.8)

label gender_choice:
    
    menu:
        'Какого персонажа ты выберешь?'

        'Женщина':
            $ gender = 1
            jump creat_woman
        'Мужчина':
            $ gender = 0
            jump creat_man

label start:
    $ variants = [1, 2, 3, 4, 5, 6, 7]
    scene choice character
    with fade

    call gender_choice from _call_gender_choice
    
    call screen choice_character
    
    image skin = '[skin]'

    return