from flask import Flask, render_template, jsonify, request
from monitor import (
    get_system_metrics,
    simulate_cpu_load,
    simulate_memory_load,
    reset_simulation,
    adaptive_reallocate,
    kill_process
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    return jsonify(get_system_metrics())

@app.route('/simulate/cpu')
def simulate_cpu():
    simulate_cpu_load()
    return jsonify({"status": "CPU load simulated"})

@app.route('/simulate/memory')
def simulate_memory():
    simulate_memory_load()
    return jsonify({"status": "Memory load simulated"})

@app.route('/reset')
def reset():
    reset_simulation()
    return jsonify({"status": "Simulation reset"})

@app.route('/reallocate')
def reallocate():
    threshold = int(request.args.get('threshold', 80))
    adaptive_reallocate(threshold)
    return jsonify({"status": f"Reallocation triggered at {threshold}%"})

@app.route('/kill/<int:pid>')
def kill(pid):
    success = kill_process(pid)
    return jsonify({"status": "Killed" if success else "Failed"})
