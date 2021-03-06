label devilishadv_day5_ru:
    $ backdrop = "dv"
    $ new_chapter (5, u"Люцифер. День 5")
    $ persistent.sprite_time = 'night'
    $ night_time()
    window show
    play music music_list ["a_promise_from_distant_days"] fadein 4
    show d3_lu_and_dv with dissolve
    show prologue_dream
    "Сегодня мне снилось то, что произошло позавчера. Алиса, гитара, дискотека."
    scene bg ext_square_night_party with dissolve
    show dv smile pioneer close with dissolve
    show prologue_dream
    "Может всё-таки эти сны имеют какое-то значение? Только вот то, что уже произошло мне снится впервые."
    stop music fadeout 2
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene bg int_house_of_dv_day with dissolve
    show unblink
    play ambience ambience_int_cabin_day
    play music music_list["take_me_beautifully"] fadein 2
    "Я проснулся от чувства ужасной жажды. Вчера ведь мы кроме виски то ничего и не пили. "
    "Я хотел было встать, но вот незадача. Моя рука была прижата Алисой, которая мирно посапывала рядом со мной. "
    th "Да уж, вечерок вчера удался. А сколько вообще сейчас время? Вряд ли раннее утро, мы тогда только уснули"
    "Первой идеей было узнать время на телефоне, но мои брюки были вне зоны досягаемости. Какое-то время я просто лежал, размышляя как бы встать, не будя Алису. Пить хотелось всё сильнее. "
    play sound sfx_dinner_horn_processed
    "Меня спас горн, предположительно зовущий всех на обед. Алиса поморщилась и приоткрыла свои прекрасные янтарные глаза. "
    show cg epilogue_uv_dv with dissolve
    dv "Что, уже завтрак?"
    "Я поцеловал её, после чего сказал:"
    lur "Скорее обед, мы с тобой ещё те засони. "
    stop music fadeout 1
    hide cg
    play music music_list["awakening_power"] fadein 1
    show dv shocked pioneer2 close with hpunch
    play sound sfx_bed_squeak1
    dv "Обед?! А что мы скажем вожатой, где пол дня пропадали?"
    lur "Да не волнуйся ты, придумаем что-нибудь. А теперь пора вставать. "
    "Она поднялась и освободила мою руку, после чего мы начали собирать одежду из разных уголков домика. Пока я одевался я бросил ещё пару взглядов на свою нагую красавицу. "
    dv "Успеешь ещё насмотреться, а вот на обед такими темпами можем не успеть."
    lur "Ладно, ладно. Но ловлю на слове. "
    stop ambience
    scene bg ext_dining_hall_near_day with dissolve
    "Мы быстро оделись и пошли к столовой. Помянешь {i}меня{/i} - он тут как тут, на пороге нас встретила Ольга Дмитриевна."
    show mt angry pioneer with dspr
    show dv normal pioneer2 at fright with dspr
    mt "И где вас всё утро носило? Пропустили и линейку и завтрак!{w} Даже спрашивать не буду, где вы были ночью.{w} У нас есть проблемы поважнее: пропал Шурик."
    lur "Любите же вы нагрузить спросонья. Мы Шурика не видели, следуя из того, что вы всё о нас знаете.{w} Где мы были вы тоже можете догадаться. Теперь нам можно пойти поесть?"
    mt "Да, можете. Но сразу после этого вы присоединитесь к поискам. "
    lur "Так точно!"
    "Выпалил я, делая самое наигранное воинское приветствие вожатой. Она лишь закатила глаза и зашла за нами внутрь здания."
    stop music fadeout 2
    scene bg int_dining_hall_people_day with dspr
    play music music_list["you_won_t_let_me_down"] fadein 2
    play sound sfx_close_door_1
    play ambience ambience_dining_hall_full
    show dv smile pioneer2 close with dspr
    dv "Скоро главной целью вожатой станешь ты, а не я. Такими нахальными ответами и я похвастаться не могу. "
    lur "Учись, пока есть возможность."
    dv "Да ну тебя, я просто не хочу так привлекать её внимание. На мне его всегда было достаточно. "
    lur "Хорошо, можем, как примерные пионеры, пойти после еды и правда поискать Шурика. Может проявим себя с хорошей стороны перед Ольгой. "
    dv "Давай, можем этим воспользоваться, чтобы собрать ингредиенты. "
    lur "Какие ещё ингредиенты?"
    dv "Я давно хотела устроить что-то взрывное. Думала заложить бомбу под Генду. "
    lur "С одной стороны ищем Шурика и помогаем лагерю, с другой стороны взрываем памятник партийному деятелю. Лицемернее не придумаешь. "
    show dv angry pioneer2 close with dspr
    dv "Не хочешь - сама сделаю!"
    lur "Да я не против. Но тогда лучше будет разделиться, чтобы это не выглядело слишком подозрительно. И ингредиенты твои быстрее соберём. "
    show dv smile pioneer2 close with dspr
    dv "Вот и отлично. На тебе уголь, остальное я достану. "
    lur "Прогулка в медпункт? Проще некуда. Да и с медсестрой у нас довольно тёплые отношения."
    th "А вот последнее можно было и умолчать"
    show dv angry pioneer2 close with dspr
    dv "Какие-какие отношения? У вас с ней что-то было?"
    lur "Чёрт, зря я это упомянул."
    dv "Давай рассказывай, а то не поздоровится. И в медпункт тебе придётся идти не только за углём."
    lur "Ээ, ну скажем так, у нас был очень {i}детальный{/i} медицинский осмотр друг друга на второй день. "
    play sound sfx_face_slap
    "По лицу прилетела ожидаемая пощёчина." with hpunch
    show dv rage pioneer2 close with dspr
    lur "Ау, ну мы же с тобой тогда ещё не были вместе. "
    dv "В муз-клубе значит звал меня гулять на вечер, а параллельно с медсестрой кувыркался? Запасные варианты собирал?"
    lur "Ты всё не так поняла… "
    dv "Я поняла всё, что мне нужно было."
    hide dv with moveoutright
    "Она выбежала из столовой, выражая что-то между несоизмеримой яростью и вселенской грустью. "
    th "Даа, ну ты и попал, ловелас хренов"
    play sound sfx_punch_washstand
    "Я ударил кулаком по столу, который чуть не разбился от этого. На произошедшую ситуацию, кажется, смотрела вся столовая. "
    stop ambience
    scene bg ext_dining_hall_near_day with dspr
    play sound sfx_close_door_1
    $ renpy.pause(1)
    play sound sfx_alisa_lighter
    "Я тоже бросил свою еду на столе и вышел из столовой. На крыльце я закурил, чтобы успокоить нервы."
    th "Эту проблему быстро не исправишь"
    scene bg ext_musclub_day with dissolve
    "Докурив, я пошёл в музыкальный клуб. Я постучался и вошёл. "
    play sound sfx_knock_door2
    play sound sfx_open_door_1
    scene bg int_musclub_day with dspr
    show mi smile pioneer with dspr
    mi "Люцифер, привет. Как дела? Пришёл поиграть?"
    lur "Нет настроения, Микусь."
    "Я прошёл мимо Мику и сел за пианино."
    hide mi with dspr
    show mi sad pioneer at right with dspr
    show lu_piano with dspr
    "[Creep - Radiohead (Lucifer cover)]"
    play music creep
    "Пока я играл, Мику молча наблюдала за мной со стороны, перемещаясь то на стул, то в угол комнаты. Она не могла найти себе места."
    "[Нажми, чтобы закончить песню.]"
    stop music fadeout 2
    "Когда песня закончилась, над комнатой повисла гробовая тишина. Это могло продолжаться ещё долго, но тишину наконец решилась нарушить Мику. "
    play ambience ambience_music_club_day
    hide lu_piano with dspr
    mi "У вас с Алисой что-то случилось? "
    "С легкой задержкой я ответил:"
    lur "Да, можно и так сказать. Я сделал что-то раньше, о чём теперь сожалею. В итоге я виноват перед Алисой."
    mi "А как ты будешь заглаживать вину?"
    lur "Даже не знаю, Мику, даже не знаю."
    mi "Попробуй цветы. Я всегда радуюсь, когда мне дарят цветы. Думаю, Алиса тоже обрадуется и простит тебя."
    lur "Если бы всё было так просто…{w} Но спасибо за совет, я попробую. Ты знаешь, какие она любит цветы?"
    mi "Я не знаю, мы с ней только о музыке и общаемся. Лена может знать, они ведь друг друга с детства знают."
    lur "Лена? Точно. Тогда пойду и найду её. Ещё раз спасибо, Мику."
    show mi smile pioneer with dspr
    mi "Не за что, заходи поиграть ещё!"
    stop ambience
    play music music_list["meet_me_there"] fadein 4
    "К счастью, Лена как раз-таки мне все ещё должна. Я вышел из муз-клуба и пошёл искать её по лагерю."
    scene bg ext_square_day with dspr
    "Я проверил сначала площадь,"
    scene bg ext_house_of_un_day with dspr 
    "потом её домик,"
    scene bg ext_library_day with dspr
    "потом библиотеку."
    "Её нигде не было видно. "
    scene bg ext_washstand_day with dspr
    "Отчаявшись, я решил сходить к умывальникам и освежиться. Вот тут мне и повезло."
    play ambience ambience_camp_center_day
    show un normal pioneer far at right with dspr
    "Лена как раз проходила по дорожке мимо них. Что она делала именно там меня волновало меньше всего. Главное, что я её нашёл. "
    lur "Лена, привет! "
    show un surprise pioneer with dspr
    "Лена, как всегда, сделала удивлённое лицо, которое вскоре сменилось на смущение."
    show un shy pioneer with dspr
    un "Привет. "
    lur "Слушай, тут такое дело есть. Ты ведь давно Алису знаешь?"
    show un surprise pioneer with dspr
    un "Ну да. А откуда ты знаешь об этом?"
    lur "Не важно. Лучше скажи мне, знаешь ли ты, какие цветы нравятся Алисе?"
    show un normal pioneer with dspr
    un "Да, знаю… А зачем тебе?"
    lur "У нас с ней… вышло недопонимание. Мне нужно как-то загладить свою вину. "
    lur "Я особо не знаю где и какие цветы тут растут, не обращал внимания. Можешь собрать какой-нибудь букетик из того, что понравилось бы ей? Твой должок будет искуплен. "
    un "Ну хорошо, а когда?"
    lur "Как можно быстрее."
    un "Тогда давай встретимся здесь примерно через час, я соберу что-нибудь для неё. "
    lur "Отлично, спасибо тебе. "
    "Мы разошлись в разные стороны. Я к своему домику, Лена по какой-то тропинке, ведущей в лес от умывальников. "
    "Я ушёл к своему домику, пока букет собирался за меня. Может это было и не лучшей идеей, но гулять с Леной по лесу в поисках цветов звучало, как совсем ужасный план. Если на нас там наткнётся Алиса, то из этой ямы я себя никогда не выкопаю. "
    stop music fadeout 2
    stop ambience
    scene bg int_house_of_mt_day with dspr
    play sound sfx_close_door_1
    play ambience ambience_int_cabin_day
    "Зайдя внутрь, я стал размышлять о том, что я скажу Алисе, когда увижу её и отдам ей букет. Нужно было извиниться, как следует, описать почему вышло именно так."
    "Да, я правда жонглировал тремя девушками в первые дни, но я не думал, что окажусь с одной из них в отношениях, тем более влюблюсь."
    "Пока я думал, на меня нашла другая мысль: сходить за тем углём, с которого всё и началось. Положу его в букет, как знак того, что я всё-таки прислушиваюсь к ней."
    stop ambience
    scene bg ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day
    "Через пару минут я уже был в медпункте. Времени на стук у меня не было, поэтому я просто вошёл. "
    scene bg int_aidpost_day with dspr
    play sound sfx_open_door_1
    show cs smile glasses with dspr
    play music music_list["glimmering_coals"] fadein 2
    cs "О, Люцифер. Болит чего, тревожит? Или зашёл просто так со мной повидаться?"
    "Как обычно игривым голосом проговорила Виола, но на данный момент мне было не до неё. "
    lur "Мне бы угля активированного. "
    cs "Живот болит, значит? Может сначала осмотрим?"
    lur "Я бы с радостью, но сейчас у меня есть дела поважнее. Так что прошу у вас только уголь."
    cs "Что ж, должно быть {i}действительно{/i} важно. Хорошо, сейчас."
    "Она достала из шкафчика активированный уголь в таблетках и протянула его мне. "
    lur "Спасибо."
    hide cs with moveoutleft
    "Я развернулся и выходя услышал за собой:"
    cs "Не забывай про меня, пионер."
    th "Забудешь тут"
    play sound sfx_close_door_1
    stop music fadeout 2
    scene bg ext_washstand_day with dspr
    play music music_list["tried_to_bring_it_back"] fadein 4
    "Времени до конца часа оставалось немного, поэтому я сразу пошёл к умывальникам. "
    scene bg ext_washstand2_day with dspr
    "У умывальников Лены ещё не было, поэтому я пока решил освежиться и умылся у одного из кранов. "
    play sound sfx_water_emerge
    $ renpy.pause (1)
    play sound sfx_water_splash
    "Через пару минут появилась и моя доставка цветов по адресу. Лена держала в руках букет из пионов и колокольчиков. Композиция получилась неплохая, да и Лена знала, что понравится подруге детства."
    scene bg ext_washstand_day with dspr
    show un normal pioneer far with dspr
    "Она подошла ко мне."
    show un normal pioneer with dspr
    un "Вот, как-то так."
    lur "Спасибо тебе, Лен."
    show un smile pioneer with dspr
    "Я забрал у неё букет и приобнял в знак благодарности. "
    stop music fadeout 4
    show dv sad pioneer far at right with dissolve
    play music music_list["you_lost_me"] fadein 2
    "Казалось, что всё шло хорошо, пока я не заметил Алису, идущую к умывальникам. Её лицо было заплаканным, видимо хотела умыться."
    "Я сразу же отпустил Лену, но было уже поздно."
    show un surprise pioneer with dspr
    show dv rage pioneer at right with dspr
    dv "Ты! ТЫ!{w} Я значит рыдаю из-за него, пытаюсь простить, а он уже другой цветы дарит! "
    lur "Подожди, всё вовсе не так!"
    "Алиса даже не дослушала меня и побежала в обратную сторону. "
    hide dv with moveoutright
    lur "Стой! Чёрт..."
    $ sshake = Shake((0.5, 5.0, 0.5, 1.0), 1.0, dist=5)
    scene bg ext_houses_day with dspr
    play sound sfx_run_forest
    "Я побежал за ней, держа букет в руках. Она была шустрее меня, да и в туфлях бегать было не удобно." with Shake((0.5, 1.0, 0.5, 1.0), 5.0, dist=5)
    "Я отставал на приличное расстояние, но из виду её не выпускал. С одной из тропинок она свернула в лес." with Shake((0.5, 1.0, 0.5, 1.0), 5.0, dist=5)
    scene bg ext_path_day with dspr
    play sound sfx_run_forest
    "Добежав до того места, я свернул за ней и побежал в ту же сторону. Видно её уже не было, но я всё ещё рассчитывал, что вскоре её нагоню или услышу. " with Shake((0.5, 1.0, 0.5, 1.0), 5.0, dist=5)
    scene bg ext_path2_day with dspr
    play sound sfx_run_forest
    "Какое-то время я просто бежал вслепую, но тут я услышал крик.{w} Алисин крик. " with Shake((0.5, 1.0, 0.5, 1.0), 5.0, dist=5)
    play sound sfx_alisa_falls
    "Это заставило меня ускориться пуще прежнего, стирая туфли в землю. "
    stop music fadeout 2
    scene bg ext_polyana_day with dspr
    play music music_list["doomed_to_be_defeated"] fadein 2
    show pi far with dspr
    "Вскоре я выбежал на какую-то поляну и передо мной открылась неожиданная картина. Алиса лежала на земле, без сознания. Над ней стоял Пионер. "
    pi "А вот и наш горе-романтик объявился. Не такой уж ты неуязвимый, когда у тебя есть, что терять. "
    "Я сорвался на крик. Мои глаза пылали ярким пламенем."
    lur "Что ты с ней сделал?! Отвечай!"
    show pi smile with dspr
    "Бросив букет на землю, я стал сближаться со своим врагом. "
    pi "Я всего лишь вырубил её, но она жива.{w} А с тобой у нас уже будет другой разговор. Ты меня в прошлый раз унизил, теперь моя очередь. "
    "Я продолжал сближаться. Он поставил ногу на шею Алисе."
    pi "Ни шагу дальше, иначе рыжей не поздоровится."
    "Я остановился. Рисковать жизнью Алисы я не мог. "
    lur "Чего.{w} Ты.{w} Хочешь?"
    "Прошипел я. "
    pi "Ответов, мести, твоих страданий. Ничего сложного. "
    lur "Хорошо, я отвечу на твои вопросы. Но потом ты должен её отпустить. "
    pi "Задаю тут условия я, если хочешь жизни своей пассии.{w} А теперь скажи мне, дьявол, ты истекаешь кровью?"
    lur "Подойди и проверь, тварь."
    play music like_a_wounded_animal fadein 2
    pi "Не знаю, знаешь ли ты об этом, но у меня тоже есть пара фокусов. "
    show pi smile at fleft as pi2 with dspr
    show pi smile at fright as pi3 with dspr
    "Из-за деревьев слева и справа от меня вышли два таких же пионера, как тот, что стоял передо мной. "
    lur "Какого…? "
    show pi smile close at left as pi2 with dspr
    show pi smile close at right as pi3 with dspr
    "Они медленно подошли ко мне. Я всё ещё считал, что даже с тремя такими я справлюсь без проблем."
    play sound sfx_punch_medium
    "Думал, пока один из них меня не ударил в живот. Я согнулся от боли. " with hpunch
    th "Что за? Почему я это чувствую?"
    play sound sfx_punch_medium
    show pi at fleft as pi2 with vpunch
    "Второй уже хотел добить меня ударом сверху, но я резко поднялся и дал ему апперкот. Он попятился назад и чуть не упал, еле удержав равновесие. "
    th "Значит и силы мои уменьшились"
    play sound sfx_punch_medium
    "Я не успел сообразить, как первый меня ударил по лицу, и я сам чуть не упал. " with hpunch
    pi "Не такой уж ты и сильный, когда она рядом. Я за тобой следил, ты уязвим только с ней. "
    th "Так вот оно что. Я догадывался об этом, но не думал, что это работает именно так"
    pi "Перестань сопротивляться, ей будет только хуже."
    "Он надавил ей на шею ногой. Это окончательно вывело меня из себя."
    play sound sfx_punch_medium
    hide pi3 with moveoutright 
    hide pi2 with dspr
    "Я толкнул первого как можно сильнее и рванул к Пионеру, сбивая его с ног собой."
    show pi close
    play sound sfx_punch_medium
    $ renpy.pause (1)
    play sound sfx_punch_medium
    $ renpy.pause (1)
    play sound sfx_punch_medium
    "Я нанёс ему пару быстрых ударов по лицу, когда он уже был на земле."
    hide pi with dspr
    "Дальше я отбежал к Алисе. "
    show dv sad pioneer close with dspr
    lur "Алиса, ты слышишь меня? "
    "Я ощупал её горло, вроде ничего сломано не было. Алиса прокашлялась."
    dv "Д-да. Что… случилось?"
    hide dv with dspr
    show pi far at fleft as pi2 with dspr
    show pi far at left as pi3 with dspr
    show pi far as pi4 with dspr
    show pi far at right as pi5 with dspr
    show pi far at fright as pi6 with dspr
    "В этот момент из-за деревьев вышли ещё три пионера и все шестеро теперь подступали к нам с Алисой. Я встал, готовясь к битве."
    "Алиса всё ещё лежала на земле, еле приходя в сознание. В этой драке она мне уж точно не поможет. "
    "Я осмотрел окружение в поисках оружия, но на этой поляне даже палочки не завалялось. "
    show pi smile at left as pi3 with dspr
    show pi smile at right as pi5 with dspr
    "Придётся справляться, как есть. Пионеры подступали ближе."
    play sound sfx_punch_medium
    hide pi as pi3 with moveoutleft
    "К счастью, не все одновременно, поэтому удар первого я смог парировать и нанести ответный. "
    play sound sfx_punch_medium
    hide pi as pi5 with moveoutleft
    "Сразу развернувшись ко второму, я дал удар с разворота и тот на время отступил."
    show pi smile at fleft
    show pi smile at left as pi2 with dspr
    show pi smile close as pi4 with dspr
    show pi smile at right as pi6 with dspr
    "Дальше всё пошло менее в мою пользу. Оставшиеся четыре пионера решили не нападать по одному. Один из них замахнулся в меня спереди, отвлёкся на него. "
    hide pi with moveoutleft
    hide pi as pi6 with moveoutright
    "В это время меня сзади схватили двое других, а четвёртый ударил сбоку. " with hpunch
    play sound sfx_bodyfall_1
    stop music fadeout 2
    "Я попытался вырваться, но они повалили меня на землю и начали пинать со всех сторон." with vpunch
    play sound sfx_alisa_falls
    play music music_list["drown"] fadein 2
    "Я не мог ничего сделать, но тут один из ударов, летевший в меня ударил что-то другое. Недалеко от себя я услышал заглушённый визг Алисы. "
    th "Вот ублюдки, меня не хватило, взялись за девушку"
    "Меня били и пинали со всех сторон, злобно хохочущие пионеры, один из которых бил и рядом лежащую Алису." with hpunch
    "Сквозь град ударов я прополз и накрыл Алису собой, не давая обидчикам трогать хоть её. " with vpunch
    "Тело неимоверно болело со всех сторон, и я еле терпел каждый последующий удар. Внутри я чувствовал безысходность, но в то же время всё более нарастающую ярость." with hpunch
    "Ещё удары." with vpunch
    "Жизнь в лагере мелькала перед глазами." with hpunch
    "И ещё." with vpunch
    "Это не могло просто так закончиться. " with hpunch
    "Ещё." with vpunch
    "Только не сейчас. " with hpunch
    stop music fadeout 4
    th "Только не сейчас!" with Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=5)
    play music on_thin_ice fadein 2
    lur "ААААА!" with Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=5)
    show lu_wings with dspr
    "Из моей окровавленной спины вырвались огромные белоснежные крылья и раскинули обидчиков во все стороны."
    "Пользуясь возможностью, я поднял Алису с земли и взлетел, унося её в лагерь. "
    hide lu_wings with dspr
    stop music fadeout 2
    scene bg ext_square_day with dissolve
    play music music_list["farewell_to_the_past_full"] fadein 2
    play sound sfx_wind_gust
    "Я опустился в деревьях у площади и отнёс Алису на скамейку, предварительно спрятав крылья."
    show dv shocked pioneer with dspr
    dv "Ты… ты Ангел! На самом деле!"
    lur "Позже. Сейчас нужно с кое-чем разобраться. "
    play sound sfx_wind_gust
    "Я снова расправил крылья и пулей взлетел в небо, чтобы никакой зевака-пионер не заметил меня слишком чётко. "
    stop music fadeout 1
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    $ volume(0.5, "music")
    play music treat_me_like_your_mother fadein 2
    scene bg ext_polyana_day with dissolve
    "Я прилетел обратно на поляну, где меня как будто ждали эти пионеры."
    play sound sfx_body_bump
    "Я эффектно приземлился, сбивая одного из них с ног в процессе. "
    "Ярость пылала во мне, а как следствие и глаза. Я снова чувствовал всю дьявольскую силу."
    show pi far with dspr
    show pi far at right as pi2 with dspr
    show pi far at left as pi3 with dspr
    "Пионеры были явно удивлены крыльям, но всё же начали снова подходить, чтобы напасть."
    show pi close with move
    "В этот раз я не стоял, дожидаясь их, а бросился в атаку. Один взмах крыльев и я уже у одного из них перед лицом."
    play sound sfx_punch_washstand
    hide pi with moveoutright
    "Он не успел среагировать, как от удара в живот полетел в ближайшее дерево и стукнулся об него спиной. " with hpunch
    "Далее один из них попытался схватить меня за крыло, но одним его махом я отбил пионера, и он полетел на землю." with vpunch
    "Третий подбежал ко мне и хотел было ударить, но я поймал его кулак на полпути и вывернул руку в обратную сторону, ломая кость."
    pi "Аааа!"
    lur "Ваша очередь испытать боль."
    play sound sfx_body_bump
    "Ко мне в спину влетел ещё один пионер, повалив меня на землю, но взмахнув крыльями, я поднялся, откинув оппортуниста. " with hpunch
    show pi close as pi2 with move
    "Всё, что мне хотелось сейчас – отомстить, наказать их за наглость, за покушение на мою и, главное, Алисину жизнь.{w} Я ударил пятого по счёту пионера в лицо и услышал, как сломался его нос."
    hide pi as pi2 with moveoutright
    hide pi as pi3 with dspr
    show pi far with dspr
    "Остался лишь один, их главарь. Тот самый, что недавно держал ногу на шее Алисы. Он попятился назад."
    pi "Стой! Мы ещё можем всё обговорить."
    lur "Время для разговора прошло!"
    show pi close with dspr
    play sound sfx_torch
    "За два шага я уже был возле него. Я схватил его обеими руками за лицо и зажёг их."
    "Я не разрывал зрительный контакт, смотря на него с ненавистью и презрением, а также с какой-то нездоровой радостью. Пионер кричал в агонии, пока плавилась плоть на его лице и горели волосы. "
    hide pi with dspr
    play sound sfx_bodyfall_1
    stop music fadeout 2
    $ volume(1, "music")
    play music music_list["torture"] fadein 2
    "Он размахивал руками и ногами во все стороны – тщетно. Когда от лица осталась лишь неразборчивая каша, я отпустил его, и он повалился на землю. "
    "Кричать он не переставал, но это уже переросло больше в вой животного."
    "Остальные его копии расползались кто куда мог, дабы не стать жертвой такой же участи."
    "Позади себя я услышал голос."
    stop music fadeout 2
    dv "Нет, ты не Ангел, ты и есть Дьявол…"
    play music after_the_storm fadein 2
    show dv sad pioneer far with dspr
    "Я развернулся в три четверти и увидел стоящую на тропинке в лес Алису."
    "Вид у меня был действительно чертовский. Крылья давно были спрятаны, мои руки, глаза и волосы пылали оранжевым пламенем и на лице расползлась дьявольская улыбка. Завидев её, всё постепенно потухло и вернулось в нормальное состояние. "
    show dv sad pioneer with dspr
    "Я медленно пошёл к ней. Она сделала пару шагов назад, но остановилась. "
    lur "Ты в порядке? "
    dv "Что… что ты с ним сделал? "
    lur "Он получил по заслугам. За то, что сделал с тобой, и со мной. Он будет жить, но нормально – больше никогда. "
    "Алиса молча взглянула на свёрнутого калачиком Пионера, лежавшего на другой стороне поляны. Потом она перевела взгляд на меня. "
    show dv cry pioneer close with dspr
    "На её янтарных глазах блестели слёзы. Я не выдержал этого взгляда и обнял её. Сначала она просто стояла, но потом тоже обняла меня."
    dv "Я думала, что мы тут умрём. Что я больше никогда тебя не увижу. "
    "Она плакала мне в грудь. Я гладил её по голове. "
    lur "Теперь всё будет хорошо. "
    "Она перестала плакать, но пошмыгивала носом."
    dv "Правда?"
    lur "Правда. "
    $ persistent.sprite_time = 'night'
    $ night_time()
    play ambience ambience_forest_evening
    show lu_dv_forest with dissolve
    "Через какое-то время мы окровавленные и побитые, вернулись в лагерь по тропинке. Мы крепко держались за руки, не отпуская друг друга. "
    dv "Что теперь будет? Ты ведь и правда дьявол. А я тебе не верила. Разве ты можешь быть со мной?"
    lur "А что я делал всё это время, глупышка? Может мой отец и против моего нахождения тут, но я решаю кем мне быть, а кем нет. Где находиться, а где нет. "
    dv "Твой от-отец? Отец Бог?"
    lur "Он самый. Но я сделаю всё, чтобы мы были вместе, не волнуйся. "
    stop music fadeout 4
    stop ambience
    scene bg ext_square_night with dspr
    hide lu_dv_forest with dspr
    play ambience ambience_camp_center_night
    play music music_list["sweet_darkness"] fadein 2
    show dv normal pioneer at left with dspr
    show mt surprise pioneer with dspr
    "Кажется, Алиса хотела спросить что-то ещё, но мы уже подошли к площади, где наш разговор прервала Ольга Дмитриевна."
    mt "Боже, что с вами случилось? Почему вы все грязные и побитые? Была какая-то драка? "
    lur "Только не ввязывайте {i}его{/i} в это, он тут не причём. Что с нами произошло не столь важно, главное, что мы в порядке. "
    show mt normal pioneer with dspr
    mt "Раз так, то тогда у нас до сих пор осталась одна проблема. Шурик так и не появился. Вы его искали?"
    "Я тяжело вздохнул. "
    stop music fadeout 2
    lur "Дайте нам полчаса, мы его найдём. "
    play music music_list["awakening_power"] fadein 2
    show dv angry pioneer with dspr
    "Алиса, до этого тихо стоящая рядом, похоже пришла в себя."
    dv "А почему мы вообще должны его искать? Полный лагерь пионеров, но почему-то вы пристаёте с этим именно к нам!"
    show mt angry pioneer with dspr
    mt "Потому что вы только и делаете, что создаёте проблемы лагерю последние пару дней. Шурика ищут и другие, но от этого вы не отвяжетесь, как от всех остальных моих просьб. "
    show mt angry pioneer far with move
    show dv angry pioneer close with move
    "Я отвёл Алису от вожатой."
    lur "Алиса, не спорь с ней сейчас, я знаю, как решить эту проблему. Нас даже потом похвалят."
    stop music fadeout 4
    show dv normal pioneer close with dspr
    dv "И что же за план такой?"
    lur "Всё просто, я знаю, где Шурик. "
    show dv surprise pioneer close with dspr
    dv "Ты всё это время знал? А почему вожатой не сказал?"
    lur "Потому что она бы всё равно нас туда отправила. "
    show dv smile pioneer with dspr
    dv "Точно. Ладно, веди."
    lur "Он в старом лагере, но я знаю короткий путь. "
    scene bg ext_path2_night with dspr
    "Я отвёл Алису в кусты, где нас с большинства сторон прикрывали листья или деревья. "
    show dv grin pioneer with dspr
    dv "Это твой короткий путь? Через кусты?"
    lur "Не совсем."
    play music banks_of_the_sansretour fadein 4
    show dv shocked pioneer close with dspr
    "Я подхватил Алису на руки и раскрыл крылья."
    th "Раз уж у меня они есть, то почему бы ими не воспользоваться?"
    play sound sfx_wind_gust
    "Вспорхнув в небо, я полетел к старому лагерю, крепко держа своё счастье в руках."
    scene night_forest with dissolve
    show dv scared pioneer close with dspr
    dv "Ааа! Ты что творишь? "
    lur "Сокращаю путь."
    "Алиса сначала зажмурила глаза, но потом любопытство взяло верх, и она всё же их приоткрыла, с восхищением наблюдая за открывшимся перед ней видом. Всё время полёта она крепко держалась за мою шею. "
    show dv surprise pioneer close with dspr
    dv "Как красиво…"
    "Вскоре мы долетели до старого корпуса. Солнце уже заходило за горизонт и с каждой минутой это здание становилось всё страшней. "
    scene bg ext_old_building_night with dspr
    play ambience ambience_forest_night
    show dv pioneer smile with dspr
    lur "Спасибо за полёт на Дьявольских Авиалиниях. Надеюсь, вам понравилось ваше время на борту. Надеемся увидеть вас снова!"
    dv "Взлёт был немного страшный, а так всё понравилось. Такой отзыв устроит?"
    dv "Было бы хорошо, если бы меня ещё предупредили перед следующим полётом."
    lur "Может быть. А теперь пойдём внутрь, он в подземном помещении. "
    dv "Даже спрашивать не буду откуда ты это знаешь. Вдруг ты еще помимо всего провидец какой-нибудь. Мне на сегодня раскрытых тайн хватило. "
    lur "Как знаешь. "
    play sound sfx_door_squeak_light
    stop ambience
    scene bg int_old_building_night with dspr
    "Мы зашли внутрь, где я открыл люк в одной из комнат. Он вёл в подземелье, где потерялся Шурик. Я спустился первый, зная, что внизу может быть опасно. За мной спустилась и Алиса."
    play sound sfx_open_metal_hatch
    scene bg int_mine_room with dissolve
    play ambience ambience_catacombs
    play sound sfx_torch
    show d5_catac_dv_lu with dspr
    "Я зажёг маленький шарик огня в руке, чтобы осветить комнату. "
    show cg d4_sh_sit with dspr
    "В углу комнаты на полу, свёрнутый калачиком сидел Шурик. Он смотрел на нас каким-то обезумевшим взглядом."
    sh "Нет, вы не настоящие! Уходите! "
    hide cg with dspr
    hide d5_catac_dv_lu with dspr
    show dv angry pioneer at right with dspr
    show sh scared at left with dspr
    dv "Что значит не настоящие? Мы значит тут его ищем, а он в подвале прохлаждается!"
    "Она хотела было подойти и дать ему пощёчину, но я выставил перед ней руку, удерживая её возле себя. На пониженных тонах я сказал ей:"
    lur "У него в руках арматура, если на него давить, то он ей воспользуется."
    show dv scared pioneer at right with dspr
    "Агрессия на лице Алисы сменилась на волнение. Шурик тем временем всё также глядел на нас."
    play music music_list["pile"] fadein 2
    show sh rage at left with dspr
    sh "Почему вы всё ещё здесь? Хотите меня забрать, да? Я просто так не дамся!"
    show cg d4_sh_stay with dspr
    "Он вскочил с земли и замахнулся арматурой в Алису. Этого я и ожидал, поэтому среагировал быстро. "
    play sound sfx_punch_medium
    scene black with dspr
    hide cg with dspr
    "Отбив одной рукой его замах арматурой, другой я схватил его за шею и поднял с земли. В комнате повисла кромешная тьма, так как мне пришлось потушить огонёк. "
    scene bg int_mine_room with dspr
    show sh scared close with dspr
    show dv shocked pioneer at right with dspr
    "Вместо него правда зажглись мои глаза. Я выхватил арматуру из его руки."
    lur "Либо ты сейчас прекращаешь это дерьмо, либо я эту арматуру засуну так глубоко тебе в жопу, что ты металл на вкус почувствуешь. Решать тебе. "
    stop music fadeout 4
    sh "Х-х-хорошо, хорошо. Забирайте меня куда хотите, только не бейте!"
    play music music_list["door_to_nightmare"] fadein 2
    lur "Да что ты заладил. «Забирайте, забирайте». Алиса, можешь дать ту пощёчину, которую хотела."
    show dv smile pioneer close at right with dspr
    play sound sfx_face_slap
    "Алиса с довольной улыбкой подошла и дала Шурику по лицу. "
    sh "Ай! Ч-что? Где это я?"
    play sound sfx_alisa_lighter
    "Я поставил его на землю и зажёг зажигалку, чтобы не пугать его огненными руками. "
    show sh scared with move
    show dv smile pioneer with move
    lur "Это лучше ты нам скажи, что ты тут забыл. В подземном тоннеле под старым лагерем. "
    sh "Я сюда за запчастями для робота пришёл и… потерялся. Какие-то голоса водили меня кругами по шахтам..."
    show dv angry pioneer with dspr
    dv "Какие ещё голоса? Ты совсем спятил? Какого хрена ты вообще на людей с арматурой бросаешься?"
    sh "Не знаю, я слышал, что меня кто-то звал, а потом уже не помню. С какой ещё арматурой?"
    lur "С вот этой, умник. Ты правда не помнишь произошедшего 2 минуты назад?"
    sh "Н-нет. Я помню только с момента боли в щеке и потом ты меня опустил на землю."
    lur "Ясно. Алиса, пошли наверх. Если этот хочет, то пусть дальше по шахтам блуждает за «голосами»."
    dv "Полностью согласна, пойдём. "
    sh "Эй, подождите, не оставляйте меня тут! Я с вами."
    hide dv with dspr
    hide sh with dspr
    "Я пустил Алису лезть первой, затем полез за ней. Передо мной открылся довольно неплохой вид. "
    lur "А ты не врала, когда сказала, что я насмотреться ещё успею."
    dv "Я тебе сейчас твои светящиеся моргалы выколю."
    th "Помогите! Зрения лишают!"
    lur "За что это?"
    dv "За излишнее любопытство."
    stop music fadeout 2
    play music music_list["dance_of_fireflies"] fadein 2
    stop ambience
    show lu_dv_forest with dspr
    "Вскоре мы выбрались на поверхность и пошли обратно к лагерю. Мы с Алисой шли впереди, а наш объект поиска плёлся где-то позади."
    "Время от времени я посматривал назад, чтобы убедится, что он не провалился в какую-нибудь дыру в земле. "
    scene ext_square_night with dspr
    show dv smile pioneer at right with dspr
    show sh normal at left with dspr
    "Когда мы вернулись на площадь, там никого уже не было. Над лагерем стояла ночь. "
    lur "Шурик, беги к себе. Надеюсь, по дороге тебя на позовёт ещё один голос."
    sh "Очень смешно. Спокойной ночи."
    hide sh with moveoutleft
    "Он поплёлся в сторону его с Электроником домика. "
    lur "Кстати, о ночи. Мы снова идём к тебе? "
    dv "А ты не задумывался почему вчера не было Ульяны? "
    lur "Да не особо. Но это было довольно кстати."
    dv "Я её просила переночевать у подружки. Сегодня я её ни о чём не просила, так что спим сегодня раздельно."
    lur "Мда, и ко мне не пойдёшь, ведь это логово вожатой. Что ж, одну ночь я, пожалуй, без тебя переживу, а завтра что-нибудь придумаем. "
    dv "Ага, разберёмся. А теперь я очень хочу спать, до завтра!"
    lur "До завтра, милая."
    "Я поцеловал её напоследок, после чего мы разошлись по домикам. "
    stop music fadeout 4
    scene int_house_of_mt_night with dissolve
    play sound sfx_close_door_1
    play ambience ambience_int_cabin_evening
    "В домике меня ждала Ольга Дмитриевна. "
    show mt normal pioneer with dspr
    mt "Как прошли поиски? Мне надо вызывать милицию?"
    lur "Нашли мы вашего Шурика. Потерялся в старом лагере. "
    mt "Правда? А что он там делал?"
    lur "Завтра у него и узнаете. А теперь простите, сегодня был длинный день. Я хочу спать."
    mt "Хорошо, спрошу у него. Вы молодцы, что нашли его. Спокойной ночи."
    lur "Угу."
    "Я разделся и улёгся в кровать. Всё тело ныло после сегодняшнего побоища в лесу. Может нам с Алисой всё-таки стоило навестить медпункт. "
    show blink
    "Хотя это могло бы и напомнить ей о причине нашей ссоры в обед. Несмотря на боль, я быстро отрубился."
    window hide
    jump devilishadv_day666_ru