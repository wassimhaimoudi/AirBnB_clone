#!/usr/bin/python3
"""Entry point of the command interpreter for the Airbnb clone project"""
import cmd
import sys


class HBNBCCommand(cmd.Cmd):
    """HBNBC command processor"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Handles the quit command"""
        return True

    def do_EOF(self, line):
        """Handles EOF signal"""
        return True

    def emptyline(self):
        """Handles empty line when pressing Enter"""
        pass


if __name__ == '__main__':

    my_hbnbc = HBNBCCommand()
    if not sys.stdin.isatty():
        input_commands = sys.stdin.readlines()
        my_hbnbc.onecmd('\n'.join(input_commands))
    else:
        my_hbnbc.cmdloop()
