class ControlSatelite:
    # Constantes
    GRAVEDAD = 9.81            # m/s^2
    RADIO_TIERRA = 6371        # km
    KM = 1000.0                # factor km→m
    HORAS = 1.0                # 1 hora (referencia)

    def __init__(self):
        self.distancia_de_la_tierra: float = 0.0
        self.velocidad_media: float = 0.0
        self.tiempo_de_la_tierra: float = 0.0

    # Estado del satélite según la distancia (km)
    def estado_satelite(self) -> str:
        if self.distancia_de_la_tierra < 1000:
            return "El satélite está en una órbita baja."
        elif 1000 <= self.distancia_de_la_tierra < 35000:
            return "El satélite está en una órbita media."
        else:
            return "El satélite está en una órbita alta."

    # Valida que los valores sean no negativos
    def validar_valores(self, distancia_de_la_tierra: float,
                        velocidad_media: float,
                        tiempo_de_la_tierra: float) -> bool:
        return (distancia_de_la_tierra >= 0 and
                velocidad_media >= 0 and
                tiempo_de_la_tierra >= 0)

    # v = d / t
    def calcular_velocidad(self, distancia_de_la_tierra: float,
                           tiempo_de_la_tierra: float) -> float:
        self.velocidad_media = distancia_de_la_tierra / tiempo_de_la_tierra
        return self.velocidad_media

    # d = v * t
    def calcular_distancia(self, velocidad_media: float,
                           tiempo_de_la_tierra: float) -> float:
        self.distancia_de_la_tierra = velocidad_media * tiempo_de_la_tierra
        return self.distancia_de_la_tierra

    # t = d / v
    def calcular_tiempo(self, distancia_de_la_tierra: float,
                        velocidad_media: float) -> float:
        self.tiempo_de_la_tierra = distancia_de_la_tierra / velocidad_media
        return self.tiempo_de_la_tierra

    # Aceleración gravitatoria a una distancia r (en metros) del centro de masas
    # g = G * M / r^2
    def calcular_gravedad(self, distancia_metros: float) -> float:
        G = 6.67430e-11        # m^3·kg^−1·s^−2
        masa_tierra = 5.972e24 # kg
        return G * masa_tierra / (distancia_metros * distancia_metros)


# Ejemplo rápido de uso (opcional)
if __name__ == "__main__":
    sat = ControlSatelite()

    # Calcular velocidad con d=400 km y t=0.5 h (usa mismas unidades que en Java)
    v = sat.calcular_velocidad(400.0, 0.5)
    print("Velocidad media:", v, "km/h")

    # Setear distancia para evaluar estado de órbita
    sat.distancia_de_la_tierra = 2000.0  # km
    print(sat.estado_satelite())

    # Gravedad a 400 km sobre la superficie (convertimos a metros desde el centro)
    # r = (RADIO_TIERRA + 400 km) * 1000
    r_m = (sat.RADIO_TIERRA + 400.0) * sat.KM
    print("g a 400 km:", sat.calcular_gravedad(r_m), "m/s^2")
