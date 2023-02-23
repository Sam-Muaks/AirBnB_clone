#!/usr/bin/python3
""" BaseModel """
from datetime import datetime
import models
import uuid


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Initialize objects """
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self,
                            k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == '__class__':
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """ String representation """
        dic = dict(self.__dict__)
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, dic)

    def save(self):
        """ Update and save object """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return directory """
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = datetime.isoformat(dic['created_at'])
        dic['updated_at'] = datetime.isoformat(dic['updated_at'])
        return dic
