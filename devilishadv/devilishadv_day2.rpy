init:
    $ el_and_mz = 0
    $ library_visited = False
    $ medical_visited = False
    $ musical_visited = False
    $ clubs_visited = False

label devilishadv_day2_en:
    $ backdrop = "days"
    $ new_chapter (2, u"Lucifer. Day 2")
    play music music_list["into_the_unknown"] fadein 2
    scene island_reverse with fade
    show amen_angry with dspr
    show pi far at left with dspr #not working
    show prologue_dream
    window show
    "As usual, my dreams were occupied by some incoherent nonsense. A tall black man was ordering me to go back to Hell.{w} By his side was the Pioneer from the forest, whispering something into his ear. Something in those words enraged the man and he attacked me.{w} The fight lasted an eternity, or so it seemed…"
    window hide
    stop music fadeout 2
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene white with flash
    window show
    "Bright light flashed in my eyes."
    th "What, the bus again? I doubt it would even surprise me"
    play ambience ambience_int_cabin_day
    scene bg int_house_of_mt_day with flash
    play music music_list["lightness"] fadein 4
    "I opened my eyes ever so slightly to find out where I was. The dream left me somewhat disoriented.{w} I was laying on a bed and something was pushing into my back."
    play sound sfx_bed_squeak1
    "I turned towards what appeared to be Olia, peacefully asleep. "
    th "Ah yes, our nighttime entertainment. I hope she won’t treat it as something serious. Lest I’ll have to move out of this hut rather soon"
    "I got up and checked the time. “It’s a quarter to eight” – shone on my phone’s display. "
    th "Isn’t it about time for her to run off and do her counselor duties?"
    "I didn’t want to wake her up, since I was the reason for her lack of sleep.{w} However, her desire was to enforce the rules, and I haven’t forgotten about that. "
    lu "Olia…{w} Olga!{w} Olga Dmitriyevna!"
    "I whispered, slowly raising my tone with each word."
    "I gave her a slight push, which drove her to open her eyes. "
    show mt surprise swim close at right with dissolve
    mt "Lu- Lucifer?{w} What… What happened yesterday?"
    lu "Sex, of course. Kind of a dumb question if you ask me."
    "Olga looked like the events of last night just flashed before her eyes. After a pause, she said"
    show mt normal swim close at right with dspr
    mt "May I count on this remaining between us?"
    lu "Obviously, I am a Devil of my word, after all."
    show mt angry swim close at right with dspr
    mt "Good. Then not a word to anybody of this night from now on. Please refer to me as any other pioneer would.{w} I don’t know what came over me yesterday, but I hope it shan’t happen again. "
    lu "Alright, if it’s so important to you… O’ counselor mine. I won’t say a thing. "
    "She looked at the alarm clock next to her bed. "
    show mt surprise swim close at right with dspr
    mt "It’s already this late?! The morning lineup starts in 15 minutes!"
    hide mt with moveoutleft
    "She started running around the room, quickly preparing to leave. In around 5 minutes she was dressed and ready to go, while I lazily buttoned up my shirt and pulled on my pants. "
    show mt angry pioneer with dissolve
    mt "What do you think you’re wearing? Your uniform is on your bed. "
    "I took a glance at my bed, where a stack of clothes was located. A pioneer shirt, some dark-blue shorts and a bright-red tie. Wearing a pioneer uniform wasn’t part of my plans."
    "Initially, I wanted to tie it around my forearm, but then an image of people, who not so long ago, by this world’s standards, wore their red flag in the same spot. Ultimately, I tied it around my wrist on my left arm. "
    th "This’ll do fine"
    lu "I’ll stick to just the tie if you don’t mind."
    "Olga glanced at my outfit and was about to complain, but then she remembered how persuasive I can be and conceded to my compromise. "
    mt "Fine, at least the tie. Don’t be late to the lineup!"
    play sound sfx_drop_alisa_bag
    "She threw me a bag of washing materials and ran out of the hut. "
    hide mt with moveoutleft
    "Once dressed, I looked myself in the mirror, from which a certain redheaded diva looked back with a devilish glance. Found myself thinking that since yesterday I’ve adopted more and more of his character traits. The hair looked perfect, as it did yesterday."
    th "Least I don’t have to worry about one thing for sure"
    stop ambience fadeout 2
    scene bg ext_house_of_mt_day with dissolve
    play music music_list["my_daily_life"] fadein 3
    play ambience ambience_camp_center_day fadein 1
    play sound sfx_close_door_1
    "I grabbed the bag and headed off to the washbasins. It was a wonderful sunny day outside. The heat was anything but unbearable and I could even feel a slight breeze on my skin."
    scene bg ext_washstand_day with dissolve
    th "I could get used to this"
    scene bg ext_washstand2_day with dspr
    play sound sfx_open_water_sink
    $ renpy.pause (1)
    play sound sfx_water_sink_stream
    "The water in the sinks was famously freezing, though that didn’t stop me from washing up. "
    play sound sfx_water_splash
    "Upon finishing my water-related procedures, I threw the bag in my hut and headed to the plaza. "
    window hide
    scene bg ext_house_of_mt_day with fade
    $ renpy.pause (1)
    scene bg ext_square_day with dissolve
    $ renpy.pause (1)
    show cg d2_lineup with dissolve
    window show
    "There were already enough people there to make it feel crowded, so I silently joined the people I’ve already met and got lost in thought. These lineups consisted of more slogans than useful info anyway. Furthermore, if there was something of utmost importance, Olga would come up to you later and make sure you heard. "
    $ set_mode_nvl()
    "My thoughts were of the dream I had. What could it mean and who was the black stranger? \nIf the Pioneer got chummy with someone, who could help him enact his plans, there could be another fight.\nConfident in my newfound powers, I wasn’t afraid of a confrontation, however the thought of the black one made me feel uneasy for some reason…"
    $ set_mode_adv()
    hide cg with dissolve
    show mt normal pioneer with dspr
    "My thought process was interrupted by Olga. She handed me a sheet of paper. "
    mt "Here’s your go-round sheet. You have to collect all the signatures before the end of the day. "
    "I gave the most sarcastic salute I could and stammered"
    lu "It will be done, sir! "
    "Olga gave me an annoyed look but didn’t say anything and walked off."
    hide mt with moveoutleft
    th "Welp, if I have to, then I have to. Perhaps I’ll find something interesting at least at one of the locations. I’ll do this after breakfast"
    stop ambience fadeout 4
    stop music fadeout 4
    $ renpy.pause (1)
    scene bg int_dining_hall_people_day with fade
    play ambience ambience_dining_hall_full fadein 2
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    "In the lunchroom I grabbed a tray and went on in search of a seat. The only remaining places were with Lena and Slavya.{w} The rate at which this cafeteria filled with hungry pioneers was incredible. "
    "I went up to the table and asked:"
    show sl normal pioneer close at left with dspr
    show un normal pioneer close at right with dspr
    lu "Dearest ladies, may I take a seat here?"
    show sl smile pioneer close with dspr
    sl "Of course! Please, sit."
    "Lena silently nodded without making eye contact. "
    lu "Many thanks. "
    "I sat down and began eating. Between spoons of thick porridge, I found time to ask"
    lu "How’s it going, girls?"
    sl "I’m all good. Helping the counselor look after the junior cohort today."
    "Lena gave me a shy look and then said"
    show un shy pioneer close at right with dspr
    un "I’m alright. "
    sl "What about you? Any plans for the day?"
    show un normal pioneer close at right with dspr
    lu "Not half bad myself. Plans include only the go-round sheet. "
    stop music fadeout 3
    play music music_list["you_lost_me"] fadein 3
    show sl serious pioneer close at left with dspr
    sl "Ah, ok. Listen, have you seen anyone break into the lunchroom yesterday, perhaps? The lock was broken off completely. "
    lu "Maybe some very hungry pioneers couldn’t wait ‘til breakfast. Anything important stolen?"
    "The best way to avoid lying when answering a question is not answering it directly and tactfully changing the subject.{w} “The art of political doublespeak” – especially helpful, when your whole essence prevents you from lying. "
    sl "Not really, just some sweet buns and kefir. The thief, however, cannot stay unpunished! Even for such a small crime."
    show un serious pioneer close at right with dspr
    un "Maybe it was Alisa? I saw her outside yesterday evening."
    th "Why you would decide to throw your childhood friend under the bus like that is beyond me. I won’t let you do that to Alisa"
    lu "I doubt she’d get past that lock alone, moreover, broken it off. Using a large stone or whatever would be too loud, and somebody would’ve heard her."
    sl "I agree, I would’ve heard someone break in with a dull object. I was nearby on my evening patrol. "
    th "Phew"
    "In the meantime, I finished eating. "
    stop music fadeout 4
    lu "Alright, girls, I’ve got a sheet to fill out. Catch you later. "
    stop ambience fadeout 2
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    play sound sfx_alisa_lighter
    "Outside of the lunchroom I moved to the edge of the porch just past the bench and lit another expensive cigarette. "
    th "Should I have defended Alisa there?{w} Obviously yes since I was there with her and drew suspicion away from myself. If I didn’t, she’d give me away in an instant.{w} Maybe I didn’t do it for myself? Of course not, the Devil only ever cares about himself and only himself"
    "On that note the cigarette ended, and it was time to move out. "
    "Where should I go first?"
    stop ambience fadeout 2
    window hide
    $ disable_all_zones()
    $ set_zone ("clubs","dev_clubs")
    $ set_zone ("music_club","dev_musical")
    $ set_zone ("medic_house","dev_medical")
    $ set_zone ("library","dev_library")
    $ show_map ()
