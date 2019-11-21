import pickle
from abc import ABC


class DAO(ABC):

    def __init__(self, datasource = ''):
        self.datasource = datasource
        self.objectCache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.objectCache, open(self.datasource, 'wb'))

    def __load(self):
        self.objectCache = pickle.load(open(self.datasource, 'rb'))

    def add(self, key, obj):
        self.objectCache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.objectCache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.objectCache.pop[key]
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.objectCache.values()
