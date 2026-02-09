# SIGET CPU Scheduler Simulator
Project Overview
This project is a CPU Scheduler Simulator designed for the SIGET (Intelligent Traffic Management System). The goal is to simulate how an Operating System (OS) manages different urban mobility tasks—ranging from routine data processing to emergency alerts—by utilizing scheduling algorithms to prevent system collapse and ensure high performance.
Key Features
• Process Lifecycle Management: The simulator tracks each task through the five fundamental states: New, Ready, Running, Waiting (Blocked), and Terminated.
• Scheduling Algorithms:
    ◦ Priority Scheduling: Implemented to provide immediate response to critical events, such as ambulance emergencies.
    ◦ Round-Robin: Used for equitable processing of routine traffic data, ensuring all tasks coexist efficiently.
• Concurrency Simulation: Demonstrates how multiple activities share the processor, creating a pseudoparalellism environment on single-core setups or exploiting real parallelism in multi-core architectures.
Theoretical Foundation
The design of this simulator is informed by the core hardware architectures that support modern Operating Systems:
1. Hardware Architectures
• Von Neumann Architecture: We acknowledge the "bottleneck" where instructions and data compete for the same bus. This simulator models the latency that occurs when the processor must wait for data, reflecting the simplicity and flexibility of this model.
• Harvard Architecture: The project logic reflects the benefits of separate memory for data and instructions, which allows for concurrent access and superior performance in real-time signal processing.
2. Process Management
In this simulation, a Process is treated as an instance assigned to a processor. Each task requires:
• Processing time.
• Memory allocation.
• Files and devices (I/O).
The OS acts as the "Silent Architect," orchestrating these resources to maintain system stability.
Implementation Details
The simulator is written in Python, focusing on modularity and clear state transitions. It emulates:
• Context Switching: Reducing overhead during task transitions.
• Critical Sections: Protecting shared data to prevent race conditions, a concept typically managed by mutex in lower-level languages like C++.
How to Run
1. Ensure you have Python 3.x installed.
2. Clone the repository:
3. Run the script:
Conclusions
Understanding process management transforms a developer from a mere "code writer" into a Software Solutions Architect. This simulator proves that efficient scheduling and an understanding of underlying hardware (Von Neumann vs. Harvard) are essential for designing robust, efficient, and stable urban mobility systems.
