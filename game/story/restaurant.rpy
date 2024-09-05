label restaurant:

    "What a strange mail."

    friend "Hey, are we still up for movie night today?"
    friend "Just making sure, it's at 6, right?"

    menu:
        "Yep, 6pm":
            friend "Alright, see you there!"

    scene bg restaurant with fade

    waiter "Welcome to Five Little Pigs, did you book a reservation?"

    menu:
        "Yes":
            waiter "Excellent, may I get your name?"

        "No":
            waiter "All good, may I get your name?"

    $ player_name = renpy.input("My name is...", length=32).strip() or player_name

    waiter "Please take a seat, [player_name]."

    player "Thanks."

    "Time passes as you wait for [friend.name]."

    friend "Hey [player_name]!"

    menu:
        "You're right on time!":
            friend "Nice! Made it right on time."

        "You're late...":
            friend "Sorry! I was stuck in traffic."

    friend "I got a crazy mail today."

    player "What kind of mail was it?"

    friend "I don't know if it's a prank but it said I inherited some mansion."

    player "Wait a second..."

    friend "What?"

    player "I got a similar mail today."

    friend "That's creepy..."

    player "Maybe it's a scam?"

    friend "Perhaps... but what if it's real? A mansion could be worth a lot of money."

    player "What are you suggesting?{w=0.3} That we go and check it out?"

    friend "You got any other plans this weekend?"

    player "Not really."

    friend "Let's go check it out then, I think it'll be a fun adventure!"

    player "Sure, why not."

    scene bg mansion front day with fade

    "Welcome, [player_name]."

    jump end
