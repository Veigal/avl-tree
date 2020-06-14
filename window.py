########################################################
#Author: Leonardo Deitos Veiga
########################################################
from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as ScrolledText
from tree import Tree 
from node import Node 
from people import People 
import re

class Window:
    def __init__(self, master=None):

        self.default_font = ("Arial", "10")

        self.main_container = Frame(master)
        self.main_container["pady"] = 10
        self.main_container.pack()

        self.directory_container = Frame(master)
        self.directory_container["padx"] = 20
        self.directory_container.pack()

        self.cpf_container = Frame(master)
        self.cpf_container["padx"] = 20
        self.cpf_container["pady"] = 10
        self.cpf_container.pack()
        
        self.name_container = Frame(master)
        self.name_container["padx"] = 20
        self.name_container["pady"] = 10
        self.name_container.pack()

        self.birth_container = Frame(master)
        self.birth_container["padx"] = 20
        self.birth_container["pady"] = 10
        self.birth_container.pack()

        ###########################
        self.main_label = Label(self.main_container, text="Busca de pessoas")
        self.main_label["font"] = ("Arial", "10", "bold")
        self.main_label.pack()

        # Archive
        self.button_directory = Button(self.directory_container)
        self.button_directory["text"] = "Procurar arquivo"
        self.button_directory["font"] = ("Calibri", "8")
        self.button_directory["width"] = 15
        self.button_directory["command"] = self.search_archive
        self.button_directory.pack()

        # CPF
        self.cpf_label = Label(self.cpf_container,text="CPF:", font=self.default_font)
        self.cpf_label.pack(side=LEFT)

        self.cpf = Entry(self.cpf_container)
        self.cpf["width"] = 30
        self.cpf["font"] = self.default_font
        self.cpf.pack(side=LEFT)

        self.button_cpf = Button(self.cpf_container)
        self.button_cpf["text"] = "Buscar pelo CPF"
        self.button_cpf["font"] = ("Calibri", "8")
        self.button_cpf["width"] = 15
        self.button_cpf["command"] = self.search_by_cpf
        self.button_cpf.pack()  

        # Name
        self.name_label = Label(self.name_container,text="Nome:", font=self.default_font)
        self.name_label.pack(side=LEFT)

        self.name = Entry(self.name_container)
        self.name["width"] = 30
        self.name["font"] = self.default_font
        self.name.pack(side=LEFT)

        self.button_name = Button(self.name_container)
        self.button_name["text"] = "Buscar pelo nome"
        self.button_name["font"] = ("Calibri", "8")
        self.button_name["width"] = 15
        self.button_name["command"] = self.search_by_name
        self.button_name.pack()  

        # Date of birth
        self.birth_label1 = Label(self.birth_container,text="Data de nascimento de ", font=self.default_font)
        self.birth_label1.pack(side=LEFT)

        self.birth_initial = Entry(self.birth_container)
        self.birth_initial["width"] = 10
        self.birth_initial["font"] = self.default_font
        self.birth_initial.pack(side=LEFT)
        
        self.birth_label2 = Label(self.birth_container,text="até ", font=self.default_font)
        self.birth_label2.pack(side=LEFT)

        self.birth_final = Entry(self.birth_container)
        self.birth_final["width"] = 10
        self.birth_final["font"] = self.default_font
        self.birth_final.pack(side=LEFT)

        self.button_birth = Button(self.birth_container)
        self.button_birth["text"] = "Buscar pelo nascimento"
        self.button_birth["font"] = ("Calibri", "8")
        self.button_birth["width"] = 20
        self.button_birth["command"] = self.search_by_date_birth
        self.button_birth.pack()

    def search_archive(self):
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
       
        people_file = open(root.filename, 'r')

        self.t_birth = Tree("birth")
        self.t_name = Tree("name")
        self.t_cpf = Tree("cpf")

        b_date = []

        for line in people_file:
            columns = line.split(";")
            b_date = columns[3].split("/")
            columns[3] = b_date[2] + b_date[1] + b_date[0]
            people = People(columns[0], columns[1], columns[2], columns[3], columns[4]) 
            self.t_birth.insert_node(people)
            self.t_name.insert_node(people)
            self.t_cpf.insert_node(people)

    def search_by_cpf(self):
        cpf = re.sub("[^0-9]", "", self.cpf.get())
        people_list = []
        people_list.append(self.t_cpf.search_node(cpf, 0).get_key())
        self.show_list_of_people(people_list)

    def search_by_name(self):
        name = self.name.get()
        people_list = []
        people_list = self.t_name.search_people_by_name(name)
        self.show_list_of_people(people_list)

    def search_by_date_birth(self):
        
        pic_date = []
        
        pic_date = self.birth_initial.get().split("/")
        birth_initial = pic_date[2] + pic_date[1] + pic_date[0]
        
        pic_date = self.birth_final.get().split("/")
        birth_final = pic_date[2] + pic_date[1] + pic_date[0]

        if birth_initial > birth_final:
            birth_initial += birth_final
            birth_final = birth_initial - birth_final
            birth_initial = birth_initial - birth_final
        
        people_list = []
        people_list = self.t_birth.search_range_bdate(birth_initial, birth_final)
        
        self.show_list_of_people(people_list)

    def show_list_of_people(self, people_list):
        if len(people_list) > 0:
            master = Tk()

            st = ScrolledText.ScrolledText(master)
            st.pack()

            for i in range(len(people_list)):
                st.insert(END, people_list[i].string())
                
root = Tk()
Window(root)
root.mainloop()  
