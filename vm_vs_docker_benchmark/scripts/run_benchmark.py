import psutil
import time
import csv
import os
import subprocess
import shutil

# Duración del benchmark en segundos
duration = 60
end_time = time.time() + duration

results = []

# Ruta al juego
script_dir = os.path.dirname(os.path.abspath(__file__))
game_path = os.path.join(script_dir, "ticTacToe.py")

print(f"⏳ Ejecutando benchmark del juego durante {duration} segundos...")

# Lanzar el juego como proceso aparte
proc = subprocess.Popen(['python3', game_path])

while time.time() < end_time and proc.poll() is None:
    cpu = psutil.cpu_percent(interval=0.1)
    mem = psutil.virtual_memory().percent
    timestamp = time.time()
    results.append([timestamp, cpu, mem])
    print(f"CPU: {cpu}%, MEM: {mem}%")
    time.sleep(0.2)

# Si el juego sigue corriendo, lo terminamos al acabar benchmark
if proc.poll() is None:
    proc.terminate()

# Preguntar entorno: VM o Docker
is_vm = input("¿Se está ejecutando en una VM? (y/n): ").strip().lower() == 'y'
filename = f"benchmark_ticTacToe_{'vm' if is_vm else 'docker'}.csv"
filepath = os.path.join(script_dir, "..", "results", filename)

# Guardar CSV con resultados
os.makedirs(os.path.dirname(filepath), exist_ok=True)
with open(filepath, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "cpu_percent", "memory_percent"])
    writer.writerows(results)

# Calcular promedios
cpus = [r[1] for r in results]
mems = [r[2] for r in results]
avg_cpu = sum(cpus) / len(cpus) if cpus else 0
avg_mem = sum(mems) / len(mems) if mems else 0

# Calcular tamaño en disco del proyecto
base_path = os.path.abspath(os.path.join(script_dir, ".."))
total_size = 0
for dirpath, dirnames, filenames in os.walk(base_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if os.path.exists(fp):
            total_size += os.path.getsize(fp)
disk_mb = total_size / (1024 * 1024)

# Mostrar resumen
print("\n📊 RESUMEN DEL BENCHMARK")
print(f"📁 Entorno analizado: {base_path}")
print(f"🧠 RAM promedio durante ejecución: {avg_mem:.2f}%")
print(f"⚙️ CPU promedio bajo carga: {avg_cpu:.2f}%")
print(f"💾 Espacio en disco usado por entorno: {disk_mb:.2f} MB")
print(f"✅ Resultados guardados en: {filepath}")
