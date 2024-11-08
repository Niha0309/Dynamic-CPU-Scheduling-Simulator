An interactive simulation tool for visualizing and analyzing three key CPU scheduling algorithms: First-Come-First-Serve (FCFS), Shortest Job First (SJF), and Priority Scheduling. This simulator allows users to input custom process data, view scheduling results via Gantt charts, and compare performance metrics, making it an excellent educational tool for understanding CPU scheduling principles in operating systems.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Scheduling Algorithms](#scheduling-algorithms)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Acknowledgments](#acknowledgments)


## Introduction

The Dynamic CPU Scheduling Simulator is designed to demonstrate and evaluate how different CPU scheduling algorithms affect key performance metrics like waiting time, turnaround time, and CPU utilization. Through an intuitive interface, users can experiment with each scheduling algorithm, observe their behavior under various scenarios, and gain insights into the trade-offs involved in CPU scheduling.

## Features

- Interactive Input Panel: Enter custom process attributes (arrival time, burst time, and priority).
- Algorithm Selection: Choose between FCFS, SJF, and Priority Scheduling.
- Gantt Chart Visualization: Real-time Gantt charts to visualize process execution order.
- Performance Metrics: Display waiting time, turnaround time, and average statistics.
- Comparative Analysis: Compare the performance of scheduling algorithms under the same input conditions.

## Installation

### System Requirements

- Python 3.7 or higher
- Libraries: matplotlib  (for Gantt charts), numpy (for calculations)

### Steps

1. Clone the repository:
   git clone https://github.com/yourusername/dynamic-cpu-scheduler.git
   cd dynamic-cpu-scheduler
Install dependencies:
pip install matplotlib numpy

Usage
Navigate to the project directory.
    Run the main script:
python main.py

For a web-based interface, start the simulator with Streamlit:
streamlit run main.py
Then, open the provided link in a browser to interact with the simulator.

Configuration
Process Input: Use the sidebar interface to enter the number of processes, along with attributes like arrival time, burst time, and priority.
Algorithm Selection: Choose an algorithm (FCFS, SJF, or Priority) from the dropdown menu to simulate.
Scheduling Algorithms
The simulator includes implementations for three fundamental CPU scheduling algorithms:
First-Come-First-Serve (FCFS): Processes are executed in the order they arrive. Simple but can cause longer waiting times for shorter jobs.
Shortest Job First (SJF): Selects the process with the shortest burst time next. Efficient for reducing wait times but may lead to starvation of longer processes.
Priority Scheduling: Executes processes based on priority levels, with lower values indicating higher priority. This approach prioritizes critical tasks but can lead to starvation of lower-priority jobs.
Examples
Running a Simulation
Input process details in the sidebar.
Select an algorithm.
Click "Simulate" to view the scheduling results:
Gantt chart for process execution.
Detailed table with metrics like start time, completion time, turnaround time, and waiting time.

Troubleshooting
Issue: Gantt chart not displaying.
Solution: Ensure matplotlib is correctly installed. Run pip install matplotlib if necessary.
Issue: Web interface not launching.
Solution: Check if Streamlit is installed (pip install streamlit). Make sure to use Python 3.7 or higher.

Acknowledgments
This project was developed as part of a coursework in Computer Science and Engineering at the University of Science & Technology, Chittagong. Special thanks to our instructors  for their support and guidance
