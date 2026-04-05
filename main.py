from sensor_sim import EnergySensorSimulator
from dashboard import LiveDashboard

import matplotlib.pyplot as plt
import time
# Initialize
monitor = EnergySensorSimulator()
dashboard = LiveDashboard()

print("🌐 SMART ENERGY MONITOR DIGITAL TWIN STARTED")
print("📍 Location: Nyeri, Kenya | Grid: 230V nominal")
print("=" * 70)

print("Live readings (Console + Graphs):\n")

try:
    while True:
        v = monitor.read_voltage()
        i = monitor.read_current()
        p = monitor.calculate_power(v, i)
        
        # Console output
        print(f"⏱️  {time.strftime('%H:%M:%S')} | "
              f"V: {v:6.1f} V | "
              f"I: {i:6.3f} A | "
              f"P: {p:7.1f} W    ", end="\r")
        
        # Update live graphs
        dashboard.update(v, i, p)
        
        time.sleep(1.0)   # 1 reading per second

except KeyboardInterrupt:
    print("\n\n🛑 Monitor stopped by user.")
    print("✅ Week 1 MVP completed successfully!")
    plt.close()
