import psutil
import time
import csv
import os
import subprocess
import shutil
import requests
import platform

# Duración del benchmark en segundos
duration = 60
end_time = time.time() + duration

results = []

# Obtener la ruta absoluta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Detectar la ruta correcta del juego ticTacToe_web
# Intentamos buscar la carpeta 'ticTacToe_web' dentro 'scripts'
possible_game_dir = os.path.join(script_dir, "ticTacToe_web")
if not os.path.isdir(possible_game_dir):
    # Quizás estamos en la raíz y 'scripts/ticTacToe_web'
    possible_game_dir = os.path.join(script_dir, "scripts", "ticTacToe_web")
if not os.path.isdir(possible_game_dir):
    raise FileNotFoundError(f"No se encontró la carpeta ticTacToe_web en: {possible_game_dir}")

game_dir = possible_game_dir
app_path = os.path.join(game_dir, "ticTacToe.py")

print(f"⏳ Ejecutando benchmark del juego web durante {duration} segundos...")

# Lanzar el servidor Flask como proceso aparte
proc = subprocess.Popen(['python', app_path], cwd=game_dir)

# Esperar unos segundos para que el servidor arranque
time.sleep(5)

# Probar si el servidor responde
try:
    response = requests.get("http://127.0.0.1:5000")
    if response.status_code != 200:
        print("⚠️ No se pudo acceder al servidor web.")
except Exception as e:
    print("⚠️ Error al conectar con el servidor Flask:", e)

# Monitorear uso de recursos durante la ejecución
while time.time() < end_time and proc.poll() is None:
    cpu = psutil.cpu_percent(interval=0.1)
    mem = psutil.virtual_memory().percent
    timestamp = time.time()
    results.append([timestamp, cpu, mem])
    print(f"CPU: {cpu}%, MEM: {mem}%")
    time.sleep(0.2)

# Si sigue corriendo, lo terminamos
if proc.poll() is None:
    proc.terminate()

# Detectar si estamos dentro de Docker o VM automáticamente

def running_in_docker():
    """Detecta si está corriendo dentro de un contenedor Docker."""
    path = '/proc/self/cgroup'
    if os.path.exists('/.dockerenv'):
        return True
    if os.path.isfile(path):
        with open(path) as f:
            return any('docker' in line or 'kubepods' in line for line in f)
    return False

def running_in_vm():
    """Detecta si está corriendo en VM de forma muy básica (Linux)"""
    # Esto puede variar, aquí un ejemplo básico con platform
    # Se puede mejorar con comandos de sistema
    system = platform.system()
    if system != 'Linux':
        return False
    try:
        with open('/sys/class/dmi/id/product_name') as f:
            product_name = f.read().lower()
            # Algunos nombres comunes de VM:
            vm_signs = ['virtualbox', 'vmware', 'kvm', 'qemu', 'hyper-v']
            if any(sign in product_name for sign in vm_signs):
                return True
    except Exception:
        pass
    return False

if running_in_docker():
    env = 'docker'
elif running_in_vm():
    env = 'vm'
else:
    env = input("¿Se está ejecutando en una VM? (y/n): ").strip().lower()
    env = 'vm' if env == 'y' else 'docker'

filename = f"benchmark_ticTacToe_{env}.csv"
filepath = os.path.join(script_dir, "..", "results", filename)

# Guardar resultados
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
