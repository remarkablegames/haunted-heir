init python:
    MUSIC_CHANNEL_DIALOGUE = "dialogue"

    renpy.music.register_channel(MUSIC_CHANNEL_DIALOGUE, "voice", loop=True)

    def narrator_callback(event, interact=True, **kwargs) -> None:
        if event == "show_done":
            renpy.music.play("bleeps/bleep003.ogg", channel=MUSIC_CHANNEL_DIALOGUE)
        elif event == "slow_done":
            renpy.music.stop(channel=MUSIC_CHANNEL_DIALOGUE, fadeout=0.2)

    def player_callback(event, interact=True, **kwargs) -> None:
        if event == "show_done":
            renpy.music.play("bleeps/bleep009.ogg", channel=MUSIC_CHANNEL_DIALOGUE)
        elif event == "slow_done":
            renpy.music.stop(channel=MUSIC_CHANNEL_DIALOGUE, fadeout=0.2)

    def dismiss_callback() -> bool:
        renpy.sound.play("ui/click.ogg")
        return True

    config.say_allow_dismiss = dismiss_callback


define ghost = Character("Ghost", color="#e6e6fa", image="ghost")
define lord = Character("Lord", color="#cbc3e3", image="lord")
define miss = Character("Young Miss", color="#cbc3e3", image="miss")
define narrator = Character(None, callback=narrator_callback)
define player = Character("[player_name]", callback=player_callback, color="#cc0000")
define unknown = Character("???", color="#fff")
