# Qiskit-Childs-Kothari-Somma Quantum (CKS) algorithm 
Here we try to build the CKS algorithm for systems of linear equations with exponentially improved dependence on precision  on Qiskit
(see here for more https://arxiv.org/abs/1511.02306)

<ins>How to use it:</ins><br />
Run GUI.py<br />
It is based on the Kivy language, an installation guide can be found here https://kivy.org/doc/stable/gettingstarted/installation.html

<ins>What it does:</ins><br />
Phase_Estimation_IPE-py is an implementation of Iterative Phase Estiamation (IPE). When given an unitary U and its eigenstate |Ψ> such that:<br />
U|Ψ> = exp(2πiϕ)|Ψ> <br />
This algorithm returns ϕ and thus the eigenvalue. (See here for more: https://arxiv.org/abs/quant-ph/0610214v2)

<ins>What it doesn't (yet):</ins><br />
The calculated eigenvalues are bugged and returns undesired values. Needs to be solved. <br />
Add imaginary numbers as input<br />
Show eigenvalue in GUI for 2 x 2 matrices<br />
As of now the GUI has to be termianted with the task manager. Add exit button in the future. 


<ins>Why we need Phase_Estimation_IPE.py:</ins><br />
After running Phase_Estimation_IPE.py our System gets prepared into the state  we need for the next step of implementing the CKS algorithm, 
namely implementing the inverse of the input matrix A with Hamiltonmian Simulation.

<ins>Installing Qiskit:</ins><br />
To run the Phyton files you need to have Qiskit installed. Following the tutorial on Qiskit's main page will do it:
https://qiskit.org/documentation/getting_started.html

