import numpy as np

class Accumulator():
    def __init__(self):
        self.data = {}
        
    def append(self, **kwargs):
        for key, val in kwargs.items():
            if key not in self.data:
                self.data[key] = []
            self.data[key].append(val)
        
    def get_dict_list(self):
        return self.data
    
    def get_dict_numpy(self):
        return {key: np.array(val) for key, val in self.data.items()}
    
    def get_dict_avg(self):
        return {key: np.array(val).mean() for key, val in self.data.items()}
    
    def __item__(self, key):
        return self.data[key]
    