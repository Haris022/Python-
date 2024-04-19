#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install cvxpy


# In[21]:


import cvxpy as cp
import numpy as np

# Problem parameters
n = 30  # Number of components
q = 23   # Example value for q, representing levels or steps
beta = 100  # Example value for beta, representing an upper bound

# Variables
u = cp.Variable(n, integer=True)  # Positive contributions
v = cp.Variable(n, integer=True)  # Negative contributions
M = cp.Variable()  # For Infinity Norm

 
objective = cp.Minimize(cp.sum(u + v))  # Minimize L1 Norm
for i in range(5):
    run_optimization()
# Constraints incorporating beta and q
constraints = [
    u + v >= 1,  # Ensuring a non-trivial solution
    u >= 0,
    v <= 0,
    u + v <= M,  # Infinity norm constraint
    u <= beta,   # Applying beta as an upper bound
    cp.abs(u + v) <= q  # Incorporating q as a limit or range for decisions
]

# Define and solve the problem
problem = cp.Problem(objective, constraints)
problem.solve()

print("Objective value:", problem.value)
print("Solution for u:", u.value)
print("Solution for v:", v.value)
print("Maximum magnitude (M):", M.value)


# In[ ]:




