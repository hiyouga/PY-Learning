#num.py
import sys
#扩展：整数->浮点数->复数
print(pow(2,10))
print(pow(2,15))
#print(pow(2,1000))
#print(pow(2,pow(2,15)))
print(0x8f)
print(0b100110)
print(0o6172)

print(sys.float_info)

print(9.6e4)
print(-77.)

z = 1.2+4j
print(z,z.real,z.imag)

print(int(4.5))
print(float(4))
print(complex(4))

print(type(z))
print(type(4.5))

print(4+5)#加减乘
print(5/3)#除
print(5//3)#整除
print(5%3)#取模
print(5**3)#取幂
print(pow(5,3))#取幂
print(abs(-5))#绝对值
print(divmod(5,3))#x÷y=m···n