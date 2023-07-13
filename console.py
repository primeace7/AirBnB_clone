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

    def __is_valid_class(class_name):
        '''
        Determine if an input string represents a valid class name

        Args:
        class_name(str): the class name to check for validity

        Returns: True if class_name is a valid class name, False otherwise
        '''
        return class_name in valid_classes

    def get_object(class_name, obj_id):
        '''
        Get an object from storage based on its id and type

        Args;
        class_name(str): the name of the type to which the desired
            object belongs, i.e, its type
        obj_id(str): the id of the object to get

        Returns: The dictionary representation of the object if found,
            None otherwise
        '''
        all_objects = storage.all()
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
        elif not is_valid_class(line[0]):
            print('** class doesn\'t exist **')
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
        elif not is_valid_class(line[0]):
            print('** class doesn\'t exist **')
        elif len(line) == 1:
            print("** instance id missing **")
        elif (obj = get_object(line[0], line[1]):
              print(obj)
        else:
              print(('** no instance found **')

    def do_destroy(self, line):
                    '''
        Delete an instance using the class name and the instance id

        Args:
        line(str): the user's input string representing the instance to destroy
        '''
                    line = line.split()
        if line is None or len(line) == 0:
                    print("** class name missing **")
        elif not is_valid_class(line[0]):
                    print("** class doesn't exist **")
        elif len(line) == 1:
                    print('** instance id missing **')
        elif (obj = get_object(line[0], line[1])):
                    del storage.all()[line[1]]
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
        if len(line) >= 1 and not is_valid_class(line[0]):
                    print("** class doesn't exist **")
        else:
                    print(storage.all().values())


    def do_update(self, line):
                    '''
        Print the string representation of all instances of the class name
            entered by user

        Args:
        line(str): the name of the class to print the instances of
        '''
                    line = line.split()
        if line is None or len(line) == 0:
                    print("** class doesn't exist **")
        elif len(line) == 1:
                    print("** instance id missing **")
        elif len(line) == 2:
                    print("** instance id missing **")
        elif len(line) == 3:
                    print("** value missing **")
        elif not (obj = get_object(line[0], line[1])):
                    print("** no instance found **")
        else:
            obj[line[2]] = line[3]

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