label dev_clubs:
    window show
    scene ext_clubs_day with dspr
    play music music_list["smooth_machine"] fadein 4
    "Didn’t take me long to decide to go to the clubs."
    play sound sfx_open_door_clubs
    scene int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day
    "Inside, two stars of soviet engineering were waiting for me.{w} Truth be told, waiting was an overstatement. It’s doubtful that these guys ever waited for anyone inside this little sanctum, though they definitely were inside.{w} They were hard at work on something at their operating table. My entrance distracted them from it."
    show el normal pioneer at right with dspr
    show sh normal pioneer at left with dspr
    el "Oh, hey! You must be the new guy. "
    lu "Good day. I suppose you could say so. I need your signature for my sheet. "
    show el smile pioneer at right with dspr
    el "Sure, just sign up for our club and I’ll be happy to sign it."
    th "I have no desire to join your loser’s club"
    el "My name’s Electronik by the way. And this is Shurik. "
    "They both stretched out their hands to greet me. I shook Shurik’s hand first and then I thought of something."
    show sh surprise pioneer at fleft with dspr
    show el surprise close at center with dspr
    "Once I took Electronik’s hand, I didn’t let go after the shake and came close to him, making direct eye contact."
    lu "Tell me, Electronik, me signing up for you club is not what you {i}really desire{/i}, is it?"
    "Electronik froze and kept looking into my eyes, hypnotized. Shurik was observing the situation from the side, clearly confused. "
    el "N-no…"
    play sound lu_desire
    lu "Then what {b}do{/b} you desire?"
    el "To b-be with Zhenya.{w} I wanna be with Zhenya."
    show el upset pioneer close at center with dspr
    "It took him great effort to say that and his face became bright red with embarrassment."
    if library_visited == False:
        lu "Alright, favor for a favor. You sign my paper and I’ll give a good recommendation to your lady friend. I’ll be visiting the library today anyway. "
        "A diabolical smile appeared on my face."
        $ el_and_mz += 1
    else:
        th "Damn, I already talked to her today and we didn't exactly leave off on good terms. Going back there won’t work"
        lu "That's quite interesting... Would be a shame if anyone else found out about it."
        el "What do you want?"
        lu "What I {b}don't{/b} want is more like it, which is joining your little club. Sign the sheet and nobody will find out. You have my word."
    el "Ok, ok. Give me the sheet already. "
    "Still redfaced, Electronik grabbed the sheet out of my hand, quickly signed it and gave it back."
    lu "My thanks. "
    scene ext_clubs_day with dissolve
    "I took the paper and went outside. "
    stop music fadeout 3
    stop ambience
    $ clubs_visited = True
    if library_visited == True and musical_visited == True and clubs_visited == True and medical_visited == True:
        jump locations_end
    window hide
    $ disable_current_zone ()
    $ show_map ()
