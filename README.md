# Smart Energy Monitor - Digital Twin

Professional portfolio project by Lewis (Nyeri, Kenya).

A software-based Smart Energy Monitor that simulates real-time electricity usage on the Kenyan 230V grid. The system acts as a digital twin of a current and voltage sensing setup, calculates real power with `P = V * I * PF`, and displays live console output plus synchronized Matplotlib graphs.

## Status

- MVP complete (Week 1)
- Core simulator and live dashboard working
- No hardware required

## Key Features

- Realistic Kenya grid simulation (230V nominal with natural fluctuation)
- Digital twin current simulation with varying residential loads
- Live console dashboard: Voltage, Current, Real Power
- Live Matplotlib dashboard with 3 synchronized plots:
  - Voltage
  - Current
  - Power
- Clean Python virtual environment workflow
- Git and GitHub project structure

## Technologies Used

- Python 3
- `numpy` for simulation noise and numeric behavior
- `matplotlib` for real-time interactive charting
- `pandas` planned for Week 2+ analytics and reporting

## Project Structure

- `main.py`: entry point and live runtime loop
- `sensor_sim.py`: `EnergySensorSimulator` class
- `dashboard.py`: live plotting dashboard
- `requirements.txt`: dependency list

## Requirements

- Python 3.9+
- Pip

## Setup (Windows PowerShell)

1. Clone and enter project.

```powershell
git clone https://github.com/YOURUSERNAME/smart-energy-monitor-digital-twin.git
cd smart-energy-monitor-digital-twin
```

2. Create and activate virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies.

```powershell
pip install -r requirements.txt
pip install numpy
```

## Run

```powershell
python main.py
```

Expected behavior:
- Live readings print continuously in the terminal
- A Matplotlib window opens with 3 real-time graphs

Press `Ctrl+C` to stop safely.

## Troubleshooting

- `ImportError: cannot import name 'EnergySensorSimulator' from 'sensor_sim'`
  - Confirm `sensor_sim.py` defines `class EnergySensorSimulator`.
  - Confirm there is only one `sensor_sim.py` in your active project path.

- Plot window does not appear
  - Ensure `matplotlib` is installed in the active virtual environment.
  - Run from a local desktop session (not headless terminal).

- `ModuleNotFoundError: No module named 'numpy'`
  - Install numpy in the active environment: `pip install numpy`

## Methodology

- Hybrid workflow: Waterfall for planning + Agile for iterative delivery
- Week 1 delivered simulator + live dashboard MVP
