#!/usr/bin/python3
"""Base class"""
import json
import csv


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
        result = []
        for obj in list_dictionaries:
            if not isinstance(obj, dict):
                result.append(obj.to_dictionary())
            else:
                result.append(obj)
        return json.dumps(result)

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
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for ob in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
                elif cls.__name__ == "Square":
                    writer.writerow([ob.id, ob.size, ob.x, ob.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + '.csv'
        instances = []
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    r0 = int(row[0])
                    r1 = int(row[1])
                    r2 = int(row[2])
                    r3 = int(row[3])
                    r4 = int(row[4])
                    if cls.__name__ == "Rectangle":
                        instances.append(cls(r1, r2, r3, r4, r0))
                    elif cls.__name__ == "Square":
                        instances.append(cls(r1, r2, r3, r0))
        except FileNotFoundError:
            return []

        return instances
