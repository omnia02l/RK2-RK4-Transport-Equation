# Numerical Resolution of the Transport Equation
Internship Project – ESPRIT  
Author: Omnia Lahdhiri

## Overview
This project focuses on the numerical resolution of the transport equation, which models the evolution of the concentration of a chemical species in a moving fluid. Two numerical methods were implemented and compared:

- Runge–Kutta 2nd order (RK2)
- Runge–Kutta 4th order (RK4)

Both methods, originally designed for ordinary differential equations, were adapted to solve a partial differential equation (PDE).

## Objectives
- Establish the physical model of the transport equation.
- Study the RK2 and RK4 numerical methods.
- Implement both methods in Python.
- Compare their accuracy and stability.
- Apply the model to a real physical scenario.

## Mathematical Model
The transport equation studied is:

∂u/∂t + c ∂u/∂x = f(x, t)

Where:
- u(x, t): concentration
- c: transport velocity
- f(x, t): source term


