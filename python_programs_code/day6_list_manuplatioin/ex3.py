#!/usr/bin/python

inp=[12,24,35,24,88,120,155,88,120,155]

emp=[]

for i in inp:
	if i not in emp:
		emp.append(i)

emp.reverse()
print emp
