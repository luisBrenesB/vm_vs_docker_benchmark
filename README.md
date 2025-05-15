# Proyecto de Evaluación Comparativa de Rendimiento: Máquina Virtual vs Docker

## 1. Introducción: ¿Qué son las máquinas virtuales y los contenedores?

### Máquinas Virtuales (VM)

Una máquina virtual (VM) es una emulación de un sistema computacional completo que se ejecuta sobre un hardware físico, permitiendo correr múltiples sistemas operativos independientes en una misma máquina física (host). Este aislamiento es posible gracias a un software llamado hipervisor o monitor de máquina virtual, que gestiona y asigna los recursos físicos de hardware entre varias VMs.

Existen dos tipos principales de hipervisores:

- Tipo 1 (bare-metal): Se ejecutan directamente sobre el hardware físico. Ejemplos incluyen VMware ESXi, Microsoft Hyper-V, y Xen.
- Tipo 2 (hosted): Se ejecutan sobre un sistema operativo ya instalado en el host, como VirtualBox o VMware Workstation.

Cada VM contiene su propio kernel, sistema operativo y espacio de usuario, asegurando un fuerte aislamiento entre máquinas. Esto hace que las VMs sean ideales para ejecutar diferentes sistemas operativos o entornos aislados para pruebas, desarrollo o producción.

Sin embargo, esta independencia implica que las máquinas virtuales suelen consumir más recursos, tienen un tiempo de arranque más prolongado y una sobrecarga adicional por la virtualización del hardware.

**Referencia:** Smith, J. & Nair, R. (2005). The architecture of virtual machines. Computer, 38(5), 32-38.

### Contenedores Docker

Los contenedores, como los que proporciona Docker, representan un enfoque diferente a la virtualización. En lugar de virtualizar hardware completo, los contenedores virtualizan a nivel de sistema operativo utilizando características del kernel Linux como namespaces y cgroups. Esto permite que múltiples contenedores compartan el mismo kernel del host, pero manteniendo aislamiento de procesos, red y sistema de archivos.

Los contenedores son mucho más ligeros, se inician muy rápido y facilitan la portabilidad y escalabilidad de aplicaciones. Además, el ecosistema Docker incluye herramientas para construir, distribuir y ejecutar aplicaciones de manera uniforme y reproducible.

No obstante, dado que comparten kernel, la seguridad y el aislamiento no son tan estrictos como en una VM. Esto puede representar un riesgo en entornos con requisitos estrictos de seguridad.

**Referencia:** Merkel, D. (2014). Docker: lightweight Linux containers for consistent development and deployment. Linux Journal, 2014(239), 2.

## 2. Configuración del entorno de prueba

Para esta evaluación comparativa, se utilizó un equipo host con las siguientes características:

- Procesador: Intel Core i7-9750H
- Memoria RAM: 16GB DDR4
- Sistema Operativo Host: Ubuntu 20.04 LTS

Para la máquina virtual, se utilizó VirtualBox con:

- Sistema Operativo invitado: Ubuntu 20.04 LTS
- 2 CPUs asignados
- 4GB RAM asignados

Para Docker:

- Imagen base: ubuntu:20.04
- Configuración por defecto para contenedor (2 CPUs, 4GB RAM limitados)

La aplicación utilizada para la prueba fue un juego sencillo (ticTacToe) desarrollado en Python, ejecutado en ambos entornos para comparar el rendimiento y consumo de recursos bajo carga similar.

## 3. Métricas y herramientas utilizadas

Las principales métricas evaluadas fueron:

- Uso de CPU y memoria RAM durante la ejecución del juego, medido con psutil en Python.
- Espacio en disco ocupado por el entorno completo (sistema operativo, aplicaciones y dependencias).
- Tiempo de arranque del entorno.
- Latencia y rendimiento de la aplicación medida a través de tiempos de respuesta en el juego.

Se utilizaron herramientas estándar como psutil para monitorización, scripts Python personalizados para automatizar la recopilación de datos y Jupyter Notebook para análisis y generación de gráficos.

## 4. Resultados

Los datos recopilados mostraron que:

- El contenedor Docker tiene un tiempo de arranque significativamente menor que la VM.
- Docker consume menos CPU y memoria promedio durante la ejecución del juego.
- El tamaño en disco requerido por Docker es considerablemente menor que el de la VM, debido a la ausencia de un sistema operativo completo.
- La latencia de la aplicación fue similar en ambos entornos, aunque con ligeras variaciones favorables para Docker.

Los gráficos generados con Matplotlib reflejan claramente las diferencias en el uso de recursos y tiempos de ejecución.

## 5. Análisis: Fortalezas y debilidades

### Máquina Virtual

**Ventajas:**

- Aislamiento fuerte y completo, con kernel propio.
- Mejor seguridad en entornos multiusuario.
- Permite ejecutar distintos sistemas operativos.

**Desventajas:**

- Uso elevado de recursos.
- Tiempo de inicio más lento.
- Sobrecarga por virtualización del hardware.

### Docker

**Ventajas:**

- Inicio casi instantáneo.
- Bajo consumo de recursos.
- Excelente para desarrollo, pruebas y despliegue continuo.

**Desventajas:**

- Aislamiento basado en kernel compartido, menos seguro.
- Menor flexibilidad para distintos sistemas operativos.

## 6. Conclusión: ¿Cuándo usar VM vs Docker?

La elección entre VM y Docker depende del caso de uso:

- Use máquinas virtuales cuando se necesite un aislamiento completo, ejecutar sistemas operativos diferentes o cuando la seguridad sea prioritaria.
- Use Docker para entornos de desarrollo rápido, despliegues continuos, microservicios y cuando se requiera eficiencia en uso de recursos.

En este proyecto, Docker mostró ser una opción eficiente y práctica para aplicaciones ligeras, mientras que las VM ofrecen mayor seguridad y aislamiento, con un costo mayor en recursos.
