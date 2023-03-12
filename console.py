#!/usr/bin/python3

"""Import cmd module for shell like application"""
import cmd
import readline
import sys
from models.base_model import BaseModel
import signal

print("Welcome to the console")
print("type: help <command> to get further information about the command")
print("do <command> to carry out the command\n")
print("==========================================================\n")


class HBNBCommand(cmd.Cmd):
    """ Class for creating console to connect with backend """
    def __init__(self):
        super().__init__()
        #signal.signal(signal
        self.prompt = "(hbnb) "

    def help_update(self):
        print("Opens the filestorage.json file and updates the instance")

    def do_update(self, arg):
        """ prints hello and the arg to stdout """
        with open("filestorage.json", encoding="UTF-8", mode="r+") as file:
            pass

    def do_state(self, arg):
        """ create a state object """
            
    def emptyline(self):
        pass
      
    def do_update(self, *args, **kwargs):
        with open("filestorage.json", mode="r+", encoding="UTF-8") as f:
            pass
      
    def do_quit(self, arg):
        """ Quit the console """
        sys.exit(1)

    def do_EOF(self, arg):
        """ Exit the command interpreter on EOF"""
        sys.exit(1)
if __name__ == "__main__":
    HBNBCommand().cmdloop()
