import numpy as np
data_type=[('name','S15'),('class',int),('height',float)]
student_details=[('john',5,40.2),('Gillian',9,43.5),('Jethro',6,39.0),('Anna',12,44.6)]

student=np.array(student_details,dtype=data_type)
print(f"original array \n {student}")
print("sorted by height: \n ")
print(np.sort(student,order="height"))