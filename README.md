# 🤖 E2E Automation Testing - CelFar App

Proyecto de automatización de pruebas "End-to-End" realizado para la aplicación **CelFar** (Conversor de temperaturas). Este proyecto valida la lógica de negocio y la interfaz de usuario a través de 4 versiones distintas de la aplicación.
---


### 🚀 Características del Proyecto
* **Patrón de Diseño:** Implementación basada en clases para mejorar la reutilización del código.
* **Ejecución Headless:** Configurado para ejecutarse sin interfaz gráfica, ideal para entornos de Integración Continua (CI).
* **Cross-Version Testing:** Suite diseñada para iterar automáticamente sobre diferentes despliegues de la misma app.
* **Manejo de Alertas:** Lógica integrada para gestionar ventanas emergentes y errores del sistema.

### 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Herramienta de Automatización:** Selenium WebDriver
* **Driver Management:** WebDriver Manager (para gestión automática de drivers de Chrome).

### 📋 Casos de Prueba Automatizados
1. Validación de campos vacíos.
2. Control de límites de caracteres.
3. Cálculos de valores positivos, negativos y límite de cero absoluto.
4. Validación de tipos de datos (Strings en campos numéricos).

### ⚙️ Instalación y Ejecución
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar el script: `python test_celfar_e2e.py`
---

## 📊 Resultados de la Ejecución y Reporte de Bugs
La ejecución de esta suite de pruebas permitió identificar diversos fallos de lógica y visualización en las diferentes versiones de la aplicación. 

Toda la evidencia y el detalle técnico de los hallazgos se encuentra documentado en el siguiente reporte:

👉 **[Ver Reporte de Errores Completo (Excel)](./Reporte-de-Bugs-Detallado-Elizabeth-Woca.xlsx)**
