#!/usr/bin/python3
""" File Storage Management """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ FileStorage Class """
    __file_path = './file.json'
    __objects = {}

    def all(self):
        """ Return all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Add an object to the dictionary """
        FileStorage.__objects[type(obj).__name__+"."+obj.id] = obj

    def save(self):
        """ Serialize objects """
        with open(FileStorage.__file_path, 'w') as f:
            dic = {}
            for k in FileStorage.__objects.keys():
                dic[k] = FileStorage.__objects[k].to_dict()
            json.dump(dic, f)

    def reload(self):
        """ Deserialize objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dic = json.load(f)
                for k, v in dic.items():
                    cl = k.split(".")[0]
                    cl += '(**{})'.format(dict(v))
                    new_obj = eval(cl)
                    FileStorage.__objects[k] = new_obj
        except:
            pass
