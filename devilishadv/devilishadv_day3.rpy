init:
    
    $ dv_rep = 0

label devilishadv_day3_en:
    $ backdrop = "days"
    $ new_chapter (3, u"Lucifer. Day 3")
    $ persistent.sprite_time = 'day'
    $ day_time()
    window show
    play sound sfx_head_heartbeat
    play music music_list["torture"]
    scene bg ext_polyana_day with dissolve
    show pi smile with flash
    show prologue_dream
    "My dreams were filled with all sorts of tomfoolery once again, flashes before my eyes."
    "The Pioneer with his evil smile. Alisa unconscious."
    play sound evil_laugh
    "His laughing. Sharp pain in my back."
    scene black with dissolve
    hide prologue_dream
    stop music fadeout 2
    show unblink
    play music music_list["my_daily_life"] fadein 4
    scene bg int_house_of_mt_day with dspr
    "I woke up in cold sweat. Or maybe in hot sweat, it is summer after all. The dream slowly faded from memory and the world regained its colors.{w} I looked at my phone, it showed: “It’s five to eight, 40 percent battery”."
    th "Gotta turn on power saving on it, otherwise it won’t last much longer"
    "Olga was already gone from the hut."
    th "The lineup, right"
    "I slowly got dressed, tied the tie around my wrist and made my way to the washbasins, grabbing the soap bag with me."
    play sound ambience_camp_center_day
    scene bg ext_washstand2_day with dissolve
    play sound sfx_open_water_sink
    play sound sfx_water_sink_stream
    "The water was, as usual, freezing.{w} The positive effect was that it washed away any remnants of sleep I might have had. I quickly brushed my teeth with the local tooth powder.{w} Never understood the tendency to brush teeth before breakfast, rather than after, since your teeth get dirty after breakfast too. I’d do it my way, but the camp timetables wouldn’t let me. "
    scene ext_square_day with dissolve
    stop sound
    "I tossed the bag back into my hut and went to the plaza at a fast pace. When I arrived, the lineup was already coming to a close."
    show mt normal pioneer with dissolve
    "I heard Olga mention something about an evening disco and then end the gathering. She came up to me afterwards."
    mt "I decided not to wake you up. Thought you’d get up on your own and be on time. Appears I’ll have to next time. "
    "I wasn’t in the mood for arguments today, so I only nonchalantly raised my right eyebrow in response."
    play sound sfx_dinner_horn_processed
    "The breakfast horn sounded over the camp."
    mt "Alright, go have breakfast. We’ll see to your punishment later."
    lu "Ho-ho, I’m quite an expert in those. I shall be waiting. "
    show mt surprise pioneer with dspr
    stop ambience
    $ renpy.pause(1)
    play sound ambience_dining_hall_full
    scene bg ext_dining_hall_away_day with dissolve
    "Olga became slightly unsettled, our first night must’ve flashed before her eyes. Maybe she did want to respond in some way, but by that time I was already halfway to the cafeteria. "
    scene bg int_dining_hall_people_day with dspr
    "Breakfast was quite nice today, consisting of fried eggs and sausages. I grabbed a portion and sat at an empty table.{w} It was the first time I encountered such a luxury. Perhaps I came earlier this time, or some pioneers just decided not to get out of bed."
    stop ambience
    scene bg ext_dining_hall_near_day with dspr
    play sound ambience_camp_center_day
    play sound sfx_alisa_lighter
    "I finished my food in appropriate time and went outside.{w} Smoking on the porch of the lunchroom after breakfast became a sort of ritual to me at this point. The harm smokes cause people was obvious to me as a human, though I doubt it would have any effect on the Devil."
    "I perused what I’d heard in the morning in my mind. A dance party would happen in the evening. Alisa probably won’t want to attend that, considering we have other plans for the evening. Nonetheless, I’d enjoy a dance with her."
    scene bg ext_square_day with dspr
    "The remaining schedule for the day was a mystery to me, though not one I cared to solve. I aimlessly wandered to the plaza where I plopped down on the nearest bench without a single though of what I’m going to occupy myself with until the evening. "
    th "Never thought this camp could be boring"
    "I might’ve sat there for a longer time if I hadn’t heard the sounds of a guitar vaguely coming from the direction of the stage. "
    $ volume(0.3, "music")
    play music music_list["that_s_our_madhouse"] fadein 4
    th "Did she decide to practice all day long?"
    th "Perhaps if I play with her now, she’ll agree to go dance with me in the evening"
    "I went to the stage without much hesitation. The sounds got increasingly louder as I moved closer to the epicenter."
    scene ext_stage_big_day_7dl with dissolve
    $ volume(0.6, "music")
    "Once I got close enough to see, I noticed a familiar figure on stage. Eyes close, entranced in her own playing, she was performing some composition of her own accord. It was quite impressive. "
    $ volume(1, "music")
    show cg d3_dv_guitar with dspr
    "I used her spatial unawareness to come closer. Once she finished playing, I gave a slow, yet effective clap and smiled at her. "
    scene bg ext_stage_normal_day with dspr
    play sound ambience_camp_center_day
    stop music fadeout 3
    show dv shocked pioneer with dspr
    "She was surprised by my sudden appearance, yet her face regained her arrogant notes almost instantly. "
    show dv grin pioneer with dspr
    dv "So, how’d you like it?"
    lu "If self-preservation instincts tell me anything of value, the correct answer here would be: “Yes, of course”"
    show dv angry pioneer with dspr
    "My over-sarcastic response did not come across well."
    dv "Why’d you even listen then? Should’ve walked straight past."
    lu "Where in my words have you noticed dissatisfaction? You played quite well, honestly. "
    show dv normal pioneer with dspr
    dv "In that case I’d play you something else, but you can wait ‘til evening for that that. "
    lu "Don’t you wanna dance with everyone come evening?"
    show dv angry pioneer with dspr
    dv "Don’t tell me you’re actually considering going to that snooze-fest. We had a plan, remember?"
    lu "I am considering it. Obviously, I’m not a ballet star, though I wouldn’t refuse a good dance once in a while. "
    dv "Do whatever you want. I’m going back here in the evening, whether it’s with you or not."
    hide dv with moveoutleft
    "With those words she grabbed her guitar and stormed off."
    lu "Got it. “Do whatever you want, but if you don’t pick me, you’ll dearly regret it”. You could even call that an ultimatum."
    "I said that out loud and also left the stage premises. "
    scene bg ext_square_day with dissolve
    "It appeared I was still free until lunchtime. In another world I’d just play some games on my PC until duty called once more, though I had no such privilege here."
    scene bg ext_musclub_day with dspr
    "After a quick thought, I decided to go to the musical club and test if I could actually perform in advance. In this case, if Lucifer could perform, I could only do a few simple songs. "
    play sound sfx_open_door_1
    stop ambience
    stop music
    scene bg int_musclub_day with dspr
    play music music_list["so_good_to_be_careless"] fadein 3
    play ambience ambience_music_club_day
    "I came in and found Miku writing something at her desk."
    show mi smile pioneer with dissolve
    lu "Hello, Miku"
    "Miku turned her attention to me. "
    mi "Oh hi, Lucifer! Did you come to play something or just visiting me?"
    lu "Visiting you of course, though I would like to play something too. "
    mi "Aw, how nice of you. I get so lonely here sometimes. What did you wanna play? The piano again or something else?"
    lu "I wanted to try the guitar. Is there one I can use?"
    mi "Yes, yes, of course! There’s one next to the drums, take it!"
    "I grabbed the guitar and sat down on a chair. I needed to practice some soviet rock to not get caught with my pants down in the evening.{w} My fingers fell in the correct spots right away, just like they did with the piano."
    play music kukushka fadein 4
    "[Kukushka by Kino (Guitar cover) plays]"
    "Click past this message to stop the music"
    stop music fadeout 2
    "Once I finished, Miku clapped her hands."
    th "If Alisa comes in right now, it’ll be a real case of Déjà vu"
    mi "You know how to play Tsoi’s songs? He’s one of my favorite singers! And Alisa likes him too."
    th "Now that’s some useful info"
    lu "Listen, weird question, is he still alive? I haven’t been in touch with the news of late."
    mi "Who? Tsoi? Tsoi is alive! I hope releases many more songs with his group. "
    lu "So do I…"
    "I spent some more time playing the guitar, singing atimes, Miku singing along too. Our musical noon was interrupted by the lunchtime horn."
    play sound sfx_dinner_horn_processed
    mi "Yay, lunchtime! I’m so hungry. Overslept breakfast today."
    th "There’s one of the reasons I was able to find a completely free table today. "
    lu "Let us go then, hungry geisha. "
    show mi laugh pioneer with dspr
    "Miku chuckled at the mention of her culture."
    show mi smile pioneer with dspr
    mi "Yes, let’s go faster."
    stop ambience
    scene bg ext_dining_hall_away_day with dissolve
    "We left the musical club and went to the cafeteria. On the way Miku kept yammering on all sorts of useless topics, but I wasn’t really paying attention."
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full
    show mi normal pioneer close at left
    "Once inside, we occupied a free table, the amount of which were quickly diminishing. Soon Lena came up to our table. "
    show un normal pioneer at right with dspr
    un "Can I sit here? All the other tables are so full… "
    "She spoke with a cute, saddened expression."
    mi "Sure, Lucifer and I aren’t opposed to it. I mean, I’m not, but I don’t think Lucifer is either."
    lu "Miku, don’t choke on your words. I have nothing against it, please sit."
    show un smile pioneer close at right with dspr
    "Lena sat down and we began our food consumption. While eating I noticed Lena’s gaze on me a few times, though I made it look like I haven’t noticed to not make her uncomfortable.{w} The sight of her reminded me that she owed me a favor I have yet to redeem. "
    scene ext_dining_hall_near_rain_7dl with dissolve #had bg infront, didn't work
    stop ambience
    play music music_list["raindrops"] fadein 4
    play ambience ambience_rain_7dl
    "Sometime later, once lunch was over and done with, I left the cafeteria and was about to go for another walk. Possible locations included the forest or even the old campgrounds. My plans were ruined by the ominous-looking rainclouds in the sky."
    scene ext_house_of_mt_rain_7dl with dissolve
    "Thunder boomed and I quickly made my way back to my hut, catching a few raindrops on my skin before going inside. The weather was worsening by the minute. From the hut window I could see it raining cats and dogs outside. "
    scene bg int_house_of_mt_day with dissolve
    "In my swift entrance I haven’t even noticed Olga inside the hut. "
    show mt surprise pioneer with dspr
    mt "Is that rain? If it keeps going, we’ll have to cancel the dance party!"
    "She said looking out the same window I did. "
    lu "I too, hope it’ll end before dinner. "
    show mt normal pioneer with dspr
    mt "In that case we won’t have time to prepare the plaza."
    lu "Then start preparing a bit later. We just need the rain to end. "
    mt "If we start later it’ll be cutting it too close to the curfew. "
    lu "Then delay the curfew. I’m sure the pioneers would appreciate it, if anything. "
    mt "What about the rules and day plan? If we delay the curfew nobody will wake up in time for the morning lineup. "
    lu "Olga Dmitriyevna, what is it with you? You’re acting like a kid. Move the lineup too, nothing much happens before lunch anyway. "
    mt "I’ll think about it. Oh god, why did it have to rain today?"
    lu "I can assure you; He is nothing meteorological. By the way, rain is the best time for tea, wouldn’t you say?"
    show mt smile pioneer with dspr
    mt "Good idea. I’ll heat up the kettle. "
    mt "Oh, I think I’ve run out of matches."
    "The small hob that the kettle was on couldn’t be lit up without matches. "
    lu "Let me try something."
    hide mt with moveoutleft
    play sound sfx_ignite_torch
    "Olga stepped back from the hob and I came closer to it. A strange craving for putting my fingers next to it overcame me. I poked at it with one and to my surprise, the finger lit up with a red flame. What surprised me even more is that I felt no pain from it. I turned on the gas and the hob lit up. I dragged my finger away from it and the flame dampened. "
    th "Could’ve just pulled out my lighter"
    show mt surprise pioneer with dspr
    mt "How did you light it?"
    lu "I’m the Devil, I can do a lot of things."
    "Olga gave me a questioning look. I sighed and pulled out the lighter from my pocket and waved it at her. "
    show mt normal pioneer with dspr
    mt "Should’ve just said you had a lighter."
    "Of course, I didn’t light the hob with the lighter, but shocking the counselor with fiery fingers and then explaining my whole story to her seemed rather unwise."
    "The tea boiled and soon we were already talking about something insignificant and eating gingerbread. "
    "While finishing my tea I looked out the window where the rain was barely drizzling as opposed to the near hailstorm that was going on before. Seems the disco will happen after all."
    show blink
    stop music fadeout 4
    "I laid down on the bed and closed my eyes for the nearest hour."
    stop ambience
    hide mt with dspr
    play sound sfx_dinner_horn_processed
    show unblink
    play music music_list["sweet_darkness"] fadein 4
    "The dinner horn awoke me from my slumber. Olga was nowhere to be found in the hut. Must’ve left to make sure everything is ready for the evening."
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    scene ext_house_of_mt_sunset with dissolve
    "I left the hut and felt a chilly wind on my skin. "
    scene int_dining_hall_people_day with dissolve
    "I made my way over to the cafeteria carefully sidestepping around puddles. Once inside, I grabbed my food and headed to a free table." 
    show sl smile pioneer with dspr
    "Soon Slavya joined me at it."
    sl "You mind if I sit here?"
    lu "‘Course not. "
    show sl smile pioneer close with dspr
    "For some time, we ate in silence, which I decided to break soon enough."
    lu "So, is the disco happening? Got everything prepped in time?"
    sl "It’s happening alright, just might start a bit later. We didn’t have time to finish up with the setup. We’ll continue after dinner. Wanna lend us a hand?"
    lu "I’d be happy to, but I’ve got some business of my own after dinner. Sorry about that."
    sl "That’s alright, I’ll ask the guys from cybernetics. "
    scene int_house_of_mt_day with dissolve
    "Once I finished my food, I headed over to my hut where I threw on my blazer. The tie on my wrist no longer looked appealing in the bigger picture, so I stuffed it in the outside pocket of my blazer, making an improvised handkerchief.  "
    $ persistent.sprite_time = 'night'
    $ night_time()
    scene ext_stage_big_night with dissolve
    "I came to the stage and noticed that Alisa was late."
    th "Typical"
    scene ext_stage_normal_night with dspr
    play ambience ambience_camp_center_night
    "I climbed the stage to see where we could sit, once she was here. The wooden flooring was soaked after the rain. Our sit-down with the guitar might end here and now because of this. However, I remembered my burning fingers from teatime today. It’s as if a light bulb lit up in my head, forming the most cliché image imaginable. "
    "I put my hand next to the planks and tried to imitate the feelings I had when I’ve done this before. At first, nothing happened. Although after a few attempts my finger lit up, after which I pushed harder and my whole palm was suddenly in flames."
    play sound sfx_ignite_torch
    "I pressed my palm down against the wet planks and it dried them in a matter of seconds, even leaving a slightly burned tint. After drying enough room for about two people I sat down on the warm wood and hung my feet down from the stage, awaiting my evening companion. "
    show dv normal pioneer far at right with dissolve
    "Soon Alisa appeared with her guitar. "
    show dv grin pioneer with move
    "She came closer and said"
    dv "You came, after all. What about that disco you wanted to attend so badly?"
    lu "First some good music, then a dance. – I replied, smiling at her."
    dv "Not afraid of the rain?"
    lu "What’s there to fear? Water is all. "
    show dv grin pioneer close with dspr
    "She climbed the stage and sat next to me on the dried spot. "
    lu "So, gonna show me a master-class performance?"
    dv "Watch and learn!"
    play music music_list["that_s_our_madhouse"] fadein 2
    "She once again played her song, which seemed to be the only one in her arsenal. The melody wasn’t incredibly complicated, though it was quite energetic. The girl seemed to give it her all. "
    stop music fadeout 4
    dv "How was it?"
    lu "Impeccable, just like during the day. You compose this yourself?"
    dv "Sure did! Now it’s your turn."
    "She handed me the guitar."
    lu "What do you want me to play?"
    "Whatever you can. Or try to repeat mine. "
    menu:
        "Try to repeat her song":
            $ dv_rep +=1
            play music music_list["that_s_our_madhouse"] fadein 2
            "I tried to repeat her melody, though it was far from perfect. "
            stop music fadeout 4
            dv "You’ve got a long way to go until my level."
            lu "Let me play something I know instead. "
            dv "Alight then, surprise me. "
        "Play your own":
            lu "I think I'll stick to something I know well"
            dv "Alight then, surprise me. "
            $ dv_rep = 0
    show d3_lu_and_dv with dspr
    play music solntse fadein 2
    "[Zvezda po imeni Solntse by Kino plays]"
    "When I started to play Tsoi, Alisa was, in fact, very surprised. She started speaking only a short pause after I finished playing."
    stop music fadeout 4
    $ renpy.pause (1)
    dv "Well, you sure did what I asked for. Never expected you to play Tsoi. I thought you only liked foreign music."
    lu "Foreign music is nice, but Tsoi, Tsoi is a legend."
    dv "Yeah… That’s for certain."
    "We kept playing songs from Russian classics, sometimes foreign too. "
    play music hey_jude fadein 2
    "[Hey Jude by The Beatles plays]"
    "The atmosphere became quite relaxing and to my liking when I noticed Alisa shivering. As I noticed earlier, it was chilly out."
    stop music fadeout 4
    th "Ooh, it got a wee bit chilly out, so I set me forge on fire, roasted some wieners. Whaddya think happened ya dimwit?"
    hide dv with dspr
    hide d3_lu_and_dv with dissolve
    show dv smile pioneer with dspr
    play music yes_i_do fadein 4
    "I took off my blazer and threw it over Alisa’s shoulders. "
    lu "This better?"
    show dv shy pioneer with dspr
    dv "Y-yes, thanks."
    show dv shy pioneer close with dspr
    "I pulled her closer to me by wrapping one hand around her."
    lu "And how about now?"
    "She wanted to push away at first but then decided not to."
    dv "That’s alright too."
    "We sat there in silence for a minute, after which she spoke."
    dv "Listen, why are you here, with me? You could’ve gone to the dance party and had you dance with any of the other girls."
    lu "Because you mean something to me. Because you’d wait for me here. Because I want to be with you, for Dad’s sake. "
    show dv cry pioneer close with dspr
    "Tears glistened in her amber eyes. "
    dv "Really? You think I’m no worse than the others?"
    lu "I’d say even better, but that would feed your ego too much. "
    "I said with a genuine smile. "
    dv "Idiot!"
    "As she said that, she pressed her lips against mine and we came together in a paradisiacal kiss, which I couldn’t put on words even if I so desired. When we finally ran out of breath we came apart and kept sitting in each other’s embrace."
    lu "You know, we can still make it to the slow dance at the end of the party. You wanna go?"
    show dv shy pioneer close with dspr
    dv "But they’ll see us there… together. "
    lu "Should we care about that? The most important thing is that we’re happy and I couldn’t care less what others think."
    dv "If you think so, then let’s go. "
    stop music fadeout 4
    "I jumped down from the stage pushing myself off with my hands and held out a hand for Alisa to follow suit. When I was pushing off, I felt a strange feeling in my hand.{w} Could it be… pain?{w} And yes, it was. I scraped my hand on a rusty nail when jumping down. A drip of blood trickled down my palm."
    show dv surprise pioneer with dspr
    "I stopped for a second, examining it, clearly confused. Alisa noticed that."
    dv "Did you hurt yourself?"
    lu "Huh? Yes, a little. Nothing much, don’t worry. "
    "I grabbed her hand with my other arm, and we made our way towards the plaza, where music was still playing. It was about curfew time, but it seems Olga listened to my advice and moved it to give the pioneers some more time to have fun. "
    play music music_list["waltz_of_doubts"] fadein 4
    scene ext_square_night_party with dissolve
    show dv smile pioneer close with dissolve
    "We arrived just in time for the slow dance rounding off the party. Alisa was slightly standing out from the crowd, since she came in her regular uniform rather than a fancy dress. It didn’t bother us in the slightest."
    "I put one hand around her waist and grabbed her hand with the other. We slowly moved in a romantic dance and I felt the stares of pioneers on us. No judging stares could ruin this moment for us. "
    if el_and_mz == 1:
        "Somewhere in the crowd I noticed Elektronik dancing with Zhenya."
        th "Good job, boy. Now I’m not the only one with a pair tonight"
    else:
        "I noticed Electronik shyly standing at the edge of the plaza, looking at Zhenya."
        "She, on the other hand, wasn't looking even remotely in his direction."
        th "Poor kid, maybe he'll find his happiness one day."
    "At the end of the song I let go of Alisa’s hand and ran my hand across her chin and cheek. I looked into her eyes, as she smiled, with genuine happiness. "
    stop music fadeout 2
    play ambience ambience_medium_crowd_outdoors
    hide dv with dspr
    show dv angry pioneer at right with dspr
    show mt angry pioneer at left with dspr
    "The evening would’ve passed perfectly if not for Olga coming up to us after the dance."
    mt "And where were you lovebirds during the party, huh?"
    lu "At the stage, playing guitar. "
    mt "What about the disco? You were absent all evening and you didn’t even warn me.{w} Dvachevskaya, it was you who dragged Lucifer there, wasn’t it? "
    "Alisa was about to say something, but I spoke first. "
    lu "Don’t overdramatize things, Olga. Nothing happened to us for one and we came here by the end, didn’t we? No need to blame Alisa for anything. "
    mt "Fine, I’ll let you two off this time, but do warn me next time you want to pull something like this, or else!"
    lu "Yes, yes, of course. And now excuse us, everyone’s leaving and so are we. "
    hide mt with moveoutleft
    stop ambience fadeout 2
    play ambience ambience_camp_center_night
    show dv normal pioneer with dspr
    "We moved away from the counselor who was still trying to say something at our backs. "
    dv "Thanks for defending me back there. She only ever sees the worst in me."
    show dv shy pioneer with dspr
    lu "No need. We’re together now and we’ll solve these issues together. I won’t let you in harm’s way."
    "She blushed and didn’t reply. We walked to her hut in silence."
    scene ext_house_of_dv_night with dissolve
    show dv smile pioneer with dspr
    "On the porch she gave me back my blazer. Her face expressed true happiness and I shared that feeling with her. "
    dv "See you tomorrow, Lucey!"
    hide dv with dspr
    play sound sfx_close_door_1
    "She gave me a quick hug and ran into her hut."
    "I swung my blazer over my shoulder and contently walked back to my hut. The only thing that worried me was that I got hurt by some random nail in the flooring. Before today I felt myself completely invulnerable. "
    scene ext_house_of_mt_night with dissolve
    play sound sfx_punch_medium
    "Closer to my hut I decided to try hurting myself, so I hit a tree with my fist, expecting to spill some blood. Nothing of the sort happened. I felt no pain once again. "
    th "What is it that causes my vulnerability. I doubt it’s that nail in particular"
    stop ambience
    scene int_house_of_mt_night with dspr
    "I came into the hut, undressed and fell in bed. The day was eventful, to say the least. "
    show blink
    "All my thoughts were occupied by Alisa. With pleasant memories of the evening I drifted off to sleep."
    window hide
    jump devilishadv_day4_en

























