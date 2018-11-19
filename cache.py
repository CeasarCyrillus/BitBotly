import sys
class Cache():
    def __init__(self):
        self.data = {}
        self.valid_matrix = {}

    def no_key_error(self, key, namespace=False):
        if not namespace:
            print("key '"+str(key)+"' does not exsist in cache")
        else:
            print("key '"+str(key)+"' does not exsist in namespace '"+str(namespace)+"'")

    def add(self, key, value, lifetime=namespace=False):
        if not namespace:
            self.data[key] = value
        else:
            self.data[namespace+"_"+key] = value
    
    def get(self, key, namespace=False):
        result = False
        try:
            if not namespace:
                result = self.data[key]
            else:
                result = self.data[namespace+"_"+key]
        except KeyError:
            no_key_error(key, namespace)
    
    def remove_namespace(self, namespace):
        try:
            for key in self.data.keys():
                if(key.startswith(namespace+"_")):
                    self.remove(key, namespace)
        except KeyError:
            no_key_error(key, namespace)

    def remove(self, key, namespace=False):
        try:
            if not namespace:
                del self.data[key]
            else:
                del self.data[namespace+"_"+key]
        except KeyError:
            no_key_error(key, namespace)