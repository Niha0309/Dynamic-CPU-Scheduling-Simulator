import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


# Define Process class
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.start_time = 0


# First-Come-First-Serve (FCFS) Scheduling
def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort by arrival time
    current_time = 0
    for process in processes:
        process.start_time = max(current_time, process.arrival_time)
        process.completion_time = process.start_time + process.burst_time
        process.waiting_time = process.start_time - process.arrival_time  # Corrected
        process.turnaround_time = process.completion_time - process.arrival_time  # Corrected
        current_time = process.completion_time
    return processes


# Shortest Job First (SJF) Scheduling
def sjf(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))  # Sort by arrival time, then burst time
    current_time = 0
    completed = 0
    n = len(processes)

    while completed < n:
        available_processes = [p for p in processes if p.arrival_time <= current_time and p.completion_time == 0]
        if available_processes:
            process = min(available_processes, key=lambda x: x.burst_time)
            process.start_time = max(current_time, process.arrival_time)
            process.completion_time = process.start_time + process.burst_time
            process.waiting_time = process.start_time - process.arrival_time  # Corrected
            process.turnaround_time = process.completion_time - process.arrival_time  # Corrected
            current_time = process.completion_time
            completed += 1
        else:
            current_time += 1  # If no process is ready, move time forward
    return processes


# Priority Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.priority))  # Sort by arrival time, then priority
    current_time = 0
    for process in processes:
        process.start_time = max(current_time, process.arrival_time)
        process.completion_time = process.start_time + process.burst_time
        process.waiting_time = process.start_time - process.arrival_time  # Corrected
        process.turnaround_time = process.completion_time - process.arrival_time  # Corrected
        current_time = process.completion_time
    return processes


# Calculate metrics for processes
def calculate_metrics(processes):
    for process in processes:
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
    return processes


# Updated Gantt Chart Visualization with improved Waiting and Turnaround Time Annotations
def visualize_gantt_chart(processes, algorithm_name):
    fig, ax = plt.subplots()
    yticks = []
    labels = []

    for i, process in enumerate(processes):
        yticks.append(i)
        labels.append(f"P{process.pid}")

        # Waiting Time Segment (in grey)
        ax.barh(y=i, width=process.start_time - process.arrival_time, left=process.arrival_time, color='grey',
                edgecolor='black', label='Waiting Time' if i == 0 else "")

        # Execution Time Segment (in blue)
        ax.barh(y=i, width=process.burst_time, left=process.start_time, color='skyblue', edgecolor='black',
                label='Execution Time' if i == 0 else "")

        # Add annotations for Waiting Time and Turnaround Time with improved positioning
        # Waiting Time Annotation - positioned slightly to the left of the waiting bar
        if process.waiting_time > 0:
            ax.text(process.arrival_time + (process.start_time - process.arrival_time) / 2, i,
                    f"W={process.waiting_time}",
                    ha='center', va='center', color='black', fontsize=9,
                    bbox=dict(facecolor='white', edgecolor='none', pad=1))

        # Turnaround Time Annotation - positioned at the end of the execution bar
        ax.text(process.completion_time + 0.2, i, f"T={process.turnaround_time}",
                ha='left', va='center', color='black', fontsize=9,
                bbox=dict(facecolor='white', edgecolor='none', pad=1))

    # Set labels and legend
    ax.set_yticks(yticks)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title(f"Gantt Chart for {algorithm_name} Scheduling")
    ax.legend()
    st.pyplot(fig)


# Display metrics report
def print_report(processes, algorithm_name):
    data = {
        "Process ID": [p.pid for p in processes],
        "Arrival Time": [p.arrival_time for p in processes],
        "Burst Time": [p.burst_time for p in processes],
        "Priority": [p.priority for p in processes],
        "Start Time": [p.start_time for p in processes],
        "Completion Time": [p.completion_time for p in processes],
        "Turnaround Time": [p.turnaround_time for p in processes],
        "Waiting Time": [p.waiting_time for p in processes]
    }
    df = pd.DataFrame(data)
    st.write(f"### {algorithm_name} Scheduling Report")
    st.write(df)
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    st.write(f"**Average Turnaround Time**: {avg_turnaround_time}")
    st.write(f"**Average Waiting Time**: {avg_waiting_time}")


# Streamlit App
st.title("Dynamic CPU Scheduling Simulator")
st.sidebar.header("Enter Process Details")
num_processes = st.sidebar.number_input("Number of Processes", min_value=1, max_value=10, value=3)

processes = []
for i in range(num_processes):
    st.sidebar.write(f"### Process {i + 1}")
    pid = i + 1
    arrival_time = st.sidebar.number_input(f"Arrival Time of Process {pid}", min_value=0, max_value=100, value=0)
    burst_time = st.sidebar.number_input(f"Burst Time of Process {pid}", min_value=1, max_value=100, value=1)
    priority = st.sidebar.number_input(f"Priority of Process {pid}", min_value=1, max_value=10, value=1)
    processes.append(Process(pid, arrival_time, burst_time, priority))

algorithm = st.selectbox("Select Scheduling Algorithm", ("FCFS", "SJF", "Priority"))
if st.button("Simulate"):
    if algorithm == "FCFS":
        scheduled_processes = fcfs(processes)
        st.write("## FCFS Scheduling")
    elif algorithm == "SJF":
        scheduled_processes = sjf(processes)
        st.write("## SJF Scheduling")
    elif algorithm == "Priority":
        scheduled_processes = priority_scheduling(processes)
        st.write("## Priority Scheduling")

    calculate_metrics(scheduled_processes)
    print_report(scheduled_processes, algorithm)
    visualize_gantt_chart(scheduled_processes, algorithm)
