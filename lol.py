
import random

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
    
    def saludar(self):
        print(f"Saludos, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Herencia: El Infractor es una Persona con atributos adicionales
class Infractor(Persona): 
    def __init__(self, nombre, edad, herramienta):
        # super() inicializa los atributos de la clase base (Persona)
        super().__init__(nombre, edad)
        self.herramienta = herramienta
        self.fondos_sustraidos = 0

    def ejecutar_accion(self):
        print(f"Iniciando intervención. Identidad: {self.nombre}. Herramienta: {self.herramienta}.")
        
        # Lógica de probabilidad de éxito (60% de éxito)
        if random.random() > 0.4:
            monto = random.randint(500, 2000)
            self.fondos_sustraidos += monto
            print(f"✅ Acción exitosa. Monto recuperado: ${monto}. Total en cuenta: ${self.fondos_sustraidos}")
            return True
        else:
            print("❌ La acción ha fallado debido a complicaciones técnicas.")
            return False

class OficialSeguridad(Persona):
    def __init__(self, nombre, rango):
        super().__init__(nombre, 35)
        self.rango = rango

    def realizar_detencion(self, sujeto):
        print(f"🚓 El {self.rango} {self.nombre} ha interceptado a {sujeto.nombre}.")
        
        # Simulación de probabilidad de captura
        efectividad = random.randint(1, 10)
        if efectividad > 5:
            print(f"👮 Procedimiento completado. El sujeto a sido parado por la policia.")
        else:
            print(f"🏃 El sujeto ha evadido a la policia.")

# --- EJECUCIÓN DEL PROGRAMA ---

# 1. Instanciación de objetos
infractor1 = Infractor("Juan", 65, "Herramienta de precisión")
oficial_perez = OficialSeguridad("Pérez", "Sargento")

# 2. Flujo de eventos
if infractor1.ejecutar_accion():
    print("--- Reporte de incidencia en curso ---")
    # 3. Intervención de seguridad
    oficial_perez.realizar_detencion(infractor1)