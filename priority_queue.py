class PriorityQueue:
    pivot_value = {}
    value_key = {}
    keys=[]

    
 
    def get(self):
        key = self.keys[0]
        value = self.pivot_value[key]
        del self.pivot_value[key]
        del self.value_key[value]
        self.keys = self.keys[1:]
        return value

    def put(self, key, valueue):
        if valueue in list(self.value_key.keys()):
            okey = self.value_key[valueue]
            self.value_key[valueue] = key
            self.pivot_value[key] = valueue
            self.keys[self.keys.index(okey)]=key
            self.keys.sort()
        else:
            self.pivot_value[key] = valueue
            self.value_key[valueue] = key
            self.keys.append(key)
            self.keys.sort()


