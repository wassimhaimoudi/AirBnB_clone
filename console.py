#!/usr/bin/python3
"""Entry point of the command interpreter for the Airbnb clone project"""
import cmd
from models.base_model import BaseModel
from models import storage, FileStorage


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
            return
        if line not in storage.classes():
            print("** class doesn't exist **")
            return

        new = storage.classes()[line]()
        new.save()
        print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        parse_line = line.split(' ')
        if parse_line[0] == '' or parse_line[0] is None:
            print("** class name missing **")
            return

        class_name = parse_line[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(parse_line) < 2 or parse_line[1] == '' or parse_line[1] is None:
            print("** instance id missing **")
            return

        instance_id = parse_line[1]
        key = '.'.join([class_name, instance_id])
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, line):
        """Deletes an instance"""
        parse_line = line.split(' ')
        if parse_line[0] == '' or parse_line[0] is None:
            print("** class name missing **")
            return
        class_name = parse_line[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(parse_line) < 2 or parse_line[1] == '' or parse_line[1] is None:
            print("** instance id missing **")
            return
        instance_id = parse_line[1]

        key = '.'.join([class_name, instance_id])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Prints a list of all string representations of all instances"""
        if not line:
            print("** class doesn't exist  **")
            return

        instances = [str(val) for key, val in storage.all().items()]
        print(instances)

    def do_update(self, line):
        """To be added"""
        pass


if __name__ == '__main__':
    HBNBCCommand().cmdloop()
