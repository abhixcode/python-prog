#!/usr/bin/python

class Employee:
  'Common base class for all Employees'
  empCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1 #why prefix classname before?

  def displayCount(self):
    print "Total Employee %d" % Employee.empCount

  def displayEmployee(self):
    print "Name : ",self.name, " , Salary : ",self.salary


emp1 = Employee("Abhinav",96000)
emp2 = Employee("Aby",1000000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee : %d" % Employee.empCount
