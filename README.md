
## **1x8 Silicon Photonic Power Divider**

### **Project Overview**

This project involves the design and implementation of a **1x8 power divider** using silicon photonics technology. The device is constructed by cascading multiple **1x2 Multi-Mode Interference (MMI)** couplers to split a single optical input into eight equal outputs.

### **Key Features**

* **Architecture**: A tree-like structure utilizing seven `MMI1x2Optimized1550` components .
* **Operating Wavelength**: Optimized for **1550 nm**.
* **Design Tools**: Developed using **Luceda IPKISS Canvas** and scripted in **Python** (IPKISS 3.10.1).
* **Layout Format**: Final design exported as a **GDSII (.gds)** file for fabrication readiness.

---

### **Design Architecture**

The divider is built using three stages of 1x2 MMIs:

**Stage 1**: One MMI splits the main input into two branches.

**Stage 2**: Two MMIs further split those branches into four.

**Stage 3**: Four MMIs create the final eight output ports.

---

### **Repository Contents**

* **`Power_Divider_1x8.py`**: The Python script containing the circuit logic, component placement, and routing specifications.


* **`Power_Divider_1x8.gds`**: The geometric layout file representing the physical design of the photonic chip.


* **`Simulation_Results.pdf`**: A summary of the scattering parameter (S-parameter) analysis.

---

### **Simulation Results**

The device performance was verified through S-parameter simulations in a PyCharm environment.

* **Transmission**: The simulation shows uniform power distribution across all eight output ports (approximately **-9 dB to -10 dB** per port, accounting for ideal splitting and minor losses).


* **Reflection**: The input reflection (S11) remains consistently low across the 1.5 $\mu$m to 1.6 $\mu$m wavelength range, indicating an efficient, well-matched design.

---

### **How to Run**

1. **Prerequisites**: Ensure you have **Luceda IPKISS** installed.

2. **Execution**: Run the Python script to generate the layout and view the circuit visualization.

python Power_Divider_1x8.py


3. **Output**: The script will generate a `.gds` file and display the transmission/reflection plots.

---
Developed as part of the Nano-Photonics (EE 590) curriculum at Western New England University.
