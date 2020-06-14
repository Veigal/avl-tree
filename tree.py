########################################################
#Author: Leonardo Deitos Veiga
########################################################

from node import Node 
from people import People 

class Tree:
    def __init__(self, indexer):
        self.root = None
        self.indexer = indexer

    def get_order(self, node):
        if self.indexer == "cpf":
            return node.get_key().get_cpf()
        elif self.indexer == "birth":
            return node.get_key().get_b_date()
        else:
            return node.get_key().get_name()
    
    def get_root(self):
        return self.root

    def search_node(self, wanted_node_name, show_rote):
        return self.rsearch_node(wanted_node_name, self.root, show_rote)

    def rsearch_node(self, wanted_node_name, current_node, show_rote):
        if current_node == None:
            if show_rote:
                print("Fim da busca")
            return None
        if show_rote:
            print("\nPassou pelo nodo: " + str(current_node.get_key()))
        if str(wanted_node_name) == current_node.get_key().get_cpf():
            if show_rote:
                print("Fim da busca")
            return current_node
        return self.rsearch_node(wanted_node_name, current_node.get_target_left() if str(wanted_node_name) < current_node.get_key().get_cpf() else current_node.get_target_right(), show_rote)

    def search_range_bdate(self, start_date, end_date):
        people_list = []
        self.rsearch_range_bdate(int(start_date), int(end_date), self.root, people_list)
        return people_list
    
    def rsearch_range_bdate(self, start_date, end_date, node, people_list):
        if node == None:
            return
        date = node.get_key().get_b_date()
        if int(date) >= start_date and int(date) <= end_date:
            people_list.append(node.get_key())
        if int(date) <= end_date:
            self.rsearch_range_bdate(start_date, end_date, node.get_target_right(), people_list)
        if int(date) >= start_date:
            self.rsearch_range_bdate(start_date, end_date, node.get_target_left(), people_list)

    def search_people_by_name(self, name):
        people_list = []
        self.rsearch_people_by_name(name, self.root, people_list)
        return people_list    

    def rsearch_people_by_name(self, name, node, people_list):
        if node == None:
            return
        actual_name = node.get_key().get_name()
        if actual_name >= name:
            if actual_name.find(name, 0, len(name)) != -1:
                people_list.append(node.get_key())              
            self.rsearch_people_by_name(name, node.get_target_right(), people_list)
            self.rsearch_people_by_name(name, node.get_target_left(), people_list)
        if actual_name < name:
            self.rsearch_people_by_name(name, node.get_target_right(), people_list)

    def insert_node(self, inserted_node):
        if self.root == None:
            self.root = Node(inserted_node)
        else:
            new_node = Node(inserted_node)
            self.rinsert_node(new_node, self.root) 
            self.root.set_source(None)
            self.balance(new_node, 1)

    def rinsert_node(self, inserted_node, current_node):
        if self.get_order(inserted_node) == self.get_order(current_node):
            return
        elif self.get_order(inserted_node) > self.get_order(current_node):
            if current_node.get_target_right() == None:
                current_node.set_target_right(inserted_node)
                inserted_node.set_source(current_node)
                return
            self.rinsert_node(inserted_node, current_node.get_target_right())
        else:
            if current_node.get_target_left() == None:
               current_node.set_target_left(inserted_node)
               inserted_node.set_source(current_node)
               return
            self.rinsert_node(inserted_node, current_node.get_target_left())
    
    def symple_rotation_right(self, current_node):
        left_node = current_node.get_target_left()

        if current_node == self.root:
            self.root = left_node
        else:    
            left_node.set_source(current_node.get_source())
            if current_node.get_source().get_target_left() == current_node:
                current_node.get_source().set_target_left(left_node)
            else:
                current_node.get_source().set_target_right(left_node)

        current_node.set_target_left(left_node.get_target_right())

        if left_node.get_target_right() != None:
            left_node.get_target_right().set_source(current_node)

        left_node.set_target_right(current_node)
        current_node.set_source(left_node)

    def symple_rotation_left(self, current_node):
        right_node = current_node.get_target_right()

        if current_node == self.root:
            self.root = right_node
        else:    
            right_node.set_source(current_node.get_source())
            if current_node.get_source().get_target_left() == current_node:
                current_node.get_source().set_target_left(right_node)
            else:
                current_node.get_source().set_target_right(right_node)

        current_node.set_target_right(right_node.get_target_left())

        if right_node.get_target_left() != None:
            right_node.get_target_left().set_source(current_node)

        right_node.set_target_left(current_node)
        current_node.set_source(right_node)

    def double_rotation_right(self, current_node):
        self.symple_rotation_left(current_node.get_target_left())
        self.symple_rotation_right(current_node)

    def double_rotation_left(self, current_node):
        self.symple_rotation_right(current_node.get_target_right())
        self.symple_rotation_left(current_node)

    def height(self, current_node):
        if current_node == None:
            return -1
        return 1 + max(self.height(current_node.get_target_left()), self.height(current_node.get_target_right()))    
        
    def balance(self, current_node, adjust_more_nodes):
        if current_node == None:
            return
        factor_current = self.factor(current_node)
        factor_left = self.factor(current_node.get_target_left())
        factor_right = self.factor(current_node.get_target_right())

        if factor_current > 1 and factor_left > 0:
            self.symple_rotation_right(current_node)
            if adjust_more_nodes:
                return
        elif factor_current < -1 and factor_right < 0:
            self.symple_rotation_left(current_node)
            if adjust_more_nodes:
                return
        elif factor_current > 1 and factor_left < 0:
            self.double_rotation_right(current_node)
            if adjust_more_nodes:
                return
        elif factor_current < -1 and factor_right > 0:
            self.double_rotation_left(current_node)
            if adjust_more_nodes:
                return

        self.balance(current_node.get_source(), adjust_more_nodes)  

    def factor(self, node):
        if node == None:
            return 0
        node_left = node.get_target_left() 
        node_right = node.get_target_right()
        return self.height(node_left) - self.height(node_right)