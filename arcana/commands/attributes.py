from evennia import Command
from evennia.utils.evmenu import EvMenu

def attributes(caller):
    text = """
    This is an example menu.

    If you enter anything except the valid options, your input will be
    recorded and you will be brought to a menu entry showing your
    input.

    Select options or use 'quit' to exit the menu.
    """
    options = ({"key": ("(1) Strength", "1"),
                "desc": "Physical Power",
                "goto": "assignStr"},
               {"key": ("(2) Dexterity", "2"),
                "desc": "Speed and Control",
                "goto": "assignDex"},
               {"key": ("(3) Stamina", "3"),
                "desc": "Health and Endurance",
                "goto": "assignStr"},
               {"key": ("(4) Charisms", "4"),
                "desc": "NPC Reactions",
                "goto": "assignCha"},
               {"key": ("(5) Manipulation", "5"),
                "desc": "Social Skills",
                "goto": "assignMan"},
               {"key": ("(6) Appearance", "6"),
                "desc": "Bonus Social Roles",
                "goto": "assignApp"},
               {"key": ("(7) Perception", "7"),
                "desc": "Awareness of Surroundings",
                "goto": "assignPer"},
               {"key": ("(8) Intelligence", "8"),
                "desc": "Mental Skils",
                "goto": "assignInt"},
                {"key": ("(9) Wits", "9"),
                "desc": "Mental Deffenses",
                "goto": "assignWit"})

    return text, options

def assignStr(caller):
    caller.db.strength = caller.db.strength + 1
    text = ("Your attribute 'Strength' was increased to: %s." % caller.db.strength)

    options = {"key": ("back (default)", "_default"),
               "desc": "back to main",
               "goto": "test_start_node"}
    return text, options

def assignDex(caller):
    caller.db.dexterity = caller.db.dexterity + 1
    text = ("Your attribute 'Dexterity' was increased to: %s." % caller.db.dexterity)

    options = {"key": ("back (default)", "_default"),
               "desc": "back to main",
               "goto": "test_start_node"}
    return text, options

def assignSta(caller):
    caller.db.stamina = caller.db.stamina + 1
    text = ("Your attribute 'Stamina' was increased to: %s." % caller.db.stamina)
    options = {"key": ("back (default)", "_default"),
               "desc": "back to main",
               "goto": "test_start_node"}
    return text, options

def assignCha(caller):
    caller.db.charisma = caller.db.charisma + 1
    text = ("Your attribute 'Charisma' was increased to: %s." % caller.db.charisma)
    options = {"key": ("back (default)", "_default"),
               "desc": "back to main",
               "goto": "test_start_node"}
    return text, options

def assignMan(caller):
    caller.db.manipulation = caller.db.manipulation + 1
    text = ("Your attribute 'Manipulation' was increased to: %s." % caller.db.manipulation)
    options = {"key": ("back (default)", "_default"),
               "desc": "back to main",
               "goto": "test_start_node"}
    return text, options

def assignApp(caller):
    caller.db.appearance = caller.db.appearance + 1
    text = ("Your attribute 'Appearance' was increased to: %s." % caller.db.appearance)
    options = {"key": ("back (default)", "_default"),
               "desc": "back to main",
               "goto": "test_start_node"}
    return text, options

def  test_displayinput_node(caller, raw_string):
    text = """
    You entered the text:

        "%s"

    ... which could now be handled or stored here in some way if this
    was not just an example.

    This node has an option with a single alias "_default", which
    makes it hidden from view. It catches all input (except the
    in-menu help/quit commands) and will, in this case, bring you back
    to the start node.
    """ % raw_string
    options = {"key": "_default",
               "goto": "test_start_node"}
    return text, options

def test_end_node(caller):
    text = """
    This is the end of the menu and since it has no options the menu
    will exit here, followed by a call of the "look" command.
    """
    return text, None

# Menu command to create the menu

class CmdAttr(Command):
    """
    Test menu

    Usage:
      testmenu <menumodule>

    Starts a demo menu from a menu node definition module.

    """
    key = "@attributes"

    def func(self):
        EvMenu(self.caller, "commands.attributes",
               startnode="attributes",
               cmdset_mergetype="Replace")