# Reference: Infrared Optical Sensor Circuit Analysis (9V)

This page details the circuit dynamics, voltage drops, and current calculations for a standard active Infrared (IR) sensor breadboard setup powered by a **9V Supply**.

---

##  Circuit Architecture
The circuit splits into **two parallel branches** connected across the 9V power supply:
1. **Emitter Branch:** Continuous infrared light production.
2. **Receiver Branch:** Light-dependent variable resistance sensing.

---

## 1. Emitter Branch (IR LED + $320\,\Omega$ Resistor)
This branch provides a constant, safe current to illuminate the infrared LED. The resistor ($R_1$) is wired in series with the IR LED.

### Core Specifications
* **Supply Voltage ($V_{cc}$):** $9\text{ V}$
* **IR LED Forward Voltage ($V_f$):** $\approx 1.2\text{ V}$ (Typical for infrared LEDs)
* **Current-Limiting Resistor ($R_1$):** $320\,\Omega$

### Calculations & Behavior
* **Voltage Drop across Resistor ($V_{R1}$):** 
  $$V_{R1} = V_{cc} - V_f = 9\text{ V} - 1.2\text{ V} = 7.8\text{ V}$$
* **Current Flow ($I_{LED}$):** Derived using Ohm's Law ($I = \frac{V}{R}$)
  $$I_{LED} = \frac{7.8\text{ V}}{320\,\Omega} \approx 0.0244\text{ A} = 24.4\text{ mA}$$

> [!SUCCESS] Safe Operation
> A continuous current of **24.4 mA** keeps the IR LED running at optimal brightness without overdriving or burning it out.

---

##  2. Receiver Branch (Photoresistor / Photodetector)
The receiver branch converts changes in light intensity into an electrical signal. The photoresistor acts as a variable resistor whose internal resistance drops when exposed to IR light.

### State Snapshot (At $24\text{ k}\Omega$)
When the photoresistor's internal resistance is exactly **$24\text{ k}\Omega$ ($24,000\,\Omega$)**, the behavior is as follows:

* **Current Flow ($I_{Receiver}$):** 
  $$I_{Receiver} = \frac{9\text{ V}}{24,000\,\Omega} \approx 0.000375\text{ A} = 0.38\text{ mA}$$
* **Voltage Drop Configuration:** The entire $9\text{ V}$ drops completely across the photoresistor component.

### Dynamic Sensing Mechanism
Because it is a variable component, its state fluctuates depending on reflections:

* **Dark State (No IR Reflection / Obstacle Far Away):** 
  * Resistance spikes heavily (often $>100\text{ k}\Omega$).
  * The current drops to near-zero.
  * It consumes nearly the full $9\text{ V}$ supply drop.
* **Light State (IR Reflected / Obstacle Close):** 
  * Resistance drops drastically (often well below $1\text{ k}\Omega$).
  * The voltage drop across the photoresistor plummets.

---

## Summary Reference Matrix

| Circuit Branch | Component | Nominal Resistance | Individual Voltage Drop | Calculated Current Flow |
| :--- | :--- | :--- | :--- | :--- |
| **Emitter** | Resistor ($R_1$) | $320\,\Omega$ | $7.8\text{ V}$ | **$24.4\text{ mA}$** |
| **Emitter** | IR LED | *Internal (Dynamic)* | $1.2\text{ V}$ | **$24.4\text{ mA}$** |
| **Receiver** | Photoresistor | $24\text{ k}\Omega$ *(Variable)* | Varies with ambient IR light | **$0.38\text{ mA}$** *(At $24\text{ k}\Omega$)* |

---
