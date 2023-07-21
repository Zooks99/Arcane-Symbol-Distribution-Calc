import numpy as np
import cvxpy as cp
req = [0, 12, 15, 20, 27, 36, 47, 60, 75, 92, 111, 132, 155, 180, 207, 236, 267, 300, 335, 372]
weeklyRates = np.array([171, 157, 122, 108, 101, 101])

#Symbol = [Current Level, Symbols gained to next level]
vj = [10, 104] 
chu = [10, 9]
lach = [9, 16]
arc = [8, 57]
mor = [9, 28]
esf = [9, 26]
symbolsUsed = 1200 # Number of symbols you would like to use on this char

syms = [vj, chu, lach, arc, mor, esf]

symsLeft = []
for i in syms:
   symsLeftTemp = req[i[0]] - i[1] + sum(req[i[0]:-1])
   symsLeft.append(symsLeftTemp)

symsLeft = np.array(symsLeft)

# Setting up optimization problem
weeksLeft = cp.Variable()
symb = cp.Variable((6),nonneg=True)
opt = cp.Minimize(weeksLeft)
const = [cp.sum(symb) == symbolsUsed, symsLeft - weeklyRates * weeksLeft - symb <= 0]

prob = cp.Problem(opt, const)
prob.solve()
distr = np.floor(symb.value)
print('Number of weeks left to max:',  np.ceil(prob.value))
print('How to distribute 1200 symbols:')
print('VJ:', distr[0])
print('Chu Chu:', distr[1])
print('Lachlein:', distr[2])
print('Arcana:', distr[3])
print('Morass:', distr[4])
print('Esfera:', distr[5])



