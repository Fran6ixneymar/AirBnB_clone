import json
from os.path import exists


class FileStorage:
    """
    This class handles serialization and 
    deserialization of instances to a JSON file.
    It provides methods to store instances in memory, 
    save them to a file, and reload them from the file.
    """

    __file_path = "file.json"  # The path to the JSON file
    __objects = {}  # Dictionary to store instances

    def all(self):
        """
        Retrieve all instances stored in memory.

        Returns:
            dict: A dictionary containing all the instances.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new instance to the dictionary.

        Args:
            obj: The instance to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize the instances and save them to a JSON file.
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserialize instances from the JSON file and load them into memory.
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    self.__objects[key] = class_.from_dict(obj_dict)


# Create an instance of FileStorage and load data from the JSON file
storage = FileStorage()
storage.reload()

