# Qiskit-Childs-Kothari-Somma Quantum (CKS) algorithm 
Here we try to build the CKS algorithm for systems of linear equations with exponentially improved dependence on precision  on Qiskit
(see here for more https://arxiv.org/abs/1511.02306). The CKS algorithm is build out of multiple steps, each step having its own folder with the 
starting one being GPE. In the future more folders will be added until all pieces together form the CKS.

<ins>GPE:</ins><br />
Gapped Phase Estimation, as the name suggests, estiamtes the Phase (and thus the eigenvalues) of an Hermitian input Matrix A in 
a desired interval. It's a low low-precision variant of phase estimation.

<ins>Matrix Inverse</ins><br />
A big part of solving the linear equation Ax = b is to find the inverse of A. In this Folder we estimate this inverse with a Hamiltonian 
Siimulation. 

<ins>Installing Qiskit:</ins><br />
To run the Phyton files you need to have Qiskit installed. Following the tutorial on Qiskit's main page will do it:
https://qiskit.org/documentation/getting_started.html


