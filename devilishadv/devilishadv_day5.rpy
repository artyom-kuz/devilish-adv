init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # центральная позиция
                self.dist = dist    # максимальное расстояние, в пикселях, от начальной точки
                self.child = child
                
            def __call__(self, t, sizes):
                # Число с плавающей точкой в целое число... превращает числа с плавающей точкой
                # в целые.      
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#

label devilishadv_day5_en:
    $ backdrop = "dv"
    $ new_chapter (5, u"Lucifer. Day 5")
    $ persistent.sprite_time = 'night'
    $ night_time()
    window show
    play music music_list ["a_promise_from_distant_days"] fadein 4
    show d3_lu_and_dv with dissolve
    show prologue_dream
    "Today I dreamt of what happened a few days back. Alisa, the guitar, a dance party."
    scene bg ext_square_night_party with dissolve
    show dv smile pioneer close with dissolve
    show prologue_dream
    "Maybe these dreams do have some meaning? Yet things that have already come to pass haven’t visited my dreams before."
    stop music fadeout 2
    $ persistent.sprite_time = 'day'
    $ day_time()
    scene bg int_house_of_dv_day with dissolve
    show unblink
    play ambience ambience_int_cabin_day
    play music music_list["take_me_beautifully"] fadein 2
    "I woke up with a feeling of immense dehydration. The realization that we only drank whiskey yesterday hit me."
    "My first thought was to get up, but even here there was a nuance. My hand was pinned down by Alisa, who was peacefully dreaming next to me."
    th "What a day yesterday turned out to be. What’s the time? Surely, it’s not early morning – that’s when we went to sleep"
    "Getting my phone to check the time was also an impossible task, due to my pants being far out of reach. I just laid there, thinking of how to possibly get up without waking up my significant other. The thirst only increased. "
    play sound sfx_dinner_horn_processed
    "My savior came from an unexpected place. A horn sounded over the camp, calling everyone to what I presumed was lunch. Alisa winced and slightly opened her stunning amber eyes."
    show cg epilogue_uv_dv with dissolve
    dv "Is it breakfast already?"
    "I kissed her and then said"
    lu "More like lunch, sleepyhead. "
    stop music fadeout 1
    hide cg
    play music music_list["awakening_power"] fadein 1
    show dv shocked pioneer2 close with hpunch
    play sound sfx_bed_squeak1
    dv "Lunch?! What are we gonna tell the counselor about where we’ve been half the day?"
    lu "You worry too much. We’ll think of something. But it is time to get up."
    "She got up and freed my hand from its imprisonment, after which we started picking up our clothes from different parts of the hut. While dressing I made a few glances at my beauty in the nude."
    dv "You’ll have ample opportunity to stare later. Now, however, we might not make it to lunch at this rate."
    lu "Fine, fine. But I’ll quote you on that."
    stop ambience
    scene bg ext_dining_hall_near_day with dissolve
    "We quickly finished dressing and walked to the cafeteria at a fast pace. Speaking of the {i}Me{/i}, Olga greeted us at the entrance."
    show mt angry pioneer with dspr
    show dv normal pioneer2 at fright with dspr
    mt "Where were you all morning? You skipped the lineup, breakfast and everything else! I’m not even going to ask where you were at night.{w} You’re lucky the camp is facing more important issues at the moment: Shurik is missing. "
    lu "Don’t you love it when you get a myriad of problems dropped on your head the moment you wake up?{w} We haven’t seen Shurik, referencing that you know all about where we’ve been and how. May we go eat now?"
    mt "Yes, you may. Right after that you are expected to join the search efforts around the camp. "
    lu "Sir, yes, sir!"
    "I made the silliest salute possible. Olga rolled her eyes and went into the building after us."
    stop music fadeout 2
    scene bg int_dining_hall_people_day with dspr
    play music music_list["you_won_t_let_me_down"] fadein 2
    play sound sfx_close_door_1
    play ambience ambience_dining_hall_full
    show dv smile pioneer2 close with dspr
    dv "Soon you’ll be on top of her most wanted list instead of me. The arrogance with which you respond to her is one to envy."
    lu "Watch and learn, while you have the chance."
    dv "Stop lollygagging, I just don’t want to draw too much attention to myself. I get enough of it as is."
    lu "Alright, we can be exemplary pioneers after lunch and join the search party. Find our dearest scientist. "
    dv "That’s good, we can use that to collect ingredients."
    lu "What ingredients?"
    dv "I wanted to put on an explosive show long ago. Thought of making a bomb to blow up Genda."
    lu "Helping the camp find a lost pioneer on one hand, planting explosives under a statue of a party member on the other. You don’t get much more hypocritical than that."
    show dv angry pioneer2 close with dspr
    dv "If you don’t wanna help, I’ll do it myself!"
    lu "Never said I was against it. We’ll have to divide and conquer though, to make it look less suspicious. And getting the ingredients should go faster."
    show dv smile pioneer2 close with dspr
    dv "Good. In that case, get some activated carbon. I’ll get the rest."
    lu "A trip to the medical center? Easy as pie. The local nurse and I have quite warm relations."
    show dv angry pioneer2 close with dspr
    dv "What was that about relations? You had something with her?"
    lu "Bloody hell, should not have mentioned that."
    dv "Talk, or else you’ll get a whole new reason to go to the medical center."
    lu "Let’s say we had a very {i}detailed{/i} medical inspection of each other on my second day here. "
    play sound sfx_face_slap
    "A very much expected slap in the face flew my way." with hpunch
    show dv rage pioneer2 close with dspr
    lu "Ouch, we weren’t even dating back then."
    dv "Asked me out for the evening at the musical club and had fun with the nurse all in the same morning? How productive of you. And with a far outlook, collecting spare choices if it doesn’t work out with one. "
    lu "Alisa, it’s not like that at all, you don’t understand…"
    dv "I understood all I needed to."
    hide dv with moveoutright
    "She ran out of the lunchroom, her face expressing something between bloodthirsty rage and sadness on a universal scale. "
    th "You’re really in for it now, playboy"
    play sound sfx_punch_washstand
    "I hit the table with my fist, which almost broke from the impact. The situation that transpired was spectated by the whole camp, it seemed. "
    stop ambience
    scene bg ext_dining_hall_near_day with dspr
    play sound sfx_close_door_1
    $ renpy.pause(1)
    play sound sfx_alisa_lighter
    "I left my unfinished food on the table and left the building. I lit a fag on the porch to cool off. "
    th "Me and my big mouth"
    scene bg ext_musclub_day with dissolve
    "Once I finished the cigarette, I went over to the musical club. I knocked as I entered. "
    play sound sfx_knock_door2
    play sound sfx_open_door_1
    scene bg int_musclub_day with dspr
    show mi smile pioneer with dspr
    mi "Hi, Lucifer. How are you? Here to play?"
    lu "Not in the mood, Miku."
    "I passed by Miku and sat at the piano."
    hide mi with dspr
    show mi sad pioneer at right with dspr
    show lu_piano with dspr
    "[Creep - Radiohead (Lucifer cover) plays]"
    play music creep
    "While I played, Miku silently watched as I played, pacing from one end of the room to the other, not finding a place for herself. "
    "[Click past here to end the song]"
    stop music fadeout 2
    "When the song ended, a dead silence filled the room. This could’ve gone on for a while, until Miku decided to speak up. "
    play ambience ambience_music_club_day
    hide lu_piano with dspr
    mi "Did something happen between you and Alisa?"
    "I responded with a slight delay."
    lu "Yes, you could say that. I did something earlier that I now regret. As a result, I’m guilty before Alisa."
    mi "And how are you going to atone for that guilt?"
    lu "I don’t know, Miku. I really don’t know."
    mi "You should try flowers. I’m always happy when someone gives me flowers. I think Alisa would like it too."
    lu "If only it were so simple…{w} Thanks for the tip, though, I’ll give it a shot. Do you know what kind of flowers she likes?"
    mi "I have no idea; we only ever talk about music with her. Try Lena, she knows her since childhood, so she ought to know. "
    lu "Lena? Right. Then I best go and find her. Thanks again, Miku."
    show mi smile pioneer with dspr
    mi "You’re welcome, come play anytime!"
    stop ambience
    play music music_list["meet_me_there"] fadein 4
    "Fortunately, Lena still owed me a favor. I left the musical club and started my search for her around the camp. "
    scene bg ext_square_day with dspr
    "I checked the plaza,"
    scene bg ext_house_of_un_day with dspr 
    "her hut,"
    scene bg ext_library_day with dspr
    "and the library."
    "She was nowhere to be found."
    scene bg ext_washstand_day with dspr
    "Discouraged, I went to the washbasins to rinse my face and that’s where fortune smiled upon me."
    play ambience ambience_camp_center_day
    show un normal pioneer far at right with dspr
    "Lena was passing by that area just as I got there. What she was doing there at the time was the least of my concerns. "
    lu "Lena, hey!"
    show un surprise pioneer with dspr
    "Lena made her usual shocked expression transitioning into shyness. "
    show un shy pioneer with dspr
    un "Hi."
    lu "Listen, I need to collect on that favor you owe me. You’ve known Alisa for a long time, right?"
    show un surprise pioneer with dspr
    un "Well, yes. But how do you know that?"
    lu "Doesn’t matter. Tell me, do you know what kind of flowers she likes?"
    show un normal pioneer with dspr
    un "Yes, I do… What do you need that for?"
    lu "We… had a falling out of sorts and I need to make up for it."
    lu "I haven’t the faintest clue where flowers grow on these campgrounds, so would you be a doll and collect a bouquet of something she’d like? Your favor will count as collected."
    un "Um, sure. When do you need it?"
    lu "As soon as possible, preferably."
    un "Let’s meet here in about an hour, I’ll get something she’ll like."
    lu "Great, thank you."
    "We went our separate ways. I, to my hut and her to some path leading into the forest. Going to my hut while the bouquet was being assembled for me might not have been the best idea;"
    "Yet strolling across the forest with Lena and picking flowers might end up even worse. If Alisa spots me there with her, I’ll dig myself in a hole I’ll never climb out of."
    stop music fadeout 2
    stop ambience
    scene bg int_house_of_mt_day with dspr
    play sound sfx_close_door_1
    play ambience ambience_int_cabin_day
    "In the hut I started to think about what I’m going to say to Alisa when I see her and give her the flowers. I needed to apologize like I meant it and explain what really happened and why. Yes, in the first few days I did juggle between three women and perhaps even planned for more."
    "One thing I didn’t think of is that I’d end up in a relationship with one of them, and better yet, fall in love."
    "While I was thinking, another thought crossed my mind: I should go and get the carbon which started our argument. I’ll slip it in the bouquet as a sign of actually listening to what she says."
    stop ambience
    scene bg ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day
    "A few minutes later I was already at the medical center. I didn’t have time to knock, so I just went in."
    scene bg int_aidpost_day with dspr
    play sound sfx_open_door_1
    show cs smile glasses with dspr
    play music music_list["glimmering_coals"] fadein 2
    cs "Oh, Lucifer. Anything bothering you, or are you here just to pay me a visit?"
    "In her usual innuendo-filled tone said the nurse. I paid no attention to it, as I had other matters on my mind."
    lu "I need some activated carbon."
    cs "Stomach problems, eh? Maybe a medical exam is in order?"
    lu "I’d be happy to, though I’m afraid I have some inchoate business to attend to. Only the carbon for now."
    cs "Hm, must be {i}very{/i} important. Okay, give me a moment."
    "She opened a cupboard and pulled out some carbon, giving it to me afterwards."
    lu "Much obliged."
    hide cs with moveoutleft
    "I turned to exit and heard a few parting words behind my back:"
    cs "Don’t forget about me, Pioneer."
    th "If I only could with all this"
    play sound sfx_close_door_1
    stop music fadeout 2
    scene bg ext_washstand_day with dspr
    play music music_list["tried_to_bring_it_back"] fadein 4
    "There wasn’t much time left ‘til the end of the hour, so I hurried to the washbasins, where we’d agreed to meet."
    scene bg ext_washstand2_day with dspr
    "Lena wasn’t there yet, so I took the time to actually rinse my face, which I’ve forgotten about previously."
    play sound sfx_water_emerge
    $ renpy.pause (1)
    play sound sfx_water_splash
    "In a few minutes, my flower delivery service arrived. Lena held a bouquet of peonies and campanulas. The composition was pleasant on the eyes and I trusted Lena to know what her childhood friend would like. "
    scene bg ext_washstand_day with dspr
    show un normal pioneer far with dspr
    "She came over to me."
    show un normal pioneer with dspr
    un "Here, I got what I could find."
    lu "Thanks again, Lena. "
    show un smile pioneer with dspr
    "I took the flowers from her and gave her a slight hug as a sign of gratitude."
    stop music fadeout 4
    show dv sad pioneer far at right with dissolve
    play music music_list["you_lost_me"] fadein 2
    "Everything seemed to be looking up for me, until I noticed Alisa walking towards the washbasins. Her face was tear-stained, she probably wanted to wash up."
    "I instantly let go of Lena, but it was too late."
    show un surprise pioneer with dspr
    show dv rage pioneer at right with dspr
    dv "You! YOU!{w} Here I am, crying over him, trying to forgive him and he’s busy giving flowers to another!"
    lu "Wait, it's not what it bloody looks like!"
    "Alisa didn’t bother listening to me and ran in the opposite direction."
    hide dv with moveoutright
    lu "Wait! Dammit..."
    $ sshake = Shake((0.5, 5.0, 0.5, 1.0), 1.0, dist=5)
    scene bg ext_houses_day with dspr
    play sound sfx_run_forest
    "I ran after her, carrying the bouquet in my hands. She was faster than me and running in classical shoes was an added challenge to this." with Shake((0.5, 1.0, 0.5, 1.0), 5.0, dist=5)
    "I was falling behind by a significant distance, though not significant enough to lose sight of her." with Shake((0.5, 1.0, 0.5, 1.0), 5.0, dist=5)
    scene bg ext_path_day with dspr
    play sound sfx_run_forest
    "On one of the paths, she turned and ran into the forest. I made the same turn when I got there, losing sight in the process." with Shake((0.5, 1.0, 0.5, 1.0), 5.0, dist=5)
    scene bg ext_path2_day with dspr
    play sound sfx_run_forest
    "I ran in the direction I presumed she did, until I heard a bloodcurdling screech.{w} Alisa’s screech." with Shake((0.5, 1.0, 0.5, 1.0), 5.0, dist=5)
    play sound sfx_alisa_falls
    "This made me sprint even faster, tearing my shoes to dust."
    stop music fadeout 2
    scene bg ext_polyana_day with dspr
    play music music_list["doomed_to_be_defeated"] fadein 2
    show pi far with dspr
    "Soon enough I made it to a clearing in the woods, where an unexpected view greeted me. Alisa was on the ground, unconscious. The Pioneer was standing over her. "
    "I screamed, my eyes lighting ablaze."
    lu "What did you do to her?! Answer me!"
    show pi smile with dspr
    "I dropped the flowers and walked towards my enemy."
    pi "I only knocked her out, she’s alive.{w} Now me and you are going to have a little chat. Last time you humiliated me, now it’s my turn."
    "I kept shortening the distance. He put a foot over Alisa’s neck."
    pi "Not a step closer, or the ginger gets it."
    "I stopped, knowing full well I can’t risk her life."
    lu "What.{w} Do you.{w} Want?"
    "I hissed at him."
    pi "Answers, revenge, your suffering. Simple."
    lu "Fine, I’ll answer your questions. But you swear that You’ll let her go afterwards. "
    pi "I am the one who sets the rules here if you want her to live.{w} Now tell me, Devil, do you bleed?"
    lu "Come and see, bastard."
    play music like_a_wounded_animal fadein 2
    pi "I don’t know if you’ve noticed, but I have a few tricks of my own. "
    show pi smile at fleft as pi2 with dspr
    show pi smile at fright as pi3 with dspr
    "From behind a few trees on the sides emerged two pioneers, identical to the one standing before me."
    lu "What the blazes?"
    show pi smile close at left as pi2 with dspr
    show pi smile close at right as pi3 with dspr
    "They slowly came up to me. I still thought myself invincible and these odds didn’t scare me one bit."
    play sound sfx_punch_medium
    "Thought so, until one of them hit me in the stomach and I bent down from the unexpected pain. " with hpunch
    th "What the? Why can I feel this?"
    play sound sfx_punch_medium
    show pi at fleft as pi2 with vpunch
    "The second pioneer was about to hit me from the top, but I quickly got up with an uppercut to his face. He wavered and took a few steps back, barely keeping his balance. "
    th "My strengths have diminished"
    play sound sfx_punch_medium
    "I didn’t have time to react before the first one hit me in the face and I myself almost fell over." with hpunch
    pi "You’re not so tough when she’s around, are you? I was watching you, keeping track. You’re only vulnerable when she’s close."
    th "So that’s what it is. I almost figured it out myself, though I didn’t think it worked exactly this way"
    pi "Every time you resist, it only gets worse for her."
    "He stepped on her neck. I felt rage, overwhelming, all-consuming rage."
    play sound sfx_punch_medium
    hide pi3 with moveoutright 
    hide pi2 with dspr
    "Pushing off the one who hit my face as hard as I could, I dashed for the Original, knocking him off his feet."
    show pi close
    play sound sfx_punch_medium
    $ renpy.pause (1)
    play sound sfx_punch_medium
    $ renpy.pause (1)
    play sound sfx_punch_medium
    "As I was on top of him, I got a few quick blows in when he was on the ground."
    hide pi with dspr
    "Then I dashed to Alisa."
    show dv sad pioneer close with dspr
    lu "Alisa, do you hear me?"
    "I felt around her throat, nothing felt broken or out of place. Alisa coughed. "
    dv "Y-yes. What… happened?"
    hide dv with dspr
    show pi far at fleft as pi2 with dspr
    show pi far at left as pi3 with dspr
    show pi far as pi4 with dspr
    show pi far at right as pi5 with dspr
    show pi far at fright as pi6 with dspr
    "At this moment, three more copies emerged from behind the trees and the cumulative six were approaching us. I got up, preparing for battle."
    "Alisa was still on the ground, barely grasping the surroundings. She definitely won’t be any help in this fight."
    "I looked around the clearing in search of weapons, yet there wasn’t so much as a large stick laying around. "
    show pi smile at left as pi3 with dspr
    show pi smile at right as pi5 with dspr
    "The Pioneers came closer. Luckily, they were approaching from different distances and that gave me a slight advantage."
    play sound sfx_punch_medium
    hide pi as pi3 with moveoutleft
    "I parried the first one’s hit and counterattacked."
    play sound sfx_punch_medium
    hide pi as pi5 with moveoutleft
    "Turning towards the second right away, I hit him, performing a pirouette."
    show pi smile at fleft
    show pi smile at left as pi2 with dspr
    show pi smile close as pi4 with dspr
    show pi smile at right as pi6 with dspr
    "Up next, things went less my way. The remaining four decided not to attack one-by-one. One of them was about to hit me from the front, so I directed my attention to him."
    hide pi with moveoutleft
    hide pi as pi6 with moveoutright
    "Two of the others grabbed me from behind, constricting my movement and the fourth hit me in the side." with hpunch
    play sound sfx_bodyfall_1
    stop music fadeout 2
    "I tried to break free, but they threw me to the ground and started kicking from all sides. I couldn’t do a thing except anticipate which side the next hit will come from." with vpunch
    play sound sfx_alisa_falls
    play music music_list["drown"] fadein 2
    "One of the feet heading for me, however, hit something close instead. I heard a muffled cry from Alisa."
    th "The swine, I wasn’t enough to them, so they hit the girl"
    "I was hit and kicked from all sides, accompanied by malevolent laughter. One of the was standing to the side, also kicking the barely conscious Alisa." with hpunch
    "Through the hailstorm of hits, I managed to get closer and cover Alisa with myself, to protect her in the least. " with vpunch
    "My body felt incredible pain on all sides, I didn’t know how much more I could take. Inside, I felt powerless, yet also felt my rage building with each incoming hit." with hpunch
    "More hits." with vpunch
    "Life at the camp flashed before my eyes." with hpunch
    "Hits." with vpunch
    "This couldn’t just end here." with hpunch
    "Even more hits." with vpunch
    "Not now." with hpunch
    stop music fadeout 4
    th "This won’t end now!" with Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=5)
    play music on_thin_ice fadein 2
    lu "AAAAA!" with Shake((0.5, 1.0, 0.5, 1.0), 2.0, dist=5)
    show lu_wings with dspr
    "From my bloodied back a pair of massive snow-white wings emerged and knocked the attackers off their feet."
    "Using this opportunity, I picked Alisa up from the ground and flew up into the air, bringing her back onto the campgrounds."
    hide lu_wings with dspr
    stop music fadeout 2
    scene bg ext_square_day with dissolve
    play music music_list["farewell_to_the_past_full"] fadein 2
    play sound sfx_wind_gust
    "I landed in the trees next to the plaza and walked to it, hiding my wings in the process. I laid Alisa down on a bench there."
    show dv shocked pioneer with dspr
    dv "You… you’re an Angel! A real one!"
    lu "Later. Now that you’re safe, I have to deal with something. "
    play sound sfx_wind_gust
    "I opened my wings once again and dashed into the sky, making sure no passersby noticed me."
    stop music fadeout 1
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    $ volume(0.5, "music")
    play music treat_me_like_your_mother fadein 2
    scene bg ext_polyana_day with dissolve
    "I flew back to the clearing where the Pioneers looked like they were waiting for me. "
    play sound sfx_body_bump
    "Making an effective entrance, I landed right in the middle of them, knocking one off his feet."
    "Rage was teeming inside me and my eyes shone bright red. I once again felt my full devilish powers."
    show pi far with dspr
    show pi far at right as pi2 with dspr
    show pi far at left as pi3 with dspr
    "The Pioneers were no doubt surprised to see wings, yet that didn’t stop them from coming closer to try to attack once more."
    show pi close with move
    "This time I didn’t wait for them to strike, instead moving in to attack. One flap of my wings and I was already next to one of them."
    play sound sfx_punch_washstand
    hide pi with moveoutright
    "He didn’t have time to react before a swift hit in the stomach sent him flying at the nearest tree." with hpunch
    "One of the others tried to grab my wing, though I shrugged him off with ease, knocking hit to the ground. The third one ran up to me with a punch at the ready." with vpunch
    "I caught his fist mid-blow and twisted his arm back, breaking his bones."
    pi "Aaaa!"
    lu "Your turn to feel pain."
    play sound sfx_body_bump
    "Another one pounced at me from the back, knocking me down, yet one flap of my wing and I was back on my feet, unlike my opponent." with hpunch
    show pi close as pi2 with move
    "All I wanted right now was vengeance, punishing them for an attempt on my life, and more importantly, Alisa’s life. I hit the fifth copy in his face and heard his nose crack. "
    hide pi as pi2 with moveoutright
    hide pi as pi3 with dspr
    show pi far with dspr
    "The only remaining one was the Original, their leader. The same one who held his foot over Alisa’s neck not long ago. He slowly backed away. "
    pi "Wait, we can still talk this out!"
    lu "The time for talk is over!"
    show pi close with dspr
    play sound sfx_torch
    "Two swift steps and I was right in front of him. I grabbed his face with both my hands and lit them on fire. "
    "While doing so, I kept my eye contact with him, looking into his eyes with hatred and malice, even with some insane joy. The Pioneer screamed in agony while the flesh on his face melted and his hair burned away."
    hide pi with dspr
    play sound sfx_bodyfall_1
    stop music fadeout 2
    $ volume(1, "music")
    play music music_list["torture"] fadein 2
    "He tried to push me away, waved his hands and feet – useless. When his face no longer resembled that of a human and more of burned pate, I dropped him to the ground."
    "He never stopped screaming, but now it sounded more like the howling of a dying animal. "
    "His copies, upon witnessing their leader’s fate stumbled and ran in everywhich direction, just to not meet the same consequences. "
    "I heard a voice behind my back."
    stop music fadeout 2
    dv "No, you’re no Angel, you are the Devil…"
    play music after_the_storm fadein 2
    show dv sad pioneer far with dspr
    "I made a half-turn towards Alisa, standing at the end of the path, leading to this clearing."
    "I definitely looked hellish at the moment. My wings were hidden, my hands, eyes and hair were lit up in an orange flame and a malevolent smile was occupying my face. Upon seeing her, everything slowly went back to normal."
    show dv sad pioneer with dspr
    "I walked towards her. She took a few steps back and then stopped. "
    lu "Are you alright? "
    dv "What… what did you do to him?"
    lu "He got what he deserved. For what he did to you, and me. He’ll live, but his life will never be the same. "
    "Alisa gave a silent look at the now curled up burnt Pioneer on the other side of the clearing. Then she directed her sight at me."
    show dv cry pioneer close with dspr
    "Her amber eyes sparkled with tears. I couldn’t handle the look and hugged her. At first, she just stood there, but later wrapped her arms around me too."
    dv "I thought we’d die here. That I’d never see you again."
    "She cried into my chest, I stroked her head. "
    lu "From now on, everything will be alright. "
    "She stopped crying, yet still sniffled from time to time. "
    dv "Truly?"
    lu "Yes, truly. "
    $ persistent.sprite_time = 'night'
    $ night_time()
    play ambience ambience_forest_evening
    show lu_dv_forest with dissolve
    "A few moments later the both of us, bloodied and bruised, came back to the camp by the same path that we were running on when it all began. We were firmly holding each other’s hands, not letting the other go."
    dv "What happens now? You really are the Devil, and I didn’t believe you the whole time. Can you even be with me now that I know?"
    lu "What have I been doing this whole time then, silly? Maybe my father is against me being here, but I decide who I can and cannot be, and with whom."
    dv "Your f-father? As in God?"
    lu "Yes, he can be quite a pain sometimes. Don’t worry, I’ll do everything in my power so that we can be together."
    stop music fadeout 4
    stop ambience
    scene bg ext_square_night with dspr
    hide lu_dv_forest with dspr
    play ambience ambience_camp_center_night
    play music music_list["sweet_darkness"] fadein 2
    show dv normal pioneer at left with dspr
    show mt surprise pioneer with dspr
    "It looked like Alisa was about to ask something else, though at this point we reached the plaza, where our chat was interrupted by Olga Dmitriyevna. "
    mt "Oh God, what happened to you guys? Did you get in a fight?"
    lu "I assure you {i}he{/i} has nothing to do with it. What happened to us is our concern. All you need to know is that we’re fine. "
    show mt normal pioneer with dspr
    mt "If you really don’t need help, there’s still one problem. Shurik never showed up. Did you search for him, as I asked?"
    "I sighed, heavily."
    stop music fadeout 2
    lu "Give us half an hour, we’ll find him."
    play music music_list["awakening_power"] fadein 2
    show dv angry pioneer with dspr
    "Alisa, who was silently standing next to me until this point, decided to intervene."
    dv "Why should we even search for him? There’s a whole camp of pioneers and your own search party out there and you need specifically the two of us to do the dirty work?"
    show mt angry pioneer with dspr
    mt "Because all you do is create problems for this camp and break the rules. It’s about time you actually helped around here."
    mt "True, others are already out on the search, but it’s been a whole day and none of them found anything. You’re not getting out of this one like the others."
    show mt angry pioneer far with move
    show dv angry pioneer close with move
    "I took Alisa a few steps away from the counselor."
    lu "Alisa, don’t argue with her right now. I know how to solve this. They’ll even congratulate us afterwards. "
    stop music fadeout 4
    show dv normal pioneer close with dspr
    dv "What do you have in mind?"
    lu "It’s easy, I know where Shurik is. "
    show dv surprise pioneer close with dspr
    dv "You knew this whole time? Then why didn’t you tell the counselor?"
    lu "Because she’d send us to fetch him from there anyway."
    show dv smile pioneer with dspr
    dv "Right. Then you lead."
    lu "He’s at the old campgrounds, but I know a shortcut."
    scene bg ext_path2_night with dspr
    "I lead Alisa into the trees and bushes on the side. "
    show dv grin pioneer with dspr
    dv "This is your shortcut? Through the bushes?"
    lu "Not exactly."
    play music banks_of_the_sansretour fadein 4
    show dv shocked pioneer close with dspr
    "I picked Alisa up and opened my wings."
    th "If I have them, I might as well use them"
    play sound sfx_wind_gust
    "I darted into the sky and flew towards the old camp, firmly holding my treasure in my hands."
    scene night_forest with dissolve
    show dv scared pioneer close with dspr
    dv "Aaah! What are you doing?"
    lu "Shortening the way. "
    "Alisa shut her eyes at first, however her curiosity took over soon and she slowly opened them back up, taking in the view that opened up before her. The whole flight she firmly held her hands around my neck. "
    show dv surprise pioneer close with dspr
    dv "So pretty…"
    "We soon arrived at the old camp. The sun was setting and with each moment the place got darker, the atmosphere becoming eerier by the second. "
    scene bg ext_old_building_night with dspr
    play ambience ambience_forest_night
    show dv pioneer smile with dspr
    lu "Thank you for flying on Devilish Airlines. I hope you enjoyed your trip and will choose to fly with us again one day. "
    dv "The take off was a bit scary, otherwise quite enjoyable. This a good enough review?"
    dv "And how about you warn me next time you plan to take me on a trip?"
    lu "Perhaps, now let’s go in. He’s underground. "
    dv "I’m not even gonna ask how you know all this. What if you’re also some kind of clairvoyant. I’ve had enough revealed secrets for today."
    lu "Good choice."
    play sound sfx_door_squeak_light
    stop ambience
    scene bg int_old_building_night with dspr
    "We came into the old building, where I opened a hatch leading to the below ground level. I went in first, knowing it might be dangerous inside. Alisa climbed down after me. "
    play sound sfx_open_metal_hatch
    scene bg int_mine_room with dissolve
    play ambience ambience_catacombs
    play sound sfx_torch
    show d5_catac_dv_lu with dspr
    "I lit a small fireball in my palm to light the room."
    show cg d4_sh_sit with dspr
    "In the corner of the now dimly lit basement we saw a crouching figure, facing the wall. It was Shurik and he was staring at us with an insane gaze. "
    sh "No, you’re not real! Go away!"
    hide cg with dspr
    hide d5_catac_dv_lu with dspr
    show dv angry pioneer at right with dspr
    show sh scared at left with dspr
    dv "What do you mean, “not real”? We’re out there searching for him and he’s crouching in a basement this whole time!"
    "She was about to come up to him and slap him in the face, but I stopped her by holding out a hand in front of her. I lowered my voice and said:"
    lu "He has a metal armature in his hand, don’t provoke him."
    show dv scared pioneer at right with dspr
    "The aggression on Alisa’s face changed to worry. Shurik was still staring at us."
    play music music_list["pile"] fadein 2
    show sh rage at left with dspr
    sh "Why are you still here? Want to take me with you, huh? I won’t go willingly!"
    show cg d4_sh_stay with dspr
    "He hopped up from the ground and swung the metal bar at Alisa. This was exactly what I expected, so I reacted quickly."
    play sound sfx_punch_medium
    scene black with dspr
    hide cg with dspr
    "I hit off his hand with the weapon with one hand and grabbed him by the neck, lifting him up with the other. The room fell into complete darkness since I had to douse the flame in my hand."
    scene bg int_mine_room with dspr
    show sh scared close with dspr
    show dv shocked pioneer at right with dspr
    "Instead of it, however, my eyes lit up. I grabbed the armature out of his hand. "
    lu "Either you calm down {i}now{/i}, or I’ll stick this so far up your ass you’ll taste metal. "
    stop music fadeout 4
    sh "O-o-okay, okay. Take me wherever you want, just don’t hurt me!"
    play music music_list["door_to_nightmare"] fadein 2
    lu "You don’t snap out of it, do you? “Take me, take me”. Alisa, you can slap him like you meant to, now. "
    show dv smile pioneer close at right with dspr
    play sound sfx_face_slap
    "Alisa came up to him and slapped him in the face with a content smile. "
    sh "Ow! W-what? Where am I?"
    play sound sfx_alisa_lighter
    "I put him down on his feet and lit up my lighter to not scare him further with flaming hands. "
    show sh scared with move
    show dv smile pioneer with move
    lu "That’s what we’re trying to find out. How’d you even end up in the basement of the old camp?"
    sh "I came her for spare electronics and scrap and… I got lost. Some kind of voices led me around the mineshafts in circles…"
    show dv angry pioneer with dspr
    dv "What voices? Are you actually insane? What the hell were you thinking when you pounced on people with an armature? "
    sh "I don’t know, it’s as if someone was calling for me and then I don’t remember. What armature?"
    lu "With this one, genius. You really can’t recall what happened 2 minutes ago?"
    sh "N-no. I only remember a sharp pain in my cheek and then you put me down. "
    lu "Right. Alisa let’s get out of here. If this one wants to keep following voices down here, then let him."
    dv "Couldn’t agree more. Let’s go."
    sh "Hey, wait, don’t leave me here! I’m going with you."
    hide dv with dspr
    hide sh with dspr
    "I let Alisa climb first and climbed up after her. Quite an alluring view opened up before me."
    lu "You didn’t lie when you said I’d get ample opportunity to stare later."
    dv "I’ll stab out your shining eyeballs soon enough. "
    lu "What for, dear?"
    dv "For excessive curiosity in observation. "
    stop music fadeout 2
    play music music_list["dance_of_fireflies"] fadein 2
    stop ambience
    show lu_dv_forest with dspr
    "Soon we returned to the surface and went back to the camp. Alisa and I walked ahead, whereas our search object dragged on behind us."
    "I looked back from time to time, just to check if he was still there and not fallen into a random hole in the ground. "
    scene ext_square_night with dspr
    show dv smile pioneer at right with dspr
    show sh normal at left with dspr
    "When we came to the plaza, it was already nighttime."
    lu "Shurik, run along to your place. And do try not to follow any voices along the way, will you?"
    sh "Very funny. Goodnight. "
    hide sh with moveoutleft
    "He walked off in the direction of his and Elektronik’s hut."
    lu "Speaking of good nights, are we going back to your place?"
    dv "Have you not wondered even for a second where Ulyana was yesterday?"
    lu "For a split second, perhaps. It was rather convenient yesterday. "
    dv "I asked her to spend the night at a friend’s house. We had no arrangements for today, so sorry to say we’re sleeping separately tonight. "
    lu "Well, I suppose we couldn’t go to mine either, with the counselor living there and all that. Seems I’ll have to survive one night without you. We’ll think of something tomorrow though. "
    dv "I’m sure you’ll figure it out. Now I really want to sleep, so see you tomorrow!"
    lu "‘til tomorrow, darling."
    "We gave each other a parting kiss and went to our huts."
    stop music fadeout 4
    scene int_house_of_mt_night with dissolve
    play sound sfx_close_door_1
    play ambience ambience_int_cabin_evening
    "In mine, Olga awaited my return. "
    show mt normal pioneer with dspr
    mt "How was the search effort? Do I need to call the police? "
    lu "We found your Shurik. He got lost at the old campgrounds."
    mt "Really? What was he doing there?"
    lu "You can ask him that personally tomorrow. Now, if you’ll excuse me, I had a long day. I’m going to sleep."
    mt "Okay, I’ll do that. You and Alisa have done well, finding him. Goodnight. "
    lu "U-huh."
    "I undressed and lay down in bed. My whole body ached after our brawl in the forest. Maybe Alisa and I should’ve gone to the medical center after all."
    show blink
    "Although, that might remind her of our argument this morning. Even with the pain, I quickly fell asleep. "
    window hide
    jump devilishadv_day666_en











    



    











