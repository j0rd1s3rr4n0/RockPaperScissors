# Piedra Papel Tijeras
# By Jordi Serrano
# Instagram: @jordi_serrano
import os
import time
import random
pts_machine = 3
pts_player = 3
os.system('title Rock Paper Scissors ~ By Jordi Serrano')
os.system('cls')
abc = ['tijeras','papel','piedra']
logo="""
  _____            _      _____                      _____      _                        
 |  __ \\          | |    |  __ \\                    / ____|    (_)                       
 | |__) |___   ___| | __ | |__) |_ _ _ __   ___ _ _| (___   ___ _ ___ ___  ___  _ __ ___ 
 |  _  // _ \\ / __| |/ / |  ___/ _` | '_ \\ / _ \\ '__\\___ \\ / __| / __/ __|/ _ \\| '__/ __|
 | | \\ \\ (_) | (__|   < _| |  | (_| | |_) |  __/ |_ ____) | (__| \\__ \\__ \\ (_) | |  \\__ \\
 |_|  \\_\\___/ \\___|_|\\_( )_|   \\__,_| .__/ \\___|_( )_____/ \\___|_|___/___/\\___/|_|  |___/
                       |/           | |          |/                                      
                                    |_|                                                  

  ╦┌┐┌┌─┐┌┬┐┌─┐┌─┐┬─┐┌─┐┌┬┐   ┌─┐ ┬┌─┐┬─┐┌┬┐┬    ┌─┐┌─┐┬─┐┬─┐┌─┐┌┐┌┌─┐
  ║│││└─┐ │ ├─┤│ ┬├┬┘├─┤│││ : │└┘ ││ │├┬┘ │││    └─┐├┤ ├┬┘├┬┘├─┤││││ │
  ╩┘└┘└─┘ ┴ ┴ ┴└─┘┴└─┴ ┴┴ ┴   └──└┘└─┘┴└──┴┘┴────└─┘└─┘┴└─┴└─┴ ┴┘└┘└─┘
"""
ui_e =' '
ui_p =' '
# PLAYER =============================================================
#Rock

p_rock="""
JUGADOR ( TU )
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

#Paper
p_paper="""
JUGADOR ( TU )
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
p_scissors="""
JUGADOR ( TU )
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# MACHINE ==============================================================

m_rock="""                                 ORDENADOR
                                         _______    
                                        (____   '---
                                       (_____)      
                                       (_____)      
                                        (____)      
                                         (___)__.---
"""

#Paper
m_paper="""                                     ORDENADOR
                                              _______     
                                         ____(____    '---
                                        (______           
                                      (_______          
                                       (_______         
                                           (_________----
"""

# Scissors
m_scissors="""                                 ORDENADOR 
                                              _______   
                                         ____(____   '---
                                        (______          
                                      (__________        
                                           (____)              
                                            (___)__.---         
"""
victoria="""
db    db d888888b  .o88b. d888888b  .d88b.  d8888b. d888888b  .d8b.  
88    88   `88'   d8P  Y8 `~~88~~' .8P  Y8. 88  `8D   `88'   d8' `8b 
Y8    8P    88    8P         88    88    88 88oobY'    88    88ooo88 
`8b  d8'    88    8b         88    88    88 88`8b      88    88~~~88 
 `8bd8'    .88.   Y8b  d8    88    `8b  d8' 88 `88.   .88.   88   88 
   YP    Y888888P  `Y88P'    YP     `Y88P'  88   YD Y888888P YP   YP 
"""
derrota="""
`7MM'''Yb.                                      mm            
  MM    `Yb.                                    MM            
  MM     `Mb  .gP"Ya `7Mb,od8 `7Mb,od8 ,pW"Wq.mmMMmm  ,6"Yb.  
  MM      MM ,M'   Yb  MM' "'   MM' "'6W'   `Wb MM   8)   MM  
  MM     ,MP 8M""""""  MM       MM    8M     M8 MM    ,pm9MM  
  MM    ,dP' YM.    ,  MM       MM    YA.   ,A9 MM   8M   MM  
.JMMmmmdP'    `Mbmmd'.JMML.   .JMML.   `Ybmd9'  `Mbmo`Moo9^Yo.
"""

while pts_machine or pts_player >= 0: # establece que haga todo esto hasta que tenga valor a 0 de vidas
	if pts_machine == 0:
		print(victoria)
		break
	elif pts_player == 0:
		print(derrota)
		break
	print(logo)
	print(" Vidas Restantes maquina: "+str(pts_machine))
	print(" Vidas Restantes del jugador: "+str(pts_player))
	# Genera Alatoriamente la opcion de la maquina y pregunta al usuario cual desea escoger
	e_machine = random.choice(['piedra', 'papel', 'tijeras'])
	e_player = str(input(" Elige: (1)PIEDRA (2)PAPEL (3)TIJERAS: "))
	e_player = e_player.lower()
	# Definine la parte visual de Rock Paper Scissors
	#if e_player =="piedra":
	#	ui_p = p_rock
	#elif e_player == "papel":
	#	ui_p = p_paper
	#elif e_player == "tijeras":
	#	ui_p = p_scissors
	#elif e_machine =="piedra":
	#	ui_m = m_rock
	#elif e_machine == "papel":
	#	ui_m = m_paper
	#elif e_machine == "tijeras":
	#	ui_m = m_scissors
	
	if e_player =='1' and e_machine == 'tijeras':
		pts_machine = pts_machine-1
		stat=' Gana el Jugador'
		print(m_scissors)
		print(p_rock)
	elif e_player == '1' and e_machine == 'papel':
		stat=' Gana el Ordenador'
		pts_player = pts_player-1
		print(m_paper)
		print(p_rock)
	elif e_player == '1' and e_machine == 'piedra':
		stat=' Empate'
		print(m_rock)
		print(p_rock)	
	elif e_player == '2' and e_machine == 'tijeras':
		pts_player = pts_player-1
		stat=' Gana el Ordenador'
		print(m_scissors)
		print(p_paper)	
	elif e_player == '2' and e_machine == 'papel':
		stat=' Empate'
		print(m_paper)
		print(p_paper)	
	elif e_player == '2' and e_machine == 'piedra':
		pts_machine = pts_machine-1
		stat=' Gana el Jugador'
		print(m_rock)
		print(p_paper)	
	elif e_player == '3' and e_machine == 'tijeras':
		stat=' Empate'
		print(m_scissors)
		print(p_scissors)	
	elif e_player == '3' and e_machine == 'papel':
		pts_machine = pts_machine-1
		stat=' Gana el Jugador'
		print(m_paper)
		print(p_scissors)	
	elif e_player == '3' and e_machine == 'piedra':
		pts_player = pts_player-1
		stat=' Gana el Ordenador'
		print(m_rock)
		print(p_scissors)	
	elif e_player not in  abc:
		print("  ")
		print("  ERROR")
		print(""" Se introdujeron parametos no validos.
 porfavor introduzca datos validos.""")
		stat="ERROR"
	print("  ")
#	print(" Elección de la màquina: "+e_machine)
#	print(" Elección del jugador: "+e_player)
	print(" ________________________DATOS_DE _PARTIDA________________________")    
	print(" Estado del juego: "+stat)
	print("  ")
	time.sleep(1)
	os.system('cls')
print(" GRACIAS POR JUGAR")
	#Eliminar los '#' par activar esta funcion (inacabada)
	#stats="Datos del Juego:"+"""
	#Elección de la màquina: """+e_machine+"""
	#Elección del jugador: """+e_player+"""
	#Estado del juego: """+stat
	#print(stats)
time.sleep(1)
