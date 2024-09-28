label day2_lord_intro:

    $ event_meet_lord2 = True

    play music the_old_castle

    scene bg hallway day with dissolve

    show lord smirk with dissolve

    lord "Good morning, [player_name]."
    player "Morning."
    lord "You appear troubled. Did something happen?" 
    player "It wasn’t the best sleep. I saw… hmm… This probably sounds crazy, but I thought I saw a woman who was missing parts of her face. She looked like a ghost or something. I don’t know. It seemed so real, but…" 
    lord "I see. I can assure you, that you’re not crazy. Your experience was very real. {w=0.3} This manor is indeed haunted. A category 2 haunting, to be precise. Several spirits find themselves bound to these grounds, trapped in a space between the world of the living and the world of the dead, incapable of crossing over on their own."
    player "Is this a joke? {w=0.3} Are you just messing with me right now?" 
    lord "Not at all. Though I certainly understand your incredulity, the supernatural is a very real part of this world." 
    player "Uh huh… um… Well… putting aside my disbelief for a moment… I guess I shouldn’t be surprised. No one just gives a mansion away for free. I figured there would be a catch… I just didn’t expect the catch to be ghosts!"
    lord "And that brings me to the condition I mentioned yesterday."
    player "Is it like that one movie where the main character had to survive a night alone, locked in the mansion?" 
    lord "Nothing so dramatic. I want you to help these spirits pass on to the other side."
    player "Okay… and how exactly am I supposed to do that? I only just learned ghosts are real. How am I supposed to get rid of them?"
    lord "Your task is simpler than you think. You merely need to talk to them. Help them come to terms with their lives... and their deaths. It may take some time, but I believe you're capable of helping them cross over."
    player "Right... but wouldn’t you be better at this? Maybe you could give me a different job instead." 
    lord "Pity. But if you really believe you're incapable of such a simple task, I could always find someone else to inherit the estate..." 
    player "Whoa. Slow down. I can do it. I don’t know why you chose me for this, but I’ll talk to the ghosts and help them cross over or whatever. Just make sure you have the deed ready."

    scene black with dissolve

    stop music fadeout 4

    jump explore_inside_day