label dev_musical:
    window show
    scene bg ext_musclub_day with dspr
    "I came up to the musical club and went in without knocking."
    play sound sfx_open_door_2
    play music music_list["so_good_to_be_careless"] fadein 4
    play ambience ambience_music_club_day
    scene bg int_musclub_day with dissolve
    th "Strange, usually I’d knock. Seems that with each day I play this role better"
    "At first, I didn’t see anyone inside, until I noticed that someone is bent down under the piano."
    th "The piano. I’d like to see if the rumors about the Devil being a musical virtuoso are true. This walk around camp is proving to be more interesting than expected"
    show cg d2_miku_piano2 with dissolve
    "I came closer and a rather piquant view of a pioneer girl under the piano opened before me. "
    th "What are you doing, step bro?"
    lu "Nice view, though unfortunately I’m not here for that. I need your signature."
    show cg d2_miku_piano with vpunch
    play sound sfx_piano_head_bump
    "The girl likely didn’t hear me come in, so my words startled her. She tried to jump up and hit her head on the piano. Her second attempt to get out was more successful."
    hide cg with dspr
    show mi smile pioneer with dspr
    mi "Oh hi! I didn’t see you there. You’re new here, right? My name’s Miku. I saw you at the plaza yesterday, smoking with Alisa. You know that smoking is bad for you, right?"
    "A torrent of words from her mouth suddenly hit me. "
    th "Strange. I haven’t seen her among the others yesterday"
    lu "Whoa, hold your horses. Yes, I’m new. The name’s Lucifer. I’m here with a go-round sheet. Can you sign that for me, please?"
    mi "Oh, yes, of course. Would you like to join our club? There aren’t many of us, but we do have a lot of instruments. Enough to go around. Do you play anything?"
    lu "Yes, I play. I’d like to try your piano if you don’t mind."
    mi "No, I don’t mind at all. So, shall I sign you up for the club?"
    lu "Guess I don’t see a reason not to. Sign me up, then. "
    hide mi with dspr
    show mi smile pioneer far at right with dspr #flies into ground
    "I gave her the sheet and took a seat at the piano. After a crack of my fingers I put them on the keys. "
    show lu_piano with dspr
    stop music fadeout 2
    th "Let’s see what these devilish fingers are capable of"
    play music all_along_the_watchtower fadein 1
    "[Playing for Change - All Along the Watchtower (Lucifer cover)]"
    show mi surprise far at right with dspr
    "Turns out my signing voice improved, as well as playing the piano was a given."
    "Miku watched me play in awe, almost forgetting to sign the paper. "
    "[Clicking past this point will end the song]"
    hide lu_piano with dspr
    stop music fadeout 2
    show mi surprise at right with move
    mi "Wow, you play so well, and sing too? Where’d you learn all that? And the song’s in English. You speak English?"
    lu "Thank you, I did my best. I speak every language."
    mi "Truly every language? (In Japanese) Even Japanese?"
    lu "(In Japanese) Of course. Every language means every language. No exceptions. "
    "Never spoke Japanese in my life, although now I knew I had the whole suite of devilish powers available to me. "
    show mi happy at right with dspr
    mi "Incredible. Never thought I’d meet someone who speaks Japanese here! I’m so happy you joined my club."
    "Miku was ecstatic and almost jumping from excitement. At this moment Alisa came into the building."
    play sound sfx_close_door_1
    show mi smile at right with dspr
    show dv normal pioneer2 at left with dspr
    dv "What’s going on here?"
    mi "Oh hi, Alisa! It’s good you came.{w} Can you believe that Lucifer speaks Japanese, plays the piano, and sings really well?"
    show dv smile pioneer2 at left with dspr
    dv "All of that? No joke?"
    mi "Yes, yes! Lucifer play us something, or sing, or both!"
    lu "Your wish is my command."
    play music shepard_tone
    lu "This is called Shepard’s tone. In essence, it’s just a repeating melody, but it sounds as if the tone keeps rising into infinity. "
    "Now instead of one keen observer I had two. Never liked too much attention, though this felt quite nice."
    show mi happy at right with dspr
    show dv smile pioneer2 close at left with dspr
    stop music
    "Miku clapped her hands. Alisa gave a faint smile and came up to me."
    dv "You really are good. Leave some talents for the rest of us."
    lu "I’m sure there’s plenty to go around."
    "As I said that, I looked at her and then gave a glance to the guitar next to the wall."
    show dv surprise pioneer2 close at left with dspr
    $ renpy.pause (1)
    show dv smile pioneer2 close at left with dspr
    "She understood my hint, and slight surprise flashed on her face, before going back to normal right away. She knew I never saw her with a guitar. She bent down and whispered into my ear:"
    dv "Come to the stage in the evening, I’ll show you what I’m capable of. "
    show mi normal pioneer at right with dspr
    mi "What’re you guys whispering about there?"
    play music music_list["awakening_power"] fadein 4
    show dv angry pioneer2 at left with dspr
    dv "Curiosity killed the cat, and trust me, you don’t wanna be the cat.{w} By the way, did you fix my guitar?"
    show mi scared pioneer at right with dspr
    mi "I-I wanted to fix it today, but it turned out harder than I thought…"
    show dv rage pioneer2 at left with dspr
    dv "As usual. Nothing ever gets done without a good threat. I want that guitar repaired by tomorrow or else!"
    hide dv with moveoutright
    play sound sfx_slam_door_campus
    stop music fadeout 2
    "She gave Miku an evil glance and rushed out of the musical club, slamming the door behind her. Looked as if she was a bit angrier the whole building would’ve collapsed as she left."
    show mi sad pioneer at right with dspr
    lu "I’ll be going now too. Good luck, Miku."
    stop ambience
    play sound sfx_close_door_1
    play ambience ambience_camp_center_day
    play music i_tried_to_bring_it_back fadein 4
    scene ext_musclub_day with dissolve
    "I exited the club and saw Alisa waiting for me just outside. "
    show dv sad pioneer2 with dissolve
    lu "I suppose our plan for the evening is cancelled?"
    "I expected her to be fuming, but the rage passed as swiftly as it came over her. All that remained was sadness. "
    dv "I guess so. Miku ruining plans as usual."
    lu "Don’t be so mad with her. We can go to the stage some other time.{w} Today, however, we can just go for a walk. How does that sound?"
    show dv normal pioneer2 with dissolve
    $ renpy.pause (1)
    show dv grin pioneer2 with dissolve
    "Alisa gave it a quick thought and then, with an obviously raised mood said:"
    dv "Well if you insist."
    lu "See you after dinner then."
    dv "So long!"
    hide dv with moveoutright
    "She ran off to do something else, while I continued my tour de camp."
    $ musical_visited = True
    stop music fadeout 4
    stop ambience fadeout 2
    if library_visited == True and musical_visited == True and clubs_visited == True and medical_visited == True:
        jump locations_end
    window hide
    $ disable_current_zone ()
    $ show_map ()
