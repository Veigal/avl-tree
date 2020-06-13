########################################################
#Author: Leonardo Deitos Veiga
########################################################

class Node:
    def __init__(self, name, source = None, target_left = None, target_right = None ):
        self.source = source
        self.name = name
        self.target_left = target_left
        self.target_right = target_right

    #Sets
    def set_source(self, source):
        self.source = source

    def set_name(self, name):
        self.name = name

    def set_target_left(self, target_left):
        self.target_left = target_left

    def set_target_right(self, target_right):
        self.target_right = target_right

  
    #Gets
    def get_source(self):
        return self.source

    def get_name(self):
        return self.name
        
    def get_target_left(self):
        return self.target_left

    def get_target_right(self):
        return self.target_right

