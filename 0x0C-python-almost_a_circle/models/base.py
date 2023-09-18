#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, Id=None):
        """class constructor"""
        if Id is not None:
            self.id = Id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps([obj.to_dictionary() for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            val = cls.to_json_string(list_objs)
            f.write(val)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                json_str = f.read()
                if json_str:
                    dict_list = cls.from_json_string(json_str)
                    instances = [cls.create(**d) for d in dict_list]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []
