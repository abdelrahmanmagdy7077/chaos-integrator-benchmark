
# A Comparative Analysis of Explicit Integration Methods for Conservative and Dissipative Chaotic Dynamical Systems

## Abstract

This repository contains a computational physics framework designed to systematically evaluate the performance, accuracy, and computational efficiency of numerical integration strategies across chaotic dynamical systems. Written entirely from scratch in Python using minimal dependencies (NumPy and Matplotlib), this project serves as a foundational investigation into Numerical Analysis and Computational Physics.

The primary objective is to determine how the choice of numerical integrator impacts the long term simulation of chaotic behavior, specifically analyzing whether an integrator's effectiveness is tied to the underlying physics of the system. Namely, whether the system constantly loses energy (dissipative) or strictly conserves it (conservative).

## The Research Question

Which numerical integrator works best for chaotic systems, and does the optimal choice change depending on whether the system conserves energy or dissipates it? Furthermore, how much does the integrator's performance depend on the specific physical traits of the system itself?

## Dynamical Systems Analyzed

The benchmarking framework applies the integrators to four distinct nonlinear chaotic systems. These were chosen to represent both conservative and dissipative physics:

- **Lorenz 63 (Dissipative):** A simplified mathematical model for atmospheric convection. It constantly loses energy, causing the system's trajectories to eventually settle into a distinct, predictable pattern known as the famous "butterfly" attractor.
    
- **Double Pendulum (Conservative):** A classic physics problem. It strictly conserves total mechanical energy but is extremely sensitive to its starting position, making it an ideal test to see if a numerical method "leaks" energy over time.
    
- **Planar 3 Body Problem (Conservative):** A foundational problem in celestial mechanics describing the motion of three point masses under mutual gravitational attraction. It is highly chaotic and computationally demanding because the masses frequently pass very close to one another, causing massive spikes in gravitational force.
    
- **Henon Heiles System (Conservative):** Originally developed to describe the motion of a star around a galactic center. It is a benchmark system in astrophysics for studying how a system transitions from stable, predictable movement into total chaos.
    

## Numerical Integration Methods

To evaluate these systems, the physical equations of motion are integrated using five distinct numerical schemes, ranging from basic calculations to advanced, self adjusting algorithms:

- **Forward Euler:** A basic first order method. It is included primarily as a baseline to demonstrate computational simplicity and show how quickly simple math accumulates errors over time.
    
- **Symplectic Euler:** A modified first order integrator designed specifically to conserve energy over time, making it much better suited for systems like the pendulum or planets.
    
- **Runge Kutta 4 (RK4):** The industry standard fourth order method. It provides highly accurate results using a fixed, predictable time step.
    
- **Velocity Verlet:** A second order method heavily used in physics simulations because it is highly stable and excellent at keeping energy constant over long periods.
    
- **Adaptive RK45 (Dormand Prince):** A smart, variable step size method. It constantly checks its own accuracy and adjusts its time jumps on the fly to guarantee the error stays below a strict limit.
    

## Benchmarking & Data Visualization

The framework automatically generates comprehensive visual analytics to quantify the strengths and weaknesses of each method. The primary metrics evaluated over a standardized 100 second simulation span include:

- **Phase Space Portraits:** 2D and 3D graphs showing the physical paths and geometric shapes the systems create.
    
- **Energy Error Bar Charts:** Measuring how much energy the simulation artificially lost or gained over time (critical for evaluating the conservative systems).
    
- **Sensitivity Plots:** Measuring the "butterfly effect" by tracking how quickly two nearly identical starting points drift apart.
    
- **Computation Time:** The raw time your CPU requires to run the simulation from start to finish.
    
- **Computational Load (Step Counts):** A bar chart comparing the fixed 100,000 calculation steps forced by the basic methods against the optimized, flexible jumps taken by the Adaptive RK45 method.
    

## Summary of Results

*(Note: This section will be updated upon the conclusion of the data collection and analysis phase. It will summarize the definitive integrator recommendations for conservative versus dissipative domains.)*

## Usage & Architecture

This project is built from scratch without reliance on high level solvers (for example, SciPy's solve_ivp is used only for benchmarking the RK45 baseline, while all other physics engines are custom built).

Dependencies:

- numpy (for rapid matrix and vector operations)
    
- matplotlib (for phase space and statistical visualization)
