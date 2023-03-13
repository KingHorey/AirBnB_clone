#!/usr/bin/python3

"""
    --> Import cmd module for shell like application
    --> readline allows for an empty line to not process
        previous command
    --> sys module to exit interpreter
    --> import basemodel so instances can be created
    --> import storage to store files into json file
"""
import cmd
import readline
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class for creating console to connect with backend """
    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb) "

    def do_all(self, arg):
        """ prints a string representation of all instances """
        if (arg):
            if (arg in globals()):
                db = storage.all()
                for k in db.keys():
                    txt = k.split(".")
                    if arg == txt[0]:
                        print(str(db[k]))
            else:
                print("** class doesn't exist **")
        else:
            db = storage.all()
            for k in db.values():
                print(str(k))

    def do_create(self, arg):
        """ creates a new instance, caves to JSON and prints id """
        if (arg):
            if (arg in globals()):
                model = globals()[arg]()
                storage.save()
                print(model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ deletes an instance based on the class name and id """
        if (arg):
            text = arg.split(" ")
            if text[0] in globals():
                if len(text) == 2:
                    name = text[0]
                    ids = text[1]
                    key = "{}.{}".format(name, ids)
                    db = storage.all()
                    if key in db:
                        del db[key]
                        return
                    print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_EOF(self, arg):
        """ Exit the command interpreter on EOF"""
        sys.exit(1)

    def emptyline(self):
        """ Prevents execution of previous command
        when enter is pressed on an empty line"""
        pass

    def do_quit(self, arg):
        """ Quit the console """
        sys.exit(1)

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id """
        if (arg):
            text = arg.split(" ")
            if (text[0] in globals()):
                if len(text) == 2:
                    name = text[0]
                    ids = text[1]
                    f_text = "{}.{}".format(name, ids)
                    info = storage.all()
                    if f_text in info:
                        print(info[f_text])
                        return
                    print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """updates an instance based on the class name and id"""
        if arg:
            text = arg.split(" ")
            if text[0] in globals():
                if len(text) == 2:
                    print("** attribute name missing **")
                elif len(text) == 3:
                    print("** value missing **")
                elif len(text) == 4:
                    obj_name = text[0]
                    obj_id = text[1]
                    obj_attr = text[2]
                    obj_value = text[3]
                    key = "{}.{}".format(obj_name, obj_id)
                    db = storage.all()
                    if key in db:
                        db[key][obj_attr] = obj_value
                        # temp_instancsave()e(**)
                        # storage.
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
