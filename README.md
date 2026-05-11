# ACP Brevet Time Calculator

**Author:** Ty Larson
**Email:** tyl@uoregon.edu

---

## Project Overview
This application is a reimplementation of the **RUSA ACP controle time calculator** using **Flask** and **AJAX**. It calculates the minimum (opening) and maximum (closing) arrival times for control points along a brevet cycling event based on the official ACP algorithm.

The implementation uses **moment.js** on the frontend for time formatting and **arrow** on the backend for precise datetime calculations.

## ACP Control Time Rules
The calculator determines times based on standard ACP speed brackets.

| Distance Interval (km) | Max Speed (Open) | Min Speed (Close) |
| :--- | :--- | :--- |
| 0 - 200 | 34 km/hr | 15 km/hr |
| 200 - 400 | 32 km/hr | 15 km/hr |
| 400 - 600 | 30 km/hr | 15 km/hr |
| 600 - 1000 | 28 km/hr | 11.428 km/hr |

### Key Algorithmic Details
* **Control at Finish:** When a control distance is equal to or greater than the nominal brevet distance, the nominal distance is used for the closing time (e.g., a 200km brevet always closes at 13h30).
* **Start Point (0km):** The opening time is the start time, while the closing time is one hour after the start.
* **Over-distance:** Controls are permitted up to 20% beyond the nominal distance, but calculation speed tiers are capped at the brevet distance.