label dev_medical:
    window show
    scene ext_aidpost_day with dspr
    "My next stop was the medical center. I came in without so much as a knock once again. "
    play sound sfx_open_door_2
    play ambience ambience_medstation_inside_day
    play music music_list["eternal_longing"] fadein 4
    scene int_aidpost_day with dissolve
    show cs smile
    "The nurse that was sitting behind her table turned around. She was an extremely sexual woman with heterochromia."
    cs "Nobody taught you to knock, pioneer? And where’s the uniform?"
    lu "Good day to you too. "
    "I pointed to the tie on my wrist to answer the latter."
    lu "Me and Olga Dmitriyevna came to a certain agreement concerning my uniform. I need this go-round sheet signed."
    cs "Alight, we’ll get it signed. But before we do that, take off your clothes."
    "Obviously, she wanted to startle a new pioneer with sexual innuendos. "
    th "Not this time, Viola, not this time"
    lu "Fine, let’s do it. But we have to be quick about it, I need to visit the other places today too."
    "I started to slowly unbutton my shirt."
    cs "Hold up, pioneer. Do what?"
    lu "You were undoubtedly hinting at fulfilling your carnal desires, so chop-chop. Let’s do this quickly and I’ll be on my way."
    show cg d5_cs with dissolve
    cs "First a medical exam and then we’ll see…"
    $ renpy.pause (1)
    hide cg with fade
    scene black with fade
    "She touched my torso with her stethoscope and began to listen. Or pretend to listen, for all I know. I on the other hand started unbuttoning her medical gown."
    play sound sfx_bed_squeak1
    "Soon the medical bunk started shaking as if someone was being brought to life on it with a defibrillator at ten times the power."
    scene int_aidpost_day with dissolve
    show cs smile close at right with dspr
    "Once the dirty deed was done, I gave the nurse a parting kiss and began to dress. "
    cs "I think I understand how you and Olga came to your “agreement”."
    "I responded with a sly smile."
    lu "And now the signature, please. "
    "I handed her the sheet and a pen from the table. She swiftly signed it and laid back on the bunk. "
    "I received my quest item and made my way to the exit."
    show cs smile far at right with dspr
    cs "Do visit more often, Lucifer. "
    lu "Of course."
    "I flashed my eyes at her and left."
    $ medical_visited = True
    stop music fadeout 4
    stop ambience fadeout 2
    window hide
    if library_visited == True and musical_visited == True and clubs_visited == True and medical_visited == True:
        jump locations_end
    $ disable_current_zone ()
    $ show_map ()
