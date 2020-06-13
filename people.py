class People:
    def __init__(self, cpf, rg, name, b_date, b_city):
        self.cpf = cpf
        self.rg = rg
        self.name = name
        self.b_date = b_date
        self.b_city = b_city

    def get_cpf(self):
        return self.cpf
        
    def get_rg(self):
        return self.rg

    def get_name(self):
        return self.name

    def get_b_date(self):
        return self.b_date

    def get_b_city(self):
        return self.b_city

    def string(self):
        return "CPF: " + self.cpf + "; " + "RG: " + self.rg + "; " + "Nome: " + self.name + "; " + "Data de nascimento: " + self.b_date + "; " + "Cidade de nascimento: " + self.b_city