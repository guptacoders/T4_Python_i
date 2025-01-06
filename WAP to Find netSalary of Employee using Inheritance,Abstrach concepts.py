# Code Practice

from abc import ABC,abstractmethod

class Employee(ABC):
    
    def getEmployee(self):
        self.id=input("Enter User Id:")
        self.nm=input("Enter User Name:")
        self.sal=int(input("Enter User Salary:"))
    
    def printEmployeeDetails(self):
        print("User Id: ",self.id)
        print("User Name: ",self.nm)
        print("User Salary: ",self.sal)
        
    def getSalary(self):
        return self.sal
    
    @abstractmethod
    def emp_id(self):
        pass
        
        
class Perks(Employee):
    
    
    def calcPerks(self):
        self.getEmployee()
        x=self.getSalary()
        self.da=x*0.35
        self.hra=x*0.17
        self.pf=x*0.12
        
        
    def putPerks(self):
        print("Dearness Allowance(DA): ",self.da)
        print("House Rent Allowance(HRA): ",self.hra)
        print("Provident Fund(PF): ",self.pf)
        
    def totalPerks(self):
        return self.da+self.hra-self.pf
    def emp_id(self):
        print("hi")
    
    
    
class NetSalary(Perks):
       
    def getTotal(self):
        self.calcPerks()
        self.ns=self.getSalary()+self.totalPerks()
    
    def showTotal(self):
        print("Employee Details: ")
        super().printEmployeeDetails()
        
        super().putPerks()
        
        print("Net Salary: ",self.ns)
        
e=NetSalary()
e.getTotal()
e.showTotal()
