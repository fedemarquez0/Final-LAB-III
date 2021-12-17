# Trabajo Final - Laboratorio III

[![N|Solid](https://www.ubp.edu.ar/wp-content/themes/ubp-pmkt/img/logo-ubp.png)](https://www.ubp.edu.ar/)

## _Sobre el proyecto_


Este proyecto tiene como fín el control de stock para una cava, el mismo será útilizado por el dueño de la misma y así administrarla de manera digital.

## Instalación

Para el úso del sistema hay como requisitos ciertos pasos:

1- Instalar las dependencias de python 

```sh
pip install Django==3.2.9
pip install requests
```

*Se recomienda el uso de entornos virtuales para la instalación.*

## Clonar el repositorio

```sh
git init
git clone https://github.com/matigodoy/Final-Lab3.git
```

## Implementación API 

El sistema de inventario incorpora la API de `Conversión de moneda ` la misma se utiliza para calcular el precio de los productos al valor del día *(dolares->pesos)*.

>NOTA: Este se ejecuta al abrir un producto, no antes.

## ¿Como ejecutarlo?
Para ejecutar el sistema abrir una consola sobre la ubicación donde clonó el repositorio y ejecutar el siguiente comando:
```sh
py manage.py runserver
```
Una vez ejecutado el comando, dirigirse a la url http://127.0.0.1:8000/

