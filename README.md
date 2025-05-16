# Proyecto de Evaluación Comparativa de Rendimiento: Máquina Virtual vs Docker 

## 1. Introducción: ¿Qué son las máquinas virtuales y los contenedores?

### Máquinas Virtuales (VM)

Una máquina virtual (VM) es una emulación de un sistema computacional completo que se ejecuta sobre un hardware físico, permitiendo correr múltiples sistemas operativos independientes en una misma máquina física (host). Este aislamiento es posible gracias a un software llamado **hipervisor**, que gestiona y asigna los recursos físicos entre varias VMs.

Tipos de hipervisores:

- **Tipo 1 (bare-metal):** Se ejecutan directamente sobre el hardware (VMware ESXi, Microsoft Hyper-V, Xen).
- **Tipo 2 (hosted):** Se ejecutan sobre un sistema operativo anfitrión (VirtualBox, VMware Workstation).

Cada VM contiene su propio kernel, sistema operativo y espacio de usuario, asegurando un fuerte aislamiento. Esto las hace ideales para pruebas, desarrollo y producción con distintos sistemas operativos.

**Desventajas:** alto consumo de recursos, mayor tiempo de arranque y sobrecarga por virtualización.

> Referencia: Smith, J. & Nair, R. (2005). *The architecture of virtual machines*. *Computer*, 38(5), 32-38.

### Contenedores Docker (en Codespace)

Los contenedores virtualizan a nivel de sistema operativo usando funciones como `namespaces` y `cgroups`, permitiendo ejecutar múltiples contenedores aislados que comparten el mismo kernel.

En este proyecto se usó **GitHub Codespaces**, un entorno cloud que permite usar Docker sin configuración local, con arranque inmediato y bajo uso de recursos.

**Ventajas:** ligeros, rápidos, portables y adecuados para CI/CD.

**Desventajas:** menor aislamiento y seguridad comparado con una VM.

> Referencia: Merkel, D. (2014). *Docker: lightweight Linux containers for consistent development and deployment*. *Linux Journal*, 2014(239), 2.

---

## 2. Configuración del entorno de prueba

**Equipo host:**

- Procesador: Intel Core i7-9750H  
- Memoria RAM: 16GB DDR4  
- Sistema Operativo Host: Ubuntu 20.04 LTS  

**Máquina Virtual:**

- VirtualBox con Ubuntu 20.04 LTS  
- 2 CPUs, 4GB RAM asignados  

**Contenedor Docker (en Codespace):**

- Imagen base: `ubuntu:20.04`  
- 2 CPUs, 4GB RAM limitados por configuración  

**Aplicación usada:** Juego de TicTacToe en Python, ejecutado en ambos entornos para comparar el rendimiento bajo una misma carga.

---

## 3. Métricas y herramientas utilizadas

**Métricas analizadas:**

- Uso de CPU y memoria (medido con `psutil`)
- Espacio en disco total ocupado
- Tiempo de arranque del entorno
- Latencia en la respuesta de la aplicación

**Herramientas:**

- Python (`psutil`, `subprocess`, `time`)
- Scripts personalizados de benchmarking
- Docker (en Codespace) y VirtualBox
- Matplotlib, Pandas y Jupyter Notebook para análisis y gráficos

---

## 4. Resultados

- Docker (en Codespace) tiene un tiempo de arranque significativamente menor que la VM.
- Docker consume menos CPU y memoria promedio durante la ejecución.
- Docker requiere mucho menos espacio en disco.
- La latencia del juego fue ligeramente mejor en Docker.

**Gráficos generados:**

- Comparación Uso de CPU: TicTacToe VM vs Docker  
- Comparación Uso de Memoria: TicTacToe VM vs Docker  
- Promedio uso CPU y Memoria: VM vs Docker  

---

## 5. Análisis: Fortalezas y debilidades

| Aspecto              | Máquina Virtual                        | Docker (en Codespace)                          |
|----------------------|----------------------------------------|------------------------------------------------|
| **Aislamiento**      | Fuerte, kernel separado y seguro       | Compartición del kernel, menor aislamiento     |
| **Uso de recursos**  | Alto consumo de CPU, RAM y disco       | Bajo consumo, entorno ligero y eficiente       |
| **Tiempo de arranque** | Más lento (segundos a minutos)         | Muy rápido (milisegundos a segundos)           |
| **Portabilidad**     | Menos flexible, imágenes pesadas       | Alta portabilidad y despliegue ágil            |
| **Seguridad**        | Aislamiento completo, más seguro       | Requiere configuración adicional               |

---

## 6. Conclusión: ¿Cuándo usar VM vs Docker?

- **Usar VM** cuando se requiera un entorno aislado, ejecución de diferentes sistemas operativos o alta seguridad.
- **Usar Docker** para desarrollo rápido, CI/CD, microservicios o cuando se priorice eficiencia y portabilidad.

Docker (en Codespace) demostró ser una solución eficiente y práctica para ejecutar aplicaciones ligeras como TicTacToe, mientras que las VMs siguen siendo preferibles en contextos con mayores requisitos de aislamiento y control.

---
