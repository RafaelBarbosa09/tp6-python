import os
import subprocess
import platform
import nmap


def scan_host(host):
    nm = nmap.PortScanner()

    nm.scan(host)
    print(nm[host].hostname())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocolo : %s' % proto)

        lport = nm[host][proto].keys()
        # lport.sort()
        for port in lport:
            print('Porta: %s\t Estado: %s' %
                  (port, nm[host][proto][port]['state']))


def obter_hostnames(host_validos):
    nm = nmap.PortScanner()
    print("entrando")
    for i in host_validos:
        try:
            print("processando", i)
            nm.scan(i)
            print("O IP", i, "possui o nome", nm[i].hostname())
        except:
            print("Deu ruim", i)
            pass


def retorna_codigo_ping(hostname):
    """Usa o utilitario ping do sistema operacional para encontrar   o host. ('-c 5') indica, em sistemas linux, que deve mandar 5   pacotes. ('-W 3') indica, em sistemas linux, que deve esperar 3   milisegundos por uma resposta. Esta funcao retorna o codigo de   resposta do ping """

    plataforma = platform.system()
    args = []
    print(hostname)
    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]

    ret_cod = subprocess.call(args,
                              stdout=open(os.devnull, 'w'),
                              stderr=open(os.devnull, 'w'))
    return ret_cod


def verifica_hosts(base_ip):
    """Verifica todos os host com a base_ip entre 1 e 255 retorna uma lista com todos os host que tiveram resposta 0 (ativo)"""
    print("Mapeando\r")
    host_validos = []
    return_codes = dict()
    for i in range(1, 255):

        return_codes[base_ip +
                     '{0}'.format(i)] = retorna_codigo_ping(base_ip + '{0}'.format(i))
        if i % 20 == 0:
            print(".", end="")
        if return_codes[base_ip + '{0}'.format(i)] == 0:
            host_validos.append(base_ip + '{0}'.format(i))
    print("\nMapping ready...")

    return host_validos


# Chamadas
ip_string = input("Entre com o ip alvo: ")
ip_lista = ip_string.split('.')
base_ip = ".".join(ip_lista[0:3]) + '.'
print("O teste ser?? feito na sub rede: ", base_ip)
host_validos = verifica_hosts(base_ip)
print("Os host v??lidos s??o: ", host_validos)

# altere o codigo para salvar os host_validos e poder utilizar na   nova funcao
# obter_hostnames(host_validos)

print("")
print("Fazendo varredura no IP", ip_string)
scan_host(ip_string)
