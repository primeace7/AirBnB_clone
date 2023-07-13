#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Class that contains the entry point of the command
    interpreter

    Attributes:
    prompt(str): the prompt to display when soliciting for input
    """
    prompt = '(hbnb) '
    valid_classes = ['BaseModel']
    storage = models.storage

    def is_valid_class(self, class_name):
        '''
        Determine if an input string represents a valid class name

        Args:
        class_name(str): the class name to check for validity

        Returns: True if class_name is a valid class name, False otherwise
        '''
        return class_name in self.valid_classes

    def get_object(self, class_name, obj_id):
        '''
        Get an object from storage based on its id and type

        Args;
        class_name(str): the name of the type to which the desired
            object belongs, i.e, its type
        obj_id(str): the id of the object to get

        Returns: The dictionary representation of the object if found,
            None otherwise
        '''
        all_objects = self.storage.all()
        for obj in all_objects.keys():
            #split each key into a list of class name and it's id
            obj_split = obj.split('.')
            if (class_name, obj_id) == (obj_split[0], obj_split[1]):
                return all_objects[obj]
        return None

    def do_create(self, line):
        '''
        Create an instance of <line>, provided <line> is a valid class name

        Args:
        line(str): the user's input string representing the class to instantiate
        '''
        line = line.split()
        if line is None or len(line) == 0:
            print('** class name missing **')
            return
        elif not self.is_valid_class(line[0]):
            print('** class doesn\'t exist **')
            return
        new = BaseModel()
        new.save()
        print(new.id)

    def do_show(self, line):
        '''
        print a string representation of an instance based on the name given by
        user and the id

        Args:
        line(str): the user's input string representing the instance to print
        '''
        line = line.split()
        if line is None or len(line) == 0:
            print('** class name missing **')
            return
        elif not self.is_valid_class(line[0]):
            print('** class doesn\'t exist **')
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        obj = self.get_object(line[0], line[1])
        if (obj is not None):
            print(str(BaseModel(**obj)))
        else:
            print('** no instance found **')

    def do_destroy(self, line):
        '''
        Delete an instance using the class name and the instance id

        Args:
        line(str): the user's input string representing the instance to destroy
        '''
        line = line.split()
        if line is None or len(line) == 0:
            print("** class name missing **")
            return
        elif not self.is_valid_class(line[0]):
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print('** instance id missing **')
            return
        obj = self.get_object(line[0], line[1])
        if (obj is not None):
            del self.storage.all()[f'{line[0]}.{line[1]}']
            self.storage.save()
        else:
            print('** no instance found **')

    def do_all(self, line):
        '''
        Print the string representation of all instances of the class name
            entered by user, as a list

        Args:
        line(str): the name of the class to print the instances of
        '''
        line = line.split()
        if len(line) >= 1 and not self.is_valid_class(line[0]):
            print("** class doesn't exist **")
            return
        else:
            all_obj_list = [str(BaseModel(**obj)) for obj in\
                        self.storage.all().values()]
            print(all_obj_list)

    def do_update(self, line):
        '''
        Print the string representation of all instances of the class name
            entered by user

        Args:
        line(str): the name of the class to print the instances of
        '''
        line = line.split()
        if line is None or len(line) == 0:
            print("** class name missing **")
            return
        elif not self.is_valid_class(line[0]):
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        elif len(line) == 2:
            print("** attribute name missing **")
            return
        elif len(line) == 3:
            print("** value missing **")
            return
        obj = self.get_object(line[0], line[1])
        if obj is None:
            print("** no instance found **")
        else:
            obj = self.get_object(line[0], line[1])
#add a new value to the dict of the object whose key is line[2]
            obj[line[2]] = line[3]
            self.storage.save()

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
