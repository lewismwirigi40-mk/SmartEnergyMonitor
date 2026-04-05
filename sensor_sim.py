import numpy as np
import random

class EnergySensorSimulator:
    """Digital Twin of ACS712 current sensor + Voltage sensor for Kenya grid"""
    
    def __init__(self):
        self.voltage_base = 230.0      # Kenya nominal voltage (Nyeri area)
        self.power_factor = 0.92       # Typical residential power factor
        self.load_profile = "residential"
    
    def read_voltage(self):
        """Simulate realistic voltage with small fluctuations (±3.5V)"""
        noise = np.random.normal(0, 3.5)
        voltage = self.voltage_base + noise
        return round(max(210.0, min(250.0, voltage)), 2)
    
    def read_current(self):
        """Simulate current based on varying home appliances"""
        base_load_watts = random.choice([40, 85, 180, 320, 550, 780, 1050])
        current = base_load_watts / (self.voltage_base * self.power_factor)
        noise = np.random.normal(0, 0.08)
        return round(current + noise, 3)
    
    def calculate_power(self, voltage, current):
        """Calculate real power: P = V × I × PF"""
        return round(voltage * current * self.power_factor, 2)