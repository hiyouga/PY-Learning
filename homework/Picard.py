from sympy import symbols, Matrix, integrate, init_printing
from IPython.display import display
init_printing(use_unicode = False, wrap_line = True, no_global = True)

n = int(input("The dimension of matrix:"))
mat = []
init = []
for i in range(n):
    mat.append(list(map(int, input("The " + str(i+1) + " row of matrix:").split())))
for i in range(n):
    init.append([int(input("The " + str(i+1) + " row of initvalue:"))])
ite = int(input("Iteration:"))
A = Matrix(mat)
x0 = Matrix(init)
t, s = symbols('t s')
phi = []
phi.append(x0)
for i in range(ite):
    fun = A * phi[i]
    fun = fun.subs(t, s)
    res = x0 + integrate(fun, (s, 0, t))
    #print(res)
    phi.append(res)
print("The results are:")
for i in range(n):
    display(res[i])