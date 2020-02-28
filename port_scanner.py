from socket import *
from scapy.all import *
import os
import PySimpleGUI as sg


def tcpScanner(IPalvo,porta_min,porta_max):
	lista_aberto = []
	lista_aberto.append("Portas abertas do IP {}:   ".format(IPalvo))

	for porta in range(porta_min,porta_max+1):
		sock = socket.socket(AF_INET,SOCK_STREAM)
		try: 
			sock.connect((IPalvo,int(porta)))
			string = "Porta: " +str(porta) +" - Aberta"
			try:
				serv_name = str(getservbyport(porta, "tcp"))
				string+=" | Serviço: " + serv_name
				lista_aberto.append(string)
			except:
				lista_aberto.append(string)
				
			sock.close()
		except:
			sock.close()

	return lista_aberto


# Créditos: https://github.com/cptpugwash/Scapy-port-scanner/blob/master/port_scanner.py
def udpScanner(IPalvo,porta_min,porta_max):
	lista_aberto = []
	lista_aberto.append("Portas abertas do IP {}:   ".format(IPalvo))
	for porta in range(porta_min,porta_max+1):
		pkt = sr1(IP(dst=IPalvo)/UDP(sport=porta, dport=porta), timeout=2, verbose=0)
		if pkt == None:
			string = "Porta: : " + str(porta)+" - Aberta"
			try:
				serv_name = str(getservbyport(porta, "udp"))
				string+=" | Serviço: "+ serv_name
				lista_aberto.append(string)
			except:
				lista_aberto.append(string)
	return lista_aberto



def run(ip_rede,ip_alvo,range_min,range_max,tcp_udp):

	if ip_rede == 'Host':
		host_is_up  = True if os.system("ping -c 1 " + ip_alvo) is 0 else False

		if host_is_up:
			if tcp_udp == 'TCP':
				result = tcpScanner(ip_alvo,int(range_min),int(range_max))
			else:
				result = udpScanner(ip_alvo,int(range_min),int(range_max))
		else:
			result = ['Host '+ip_alvo+' Indisponível']
		return result
	else:
		list_result = []

		splitted = ip_alvo.split('-')

		ip_min = int((splitted[0].split('.'))[3])
		ip_max = int((splitted[1].split('.'))[3]) + 1


		ip_form = splitted[0].split('.')
		dot = '.'
		
		for ip in range(ip_min,ip_max):
			ip_form[3] = str(ip)
			ip_alvo = dot.join(ip_form)

			host_is_up  = True if os.system("ping -c 1 " + ip_alvo) is 0 else False

			if host_is_up:
				if tcp_udp == 'TCP':
					result = tcpScanner(ip_alvo,int(range_min),int(range_max))
				else:
					result = udpScanner(ip_alvo,int(range_min),int(range_max))
				list_result+=result
			else:
				list_result.append('Host '+ip_alvo+' Indisponível')

		return list_result


def main():

	sg.theme('LightGreen2')

	layout = [ 	[sg.Text('Selecione se o alvo é um host ou uma rede'),sg.Combo(['Host', 'Rede'],size=(15,1))],
				[sg.Text('Insira o IP do alvo ou o range de IPs a ser escaneado\n=>Exemplo Host: 192.168.1.102\n=>Exemplo Rede: 192.168.1.102-192.168.1.152'), sg.InputText()],
	            [sg.Text('Insira a porta para iniciar o scanner'), sg.InputText()],
	            [sg.Text('Insira a porta final do scanner'), sg.InputText()],
	            [sg.Text('Selecione o protocolo desejado'),sg.Combo(['TCP', 'UDP'],size=(15,1))],
	            [sg.Button('Iniciar',size=(15,1)),sg.Button('Sair',size=(15,1))] ]

	
	window = sg.Window('Escaneador de Portas', layout,size=(500,170))
	while True:
	    event, values = window.read()
	    if event in (None, 'Cancel'):
	        break

	    result = run(values[0],values[1],values[2],values[3],values[4])
	    
	    break
	window.close()

	
	s = '\n'.join([str(i) for i in result])
	sg.PopupScrolled("Escaneamento completo", f"As seguintes portas estão abertas: \n", f"{s}")



if __name__ == "__main__":
    main()






## UDP Scanner usando Socket(Aparenta não funcionar corretamente)
# def udpScanner(IPalvo,porta_min,porta_max):
# 	lista_aberto = []
# 	lista_aberto.append("Portas abertas do IP : {}".format(IPalvo))

# 	for porta in range(porta_min,porta_max+1):
# 		consock = socket(AF_INET,SOCK_DGRAM)
# 		try:
# 			consock.connect((IPalvo,porta))
# 			string = "Porta: : " + str(porta)+" - Aberta"
# 			try:
# 				serv_name = str(getservbyport(porta, "udp"))
# 				string+=" | Serviço: "+ serv_name
# 				lista_aberto.append(string)
# 			except:
# 				lista_aberto.append(string)
# 			consock.close()
# 		except:
# 			consock.close()

# 	return lista_aberto
