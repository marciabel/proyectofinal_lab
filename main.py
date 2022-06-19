'''
Proyecto final: "Alicia en el Pais de las Encrucijadas"
Materia: Laboratorio de Computacion I
Profesores:
            Balmaceda, Javier
            Coppo, Ricardo
Autores:
        Alvarez, Marcia Belen
        D'Annunzio, Stefano 
'''

#Import de Librerias y Modulos
import random
from re import X
import tkinter
from tkinter.font import BOLD
from tkinter.ttk import LabelFrame
from turtle import bgcolor, bgpic
from unittest import result
from PIL import ImageTk, Image

#Pantalla Bienvenida---------------------------------------------------------------------------------------------------------
def welcome():
        #Creación pantalla Bienvenida------------------------------------------------------------------------------------------------------
        welcome_screen = LabelFrame(window, width=712, height=540)
        welcome_screen.place(x=0, y=0, relheight=1, relwidth=1)

        canvas_welcome_image = tkinter.Canvas(welcome_screen, width = 712, height=540, )
        canvas_welcome_image.pack(fill="both", expand=True)
        canvas_welcome_image.create_image(0,0, image=welcome_screen_image, anchor="nw")

        #----------Texto de Bienvenida-------------------------------------------------------------------------------------------------------
        canvas_welcome_image.create_text(356, 100, text="Alicia en el Pais de las Encrucijadas", font=("Gabriola", 40, "bold"),fill="white")

        #----------Boton Comenzar------------------------------------------------------------------------------------------------------------
        start_button = tkinter.Button(welcome_screen, text = "Comenzar", font=("Gabriola",20,"bold"), padx= 75,bg ="#4160af", fg= "#efefef", command = introduction)
        start_button_window = canvas_welcome_image.create_window(400,330, anchor="nw", window=start_button)

        #----------Boton Instrucciones-------------------------------------------------------------------------------------------------------
        howto_button = tkinter.Button(welcome_screen, text = "Instrucciones", font=("Gabriola",15,"bold"), padx= 55,bg ="#b6e2d3", fg= "#4160af", command = open_how_to)
        howto_button_window = canvas_welcome_image.create_window(420,430, anchor="nw", window=howto_button)

#Ver Instrucciones-----------------------------------------------------------------------------------------------------------
def open_how_to():
        instructions_screen = LabelFrame(window, width=712, height=540)
        instructions_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_instructions_image = tkinter.Canvas(instructions_screen, width = 712, height=540, )
        canvas_instructions_image.pack(fill="both", expand=True)
        canvas_instructions_image.create_image(0,0, image=instructions_screen_image, anchor="nw")

        instructions_txt = open("Other/how-to.txt", "r")        

        #Imprimir instrucciones en pantalla------------------------------------------------------------
        canvas_instructions_image.create_text(230, 325, text=instructions_txt.read(), font=("Gabriola", 20),fill="black")
        
        #Boton-----------------------------------------------------------------------------------------
        back_button = tkinter.Button(instructions_screen, text = "Volver al menú", font=("Gabriola",20,"bold"), padx=40, bg ="#4160af", fg= "#e7e7e7",command = welcome)
        back_button_window = canvas_instructions_image.create_window(470,430, anchor="nw", window=back_button)

#Capitulo Introduccion al juego----------------------------------------------------------------------------------------------
def introduction():
        #Creación pantalla-------------------------------------------------------------------------------
        introduction_screen = LabelFrame(window, width=712, height=540)
        introduction_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_introduction_image = tkinter.Canvas(introduction_screen, width = 712, height=540)
        canvas_introduction_image.pack(fill="both", expand=True)
        canvas_introduction_image.create_image(0,0, image=introduction_screen_image, anchor="nw")

        #Imagen con dialogo------------------------------------------------------------------------------
        canvas_introduction_image.create_image(0,0, image=dialogue_image, anchor="nw")
        introduction_string = "Oh! Quién es ese Conejo Blanco corriendo con un paraguas?\n A donde irá con tanta prisa?"
        canvas_introduction_image.create_text(350, 350, text=introduction_string, font=("Calibri", 17, "bold"), fill="#1b2538")

        
        #Boton 1 (No seguir al conejo)-----------------------------------------------------------------------------------------
        back_button = tkinter.Button(introduction_screen, text = "No seguir al Conejo", font=("Gabriola",18, "bold"), padx=22, bg ="#b6e2d3", fg= "#b74153", command = welcome)
        back_button_window = canvas_introduction_image.create_window(130,450, anchor="nw", window=back_button)

        #Boton 2 (Seguir al conejo)-----------------------------------------------------------------------------------------
        continue_button = tkinter.Button(introduction_screen, text = "Seguir al Conejo", font=("Gabriola",18, "bold"), padx=22,bg ="#b6e2d3", fg= "#b74153", command = woods)
        continue_button_window = canvas_introduction_image.create_window(370,450, anchor="nw", window=continue_button)

