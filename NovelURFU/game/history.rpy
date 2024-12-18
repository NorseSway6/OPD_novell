label creat_character:
    $ alf = 'йцукенгшщзхъфывапролджэюбьтимсчяЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЮБЬТИМСЧЯqwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM'
    $ name = renpy.input('Введите имя пресонажа', length=15, allow=alf).strip()
    
    if name == '':
        $ name = 'Анна' if gender == 1 else 'Данил'
    
    return

label history:
    
    window hide
    scene teenager room
    with fade
    n "[name] [Morpher('был')] обычным абитуриентом, который готовился к поступлению в университет. [Morpher('Он')] [Morpher('проводил')] много времени за учебниками и конспектами, но иногда [Morpher('позволял')] себе отвлечься на компьютерную игру в жанре стратегий, где надо строить и развивать свой город, до начала подготовки к ЕГЭ [Morpher('он')] [Morpher('был')] одним из лучших игроков."
    n "Однажды, когда [name] [Morpher('сидел')] за компьютером и [Morpher('играл')] в свою любимую игру Town Simulator, [Morpher('он')] [Morpher('заметил')], что игра стала более реалистичной. [Morpher('Он')] [Morpher('решил')], что это из-за новых обновлений, и [Morpher('продолжил')] играть. Но вскоре [name] [Morpher('понял')], что происходит нечто необычное."
    scene into game
    with fade
    n "[Morpher('Он')] [Morpher('оказался')] в виртуальном мире, где всё было как в игре, но теперь [Morpher('он')] [Morpher('сам')] по ту сторону экрана, при этом [name] [Morpher('мог')] чувствовать запахи, слышать звуки и даже ощущать прикосновения. Мир представляет собой не совсем обычный мир, а мир будущего с множеством IT специальностей, все процессы в мире происходят благодаря им. [name] [Morpher('был')] [Morpher('поражен')] и не [Morpher('знал')], что делать в первое время, но быстро [Morpher('вкатился')] в новые реалии."
    scene mayor room
    with fade
    n "[name] [Morpher('выполнял')] работу главы города, но вдруг в городе началось землетрясение и погас весь свет, а из всех громкоговорителей в городе послышалось это: «На сервере ведутся технические работы. Приносим извинения». Жители города привыкли к этому и нормально отнеслись к данной ситуации."
    scene city attack
    with fade
    n "Ничего не предвещало беды, но в этот момент команда Herceg’s team начала свою атаку на город, взламывая системы управления транспортом, энергоснабжением и другими важными инфраструктурами. Это приводит к хаосу и панике среди жителей города. Власти города пытаются остановить Herceg, но их усилия оказываются тщетными. [name] не понимает, как Herceg смог взломать всю структуру города, так как хранилище данных в порядке и сигнализация тоже не срабатывала."
    n "Herceg продолжает свои атаки, и вскоре город оказывается под его контролем. Herceg устанавливает свою власть над городом, используя технологии для слежки за жителями и контроля над ними. После полного захвата города на всех экранах в городе показался сам Herceg и произнес следующее:"
    scene loudspeaker
    with fade
    h "«Здравствуйте, дорогие жители, теперь я новый правитель этого города! Вы должны полностью подчиняться мне и моей команде, в случае сопротивления мы будем повреждать часть файлов города и стирать ее с лица Земли. До скорых встреч, друзья»"
    n "[name] [Morpher('впал')] в отчаяние из-за чего [Morpher('решил')] зайти в ближайшее кафе, чтобы перекусить и обдумать дальнейшие действия."
    scene cafe
    with fade
    menu:
        "Смириться со случившейся ситуацией и полностью подчиниться власти Herceg":
            $ memory1 = True
            call one_1
        "Постараться найти компромисс с Herceg":
            $ memory2 = True
            call one_2
        "Начать сопротивление Herceg":
            call one_3
    $ memory1 = False
    $ memory2 = False

    scene phone
    with fade
    n "Пост быстро разлетелся по всему Интернету и собрал множество различных реакций. Кто-то винил [Morpher('его')] в разрушении четверти города, кто-то был согласен с [Morpher('ним')] и с тем, что сопротивление необходимо и так больше продолжаться не может. [name] [Morpher('был')] [Morpher('поражен')] решительностью Herceg и [Morpher('понял')], что Herceg не блефует и настроен очень серьезно. В этот момент неизвестный написал [Morpher('ему')] необычное сообщение:"
    n "«На площади, где памятник стоит,\nВ тринадцать часов здесь городской бит зазвучит.\nЗдесь люди встретят мечты и надежды,\nИ каждый их шаг — как шаг в бесконечность.»"
    menu:
        "Странный какой-то, мне не до стихов сейчас, когда такая беда в городе.":
            call two_1_2
        "Красивый стих, человек явно закладывал душу в этот стих.":
            call two_1_2
        "Я думаю, что этот стих мне отправили не просто так, здесь что-то зашифровано.":
            call two_3

    d "Я специалист по кибербезопасности и знаю, как бороться с такими угрозами. Расскажи мне подробнее о ситуации в городе."
    m "Ну, Herceg захватил контроль над городом и установил свою власть. Он использует технологии для слежки за людьми и контроля над ними."
    d "Понятно. Я могу обеспечить безопасность личных данных жителей и тогда жители смогут не подчиняться Herceg."
    m "Это отлично, но угроза разрушения города все еще останется нерешенной."
    d "К сожалению, в этом я уже помочь не смогу в силу не компетенции, но я знаю кто сможет."
    m "Кто?" 
    d "Мой учитель, его зовут King, ну это его позывной, он белый хакер – лучший специалист по кибербезопасности в этом городе. Он точно сможет помочь."
    m "Ты сможешь назначить мне встречу с ним?"
    d "Да, конечно. Я сообщу тебе когда и где будет встреча."
    m "Хорошо, а ты пока займись безопасностью личных данных жителей."
    d "Хорошо, до встречи."
    m "До встречи."
    hide skin
    hide dima

    scene mayor room
    with fade
    n "После встречи с Дмитрием [name] идет к себе домой, чтобы продумать план нападения на Herceg. Ровно в 15 часов приходит сообщение от Дмитрия:"
    n "«В заднем дворе, в тени под газоном,\nКарл Маркс размышлял о жизни и зове.\nСорок один в жизни — не просто слова,\nВ 16 часов приходит мечта.»"
    n "[name] понимает, что это снова загадка. Про задний двор и 16 часов [Morpher('он')] [Morpher('понял')] сразу."
    show skin at main_character
    m "Но в городе огромное количество задних дворов о каком именно идет речь? И причем тут Карл Маркс?"
    hide skin
    menu:
        "Может я [Morpher('должен')] встретиться с Карлом Марксом и он мне сообщит, где именно будет встреча":
            $ memory1 = True
            call three_1
        "Карл Маркс не имеет никакого отношения и случайно попал в этот стих":
            $ memory2 = True
            call three_2
        "Это улица Карла Маркса дом 41":
            call three_3
    $ memory1 = False
    $ memory2 = False

    scene street
    with fade
    n "[name] [Morpher('поспешил')] на встречу с King. Когда [name] пришел на нужное место, King уже ждал его там."
    show king at secondary_character
    k "Привет, [name]. Дмитрий передал мне, что тебе нужна моя помощь. Я знаю какая ситуация сейчас в городе и сам готов тебе помощь. Что я могу для тебя сделать?"
    show skin at main_character
    m "Привет, King. Наш город нуждается в защите от разрушения. Я знаю, что ты сможешь его защитить."
    k "Защита города от разрушения Herceg это конечно сложная задача. Но проблема даже не в этом, так как все файлы города в его руках, и он может стереть весь город с лица Земли в любой момент."
    k "Так как с каждым днем из-за митингов жителей ситуация накаляется все сильнее и сильнее, у нас просто нет столько времени, чтобы найти все уязвимости в системе и полностью защитить город."
    m "Но оставить город совсем без защиты мы тоже не можем. А если мы защитим хотя бы четверть города, чтобы Herceg не смог развалить его полностью?"
    k "Ну это звучит уже более реально, я смогу это сделать в кратчайшие сроки, но что мы будем делать с самим Herceg? Мы не можем оставить его просто так."
    m "Я не знаю, как даже подобраться к Herceg, мы не знаем где он находится."
    k "С этим я могу тебе помочь, но есть одно НО. Нужно, чтобы он вышел в Интернет. А он выходил на связь только во время захвата города, и когда ты выложил пост, то есть попытался сопротивляться ему."
    m "Я [Morpher('понял')] к чему ты ведешь, ты хочешь, чтобы я вновь [Morpher('начал')] публичное сопротивление?"
    k "Да."
    m "Но мы потеряем еще одну четверть города."
    k "У нас нет другого выбора. Чтобы спасти этот город нужно чем-то пожертвовать."
    m "Ладно, я [Morpher('готов')], но главное, чтобы это было не зря."
    m "Займись пока защитой четверти города, а я придумаю как заставить Herceg вновь заявить о себе."
    k "Хорошо."
    hide skin
    hide king
    
    scene phone
    with fade
    n "В 17 часов [name] выкладывает пост о поиске специалистов различных IT-профессий для создания команды antiHerceg. И [Morpher('его')] план сработал, в этот же момент на всех экранах города появился Herceg и сказал: [name], очень жаль, что ты так и не [Morpher('понял')] какая власть принадлежит мне и то, насколько серьезна ситуация, мне надоели вечные митинги в городе и твои действия против меня, поэтому я решил, удалить не четверть, а сразу половину города, как ты понимаешь 3 шанса не будет и весь город будет разрушен. До скорых встреч, друзья»"
    n "[name] [Morpher('был')] [Morpher('растерян')], когда за один день из-за [Morpher('него')] было разрушено ¾ города, но [Morpher('верил')], что [Morpher('делал')] все правильно, но жители города были очень злы на [Morpher('него')] и винили [Morpher('его')] во всем, что произошло с городом. Многие из них остались без домов и работы. На пост откликнулись еще 6 человек. Всем им [Morpher('он')] отправил сообщение с шифром:"
    n "«В лесопарке вечер, заходит солнца круг,\nНа дубе тихо шепчет ветер о снах.\nВосемнадцать часов, и в зените здесь вдруг\nЗажгутся звезды ярко, даря новый дух.»"
    scene oak
    with fade
    n "И [Morpher('сам')] отправился в центр лесопарка, где находился столетний дуб. Ровно к 18 часам пришли все 6 человек и началось знакомство."
    show skin at main_character
    m "Все мы здесь собрались с одной целью, чтобы раз и навсегда покончить с главной проблемой на данный момент – с Herceg. Сейчас я вас [Morpher('собрал')], чтобы вы рассказали о себе и своих умениях."
    hide skin
    show dima at center
    d "Всем привет, меня зовут Дмитрий, я senior разработчик на C++, также знаю такие языки как C, C#, Java, JavaScript, Python и другие. Я окончил ИТМО и уже 10 лет работаю в IT сфере, создавал различные проекты и готов помогать в разработке новых проектов."
    hide dima
    show diana at center
    di "Всем привет, меня зовут Диана, я уже 8 лет работаю дизайнером в IT сфере. Я окончила Российский государственный университет им. А.Н. Косыгина. Я создала много различных дизайнов проектов, реализованных по всему нашему городу."
    hide diana
    show kiril at center
    ki "Всем привет, меня зовут Кирилл, я уже 11 лет работаю тестировщиком в IT сфере. Я окончил Московский государственный технический университет им. Н.Э. Баумана, знаю многие нюансы разработки и могу помочь с тестированием различных технологий."
    ki "За свою карьеру я уже успел протестировать много новых проектов и решений и готов помочь в этом вам."
    hide kiril
    show ekaterina at center
    e "Всем привет, меня зовут Катя, я уже 6 лет работаю аналитиком в IT сфере."
    e "Я окончила Национальный исследовательский университет «Высшая школа экономики», который мне дал сильную математическую базу для анализа трендов рынка, текущего состояния, масштабируемости и планов по развитию продуктов на ближайшее время."
    e " Множество проектов, с которыми я работала продолжают активно развиваться и по сей день."
    hide ekaterina
    show alina at center
    a "Всем привет, меня зовут Алина, я уже 9 лет работаю геймдизайнером в IT сфере. Я окончила Санкт-Петербургский государственный университет. Я придумала структуру и логику многих проектов в нашем городе."
    hide alina
    show oleg at center
    o "Всем привет, меня зовут Кирилл, я уже 13 лет работаю в IT сфере, неоднократно был тимлидом ведущих проектов в городе. Я окончил «Московский государственный университет имени М. В. Ломоносова»."
    o "Умею хорошо коммуницировать с людьми, хорошо отвечаю за управление, координацию и поддержку команды и слежу за выполнением поставленных задач и реализацией проектов."
    hide oleg
    show skin at main_character
    m "Очень [Morpher('рад')] со всеми вами познакомиться. Надеюсь мы сможем вместе противостоять Herceg и продолжим развивать город."
    hide skin

    scene phone
    with fade
    n "В 20 часов [name] приходит сообщение от неизвестного:\nНа краю света раздаются мечты,\nА в глубине души звучит Эпихарм.\nТихий ветер шепчет о счастливой жизни,\nОткрывая сердца, наполняя нежностью.\nМы вместе можем преодолеть все преграды,\nЖизни радости мы будем хранить,\nЕдва поднявшись, увидим рассвет,\nМы встретим новый день с надеждой на свет."
    n "Ещё один шаг — и мы движемся без радиопомех,\nСмело идем туда, где нас ждёт успех.\nТолько вместе, с надеждой в груди,\nЕдиный путь ведёт к светлым мечтам.\nВместе мы сильнее, это наш завет,\n2 + 1 — мы создадим новый свет.\n1 — это шаг к новой жизни и целям!"
    menu:
        "Это опять шифр, но я не понимаю, что здесь зашифровано":
            $ memory1 = True 
            call four_1
        "Это опять шифр, но расшифровывать его нужно как-то по-другому":
            $ memory2 = True
            call four_2
        "Кто такой Эпихарм?":
            call four_3
    $ memory1 = False
    $ memory2 = False

    scene street
    with fade
    n "[name] решает взять с собой на встречу с King всю команду, и они отправились к нему. King был очень удивлен, когда на встречу пришло целых 7 человек вместо 1, и начался диалог:"
    show king at secondary_character
    k "Вау, ты уже успел найти команду, которая поможет нам в борьбе с Herceg?"
    show skin at main_character
    m "Да, это опытные специалисты в IT сфере. У тебя есть какие-то новости?"
    k "Да, у меня есть для тебя хорошие новости, именно поэтому я тебя и позвал."
    k "Наш план сработал, когда ты выложил пост, Herceg подключился ко всем экранам в городе и я смог определить его IP-адрес, и несмотря на то, что он использовал VPN, я знаю его реальное местоположение, и мы можем его схватить."
    m "Это отлично, а что по поводу защиты города?"
    k "Ах, да, об этом я тоже позаботился, я изучил уязвимости оставшейся части города и понял как Herceg смог разрушить его, теперь оставшаяся часть города в безопасности, и мы можем начинать нашу операцию по захвату Herceg."
    m "Отлично, пошли."
    k "Пошлите, друзья, Herceg находится в хранилище данных города, которое располагается под главным штабом правительства."
    m "Как в хранилище данных!?"
    k "Что-то не так?"
    m "В хранилище данных попасть невозможно. Даже мне закрыт туда доступ. Там тройной уровень защиты, огромное количество охраны на входе, и в случае появления в хранилище данных посторонних лиц сразу срабатывает сигнализация, поэтому проникнуть туда просто невозможно."
    m "Но система сигнализации в норме и охрана там состоит из лучших бойцов города, я проверял, когда был захват города."
    k "А у кого есть доступ к хранилищу?"
    m "Доступ к хранилищу есть всего у трех доверенных мне человек, которые там работают, всем остальным вход запрещен."
    k "Тогда у меня для тебя печальные новости, [name]. Herceg - это один из работников хранилища, а остальные - 2 его помощники."
    m "Предатели…"
    k "Пошлите к входу в хранилище, но я не знаю как нам попасть в само хранилище, если даже у тебя нет доступа к нему."
    m "Пошлите ко входу, там разберемся."
    hide king
    hide skin

    scene entry storage
    with fade
    n "[name] с командой и King приходят ко входу в хранилище. Охранники их не пускают в хранилище, тогда [name] вкратце рассказывает о том, что Herceg находится в хранилище и как они это поняли. На что охранники ответили, что тоже заметили странности в их поведении. Охранники верят [name] и вместе с [Morpher('ним')] заходят в хранилище. Группа специального назначения обходит все хранилище и ликвидирует 2 помощников Herceg. "
    n "Остается только последняя комната. Они входят в нее по карте доступа одного из ликвидированных работников и заходят в последнюю комнату там прямо по середине сидит на стуле Herceg, держа в руке красную кнопку, которая может втереть оставшуюся часть города с лица Земли."
    menu:
        "Зайти агрессивно":
            call five_1
        "Зайти спокойно":
            call five_2

    n "Команда [name] выходит на улицу, а [name] появляется на всех экранах в городе, где сообщает о том, что война с Herceg окончена. Толпа ликует. После чего [name] отказывается от статуса главы города и извиняется перед жителями за то, что из-за него ¾ города разрушены и предстоит долгая отстройка города. После чего [name] спускается к своей команде и говорит:"
    show skin at main_character
    m "Спасибо, за то, что помогли справиться с Herceg. Теперь я тоже хочу начать жизнь с чистого листа."
    m "Мне было очень интересно, когда вы рассказывали, чем вы занимаетесь, я тоже хочу попробовать себя в IT, но пока не знаю в какой именно профессии."
    #show team возможно просто вывести спрайты с разным расположение или создать вотку всех членов команды(легче)
    t "¾ города разрушено, его нужно срочно восстанавливать."
    t "Также многие люди потеряли работу и теперь в поисках новой, а нам нужно много IT специалистов, чтобы восстановить город, поэтому мы решили провести консультации по различным профессиям в IT сфере, там мы расскажем о самой профессии и о том, где можно этому обучиться."
    t "Можешь посетить каждую и узнать для себя много нового, а потом определиться, что тебе по душе и где ты себя видишь."
    m "Спасибо большое, обязательно схожу к вам всем и послушаю про разные профессии."
    scene consultation
    with fade
    m "Куда бы мне пойти?"
    hide skin
    #hide team
    call seven

    menu:
        "Консультация по кибербезопасности":
            show skin at main_character
            m "Круто, наконец то я [Morpher('понял')], кем хочу быть!"
            hide skin
        "Консультация по разработке:":
            show skin at main_character
            m "Круто, наконец то я [Morpher('понял')], кем хочу быть!"
            hide skin
        "Консультация по аналитике":
            show skin at main_character
            m "Круто, наконец то я [Morpher('понял')], кем хочу быть!"
            hide skin
        "Консультация по дизайну":
            show skin at main_character
            m "Круто, наконец то я [Morpher('понял')], кем хочу быть!"
            hide skin
        "Консультация по геймдизайну":
            show skin at main_character
            m "Круто, наконец то я [Morpher('понял')], кем хочу быть!"
            hide skin
        "Консультация про тестирование":
            show skin at main_character
            m "Круто, наконец то я [Morpher('понял')], кем хочу быть!"
            hide skin
        "Консультация про управление проектами":
            show skin at main_character
            m "Круто, наконец то я [Morpher('понял')], кем хочу быть!"
            hide skin

    scene antiherceg
    with fade
    n "Благодаря команде antiHerceg в Town появляется много молодых IT-специалистов, которые решили восстановить город и сделать его ещё лучше, в том числе и [name]. Они начинают с анализа данных о состоянии города и разработки плана восстановления под руководством Екатерины."
    n "Первым шагом становится восстановление системы управления городом. Эта система позволяет оптимизировать работу всех городских служб, таких как транспорт, водоснабжение, электроснабжение и т. д. Она также помогает отслеживать состояние зданий и инфраструктуры, что позволяет быстро выявлять и устранять проблемы. Над этой задачей трудятся Данил и его последователи разработчики."
    scene building
    with fade
    n "Затем молодые специалисты начинают восстанавливать городские здания. Диана и ее дизайнеры разрабатывают новые течения в архитектуре и дома становятся настоящими произведениями искусства. Они также используют современные технологии строительства. Кроме того, благодаря команде Данила они внедряют в городе систему «умного дома», которая позволяет жителям управлять своими домами с помощью мобильных устройств."
    n "Параллельно с восстановлением города молодые специалисты работают над созданием новых рабочих мест и развлечений, над ними работает команда геймдизайнеров во главе с Алиной.  Они разрабатывают новые проекты, которые могут быть реализованы в Town. Это привлекает в город новых жителей и предпринимателей, что способствует его развитию."
    n "Во время создания всех нововведений, новых проектов и технологий каждую технологию тщательно проверяют на работоспособность, возникновение ошибок и неисправностей команда тестировщиков Кирилла."
    n "После Herceg остался серьезный отпечаток в душе King. Он пообещал себе, что больше никогда не допустит, чтобы кто-то помешал развитию и процветанию Town. Он с Дмитрием создает команду высококлассных специалистов, которые каждую секунду следят за безопасность всей системы города."
    n "Всеми процессами в городе руководит самый опытный специалист – Олег, вместе со своими учениками. Развитие всего города проходит полностью под его контролем: все проекты и предложения одобряет, отклоняет именно он. Он также ставит определенные сроки  выполнения, поощряет хороших работников и поддерживает всех участников проекта по восстановлению города."
    scene new center
    with fade
    n "Наконец, молодые специалисты решают создать в Town центр инноваций и технологий. Этот центр станет местом, где будут разрабатываться новые проекты в области IT, робототехники, искусственного интеллекта и других областей. Он также будет служить площадкой для обмена опытом и знаниями между молодыми специалистами со всего мира."
    n "Благодаря усилиям молодых IT-специалистов Town быстро восстанавливается. Город становится ещё более развитым и процветающим, чем прежде. Жители города благодарны молодым специалистам за их труд и преданность делу. Они понимают, что благодаря им город получил новую жизнь и возможность стать ещё лучше."
    n "После тяжелого и напряженного дня [name] идет к себе домой и ложится спать."
    n "А просыпается [name] от того, что ему в глаза светит солнце на часах уже полдень и понимает, что уснул, когда играл в Town Simulator, и все, что с ним произошло, всего лишь сон, но он прекрасно помнит, что происходило этой ночью в его голове. И он, наконец-то, определился с будущей профессией. Садиться и дальше продолжает готовиться к ЕГЭ."
    nvl hide

    return