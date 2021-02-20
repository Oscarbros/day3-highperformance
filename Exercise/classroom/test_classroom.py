# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:17:54 2021

@author: oscbr226
"""

#Script to test classroom package

from person import Student
from person import Teacher

me = Student('Oscar', 'Brostrom', 'Biology')
me.printNameSubject()

teacher = Teacher('Filipe', 'Maia', 'Advanced Scientific Programming')
teacher.printNameCourse()