import subprocess

# Función para capturar las IPs o nombres de servidores
def capturar_entrada():
    print("Introduce las IPs o nombres de los servidores (presiona Enter en una línea vacía para finalizar):")
    servidores = []
    
    while True:
        server = input("Introduce la IP o el nombre del servidor (o deja vacío para finalizar): ").strip()
        if server == "":
            break
        
        servidores.append(server)
    
    return servidores

# Función para abrir una sesión RDP
def open_rdp_session(server, username, password):
    # Guardar temporalmente las credenciales usando cmdkey
    subprocess.run(f'cmdkey /generic:{server} /user:{username} /pass:{password}', shell=True)
    
    # Ejecutar mstsc para abrir una conexión RDP
    print(f"Conectando a {server}...")
    # Usamos Popen para abrir la conexión RDP sin bloquear el siguiente comando
    subprocess.Popen(f'mstsc /v:{server}', shell=True)

# Función principal para conectar a múltiples servidores
def conectar_a_servidores():
    # Capturar las IPs o nombres de los servidores
    servidores = capturar_entrada()
    
    # Configurar las credenciales comunes
    username = "Dominio\\usuario"  # Usuario común
    password = "password"  # Contraseña común
    
    # Realizar la conexión a cada servidor
    for server in servidores:
        # Iniciar la conexión a escritorio remoto
        open_rdp_session(server, username, password)

# Ejecutar el programa
if __name__ == "__main__":
    conectar_a_servidores()
