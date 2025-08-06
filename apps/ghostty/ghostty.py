from talon import Context, Module, actions

mod = Module()

mod.apps.ghostty = """
os: mac
and app.bundle: com.mitchellh.ghostty
"""

ctx = Context()
ctx.matches = r"""
app: ghostty
"""


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        if number < 9:
            actions.key(f"cmd-{number}")

    def tab_final():
        actions.key("cmd-9")


@ctx.action_class("edit")
class EditActions:
    def word_left():
        actions.key("alt-left")

    def word_right():
        actions.key("alt-right")
