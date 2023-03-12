#!/usr/bin/python3

"""Import cmd module for shell like application"""
import cmd
""" readline allows for an empty line to not process
previous command"""
import readline
""" sys module to exit interpreter """
import sys


class HBNBCommand(cmd.Cmd):
    """ Class for creating console to connect with backend """
    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb) "

    def emptyline(self):
        """ Prevents execution of previous command
        when enter is pressed on an empty line"""
        pass

    def do_quit(self, arg):
        """ Quit the console """
        sys.exit(1)

    def do_EOF(self, arg):
        """ Exit the command interpreter on EOF"""
        sys.exit(1)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
