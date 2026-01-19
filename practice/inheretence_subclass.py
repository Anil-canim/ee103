class Worker:
    def __init__(self,name:str,income:float):
        self.name=name
        self.income=income
    def info(self):
        return print(f"Object: {self.name}, income: {self.income}")
    def addition(self,extra_percent):
        self.income += self.income*extra_percent/100
        return self.income
class Admin(Worker):
    def __init__(self, name, income,bonus):
        super().__init__(name, income)
        self.bonus=bonus
    def addition(self, extra_percent):
        self.income += self.income*extra_percent/100+self.income*self.bonus/100
        return self.income
    
worker1=Worker("esteban",5000)
admin=Admin("rex,",15000,20)
income_info=(admin.addition(50), worker1.addition(50))
(worker1.info(),"and",admin.info())
print("------------------------------")
print(income_info)