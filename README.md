
# An Analysis of Numerical Integration Methods for Chaotic Dynamical Systems

## Abstract

This repository contains a computational physics framework designed to systematically evaluate the performance, accuracy, and computational efficiency of numerical integration strategies across chaotic dynamical systems. Written entirely from scratch in Python using minimal dependencies (NumPy and Matplotlib), this project serves as a foundational investigation into Numerical Analysis and Computational Physics.

The primary objective is to determine how the choice of numerical integrator impacts the long term simulation of chaotic behavior, specifically analyzing whether an integrator's effectiveness is tied to the underlying physics of the system. 

## The Research Question

Which numerical integrator works best for chaotic systems, and how much does the integrator's performance depend on the specific physical traits of the system itself?

## [Chaotic Dynamical Systems](https://en.wikipedia.org/wiki/Chaos_theory) 

The benchmarking framework applies the integrators to four distinct nonlinear chaotic systems:

* **[Lorenz 63](https://en.wikipedia.org/wiki/Lorenz_system):** A simplified three-dimensional mathematical model for atmospheric convection.
  
* **[Double Pendulum](https://en.wikipedia.org/wiki/Double_pendulum):** A classical mechanics system consisting of one pendulum attached to the end of another.

* **[3-Body Problem](https://en.wikipedia.org/wiki/Three-body_problem):** A celestial mechanics model tracking the gravitational motion of three point masses restricted to a two-dimensional plane.
  
* **[Hénon-Heiles System](https://en.wikipedia.org/wiki/H%C3%A9non%E2%80%93Heiles_system):** A two-dimensional mathematical model describing the non-linear motion of a star moving through a galactic center.
    

## [Numerical Integration Methods](https://en.wikipedia.org/wiki/Numerical_methods_for_ordinary_differential_equations)

To run the simulations, the equations of motion are solved using five numerical integrators:

* **[Euler Method](https://en.wikipedia.org/wiki/Euler_method):** A first-order method. Used as a baseline to demonstrate error accumulation in linear approximations.
  
* **[Backward Euler](https://en.wikipedia.org/wiki/Backward_Euler_method):** A modified first-order integrator that updates position and velocity sequentially to conserve system energy.
  
* **[Runge-Kutta 4](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods):** A fourth-order fixed-step method that uses weighted slope averages for higher accuracy.
  
* **[Verlet Method](https://en.wikipedia.org/wiki/Verlet_integration):** A second-order method optimized for long-term stability and energy conservation in physics engines.
  
* **[Adaptive RK45 (Dormand-Prince)](https://en.wikipedia.org/wiki/Dormand%E2%80%93Prince_method):** A variable step-size method. It compares fourth and fifth-order steps to estimate local error and dynamically adjust time jumps.

---

## Benchmarking & Data Visualization

The framework tracks performance and accuracy over a 100-second simulation across five metrics:

* **Phase Space Portraits:** 2D and 3D plots of position against momentum to map the system's geometric trajectories.
  
* **Energy Drift:** Measures the artificial energy gained or lost by the integrator over time.
  
* **Sensitivity Plots:** Tracks the divergence rate of two nearly identical initial states to quantify chaotic behavior.
  
* **Execution Time:** Measures the CPU time required to complete the simulation.
  
* **Step Counts:** Compares the fixed 100,000 steps of the standard integrators against the variable steps taken by the adaptive method.
    

## Summary of Results

*(Note: This section will be updated upon the conclusion of the data collection and analysis phase. It will summarize the definitive integrator recommendations for conservative versus dissipative domains.)*

## Usage & Architecture

This project is built from scratch without reliance on high level solvers (for example, SciPy's solve_ivp is used only for benchmarking the RK45 baseline, while all other physics engines are custom built).

Dependencies:

- numpy (for rapid matrix and vector operations)
    
- matplotlib (for phase space and statistical visualization)
