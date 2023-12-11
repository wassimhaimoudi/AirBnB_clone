#!/usr/bin/python3
"""Entry point of the command interpreter for the Airbnb clone project"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCCommand(cmd.Cmd):
    """HBNBC command processor"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quits the program"""
        return True

    def do_EOF(self, line):
        """Handles EOF signal"""
        return True

    def emptyline(self):
        """Handles empty line when pressing Enter"""
        pass

    def do_create(self, line):
        """Creates a new instance"""
        if line == "" or line is None:
            print("** class name missing **")
        if line not in storage.classes():
            print("** class doesn't exist **")

        new = storage.classes()[line]()
        new.save()
        print(new.id)


if __name__ == '__main__':
    HBNBCCommand().cmdloop()
