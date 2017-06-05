from evennia.commands.default.muxcommand import MuxCommand


class CmdScryExample(MuxCommand):
   
    key = "+scry"
    locks = "cmd:all()"

    def func(self):
        if not self.lhslist:
            self.msg("You must provide a list of directions.")
            return
        current_room = self.caller.location
        for arg in self.lhslist:
            exit_object = current_room.search(arg, candidates=current_room.exits)
            if not exit_object:
                self.msg("The path was not valid.")
                return
            current_room = exit_object.destination
        # now we've found the destination
        self.caller.msg(self.caller.at_look(current_room))