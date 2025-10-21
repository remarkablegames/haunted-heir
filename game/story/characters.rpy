init python:
    def dismiss_callback() -> bool:
        renpy.sound.play("ui/click.ogg")
        return True

    config.say_allow_dismiss = dismiss_callback


define ghost = Character("Ghost", color="#e6e6fa", image="ghost")
define lord = Character("Lord", color="#cbc3e3", image="lord")
define miss = Character("Young Miss", color="#cbc3e3", image="miss")
define player = Character("[player_name]", color="#cc0000")
define unknown = Character("???", color="#fff")
