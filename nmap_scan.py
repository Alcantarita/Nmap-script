import nmap

def main():
    # Creamos un escáner nmap
    scanner = nmap.PortScanner()
    
    # Solicitamos los hosts
    hosts = input("Ingrese los hosts (e.g., 192.168.1.1 o 192.168.1.1/24): ")
    
    # Solicitamos los puertos
    ports = input("Ingrese los puertos (e.g., 22,80,443 o 1-1024): ")
    
    # Solicitamos los argumentos
    arguments = input("Ingrese los argumentos adicionales (e.g., -sS -O): ")
    
    # Solicitamos superusuario
    super_user = input("¿Desea ejecutar el comando como superusuario? (s/n): ").lower()
    
    # Ejecutar el escaneo
    print("\nEjecutando escaneo...")
    if super_user == 's':
        scanner.scan(hosts=hosts, ports=ports, arguments=f"{arguments}", sudo=True)
    else:
        scanner.scan(hosts=hosts, ports=ports, arguments=f"{arguments}")
    
    # Imprimir resultados
    for host in scanner.all_hosts():
        print(f"Host: {host} ({scanner[host].hostname()})")
        print(f"Estado: {scanner[host].state()}")
        for protocol in scanner[host].all_protocols():
            print(f"Protocolo: {protocol}")
            ports = scanner[host][protocol].keys()
            for port in ports:
                print(f"Puerto: {port}\tEstado: {scanner[host][protocol][port]['state']}")
    
if __name__ == "__main__":
    main()

