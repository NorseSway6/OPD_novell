label one_1:

    n "Herceg c каждым днем все сильнее ужесточает контроль над обществом. Исходя из этого [name] понимает, что так продолжаться больше не может и вновь задумывается о том, как можно помешать Herceg"
    
    if memory2==True:
        menu:
            "Начать сопротивление Herceg":
                call one_3 from _call_one_3 
    else:
        menu:
            "Постараться найти компромисс с Herceg":
                call one_2 from _call_one_2
            "Начать сопротивление Herceg":
                call one_3 from _call_one_3_1

    return


label one_2:

    n "[name] начинает переговоры с Herceg в TownChat."
    show skin_man at main_character
    m "Herceg, нам нужно срочно найти компромисс в этой ситуации."
    show herceg at secondary_character
    h "Компромисс? Я не понимаю, о чём ты говоришь. Я установил полный контроль над этим городом, и я не собираюсь его терять."
    m "Но ты же понимаешь, что твой контроль над городом — это неправильно. Ты используешь технологии для слежки за людьми и контроля над ними. Это нарушает их права и свободы."
    m "Мы готовы предложить тебе альтернативу. Отпусти город и мы обещаем, что не будем преследовать тебя."
    h "Это просто смешно! Вы даже близко не сможете ко мне подойти. Этот город — мой. Я создал здесь идеальное общество, где всё контролируется и всё работает как часы."
    m "Но это не так. Люди страдают под твоим контролем. Они лишены свободы и возможности выбирать свой путь."
    m "Подумай о том, что ты делаешь. Ты можешь потерять всё, если мы не найдём компромисс."
    h "Мне надоели твои пустые угрозы, я впустую потратил свое время. Но помните, от любого вашего действия против меня будет страдать сам город. Удачи!"
    hide herceg
    hide skin_man
    n "После этого [name] понимает, что никаких компромиссов и быть не может."

    if memory1==True:
        menu:
            "Начать сопротивление Herceg":
                call one_3 from _call_one_3_2   
    else:
        menu:
            "Смириться со случившейся ситуацией и полностью подчиниться власти Herceg":
                call one_1 from _call_one_1
            "Начать сопротивление Herceg":
                call one_3 from _call_one_3_3

    return


label one_3:
    
    n "Тогда [name] на своей странице в TownChat решил выложить пост о поиске лучших cпециалистов по кибербезопасности в городе, чтобы спасти город от Herceg. В этот момент на экранах появился Herceg и сказал: 
«[name], будьте разумны, сопротивление бессмысленно, жаль, что вы не поняли это с первого раза. Я ошибок не прощаю, попрощайтесь с первой четвертью города. До скорых встреч, друзья»"