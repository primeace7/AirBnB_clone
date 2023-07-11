#!/usr/bin/python3

import cmd
import models
from models.base.model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Class that contains the entry point of the command
    interpreter
    """
    prompt = '(hbnb)'

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """
        return True

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        method not to input anything when empty
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
