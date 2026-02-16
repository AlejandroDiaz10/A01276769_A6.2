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
│   ├── test_hotel.py
│   ├── test_customer.py
│   └── test_reservation.py
├── data/                  # Archivos de persistencia (JSON)
│   ├── sample/            # Datos de referencia (no modificables)
│   │   ├── customers.json
│   │   ├── hotels.json
│   │   └── reservations.json
│   ├── customers.json     # Datos reales (modificables en tiempo de ejecución)
│   ├── hotels.json
│   └── reservations.json
└── results/               # Resultados de pruebas y análisis
    ├── flake8_analysis/
    ├── pylint_analysis/
    ├── coverage_reports/
    └── execution_tests/
        ├── customer_manual_tests/
        ├── hotel_manual_tests/
        └── reservation_manual_tests/
```

### Archivos de Datos

El proyecto utiliza dos conjuntos de archivos JSON:

- **`data/sample/`**: Archivos de **referencia** que contienen ejemplos de estructura de datos. No se modifican durante la ejecución.
- **`data/`**: Archivos **reales** que se crean y modifican durante el uso normal del programa.

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

## Uso

### Ejecutar el programa principal

El sistema incluye un programa interactivo con menú para gestionar clientes, hoteles y reservaciones.
```bash
# Opción 1: Ejecutar como módulo (recomendado)
python -m src.main

# Opción 2: Ejecutar directamente
python src/main.py
```

### Funcionalidades disponibles

**1. Customer Management (Gestión de Clientes)**
- Crear, mostrar, modificar y eliminar clientes
- Operaciones independientes, no requieren otros módulos

**2. Hotel Management (Gestión de Hoteles)**
- Crear, mostrar, modificar y eliminar hoteles
- Gestionar disponibilidad de habitaciones
- Operaciones independientes, no requieren otros módulos

**3. Reservation Management (Gestión de Reservaciones)**
- Crear reservación: **Requiere** un cliente existente y un hotel existente
- Cancelar reservación: Libera automáticamente la habitación en el hotel
- Integra los módulos Customer y Hotel

### Flujo de trabajo recomendado

1. **Crear clientes** en Customer Management
2. **Crear hoteles** en Hotel Management
3. **Crear reservaciones** vinculando clientes con hoteles
4. Las habitaciones se reservan/liberan automáticamente

### Persistencia de datos

Los datos se almacenan en archivos JSON:
- `data/customers.json` - Clientes activos
- `data/hotels.json` - Hoteles con disponibilidad de habitaciones
- `data/reservations.json` - Reservaciones activas

Los archivos en `data/sample/` contienen datos de ejemplo y no se modifican.

## Testing y Análisis de Calidad

### **Customer Module**
```bash
# Ejecutar tests
python -m unittest tests/test_customer.py -v

# Generar reporte de cobertura
coverage run -m unittest tests/test_customer.py
coverage report -m > results/coverage_reports/customer_coverage.txt

# Guardar output de tests
coverage run -m unittest tests/test_customer.py > results/execution_tests/customer_tests.txt 2>&1

# Análisis con Flake8
flake8 src/customer.py > results/flake8_analysis/customer_flake8.txt 2>&1

# Análisis con Pylint
pylint src/customer.py > results/pylint_analysis/customer_pylint.txt 2>&1
```

### **Hotel Module**
```bash
# Ejecutar tests
python -m unittest tests/test_hotel.py -v

# Generar reporte de cobertura
coverage run -m unittest tests/test_hotel.py
coverage report -m > results/coverage_reports/hotel_coverage.txt

# Guardar output de tests
coverage run -m unittest tests/test_hotel.py > results/execution_tests/hotel_tests.txt 2>&1

# Análisis con Flake8
flake8 src/hotel.py > results/flake8_analysis/hotel_flake8.txt 2>&1

# Análisis con Pylint
pylint src/hotel.py > results/pylint_analysis/hotel_pylint.txt 2>&1
```

### **Reservation Module**
```bash
# Ejecutar tests
python -m unittest tests/test_reservation.py -v

# Generar reporte de cobertura
coverage run -m unittest tests/test_reservation.py
coverage report -m > results/coverage_reports/reservation_coverage.txt

# Guardar output de tests
coverage run -m unittest tests/test_reservation.py > results/execution_tests/reservation_tests.txt 2>&1

# Análisis con Flake8
flake8 src/reservation.py > results/flake8_analysis/reservation_flake8.txt 2>&1

# Análisis con Pylint
pylint src/reservation.py > results/pylint_analysis/reservation_pylint.txt 2>&1
```

### **Análisis Completo del Proyecto**
```bash
# Ejecutar todos los tests
python -m unittest discover -s tests -v

# Cobertura total
coverage run -m unittest discover -s tests
coverage report -m
coverage html -d results/coverage_reports/html

# Análisis completo con Flake8
flake8 src/ > results/flake8_analysis/project_flake8.txt 2>&1

# Análisis completo con Pylint
pylint src/ > results/pylint_analysis/project_pylint.txt 2>&1
```

## Estándares de Calidad

- Cumple con PEP 8
- Sin errores en Flake8
- Pylint score: 10.00/10
- Cobertura de código ≥ 85%

## Resultados de Calidad

| Módulo | Flake8 | Pylint | Cobertura | Tests |
|--------|--------|--------|-----------|-------|
| Customer | 0 errores | 10.00/10 | 91% | 10/10 |
| Hotel | 0 errores | 10.00/10 | 95% | 16/16 |
| Reservation | 0 errores | 10.00/10 | 87% | 8/8 |