label dev_library:
    window show
    scene ext_library_day with dspr
    "The way to the library was uneventful."
    if el_and_mz == 1:
        "However, my thoughts were occupied by how I was supposed to get the librarian to go out with the most annoying kid in the camp a.k.a Elektronik."
    scene int_library_day with dissolve
    play ambience ambience_library_day
    play music music_list["two_glasses_of_melancholy"]
    "Once inside the library, I noticed Zhenya peacefully sleeping at her post. "
    show cg d2_micu_lib with dissolve
    lu "Rise and shine, pioneer!"
    "I proclaimed sarcastically, bending down right to her face to say it. She raised her head slightly and gave me a confused look, which quickly changed to annoyance. "
    hide cg with dspr
    show mz angry glasses pioneer close with dspr
    mz "I wasn’t sleeping. You didn’t have to shout. Now, what do you want?"
    lu "Well, someone definitely got off on the wrong foot. I need this go-round sheet signed. "
    mz "Give it here. "
    "She forcefully grabbed it out of my hand, giving me another delightful look."
    if el_and_mz == 1:
        lu "Maybe if you didn’t bark at people like a stray dog, your cavalier would gain the courage to ask you out."
        show mz rage glasses pioneer with dspr
        mz "What cavalier? What is this nonsense?"
        show mz normal glasses pioneer with dspr
        lu "Don’t pretend like you haven’t noticed the attention of our esteemed soviet scientist. "
        mz "Fine, maybe I did notice Sergey looking at me weird… What’s your deal in all this anyway?"
        lu "I’m just trying to help our little Romeo. Give him a chance, you can see he likes you, and I can see that you care. "
        mz "If I think about it, will you leave me alone already?"
        lu "With pleasure."
    else:
        "She quickly signed the paper."
        lu "{i}Absolute pleasure{/i} doing business with you, but I'm afraid I'm short on time."
    "This time I grabbed the sheet out of her hands and left the communist cave of the nicest pioneer in the camp."
    play sound sfx_slam_door_campus
    stop ambience
    play ambience ambience_camp_center_day
    scene ext_library_day with dspr
    $ library_visited = True
    window hide
    stop music fadeout 4
    stop ambience fadeout 2
    if library_visited == True and musical_visited == True and clubs_visited == True and medical_visited == True:
        jump locations_end
    $ disable_current_zone ()
    $ show_map ()
