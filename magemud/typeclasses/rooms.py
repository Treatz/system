"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from evennia.utils.utils import inherits_from

class Room(DefaultRoom):
    def at_object_creation(self):
        self.db.image = "http://mud.streetwitch.com/static/website/images/1.jpg"

    def return_appearance(self, looker):
        if not looker:
            return
        looker.msg(image=[self.db.image, ""])
        # get and identify all objects
        visible = (con for con in self.contents if con != looker and
                                                    con.access(looker, "view") and (looker.db.alive == con.db.alive or con.destination))
        exits, users, things = [], [], []
        for con in visible:
            key = con.get_display_name(looker)
            if con.destination:
                exits.append(key)
            elif con.has_player:
                users.append("{c%s{n" % key)
            else:
                things.append(key)
        # get description, build string
        string = "{c%s{n\n" % self.get_display_name(looker)
        if(looker.db.alive == 1):
            desc = self.db.desc
        if(looker.db.alive == 0):
            desc = self.db.spiritdesc
        if desc:
            string += "%s" % desc
        if exits:
            string += "\n{wExits:{n " + ", ".join(exits)
        if users or things:
            string += "\n{wYou see:{n " + ", ".join(users + things)
        return string
