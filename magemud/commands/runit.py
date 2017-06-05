from evennia.commands.default.muxcommand import MuxCommand
from evennia import create_object
from evennia import DefaultObject


class CmdMakeItExample(MuxCommand):
   
    key = "+makeit"
    locks = "cmd:all()"

    def func(self):
        myObj = create_object(DefaultObject, key="MyObj", location=self.caller.location)
        self.caller.msg("An object appears out of thin air and falls to the ground.")