label locations_end:
    window show
    play ambience ambience_camp_center_day
    play music music_list["my_daily_life"] fadein 4
    scene ext_house_of_mt_day with dspr
    "About time to take this thing back to Olga and head to lunch. I went to our hut but found nobody there."
    th "She must’ve gone to the cafeteria already"
    play sound sfx_dinner_horn_processed fadein 1
    "Right on cue, I heard the horn signaling everyone to lunch and I went there without further delay."
    scene ext_dining_hall_away_day with dissolve
    "Once I reached the gourmèt a la Soviet, I saw Olga standing near the entrance. How fortunate. I came up to her."
    scene ext_dining_hall_near_day with dspr
    show mt smile pioneer with dspr
    lu "Hello again. I filled out your errand sheet."
    mt "Hey, good job. Rest of the day you can have for yourself.{w} Business before pleasure! Now onto lunch, forward march!"
    stop ambience
    scene int_dining_hall_people_day with dspr
    play ambience ambience_dining_hall_full
    play sound sfx_open_door_1
    "Only free space was left with our future scientists, so I sat next to them. "
    show sh normal pioneer close at left with dspr
    show el normal pioneer close at right with dspr
    lu "Greetings, gents. Bon Appetit."
    if el_and_mz == 1:
        el "Hello, hello. What was that you said at the end?"
        sh "He wished you a good meal in French. "
        el "Where’d you learn that one?"
    else:
        show el upset pioneer close at right with dspr
        "Electronik gave me a sour look and returned hiz gaze to his food."
        show el normal pioneer close at right with dspr
        sh "Hello again. I could've sworn I heard that last phrase before."
        lu "Curious, where would that be?"
    sh "Some book from the school reading list, I think."
    lu "Let me guess, “War and Peace”?"
    sh "I think that’s it. A large book in a few tomes. Never liked fiction books myself."
    lu "A mistake, to be sure. Literature refines the man, makes him more cultured.{w} What’s the use of a scientist who speaks like a bootblack?"
    el "Your books don’t make any sense. Practical knowledge is much more interesting."
    sh "You can’t study everything using the empirical method. "
    lu "Why not? Though it will take a near infinite amount of time. "
    "This phrase provoked the guys to actively discuss math and physics and at that point I stopped paying attention to the conversation.{w} They didn’t seem to mind, busy in a theoretical argument. Meanwhile, I finished my meal. "
    lu "Riveting conversation, however I must make my leave here. Farewell."
    stop ambience
    scene ext_dining_hall_near_day with dissolve
    play sound sfx_close_door_1
    "I left the lunchroom and thought of where I could go. Going to the forest again seemed like a waste of time, though there was no apparent danger involved. My choice landed on the docks, so I made my way there."
    stop music fadeout 4
    scene ext_boathouse_day with dissolve
    play ambience ambience_boat_station_day
    play music music_list["trapped_in_dreams"]
    play sound sfx_alisa_lighter
    "I walked to the edge of the pier and lit a fag. Thoughts about this place flooded my mind once more. Less than 48 hours passed since my arrival here, yet it seems like much longer. A completely new life, new body, new people."
    "Even if I was acquainted to them through the game beforehand, now they seemed like different, very real people. In these unfinished 2 days more has happened to me than over 2 months in quarantine. "
    th "Least Sovyonok isn’t closed because of it"
    "I could’ve spent much longer looking at the waves and thinking, when I decided to shake off the ash from the tip of my cig.{w} Gently tapping the filter with my thumb I knocked off the ash and watched it fly to the ground. The ground which it never hit. "
    stop ambience fadeout 2
    th "What the..?"
    stop music fadeout 4
    play music music_list["just_think"]
    "The smoke also stayed mid-air, just like the waves became static. I looked around. Behind me a tall dark person in a strange robe was standing on the dock. "
    show amen with dspr
    dreamgirl "Your return to Hell was requested."
    lu "And you must be…?"
    dreamgirl "Have you really forgotten your brother in your prolonged exile? No, you would never forget."
    "Fragments of the movie series dashed in my mind."
    th "What was your name? A… Am… Right, Amenadiel"
    lu "Bad time for jokes? You always enjoyed them before, Amenadiel."
    amen "Maybe I did treat them with leniency, but your father won’t appreciate the humor. You left your throne in Hell to play pioneer here?"
    lu "My destiny was always my own and I couldn’t care less what plans dear Dad has for us. I’ll stay here as long as I want if I wish it. "
    amen "Color yourself warned, Lucifer. Father doesn’t like waiting. I hope we won’t have to have this conversation again. "
    hide amen with dspr
    play sound sfx_wind_gust
    "A set of large grey wings opened behind Amenadiel’s back. One flap and he was gone. The ash from my cigarette dropped right on my shoe. "
    lu "Oh Devil! Right, that’s me."
    "I wiped the ash off my shoe and threw the cig into the nearest bush, stubbing it first. I walked off from the damned pier in a low mood. "
    stop music fadeout 4
    "I decided to waste some time in my hut."
    scene ext_house_of_mt_day with dissolve
    "Once there, I plopped into the deck chair next to the hut. I reflectively took my phone out, but once I saw no cellular signal or Wi-Fi to be found, the factual reality hit me once more.{w} There was no internet now nor will be any time soon. I stuffed the phone back in my pocket and went for a nap."
    show blink
    $ renpy.pause (1)
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    "A slight push on the shoulder woke me up. " with hpunch
    show unblink
    scene ext_house_of_mt_sunset with dissolve
    show dv smile pioneer2 with dissolve
    play music music_list["timid_girl"] fadein 4
    play ambience ambience_camp_center_day
    dv "What do you think you’re doing here?"
    lu "Taking a nap. What does it look like? It’s my hut, after all."
    dv "Get up, you’ll miss dinner."
    lu "Is it that time already?"
    play sound sfx_dinner_horn_processed
    "My question was answered by the hollering horn. "
    "I stretched, cracked my back, got up and went to dinner with Alisa."
    scene ext_dining_hall_away_sunset with dissolve
    show dv smile pioneer2 at right with dspr
    dv "I hope you remember we have plans today."
    lu "How could I if I were the one who planned it?"
    dv "Who knows what you have in that head of yours. You could’ve just said that to raise my mood back then."
    lu "I don’t say anything without reason. If I promised you, we’d go out today, then we’ll go out today.{w} I am a devil of my word, after all."
    dv "Good on you then. But what’s the thing with the devil all the time? No other role models in the vicinity?"
    lu "So, you don’t believe me? I {b}am{/b} the Devil. And I say only the truth. Point of pride, actually."
    "Alisa chuckled."
    show dv laugh pioneer2 at right with dspr
    dv "You can tell your fantasies to Ulyana, maybe she’ll bite. I won’t believe a word without proof. "
    scene ext_dining_hall_near_sunset with dissolve
    show dv laugh pioneer2 at right with dspr
    "By now we reached the cafeteria. "
    lu "You’ll get your proof. We have plenty of time after dinner. "
    dv "A bit of intrigue, huh? Let’s go eat already or there won’t be any seats left. "
    stop music fadeout 4
    stop ambience fadeout 2
    play sound sfx_open_door_1
    scene int_dining_hall_people_day with dissolve
    play sound ambience_dining_hall_full
    show us normal pioneer far at left with dspr
    play music music_list["i_want_to_play"] fadein 4
    "We entered the building and there were, in fact, only a few seats left. Ulyana waved at us from one of the remaining tables. We grabbed our portions of buckwheat with beef and walked over to her. "
    show us normal pioneer close at left with dspr
    show dv normal pioneer2 close at right with dspr
    us "Bon Appetit!"
    lu "No bugs this time?"
    us "You caught me both last times, why would I try my luck again?"
    lu "Children often do illogical things. "
    show us dontlike pioneer close at left with dspr
    show dv smile pioneer2 close at right with dspr
    "Ulyana showed me her tongue and continued eating. Alisa smiled."
    "Alisa whispered into my ear:"
    dv "You have to show me how you find out about all her tricks later."
    "I looked her in the eyes, smiled and nodded. We ate slowly, just how I liked it. Soon people started leaving the lunchroom. "
    stop music fadeout 4
    show el normal pioneer close at fright with dissolve
    "Ulyana was also about to run off, when Elektronik came up to our table. "
    el "Guys, don’t leave after dinner, I thought up a new card game. Our whole cohort can play. "
    "Alisa and I exchanged looks. That meant our plans for the evening were either cancelled or delayed for an unknown time.{w} We couldn’t leave together when everyone was present. I nodded to Elektronik for the both of us. "
    hide el with moveoutright
    "Once I was done with my food, I decided to go out for some air."
    hide dv with dspr
    hide us with dspr
    show el smile pioneer at right with dissolve
    "Elektronik stopped me at the exit. "
    el "Hey, uh, could you get us the playing cards from the counselor? She doesn’t trust them to me since last time…"
    show mt normal pioneer at fleft with dspr
    show sl normal pioneer at left with dspr
    "I was about to complain when Olga Dmitriyevna and Slavya came up to us. "
    el "Olga Dmitriyevna! Me and Lucifer thought up a new card game. Can we take the decks and play as a cohort?"
    mt "If Lucifer’s on board then alright. Go and grab them from my hut. "
    "I couldn’t even get a word in. Now I can’t say no. "
    th "When did I become the counselor’s trusted pioneer?"
    lu "Slavya, will you join me on this trip?"
    sl "Sure, let’s go. "
    play sound sfx_close_door_1
    scene bg ext_square_sunset with dissolve
    show sl normal pioneer at right with dspr
    play music music_list["get_to_know_me_better"]
    "We walked about half-way to the hut, when Slavya said:"
    sl "Wait, I remembered that the cards were in my hut. Last time Olga took them from Sergey and game them to me for safekeeping. "
    th "Well what do you know? And I thought we’d have to go all the way to Olga’s hut to find out"
    lu "Okay, let’s go to your place."
    show sl shy pioneer at right with dspr
    $ renpy.pause (1)
    show sl normal pioneer at right with dspr
    "Slavya blushed ever so slightly, understanding the innuendo. Up next we made our way to her hut. "
    scene bg ext_houses_sunset with dissolve
    "Once there, she jumped in to grab the cards, without inviting me with her. I waited outside for her return. "
    lu "And I thought you’d invite me inside. Anyway, let’s go."
    "I said with a sly smile. "
    show sl shy pioneer at right with dspr
    $ renpy.pause (1)
    show sl normal pioneer at right with dspr
    "Slavya blushed once more and then shortly said"
    sl "Let’s go. "
    stop music fadeout 4
    scene bg int_dining_hall_sunset with dissolve
    play music music_list["afterword"] fadein 4
    "Soon we were back at the lunchroom. Inside I saw a large plaque with all our names on it in a bracket of our improvised tournament."
    show cg lvl_1 with dissolve
    lu "Can we start now? "
    hide cg with dspr
    show el normal pioneer with dspr
    el "Not everyone’s here yet. Zhenya’s missing. "
    show el normal pioneer close with dspr
    "I came up to him and lowered my voice."
    lu "Then go and get her, Romeo. And ask her out while you’re at it."
    show el grin pioneer close with dspr
    el "I- I can’t I’m the organizer, I can’t leave. "
    if el_and_mz == 1:
        lu "Oh, and I can see you’re terribly busy with all this organizational work. Go and get her, I already had my talk with her about you."
        el "Really? How’d it go? What’d she say?"
        lu "That she’ll think about it. Now go and don’t mess it up."
        el "Okay then, I’m going."
        hide el with moveoutright
        $ renpy.pause (1)
        show el smile pioneer at left with dissolve
        show mz normal pioneer at right with dissolve
        "In a few minutes, our not-so-failed romantic returned, with his beloved in tow. He was putting in an effort to hide how happy he was. Zhenya didn’t seem to share his enthusiasm. "
    else:
        show el normal pioneer with dspr
        lu "Oh, and I can see you’re terribly busy with all this organizational work. Go and get her, save us both some time."
        el "No way, she won't come if I call her. You go."
        lu "Some bloody organizer you turned out to be. Can't get the cards, can't get everyone together. Then what purpose do you even serve in all this?"
        show el angry pioneer with dspr
        el "Look, I know it didn't turn out perfectly. Just please go get her, everyone’s waiting."
        lu "I will do this for you, and in return you will owe me a favor. To be redeemed later, of course."
        el "Fine, whatever. Go already."
        "I was about to head out, when Zhenya walked into the lunchroom via the front door, relieving me from the extra errand."
        play sound sfx_close_door_1
        show mz normal pioneer at right with dissolve
        show el surprise pioneer at left with move
        mz "Let's get this dumb game over with."
    el "Okay, everyone! Let’s begin. The rules go like this…"
    "Up next he started explaining the rules to a game I was far too familiar with. I looked at the plaque and deduced that my first opponent was Lena. I went up to her table sat across from her. "
    hide el with dspr
    hide mz with dspr
    show un shy pioneer with dissolve
    lu "Good luck. "
    un "Thanks. "
    scene black with dspr
    $ renpy.pause (1)
    scene bg int_dining_hall_sunset with dspr
    show un sad pioneer with dspr
    "The game ended as quickly as it began. If you had good combos from the start you could just defend all game and win."
    "Lena lost the game and with that her mood. Her world-famous expression of sorrow was clear-cut on her lowered face.{w} Maybe there was something deep down in me which empathized with her, but it was extremely hard to make me sad because of others’ misfortune. Especially when the reason was so trivial. "
    lu "Don’t take it too hard. There are eight players but only one winner."
    hide un with moveoutleft
    stop music fadeout 4
    show cg lvl_2_semen_win with dissolve
    "I went back to the plaque to see some updated info. My next opponent was Ulyana. I sat at her table. "
    hide cg with dspr
    play music music_list["i_want_to_play"] fadein 3
    show us smile pioneer with dspr
    lu "Before you suggest anything, no, I won’t play by any other rules and no, I won’t go easy on you. No replays either. Got it?"
    "I flashed my eyes at her and she became visibly uneasy."
    show us normal pioneer with dspr
    us "But how did you- Fine…"
    scene black with dspr
    $ renpy.pause (1)
    scene bg int_dining_hall_sunset with dspr
    show us dontlike pioneer with dspr
    "Winning against her by the normal rules didn’t present a challenge. The girl frowned and ran out of the cafeteria. "
    stop music fadeout 3
    hide us with moveoutright
    "My next opponent was, of course, Alisa. I came back to the table I recently ate at. Seems she never changed places. "
    play music music_list["always_ready"] fadein 3
    show dv smile pioneer2 with dissolve
    lu "And so, there were two. You ready to congratulate me during our evening walk?"
    dv "We’ll see who’s gonna congratulate who. "
    "The game began. Alisa was indeed a much more serious opponent than the other two. However, a few fortunate cards and the game went my way with ease. These games really are decided by luck of the draw. "
    th "If my friends ever saw this game, I’d be flamed next weeklong for holding so many aces"
    show dv angry pioneer2 with dspr
    dv "Lucky bastard!"
    lu "I have the Devil’s own luck."
    stop music fadeout 3
    "I playfully smiled at my opponent. Alisa was obviously not amused by the results of the game. Seems like she wanted to show me up in front of the others.{w} Everyone else congratulated me, after which I exited the building and waited for the redhead."
    scene bg ext_dining_hall_near_sunset with dissolve
    "Pioneers slowly dispersed from the lunchroom. Alisa didn’t make me wait too long."
    show dv normal pioneer with dspr
    lu "Shall we go?"
    dv "Let’s go, champion."
    "Her mood was slightly better than after the loss."
    "We made our way from the cafeteria to the plaza. From there, just as is canon for evening walks, we went in random directions, without a final destination."
    $ persistent.sprite_time = 'night'
    $ night_time()
    scene bg ext_square_night with dissolve
    play sound ambience_camp_center_night
    play music music_list["dance_of_fireflies"]
    show dv normal pioneer with dspr
    dv "You know, I thought you’d go easy on Ulyana. She’s just a kid, after all."
    lu "Never liked human offspring. Small, annoying, loud. Why would I go easy on something like that?"
    dv "I don’t like kids myself either. But Ulyana’s an exception. We’ve gotten really close.{w} It’s like she’s the only person who understands or supports me."
    scene bg ext_playground_night with dissolve
    show dv normal pioneer with dspr
    lu "I could say that by now she isn’t the {i}only{/i} person."
    show dv smile pioneer with dspr
    dv "Who else would it be?"
    lu "Whaddya think?"
    dv "Oh, I don’t know…"
    lu "Who went to steal sweet buns with you, played the piano for you? Who’s on an evening promenade with you right now?"
    show dv grin pioneer with dspr
    dv "Actually, yeah, who? Weren’t you going to try and prove something to me?"
    lu "So that’s how it’s going to be? Still don’t believe me?"
    dv "Believe you’re the actual Devil? Who in their right mind would believe that?"
    lu "Alright, I’ll give you your proof then."
    "I stopped, she followed suit. I came closer to her and stared into her eyes."
    show dv normal pioneer close with dspr
    lu "Tell me, Alisa, what do you {i}really{/i} desire?"
    play sound lu_desire
    "At first, I thought she gave me the same hypnotized look as everyone else who I tried this on. But something went wrong. She took a step back because of how close I’d gotten to her. "
    show dv smile pioneer with dspr
    dv "Desire? For you to show me your promised proof already. Was that it?"
    lu "Wait, what? That didn’t work on you? You were supposed to reveal your deepest, darkest desires."
    show dv laugh pioneer with dspr
    "Alisa laughed"
    dv "Hah, what was that? Some kind of parlor trick? Trying to make me talk with your stare? You’ll have to think of something more convincing next time. "
    lu "I don’t understand…{w} You must have some kind of resistance."
    dv "Yes, yes, of course I do. You just didn’t think of anything better. Let’s keep going already, little devil. "
    "We went on, though I still couldn’t figure out how the mojo didn’t work on her. It worked on everyone else I tried it on."
    scene bg ext_library_night with dissolve
    show dv smile pioneer with dspr
    lu "I’ll find a way to prove it to you, just give me time. "
    dv "Please, you can pretend all you want. It spices things up a little, even. Instead of trying so hard, why don’t you come to the stage with me tomorrow?"
    dv "If Miku fixes my damn guitar. And she’ll fix it alright, if she wants to stay unharmed. "
    lu "You’re quire cruel with her. I haven’t even seen her at lunch today. Must be really afraid of you. "
    dv "I asked her to fix that guitar long ago. She just keeps giving false promises and forgetting about it the next day. This can’t go on forever. "
    lu "I’ll come tomorrow. Today though, it’s getting late. About time for us to go our separate ways to not get a juicy reprimand from the counselor."
    dv "Good idea. "
    scene bg ext_square_night with dissolve
    show dv smile pioneer with dspr
    "We came back to the plaza. "
    dv "My way’s right from here. "
    lu "Would the young lady mind if a certain charming prince of darkness accompanies her to her palace?"
    "Alisa chuckled"
    show dv grin pioneer with dspr
    dv "Since you insist, I don’t mind. "
    hide dv with dspr
    show dv grin pioneer close at right with dspr
    "I walked up next to her and extended my elbow, giving a very unsubtle hint. Alisa hesitated at first, but then put her hand around it and we walked towards her hut."
    dv "Don’t think that this is gonna happen regularly or that this means something. "
    lu "Oh, of course not. I’ll just walk you to your hut and that’ll be that."
    dv "That's right."
    scene bg ext_house_of_dv_night with dissolve
    show dv smile pioneer with dspr
    "We made it to her hut, and she let go of my hand. "
    lu "Goodnight."
    dv "Goodnight."
    lu "Perhaps a kiss before parting? – I playfully asked, not expecting anything to come out of it."
    dv "Don’t push it. Go on now."
    scene bg ext_house_of_mt_night with dspr
    "On this note, she entered her hut, and I went back to mine."
    stop music fadeout 4
    stop ambience fadeout 2
    scene bg int_house_of_mt_night with dspr
    play sound sfx_close_door_1
    "Inside my hut Olga was peacefully reading a book on her bed. I decided not to push my boundaries with her, considering the awkward situations that ensue in the morning. I simply undressed, wished her a good night and went to sleep."
    show blink
    play music music_list["trapped_in_dreams"] 
    $ set_mode_nvl()
    "My mind was filled with thoughts of Alisa. By now I’ve spent a decent amount of time with her and she seemed to enjoy my company. Seems that I liked her even with her rough personality. I pondered why my mojo had no effect on her, this might have ruined my authority in her eyes. Luckily, it seemed like she treated it just as a failed joke. I’ll come to her stage tomorrow and we’ll see what happens. "
    "\nThe meeting with my “Brother” also came to mind, though that concerned me much less than my relationship with the redheaded menace. Still, a warning that God himself wants me back in hell makes you a bit uneasy to say the least. Except I’m not the devil they know. Just someone who happens to occupy his body and mind at the moment. I have none of his memories, which makes this even harder. That’s why I physically can’t “return” there if I’ve never been there in the first place. They likely won’t be able to send me there by force, though the dark angel may try. I guess we’ll see what happens. Either way, each day holds something unexpected for me. "
    $ set_mode_adv()
    window hide
    jump devilishadv_day3_en




























