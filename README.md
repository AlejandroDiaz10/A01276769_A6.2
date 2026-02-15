# Hotel Reservation System

Sistema de reservaciones de hotel implementado en Python con persistencia en archivos JSON.

## Descripción

Este proyecto implementa un sistema completo de gestión de reservaciones hoteleras que incluye:
- Gestión de hoteles
- Gestión de clientes
- Gestión de reservaciones
- Persistencia de datos en archivos JSON
- Manejo de errores robusto

## Estructura del Proyecto

```
hotel-reservation-system/
├── src/                    # Código fuente
│   ├── hotel.py           # Clase Hotel
│   ├── customer.py        # Clase Customer
│   ├── reservation.py     # Clase Reservation
│   └── main.py            # Programa principal
├── tests/                 # Pruebas unitarias
├── data/                  # Archivos de persistencia (JSON)
└── results/               # Resultados de pruebas y análisis
```

## Instalación

1. Clonar el repositorio
2. Crear entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Requisitos

- Python 3.8+
- flake8 (análisis estático de código)
- pylint (análisis estático de código)
- coverage (cobertura de código)

## Estándares de Calidad

- Cumple con PEP 8
- Sin errores en Flake8
- Sin warnings en Pylint
- Cobertura de código ≥ 85%
