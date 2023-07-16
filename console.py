import cmd
import re
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
        "BaseModel"
    }

    def emptyline(self):
        pass

    def default(self, arg):
        print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def do_create(self, arg):
        argl = re.findall(r"[\w\[\]]+", arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(argl[0])()
            print(instance.id)
            storage.save()

    def do_show(self, arg):
        argl = re.findall(r"[\w\[\]]+", arg)
        obj_dict = storage.all()
        if len(argl) != 2 or argl[0] not in HBNBCommand.classes:
            print("** syntax error **")
        else:
            obj_key = "{}.{}".format(argl[0], argl[1])
            if obj_key in obj_dict:
                print(obj_dict[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        argl = re.findall(r"[\w\[\]]+", arg)
        obj_dict = storage.all()
        if len(argl) != 2 or argl[0] not in HBNBCommand.classes:
            print("** syntax error **")
        else:
            obj_key = "{}.{}".format(argl[0], argl[1])
            if obj_key in obj_dict:
                del obj_dict[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        argl = re.findall(r"[\w\[\]]+", arg)
        obj_dict = storage.all()
        objects = []
        if len(argl) == 0 or argl[0] in HBNBCommand.classes:
            for obj_key in obj_dict:
                class_name, obj_id = obj_key.split('.')
                if len(argl) == 0 or argl[0] == class_name:
                    objects.append(str(obj_dict[obj_key]))
        else:
            print("** class doesn't exist **")
            return
        print('\n'.join(objects))

    def do_count(self, arg):
        argl = re.findall(r"[\w\[\]]+", arg)
        count = 0
        if len(argl) == 1 and argl[0] in HBNBCommand.classes:
            obj_dict = storage.all()
            for obj_key in obj_dict:
                class_name, obj_id = obj_key.split('.')
                if class_name == argl[0]:
                    count += 1
        else:
            print("** class doesn't exist **")
            return
        print(count)

    def do_update(self, arg):
        argl = re.findall(r"[\w\[\]\{\}]+'[^']*'|\w+", arg)
        obj_dict = storage.all()

        if len(argl) < 3:
            print("** syntax error **")
            return

        class_name = argl[0]
        obj_id = argl[1]
        attr = argl[2]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if "{}.{}".format(class_name, obj_id) not in obj_dict:
            print("** no instance found **")
            return

        obj = obj_dict["{}.{}".format(class_name, obj_id)]

        if len(argl) == 3:
            print("** attribute name missing **")
        elif len(argl) == 4:
            value = argl[3].strip("'")
            setattr(obj, attr, value)
            storage.save()
        elif len(argl) == 5:
            attr_dict = eval(argl[3])
            for key, value in attr_dict.items():
                setattr(obj, key, value)
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

