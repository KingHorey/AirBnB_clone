#!/usr/bin/python3

""" import cmd module to have commandline
features for testing code and backend services"""

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """ AirBnb cmd class for AirBnb project clone """

    prompt = "(hbnb) "

    def help(self):
        """ prints the help functions for the cmd class """

    def do_quit(self, arg):
        """ exit the interpreter by typing quit"""
        sys.exit(0)

    def do_EOF(self, arg):
        """ exits program at the end of file (EOF) """
        sys.exit(1)

    def emptyline(self):
        """ Prevents the execution of the previous command
        when enter ↵ is pressed on an emptyline"""
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()
