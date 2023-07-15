#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    Class that contains the entry point of the command
    interpreter

    Attributes:
    prompt(str): the prompt to display when soliciting for input
    """
    prompt = '(hbnb) '
    valid_classes = ['BaseModel', 'User','Place', 'State', 'City',\
                     'Amenity', 'Review']
    storage = models.storage

    def precmd(self, line):
        '''
        Manipulate the input command line to detect special inputs like
          <class_name>.count(). Such inputs have special meaning and are
          handled a little differently. If it is found that the input command
          line doesn't contain such input, then the line is returned to be
          handled as normal

        Args:
        line(str): the input command line from the user

        Return: line
        '''
        #cmd_list is the entire input command line split into a list
        cmd_list = line.split('.', maxsplit=1)
        class_name = cmd_list[0]
        if len(cmd_list) < 2 or not self.is_valid_class(cmd_list[0]):
            return line
        else:
            func_strings = ['show', 'destroy', 'all', 'count', 'update']
            if '(' not in cmd_list[1] or ')' not in cmd_list[1]:
                print('invalid command:', line, '=> parentheses missing')
                return ''
            #root_cmd is the actual command e.g all, update
            root_cmd = cmd_list[1].split('(')[0]

            #retrieve the content enclosed by the parentheses ( and )
            hold_var = cmd_list[1].split('(')[1]

            #arg_string is content enclosed by parentheses, could be any type
            if hold_var.split(')')[0].endswith('}'):
                arg_string = hold_var.split(')')[0].split(', ', maxsplit=1)
            else:
                arg_string = hold_var.split(')')[0].split(', ')

            if root_cmd in func_strings:
                exec(f'self.special_{root_cmd}(arg_string, class_name)')
            else:
                print('invalid command:', line)

            return ''

    def special_all(self, arg_string, class_name):
        '''
        The special implementation of the all command e.g User.all() this call
          will only list all the instances of the specified type e.g User.all()
          will only list all existing User instances and none other

        Args:
        class_name(str): the instances to list e.g User
        arg_string(str): always empty for this method
        '''
        all_objs = [eval(f'{obj["__class__"]}(**obj)') for obj in\
                  self.storage.all().values() if obj['__class__'] == class_name]

        string_all = ''
        for i in range(len(all_objs)):
            if i != len(all_objs) - 1:
                string_all += (str(all_objs[i]) + ', ')
            else:
                string_all += str(all_objs[i])
        string_all = '[' + string_all + ']'
        print(string_all)

    def special_count(self, arg_string, class_name):
        '''
        The special implementation of the count command e.g User.count() this
          call will only count all the instances of the specified type
          e.g User.count() will only count all existing User instances
          and none other

        Args:
        class_name(str): the instances to list e.g User
        arg_string(str): always empty for this method

        Returns: int - the number of instances of the specified type
        '''
        count = 0
        for obj in self.storage.all().values():
            if obj['__class__'] == class_name:
                count += 1
        print(count)

    def special_show(self, arg_string, class_name):
        '''
        The special implementation of the show command e.g User.show(id). This
          call will only show the instance of the specified User objectwith
          id equal to the one specified

        Args:
        class_name(str): the instances to list e.g User
        arg_string(str): the supplied argument, instance id in this case
        '''
        line = class_name + ' ' + arg_string[0]
        self.do_show(line)

    def special_destroy(self, arg_string, class_name):
        '''
        The special implementation of the destroy command e.g User.destroy(id).
          This call will destroy the instance of the specified User object
          with id equal to the one specified

        Args:
        class_name(str): the object type to destroy e.g User
        arg_string(str): the supplied argument, instance id in this case
        '''
        line = class_name + ' ' + arg_string[0]
        self.do_destroy(line)

    def special_update(self, arg_string, class_name):
        '''
        The special implementation of the update command e.g User.destroy(id).
          This call will destroy the instance of the specified User object
          with id equal to the one specified

        Args:
        class_name(str): the object type to destroy e.g User
        arg_string(str): the supplied argument, instance id in this case
        '''
        if arg_string[-1].startswith('{') and arg_string[-1].endswith('}'):
            last_arg = eval(arg_string[-1])
            if isinstance(last_arg, dict):
                for key, val in last_arg.items():
                    line = class_name + ' ' + arg_string[0] + ' ' + key + ' '\
                        + val
                    self.do_update(line)
            else:
                print('there was a problem converting last_arg to dict')
        else:
            line = class_name + ' ' + arg_string[0] + ' ' + arg_string[1]\
                + ' ' + arg_string[2]
            self.do_update(line)

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
        new = eval(f'{line[0]}()')
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
            print(str(eval(f'{line[0]}(**obj)')))
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
            all_obj_list = [str(eval(f'{obj["__class__"]}(**obj)')) for obj in\
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
