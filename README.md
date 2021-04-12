# Qiskit-Childs-Kothari-Somma Quantum (CKS) algorithm 
Here we try to build the CKS algorithm for systems of linear equations with exponentially improved dependence on precision  on Qiskit
(see here for more https://arxiv.org/abs/1511.02306)

How to use it:
Run GUI.py 

What it does:
Phae_Estimation_IPE.py is an implementation of Iterative Phase Estiamation (IPE). When given an unitary U and an eigenstate of U denoted by |Ψ> such that:
U|Ψ> = exp(2πiϕ)|Ψ> 
This algorithm returns ϕ and thus the eigenvalue. (See here for more: https://arxiv.org/abs/quant-ph/0610214v2)

What it doesn't (yet):
The calculated eigenvalues for 3x3 or bigger matrices are bugged and returns undesired values. 

Why we need Phase_Estimation_IPE.py:
After running Phase_Estimation_IPE.py our System get prepared into the state that we need for the next step of implementing the CKS algorithm, 
namely implementing the inverse of the input matrix A with Hamiltonmian Simulation.

