from collections import deque

import matplotlib.pyplot as plt


class LiveDashboard:
    def __init__(self, max_points=30):
        plt.ion()
        self.max_points = max_points
        self.timestamps = deque(maxlen=max_points)
        self.voltage_data = deque(maxlen=max_points)
        self.current_data = deque(maxlen=max_points)
        self.power_data = deque(maxlen=max_points)
        self.sample_count = 0

        self.fig, self.axes = plt.subplots(3, 1, figsize=(10, 8))
        self.fig.suptitle("Smart Energy Monitor Live Dashboard")

        (self.voltage_line,) = self.axes[0].plot([], [], color="tab:blue")
        (self.current_line,) = self.axes[1].plot([], [], color="tab:green")
        (self.power_line,) = self.axes[2].plot([], [], color="tab:red")

        self.axes[0].set_ylabel("Voltage (V)")
        self.axes[1].set_ylabel("Current (A)")
        self.axes[2].set_ylabel("Power (W)")
        self.axes[2].set_xlabel("Sample")

        for axis in self.axes:
            axis.grid(True, alpha=0.3)

        plt.tight_layout()

    def update(self, voltage, current, power):
        self.sample_count += 1
        self.timestamps.append(self.sample_count)
        self.voltage_data.append(voltage)
        self.current_data.append(current)
        self.power_data.append(power)

        self.voltage_line.set_data(self.timestamps, self.voltage_data)
        self.current_line.set_data(self.timestamps, self.current_data)
        self.power_line.set_data(self.timestamps, self.power_data)

        for axis in self.axes:
            axis.relim()
            axis.autoscale_view()

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.001)