#Capitulo Bosque y Camino Rojo-----------------------------------------------------------------------------------------------
def woods():
        #Creación pantalla---------------------------------------------------------------------------
        woods_screen = LabelFrame(window, width=712, height=540)
        woods_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_woods_image = tkinter.Canvas(woods_screen, width = 712, height=540)
        canvas_woods_image.pack(fill="both", expand=True)
        canvas_woods_image.create_image(0,0, image= woods_screen_image, anchor="nw")

        #Imprimir dialogo en pantalla------------------------------------------------------------
        canvas_woods_image.create_image(0,0, image=dialogue_image, anchor="nw")
        woods_string = "Donde me encuentro? He de pensar en cómo voy a arreglármelas \npara salir de aqui. Debo volver con mi madre antes de que \nanochezca...Pero, que es eso que veo ahi?"
        canvas_woods_image.create_text(370, 370, text=woods_string, font=("Calibri", 17, "bold"), fill="#1b2538")

        #Botones
        next_button = tkinter.Button(woods_screen, image=next_arrow_image, borderwidth=0, command=red_path)
        next_button_window = canvas_woods_image.create_window(590,455, anchor="nw", window=next_button)

def woods2():
        #Creación pantalla---------------------------------------------------------------------------------------------------
        woods2_screen = LabelFrame(window, width=712, height=540)
        woods2_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_woods2_image = tkinter.Canvas(woods2_screen, width = 712, height=540)
        canvas_woods2_image.pack(fill="both", expand=True)
        canvas_woods2_image.create_image(0,0, image= woods2_screen_image, anchor="nw")

        next_button = tkinter.Button(woods2_screen, image=next_arrow_image, borderwidth=0, command=caterpillar)
        next_button_window = canvas_woods2_image.create_window(590,455, anchor="nw", window=next_button)

def red_path():
        #Creación pantalla---------------------------------------------------------------------------
        red_path_screen = LabelFrame(window, width=712, height=540)
        red_path_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_red_path_image = tkinter.Canvas(red_path_screen, width = 712, height=540)
        canvas_red_path_image.pack(fill="both", expand=True)
        canvas_red_path_image.create_image(0,0, image= red_path_screen_image, anchor="nw")

        #Imprimir dialogo en pantalla------------------------------------------------------------
        canvas_red_path_image.create_image(0,0, image=dialogue_image, anchor="nw")
        
        #Boton 1  (Seguir el camino Rojo -> Puerta Dorada)-----------------------------------------------------------------------------------------
        back_button = tkinter.Button(red_path_screen, text = "Tomar el Camino Rojo", font=("Gabriola",18, "bold"), padx=22,bg ="#b6e2d3", fg= "#b74153",  command = golden_gate)
        back_button_window = canvas_red_path_image.create_window(110,450, anchor="nw", window=back_button)

        #Boton 2  (Continuar al bosque -> Encuentro Caterpillar)-----------------------------------------------------------------------------------------
        continue_button = tkinter.Button(red_path_screen, text = "Volver al bosque", font=("Gabriola",18, "bold"), padx=22,bg ="#b6e2d3", fg= "#b74153",  command = woods2)
        continue_button_window = canvas_red_path_image.create_window(390,450, anchor="nw", window=continue_button)
 
