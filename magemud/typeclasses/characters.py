"""
GO!
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter, TICKER_HANDLER

class Character(DefaultCharacter):
# [...]
    def at_object_creation(self):
        """
        Called only at initial creation. This is a rather silly
        example since ability scores should vary from Character to
        Character and is usually set during some character 
        generation step instead.
        """
        #set persistent attributes
        self.db.tradition = "None"
        self.db.essence = "None"
        self.db.concept = "None"
        self.db.strength = 0
        self.db.dexterity = 0
        self.db.stamina = 0
        self.db.manipulation = 0
        self.db.appearance = 0
        self.db.perception = 0
        self.db.intelligence = 0
        self.db.wits = 0
        self.db.conscious = 1
        self.db.alive = 1
        self.db.conscious = 1
        self.db.alertness = 0
        self.db.athletics = 0
        self.db.awareness = 0
        self.db.brawl = 0
        self.db.intimidation = 0
        self.db.streetwise = 0
        self.db.drive = 0
        self.db.firearms = 0
        self.db.martialarts = 0
        self.db.melee = 0
        self.db.meditation = 0
        self.db.stealth = 0
        self.db.astrology = 0
        self.db.computer = 0
        self.db.language = 0
        self.db.medicine = 0
        self.db.occult = 0
        self.db.charisma = 9
        self.db.rituals = 0
        self.db.correspondence = 0
        self.db.entropy = 0
        self.db.forces = 0
        self.db.life = 0
        self.db.matter = 0
        self.db.mind = 0
        self.db.prime = 0
        self.db.spirit = 0
        self.db.time = 0
        self.db.quintessence = 0
        self.db.arete = 0
        self.db.willpower = 0
        self.db.arcane = 0
        self.db.belief = 0
        self.db.familiar = 0
        self.db.luck = 0
        self.db.resources = 0
        self.db.target = self
        self.db.attacker = self
        self.db.bashing = 0
        self.db.lethal = 0
        self.db.weapon = 0
        TICKER_HANDLER.add(60, self.heal)
        TICKER_HANDLER.add(120, self.heal_lethal)

        return

    def heal_lethal(self, *args, **kwargs):
        if(self.db.lethal > 0):
            self.msg("You heal 1 point of lethal damage.")
            self.db.lethal = self.db.lethal  - 1

        healthbar = "|X|[wHealth:"
        total = caller.db.lethal + caller.db.bashing
        if total >= 8:
                difference = total - 8
                caller.db.lethal = caller.db.lethal + difference
                caller.db.conscious = 0

        if caller.db.lethal > 8:
                caller.db.alive = 0
       
        for i in range(0,8):
                if i < caller.db.lethal - 1:
                        healthbar += " X"
                elif i < total:
                        healthbar += " /"
                else:
                        healthbar += " 0"
        
        caller.msg(prompt=healthbar)

    def get_abilities(self):
        """
        Simple access method to return ability 
        scores as a tuple (str,agi,mag)
        """
        return self.db.strength, self.db.agility, self.db.magic

    def is_alive(self):
        return self.db.alive

    def at_post_puppet(self):

        super(Character, self).at_post_puppet()

        healthbar = "|X|[wHealth:"
        total = caller.db.lethal + caller.db.bashing
        if total >= 8:
                difference = total - 8
                caller.db.lethal = caller.db.lethal + difference
                caller.db.conscious = 0

        if caller.db.lethal > 8:
                caller.db.alive = 0
       
        for i in range(0,8):
                if i < caller.db.lethal - 1:
                        healthbar += " X"
                elif i < total:
                        healthbar += " /"
                else:
                        healthbar += " 0"
        
        caller.msg(prompt=healthbar)

    def return_appearance(self, looker):
        looker.msg(image=[self.db.image, self.db.desc])

        def at_post_unpuppet(self, player, session=None):
            """
            We stove away the character when the player goes ooc/logs off,
            otherwise the character object will remain in the room also
            after the player logged off ("headless", so to say).
            Args:
            player (Player): The player object that just disconnected
                from this object.
            session (Session): Session controlling the connection that
                just disconnected.
            """
            if not self.sessions.count():
               # only remove this char from grid if no sessions control it anymore.
               if self.location:
                  self.location.for_contents(message, exclude=[self], from_obj=self)
                  self.db.prelogout_location = self.location
                  self.location = self.db.prelogout_location
                  self.ndb._menutree.close_menu()
                  self.db.target.ndb._menutree.close_menu()
