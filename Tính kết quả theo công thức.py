#Tính CT
import math
c=50
h=30
value = []
items=[x for x in input("Nhập giá trị của d: ").split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# Kết quả
print (','.join(value))
    
