# -*- coding: utf-8 -*-
"""
Proyecto: Automatización E2E - CelFar
Framework: Selenium WebDriver
Descripción: Suite de pruebas para validar múltiples versiones de la aplicación CelFar.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoAlertPresentException
import time

# Configuración de versiones y casos de prueba
versiones = {
    1: "https://nahual.github.io/qc-celfar/?v=1",
    2: "https://nahual.github.io/qc-celfar/?v=2",
    3: "https://nahual.github.io/qc-celfar/?v=3",
    4: "https://nahual.github.io/qc-celfar/?v=4"
}

casos_prueba_detallados = {
    1: [
        (1, '', 'Campo numerico vacio', "El valor ingresado no es un número"),
        (2, '1234567', 'Tamaño maximo', "El valor ingresado es muy largo"),
        (3, '35', 'Conversion numero positivo', "95"),
        (4, 'treinta y cinco', 'texto como valor', "El valor ingresado no es un número"),
        (5, '35,5', 'Coma como separador decimal', "El valor ingresado no es un número"),
        (6, '-5', 'Valor negativo', "23"),
        (7, '-273', 'Valor menor al cero absoluto', "El valor ingresado está debajo del 0 absoluto"),
        (8, None, 'Titulo de la pagina', "CelFar"),
        (9, '0', 'Cero como valor', "32")
    ]
}

# Aplicar casos a todas las versiones
for i in range(2, 5):
    casos_prueba_detallados[i] = casos_prueba_detallados[1]

class CelFarTester:
    def __init__(self, url):
        self.url = url
        options = Options()
        options.add_argument('--headless') # Ejecución sin ventana (ideal para CI/CD)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def _handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            return None

    def navegar(self):
        self.driver.get(self.url)
        time.sleep(2)

    def ingresar_valor(self, valor):
        campo_entrada = self.driver.find_element(By.ID, 'input')
        campo_entrada.clear()
        if valor is not None:
            campo_entrada.send_keys(str(valor))
            campo_entrada.submit()
            self._handle_alert()

    def obtener_resultado(self):
        try:
            return self.driver.find_element(By.ID, 'output').text
        except:
            return "Error al obtener resultado"

    def probar(self, id_test, valor, desc, expected):
        print(f"Ejecutando {id_test}: {desc}")
        self.navegar()
        if 'Titulo' in desc:
            res = self.driver.title
        else:
            self.ingresar_valor(valor)
            res = self.obtener_resultado()
        
        passed = expected in res
        print(f"Resultado: {'PASSED' if passed else 'FAILED'}")
        return passed

    def cerrar(self):
        self.driver.quit()

if __name__ == "__main__":
    for v_num, v_url in versiones.items():
        print(f"\n--- TESTING VERSION {v_num} ---")
        tester = CelFarTester(v_url)
        for c_id, val, desc, exp in casos_prueba_detallados[v_num]:
            tester.probar(f"V{v_num}C{c_id}", val, desc, exp)
        tester.cerrar()
