from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.evmenu import get_input

class CmdSpell(MuxCommand):

    key = "+spell"
    locks = "cmd:all()"
    desc1 = "A"
    desc2 = "B"
    desc3 = "C"

    def func(self):
        if not self.args:
            self.msg("You must provide a target for your spell.")
            return
        if ' ' in self.args:
            arg1, arg2 = self.args.split(' ', 1)
            playerA = self.caller.search(arg1)
            playerB = self.caller.search(arg2)
            if not playerA or not playerB:
                self.caller.msg("Couldn't find those players")
                return
            get_input(self.caller, "Please enter some text:\n", self.get_text, target_a=playerA, target_b=playerB)

    def get_text(self, caller, prompt, result, target_a=None, target_b=None):
        if not target_a or not target_b:
            caller.msg("You somehow managed to get here without setting targets.")
            return None
        if not result:
            caller.msg("Please enter some text.")
            return True
        else:
            target_a.msg(result)
            target_b.msg(result)
            caller.msg("You sent {spell} to {a} and {b}.".format(spell=result, a=target_a.key, b=target_b.key))
            return None
