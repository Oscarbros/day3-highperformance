# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:58:17 2021

@author: oscbr226
"""

#Class for a person, which has a firstname and a last name.

class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getFullName(self):
        fullname = self.firstname + ' ' + self.lastname
        return fullname
    
#Class containing students. This class is a subclass of the Person class.

class Student(Person):
    def __init__(self, firstname, lastname, subjectArea):
        super(Student, self).__init__(firstname, lastname)
        self.subjectArea = subjectArea
        
    def printNameSubject(self):
        name = self.getFullName()
        nameSubject = name + ', ' + self.subjectArea
        print(nameSubject)
    
#Class containing teachers. This class is a subclass of the Person class.

class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super(Teacher, self).__init__(firstname, lastname)
        self.course = course
        
    def printNameCourse(self):
        name = self.getFullName()
        nameCourse = name + ', ' + self.course
        print(nameCourse)