# multi-rdp-connector

## Descripción
Este script en Python permite conectar automáticamente a múltiples servidores a través de RDP (Remote Desktop Protocol) usando credenciales comunes. Ideal para administradores de sistemas que necesitan abrir varias sesiones remotas de manera rápida y sencilla.

## Funcionalidades
- Permite ingresar una lista de IPs o nombres de servidores.
- Usa credenciales comunes para todas las conexiones.
- Automatiza la creación de sesiones RDP con `mstsc`.
- Almacena temporalmente las credenciales con `cmdkey`.

## Ejemplo de uso

Introduce las IPs o nombres de los servidores (presiona Enter en una línea vacía para finalizar):
Introduce la IP o el nombre del servidor (o deja vacío para finalizar): 192.168.1.10
Introduce la IP o el nombre del servidor (o deja vacío para finalizar): servidor-ejemplo
Introduce la IP o el nombre del servidor (o deja vacío para finalizar): 

Conectando a 192.168.1.10...
Conectando a servidor-ejemplo...

## Requisitos
- Sistema operativo Windows (ya que utiliza `mstsc` y `cmdkey`).
- Python 3.x instalado.

## Uso
1. Clona este repositorio o descarga el script.
2. Edita las variables `username` y `password` dentro del script con tus credenciales.
3. Ejecuta el script con Python:
   ```bash
   python multi_rdp_connector.py