#Capitulo Puerta Dorada-----------------------------------------------------------------------------------------------
def golden_gate():
        #Creación pantalla---------------------------------------------------------------------------
        golden_gate_screen = LabelFrame(window, width=712, height=540)
        golden_gate_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_golden_gate_image = tkinter.Canvas(golden_gate_screen, width = 712, height=540)
        canvas_golden_gate_image.pack(fill="both", expand=True)
        canvas_golden_gate_image.create_image(0,0, image= golden_gate_screen_image, anchor="nw")

        #Imprimir instrucciones en pantalla------------------------------------------------------------
        canvas_golden_gate_image.create_image(0,0, image=dialogue_image, anchor="nw")
        
        #Boton 1  (Usar la llave)-----------------------------------------------------------------------------------------
        key_button = tkinter.Button(golden_gate_screen, text = "Usar la llave", font=("Gabriola",18, "bold"), padx=22, command=check_key)
        key_button_window = canvas_golden_gate_image.create_window(270,450, anchor="nw", window=key_button)

def check_key():
        if golden_key["Golden Key"] == False:
                golden_gate_screen = LabelFrame(window, width=712, height=540)
                golden_gate_screen.place(x=0, y=0, relheight=1, relwidth=1)
                canvas_golden_gate_image = tkinter.Canvas(golden_gate_screen, width = 712, height=540)
                canvas_golden_gate_image.pack(fill="both", expand=True)

                canvas_golden_gate_image.create_image(0,0, image= not_golden_gate_screen_image, anchor="nw")
                canvas_golden_gate_image.create_image(0,0, image=dialogue_image, anchor="nw")

                #Boton (Volver al bosque -> Encuentro Caterpillar)-----------------------------------------------------------------------------------------
                continue_button = tkinter.Button(golden_gate_screen, text = "Volver al bosque", font=("Gabriola",18, "bold"), padx=22, command=woods)
                continue_button_window = canvas_golden_gate_image.create_window(270,450, anchor="nw", window=continue_button)

