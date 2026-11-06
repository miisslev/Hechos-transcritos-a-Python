#reglas
REGLAS = {
    # R1: objetivo de perdida de peso
    "R1": {
        "si": lambda usuario: usuario["objetivo"] == "bajar_peso",
        "entonces": {
            "ajuste_calorico": "déficit",
            "factor_calorias": -500,
            "proteina_g_kg": 2.0,
            "mensaje": "Se considera un déficit calórico para el objetivo de pérdida de peso."
        },
        "hechos_soporte": ["H1", "H7", "H12"]
    },
    # R2: objetivo de ganancia muscular
    "R2": {
        "si": lambda usuario: usuario["objetivo"] == "ganar_musculo",
        "entonces": {
            "ajuste_calorico": "superávit",
            "factor_calorias": 300,
            "proteina_g_kg": 2.2,
            "mensaje": "Se considera un incremento del aporte energético y proteico para favorecer el desarrollo muscular."
        },
        "hechos_soporte": ["H5", "H7", "H11"]
    },
    # R3: objetivo de mantenimiento
    "R3": {
        "si": lambda usuario: usuario["objetivo"] == "mantenimiento",
        "entonces": {
            "ajuste_calorico": "normocalórica",
            "factor_calorias": 0,
            "proteina_g_kg": 1.6,
            "mensaje": "Se busca mantener un equilibrio entre la energía consumida y el gasto energético."
        },
        "hechos_soporte": ["H2", "H7", "H16"]
    },
    # R4: nivel elevado de actividad fisica
    # Se considera el gasto energético adicional, sin asumir que necesariamente deben aumentarse los carbohidratos.
    "R4": {
        "si": lambda usuario: usuario["factor_actividad"] >= 1.55,
        "entonces": {
            "considerar_gasto_adicional": True,
            "mensaje": "El nivel de actividad física puede incrementar el gasto energético total y debe considerarse al estimar las necesidades diarias."
        },
        "hechos_soporte": ["H1", "H8", "H16"]
    },
    # R5: habitos alimenticios poco saludables
    "R5": {
        "si": lambda usuario: usuario.get("habitos_inadecuados", False),
        "entonces": {
            "mejorar_habitos": True,
            "recomendacion": "Se recomienda mejorar la calidad de la alimentación, priorizando alimentos variados y de alto valor nutricional."
        },
        "hechos_soporte": ["H2", "H6", "H10", "H15"]
    },
    # R6: consumo elevado de azucar
    "R6": {
        "si": lambda usuario: usuario.get("alto_consumo_azucar", False),
        "entonces": {
            "reducir_azucar": True,
            "mensaje": "Se recomienda limitar el consumo de azúcares libres y bebidas azucaradas."
        },
        "hechos_soporte": ["H4", "H10", "H15"]
    },
    # R7: preservacion muscular durante la perdida de peso
    "R7": {
        "si": lambda usuario: (
            usuario["objetivo"] == "bajar_peso"
            and usuario.get("preservar_musculo", True)
        ),
        "entonces": {
            "proteina_g_kg": 2.2,
            "mensaje": "Se considera una mayor cantidad de proteína como parte de la estrategia para favorecer la conservación de la masa muscular."
        },
        "hechos_soporte": ["H5", "H7", "H11"]
    },
    # R8: recomendaciones generales para el mantenimiento
    "R8": {
        "si": lambda usuario: usuario["objetivo"] == "mantenimiento",
        "entonces": {
            "recomendacion_estilo_vida": "Mantener actividad física regular, incluir ejercicios de fortalecimiento muscular y procurar una alimentación equilibrada.",
            "mensaje": "Se busca fomentar hábitos saludables y sostenibles a largo plazo."
        },
        "hechos_soporte": ["H2", "H13", "H14"]
    },
# R9: distribucion de grasas
"R9": {
    "si": lambda usuario: usuario["objetivo"] in [
        "bajar_peso",
        "ganar_musculo",
        "mantenimiento"
    ],
    "entonces": {
        "porcentaje_grasas": 0.25,
        "mensaje": "Se propone destinar el 25% de las calorías diarias al consumo de grasas."
    },
    "hechos_soporte": ["H7", "H10"]
},
# R10: distribucion de carbohidratos
"R10": {
    "si": lambda usuario: usuario["objetivo"] in [
        "bajar_peso",
        "ganar_musculo",
        "mantenimiento"
    ],
    "entonces": {
        "calculo_carbohidratos": "calorias_restantes",
        "mensaje": "Los carbohidratos se determinarán utilizando las calorías restantes después de calcular proteínas y grasas."
    },
    "hechos_soporte": ["H7"]
    }
}
