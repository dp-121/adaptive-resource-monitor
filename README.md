# 🧠 Adaptive Resource Allocation in Multiprogramming Systems

---

## 📌 Project Overview

This project implements a **real-time dashboard** that monitors CPU and memory usage across multiple programs and **dynamically reallocates resources** to prevent bottlenecks.  
It simulates load, tracks system metrics, and adjusts process priorities based on configurable thresholds.

---

## 🎯 Features

- ✅ **Real-time CPU and memory monitoring**  
- 📊 **Historical graphing** with Chart.js  
- 🔍 **Top process viewer** with PID, name, CPU%, and memory%  
- 🧪 **Simulate CPU and memory load**  
- 🔁 **Reset simulation processes**  
- 🎚️ **Threshold slider** for CPU usage  
- ⚙️ **Trigger adaptive reallocation**  
- 🧠 **Kill button** for terminating processes  
- 🎨 **Responsive UI** with dark theme and neon accents  

---

## 🧩 Modules

| **Module** | **Description** |
|-------------|-----------------|
| **Monitoring Module** | Uses `psutil` to collect system metrics and identify top processes. |
| **Control Module** | Simulates load, resets state, and reallocates resources based on CPU thresholds. |
| **UI Module** | Displays gauges, graphs, and process tables with interactive controls. |

---

## 🛠️ Technologies Used

- **Language:** Python  
- **Backend Framework:** Flask  
- **System Monitoring:** `psutil`  
- **Frontend:** HTML, CSS, JavaScript  
- **Graphing Library:** Chart.js  
- **Version Control:** GitHub  

---

## 🚀 How It Works

1. The dashboard loads and fetches system metrics every 2 seconds.  
2. The user simulates load using CPU or memory buttons.  
3. Processes appear in the top process table with live stats.  
4. The user sets a threshold and triggers reallocation.  
5. The backend lowers the priority of high-CPU processes using `nice()`.  
6. The user can reset or manually kill any process.  

---

## 📂 File Structure

```
adaptive-resource-monitor/
├── app.py                 # Flask app entry point
├── monitor.py             # Backend logic for metrics and control
├── templates/
│   └── index.html         # Frontend dashboard

```
---

## 🧪 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/adaptive-resource-monitor.git
   cd adaptive-resource-monitor
   ```

2. **Install dependencies**

   ```bash
   pip install flask psutil
   ```

3. **Run the app**

   ```bash
   python app.py
   ```

4. **Open your browser** at:

   ```
   http://localhost:5000
   ```

---

## 📈 Future Enhancements

* 🔁 Auto-reallocation toggle
* 🧮 Memory-aware reallocation logic
* 🧾 Process whitelisting
* 📜 Reallocation logs and export
* 🌐 Remote monitoring support

---

## 📚 References

* [psutil Documentation](https://psutil.readthedocs.io/)
* [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
* [Flask Documentation](https://flask.palletsprojects.com/)

---

## 👨‍💻 Author

**dp-121**