#Capitulo CaterPillar-----------------------------------------------------------------------------------------------
def caterpillar():
        #Creacion Pantalla-------------------------------------------------------------------------------------------------------
        alice_caterpillar_screen = LabelFrame(window, width=712, height=540)
        alice_caterpillar_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_alice_caterpillar_image = tkinter.Canvas(alice_caterpillar_screen, width = 712, height=540)
        canvas_alice_caterpillar_image.pack(fill="both", expand=True)
        canvas_alice_caterpillar_image.create_image(0,0, image= alice_caterpillar_screen_image, anchor="nw")

        #Siguiente pantalla ------------------------------------------------------------------------------------------------------
        def caterpillar2():
                caterpillar_screen = LabelFrame(window, width=712, height=540)
                caterpillar_screen.place(x=0, y=0, relheight=1, relwidth=1)
                
                canvas_caterpillar_image = tkinter.Canvas(caterpillar_screen, width = 712, height=540)
                canvas_caterpillar_image.pack(fill="both", expand=True)
                canvas_caterpillar_image.create_image(0,0, image= caterpillar_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_caterpillar_image.create_image(0,0, image=dialogue_image, anchor="nw")
        
                #Boton 1  (Seguir el camino Rojo -> Puerta Dorada)-----------------------------------------------------------------------------------------
                back_button = tkinter.Button(caterpillar_screen, text = "Acercarte", font=("Gabriola",18, "bold"), padx=100, command = caterpillar_game)
                back_button_window = canvas_caterpillar_image.create_window(230,450, anchor="nw", window=back_button)

        #Boton Siguiente-----------------------------------------------------------------------------------------------------------
        next_button = tkinter.Button(alice_caterpillar_screen, image=next_arrow_image, borderwidth=0, command=caterpillar2)
        next_button_window = canvas_alice_caterpillar_image.create_window(590,455, anchor="nw", window=next_button)

def caterpillar_game():
        caterpillar1_screen = LabelFrame(window, width=712, height=540)
        caterpillar1_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_caterpillar1_image = tkinter.Canvas(caterpillar1_screen, width = 712, height=540)
        canvas_caterpillar1_image.pack(fill="both", expand=True)
        canvas_caterpillar1_image.create_image(0,0, image= caterpillar1_screen_image, anchor="nw")

        #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
        canvas_caterpillar1_image.create_image(0,0, image=dialogue_image, anchor="nw")
        
        def command_aux(question, score):

                if question == 1:
                        caterpillar_score.append(score)
                        second_question()
                elif question == 2:
                        caterpillar_score.append(score)
                        third_question()
                elif question == 3:
                        caterpillar_score.append(score)
                        print (caterpillar_score) #Para chequear que se agreguen correctamente
                        result_caterpillar(caterpillar_score)

        def result_caterpillar(caterpillar_score_list):

                total_score = 0
                for i in caterpillar_score_list:
                        total_score += i
        
                if total_score > 6:
                        golden_key["Golden Key"] = True
                        caterpillar_win()
                else:
                        caterpillar_loose()
        
        '''RESULTADOS DEL ENCUENTRO CON LA ORUGA'''
        # --> En el caso que el resultado sumado de las preguntas sea > 6, se obtendra la llave. 
        def caterpillar_win():
                #Construccion pantalla
                caterpillar_win_screen = LabelFrame(window, width=712, height=540)
                caterpillar_win_screen.place(x=0, y=0, relheight=1, relwidth=1)
                
                canvas_caterpillar_win_image = tkinter.Canvas(caterpillar_win_screen, width = 712, height=540)
                canvas_caterpillar_win_image.pack(fill="both", expand=True)
                canvas_caterpillar_win_image.create_image(0,0, image= caterpillar1_screen_image, anchor="nw")

                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_caterpillar1_image.create_image(0,0, image=dialogue_image, anchor="nw")

                #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                next_button = tkinter.Button(caterpillar_win_screen, image=next_arrow_image, borderwidth=0, command=woods)
                next_button_window = canvas_caterpillar_win_image.create_window(590,455, anchor="nw", window=next_button)

        # --> En el caso que el resultado sumado de las preguntas sea < 6, pierde contra la oruga. Vuelta al bosque.  
        def caterpillar_loose():
                #Construccion pantalla
                caterpillar_win_screen = LabelFrame(window, width=712, height=540)
                caterpillar_win_screen.place(x=0, y=0, relheight=1, relwidth=1)
                
                canvas_caterpillar_win_image = tkinter.Canvas(caterpillar_win_screen, width = 712, height=540)
                canvas_caterpillar_win_image.pack(fill="both", expand=True)
                canvas_caterpillar_win_image.create_image(0,0, image= caterpillar1_screen_image, anchor="nw")

                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_caterpillar1_image.create_image(0,0, image=dialogue_image, anchor="nw")

                #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                next_button = tkinter.Button(caterpillar_win_screen, image=next_arrow_image, borderwidth=0, command=woods)
                next_button_window = canvas_caterpillar_win_image.create_window(590,455, anchor="nw", window=next_button)
        
        
        #Preguntas con puntaje
        #Dejame examinarte para determinar si eres digna...
        #Pregunta 1: ¿Cuál de los siguientes colores prefieres?
        def first_question():
                #Creacion de pantalla-----------------------------------------------------------------------------------
                caterpillar_game_screen = LabelFrame(window, width=712, height=540)
                caterpillar_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
                canvas_caterpillar_game_image = tkinter.Canvas(caterpillar_game_screen, width = 712, height=540)
                canvas_caterpillar_game_image.pack(fill="both", expand=True)
                canvas_caterpillar_game_image.create_image(0,0, image= caterpillar_game_screen_image, anchor="nw")
                
                #Boton de pregunta


                #Boton Azul
                blue_button = tkinter.Button(caterpillar_game_screen, text = "Bicicleta", font=("Calibri",15, "bold"), bg="yellow", fg="red", padx=35, command = lambda: command_aux(1,1))
                blue_button_window = canvas_caterpillar_game_image.create_window(50,450, anchor="nw", window=blue_button)
                 
                #Boton Rojo
                red_button = tkinter.Button(caterpillar_game_screen, text = "Oceano", font=("Calibri",15, "bold"), bg="blue", fg = "yellow", padx=35, command = lambda: command_aux(1,2))
                red_button_window = canvas_caterpillar_game_image.create_window(230,450, anchor="nw", window=red_button)

                #Boton Amarillo
                yellow_button = tkinter.Button(caterpillar_game_screen, text = "Cafe con Leche", font=("Calibri",15, "bold"), bg="red", fg="yellow", padx=35, command = lambda: command_aux(1,3))
                yellow_button_window = canvas_caterpillar_game_image.create_window(410,450, anchor="nw", window=yellow_button)

        #Pregunta 2: ¿Cual es tu signo zodiacal?
        def second_question():
                #Creacion de pantalla-----------------------------------------------------------------------------------
                caterpillar_game_screen = LabelFrame(window, width=712, height=540)
                caterpillar_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
                canvas_caterpillar_game_image = tkinter.Canvas(caterpillar_game_screen, width = 712, height=540)
                canvas_caterpillar_game_image.pack(fill="both", expand=True)
                canvas_caterpillar_game_image.create_image(0,0, image= caterpillar_game_screen_image, anchor="nw")

                #Boton Verano
                summer_button = tkinter.Button(caterpillar_game_screen, text = "Verano", font=("Calibri",15, "bold"), bg="yellow", fg="red", padx=20, command = lambda: command_aux(2,1))
                summer_button_window = canvas_caterpillar_game_image.create_window(30,450, anchor="nw", window=summer_button)
                 
                #Boton Invierno
                winter_button = tkinter.Button(caterpillar_game_screen, text = "Invierno", font=("Calibri",15, "bold"), bg="blue", fg = "yellow", padx=20, command = lambda: command_aux(2,2))
                winter_button_window = canvas_caterpillar_game_image.create_window(150,450, anchor="nw", window=winter_button)

                #Boton Otoño
                fall_button = tkinter.Button(caterpillar_game_screen, text = "Otoño", font=("Calibri",15, "bold"), bg="red", fg="yellow", padx=20, command = lambda: command_aux(2,4))
                fall_button_window = canvas_caterpillar_game_image.create_window(300,450, anchor="nw", window=fall_button)
                
                #Boton Primavera
                spring_button = tkinter.Button(caterpillar_game_screen, text = "Primavera", font=("Calibri",15, "bold"), bg="red", fg="yellow", padx=20, command = lambda: command_aux(2,3))
                spring_button_window = canvas_caterpillar_game_image.create_window(410,450, anchor="nw", window=spring_button)
       
       #Pregunta 3: ¿Cual es tu flor favorita?
        def third_question():
                #Creacion de pantalla---------------------------------------------------------------------------------------------
                caterpillar_game_screen = LabelFrame(window, width=712, height=540)
                caterpillar_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
                canvas_caterpillar_game_image = tkinter.Canvas(caterpillar_game_screen, width = 712, height=540)
                canvas_caterpillar_game_image.pack(fill="both", expand=True)
                canvas_caterpillar_game_image.create_image(0,0, image= caterpillar_game_screen_image, anchor="nw")

                #Boton Pop
                blue_button = tkinter.Button(caterpillar_game_screen, text = "Pop", font=("Calibri",15, "bold"), bg="yellow", fg="red", padx=35, command = lambda: command_aux(3,2))
                blue_button_window = canvas_caterpillar_game_image.create_window(100,450, anchor="nw", window=blue_button)
                 
                #Boton Jazz
                red_button = tkinter.Button(caterpillar_game_screen, text = "Jazz", font=("Calibri",15, "bold"), bg="blue", fg = "yellow", padx=35, command = lambda: command_aux(3,2))
                red_button_window = canvas_caterpillar_game_image.create_window(200,450, anchor="nw", window=red_button)

                #Boton Rock
                yellow_button = tkinter.Button(caterpillar_game_screen, text = "Rock", font=("Calibri",15, "bold"), bg="red", fg="yellow", padx=35, command = lambda: command_aux(3,2))
                yellow_button_window = canvas_caterpillar_game_image.create_window(300,450, anchor="nw", window=yellow_button)
                

        #Boton Siguiente-----------------------------------------------------------------------------------------------------------
        next_button = tkinter.Button(caterpillar1_screen, image=next_arrow_image, borderwidth=0, command=first_question)
        next_button_window = canvas_caterpillar1_image.create_window(590,455, anchor="nw", window=next_button)


'''
#Capitulo Cheshire Cat



'''

'''
#Capitulo Sombrerero



'''



#Creacion de clase Carta (Card)        
class Card:
        def __init__(self, image, cardValue):
                self.image = image
                self.cardValue = cardValue

#Capitulo Red Queen
#Capitulo de juego final
def blackjack():
        #Creacion de pantalla
        blackjack_screen = LabelFrame(window, width=712, height=540)
        blackjack_screen.place(x=0, y=0, relheight=1, relwidth=1)
        canvas_blackjack = tkinter.Canvas(blackjack_screen, width = 712, height=540)
        canvas_blackjack.pack(fill="both", expand=True)
        canvas_blackjack.create_image(0,0, image= queen_screen_image, anchor="nw")

        #Boton de aceptar y comenzar el juego
        play_button = tkinter.Button(blackjack_screen, text = "Jugar", font=("Gabriola",18, "bold"), padx=22, command = final_game)

        #Juego Final
        def final_game():
                blackjack_screen.place(x=0, y=0, relheight=1, relwidth=1)
                canvas_blackjack.pack(fill="both", expand=True)
                canvas_blackjack.create_image(0,0, image= queen_screen_image_red, anchor="nw")
                #Creacion de arreglo de Cartas
                cards = []
                #Añadir cartas al arreglo con su imagen y valor respectivo
                cards.append(A_Pikas = Card(Apikas_image, 1))
                cards.append(A_Clover = Card(Aclover_image, 1))
                cards.append(A_Heart = Card(Aheart_image, 1))
                cards.append(A_Diamond = Card(Adiam_image, 1))
                cards.append(J_Pikas = Card(Jpikas_image, 10))
                cards.append(J_Clover = Card(Jclover_image, 10))
                cards.append(J_Heart = Card(Jheart_image, 10))
                cards.append(J_Diamond = Card(Jdiam_image, 10))
                cards.append(K_Pikas = Card(Kpikas_image, 10))
                cards.append(K_Clover = Card(Kclover_image, 10))
                cards.append(K_Heart = Card(Kheart_image, 10))
                cards.append(K_Diamond = Card(Kdiam_image, 10))
                cards.append(Q_Pikas = Card(Qpikas_image, 10))
                cards.append(Q_Clover = Card(Qclover_image, 10))
                cards.append(Q_Heart = Card(Qheart_image, 10))
                cards.append(Q_Diamond = Card(Qdiam_image, 10))

                #Funcion para elegir el valor de la carta si es un As
                def choose1or11():
                        #Boton para elegir 1
                        choose1Button = tkinter.Button(blackjack_screen, text = "1", font=("Gabriola",15,"bold"), padx= 75, command = addOne)
                        choose1Button_window = canvas_blackjack.create_window(300,300, anchor="nw", window=choose1Button)

                        #Boton para elegir 11
                        choose11Button = tkinter.Button(blackjack_screen, text = "11", font=("Gabriola",15,"bold"), padx= 75, command = addEleven)
                        choose11Button_window = canvas_blackjack.create_window(300,300, anchor="nw", window=choose11Button)
                
                #Agrega 1 al puntaje
                def addOne():
                        aliceScore = aliceScore + 1
                        blackjack_screen.place(x=0, y=0, relheight=1, relwidth=1)
                        canvas_blackjack.pack(fill="both", expand=True)
                        canvas_blackjack.create_image(0,0, image= queen_screen_image_red, anchor="nw")
                #Agrega 11 al puntaje
                def addEleven():
                        aliceScore = aliceScore + 11
                        blackjack_screen.place(x=0, y=0, relheight=1, relwidth=1)
                        canvas_blackjack.pack(fill="both", expand=True)
                        canvas_blackjack.create_image(0,0, image= queen_screen_image_red, anchor="nw")
                
                def addTen():
                        aliceScore = aliceScore + 10
                        blackjack_screen.place(x=0, y=0, relheight=1, relwidth=1)
                        canvas_blackjack.pack(fill="both", expand=True)
                        canvas_blackjack.create_image(0,0, image= queen_screen_image_red, anchor="nw")
                
                #Turno de ALICIA
                aliceScore = 0

                #Primer carta

                #Seleccion de la primer carta
                selectedCard = cards[random.randint(0, len(cards) - 1)]
                selectedCard_Label =tkinter.Label(image = selectedCard.image)
                selectedCard_Label.place(x=0, y=0)
                #if (selectedCard.value == 1):
                 #       choose1or11
                
                

        
                

#Creación de la ventana raiz y asignación propiedades.
window = tkinter.Tk()
window.title("Alicia en el Pais de las Encrucijadas")
window.geometry("720x565")
#window.iconbitmap() <- Agregar iconito a la ventana

#Importación de imagenes---------------------------------------------------------------------------
welcome_screen_image = ImageTk.PhotoImage(Image.open("Images/home_screen.png"))
dialogue_image = ImageTk.PhotoImage(Image.open("Images/text_box.png"))
instructions_screen_image = ImageTk.PhotoImage(Image.open("Images/instructions.png"))
introduction_screen_image = ImageTk.PhotoImage(Image.open("Images/introduction.png"))
woods_screen_image = ImageTk.PhotoImage(Image.open("Images/woods.png"))
woods2_screen_image = ImageTk.PhotoImage(Image.open("Images/woods2.png"))
alice_caterpillar_screen_image = ImageTk.PhotoImage(Image.open("Images/alice_caterpillar.png"))
caterpillar_screen_image = ImageTk.PhotoImage(Image.open("Images/caterpillar.png"))
caterpillar1_screen_image = ImageTk.PhotoImage(Image.open("Images/caterpillar1.png"))
caterpillar_game_screen_image = ImageTk.PhotoImage(Image.open("Images/caterpillar_game.png"))
red_path_screen_image = ImageTk.PhotoImage(Image.open("Images/red_path.png"))
golden_gate_screen_image = ImageTk.PhotoImage(Image.open("Images/golden_gate.png"))
not_golden_gate_screen_image = ImageTk.PhotoImage(Image.open("Images/not_golden_gate.png"))
next_arrow_image = ImageTk.PhotoImage(Image.open("Images/next_arrow.png"))
queen_screen_image = ImageTk.PhotoImage(Image.open("Images/queen.png"))
queen_red_screen_image = ImageTk.PhotoImage(Image.open("Images/queen_red.png"))


#Cartas---
Aheart_image = ImageTk.PhotoImage(Image.open("Images/Cards/Aheart.png"))
Adiam_image = ImageTk.PhotoImage(Image.open("Images/Cards/Adiam.png"))
Aclover_image = ImageTk.PhotoImage(Image.open("Images/Cards/Aclover.png"))
Apikas_image = ImageTk.PhotoImage(Image.open("Images/Cards/Apikas.png"))
Jclover_image = ImageTk.PhotoImage(Image.open("Images/Cards/Jclover.png"))
Jdiam_image = ImageTk.PhotoImage(Image.open("Images/Cards/Jdiam.png"))
Jheart_image = ImageTk.PhotoImage(Image.open("Images/Cards/Jheart.png"))
Jpikas_image = ImageTk.PhotoImage(Image.open("Images/Cards/Jpikas.png"))
Qclover_image = ImageTk.PhotoImage(Image.open("Images/Cards/Qclover.png"))
Qdiam_image = ImageTk.PhotoImage(Image.open("Images/Cards/Qdiam.png"))
Qheart_image = ImageTk.PhotoImage(Image.open("Images/Cards/Qheart.png"))
Qpikas_image = ImageTk.PhotoImage(Image.open("Images/Cards/Qpikas.png"))
Kclover_image = ImageTk.PhotoImage(Image.open("Images/Cards/Kclover.png"))
Kdiam_image = ImageTk.PhotoImage(Image.open("Images/Cards/Kdiam.png"))
Kheart_image = ImageTk.PhotoImage(Image.open("Images/Cards/Kheart.png"))
Kpikas_image = ImageTk.PhotoImage(Image.open("Images/Cards/Kpikas.png"))

#Importación de imagenes----------------------------------------------------------------------------

#Comienza el Juego
welcome()

#Llave dorada 
golden_key = {"Golden Key":False}

#Resultados de los diferentes encuentros
caterpillar_score = []


window.mainloop()