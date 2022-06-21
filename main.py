'''     Proyecto final: "Alicia en el Pais de las Encrucijadas"
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
import time
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
        back_button = tkinter.Button(introduction_screen, text = "No seguir al Conejo", font=("Gabriola",18, "bold"), padx=22, bg ="#b6e2d3", fg= "#b74153", command = lambda: ending("out"))
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

def woods2(scene= None):
        #Creación pantalla---------------------------------------------------------------------------------------------------
        woods2_screen = LabelFrame(window, width=712, height=540)
        woods2_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_woods2_image = tkinter.Canvas(woods2_screen, width = 712, height=540)
        canvas_woods2_image.pack(fill="both", expand=True)
        canvas_woods2_image.create_image(0,0, image= woods2_screen_image, anchor="nw")

        #Bosque que guia a la oruga de seda ------------------------------------------------------------------------------------
        if scene == "caterpillar":
                next_button = tkinter.Button(woods2_screen, image=next_arrow_image, borderwidth=0, command=caterpillar)
                next_button_window = canvas_woods2_image.create_window(590,455, anchor="nw", window=next_button)
        elif scene == "cheshire_cat":
                next_button = tkinter.Button(woods2_screen, image=next_arrow_image, borderwidth=0, command=cheshire_cat)
                next_button_window = canvas_woods2_image.create_window(590,455, anchor="nw", window=next_button)
        elif scene == "hatman":
                next_button = tkinter.Button(woods2_screen, image=next_arrow_image, borderwidth=0, command=hatman)
                next_button_window = canvas_woods2_image.create_window(590,455, anchor="nw", window=next_button)
        else:
                print("Woods2 Comando Incorrecto")

def red_path():
        #Creación pantalla---------------------------------------------------------------------------
        red_path_screen = LabelFrame(window, width=712, height=540)
        red_path_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_red_path_image = tkinter.Canvas(red_path_screen, width = 712, height=540)
        canvas_red_path_image.pack(fill="both", expand=True)
        canvas_red_path_image.create_image(0,0, image= red_path_screen_image, anchor="nw")

        #Imprimir dialogo en pantalla------------------------------------------------------------
        canvas_red_path_image.create_image(0,0, image=dialogue_image, anchor="nw")
        red_path_string = "Que bonito camino rojo! Aunque puede ser peligroso. \nDebería seguir este camino? O mejor vuelvo al bosque?"
        canvas_red_path_image.create_text(370, 370, text=red_path_string, font=("Calibri", 17, "bold"), fill="#1b2538")

        #Boton 1  (Seguir el camino Rojo -> Puerta Dorada)-----------------------------------------------------------------------------------------
        back_button = tkinter.Button(red_path_screen, text = "Tomar el Camino Rojo", font=("Gabriola",18, "bold"), padx=22,bg ="#b6e2d3", fg= "#b74153",  command = golden_gate)
        back_button_window = canvas_red_path_image.create_window(110,450, anchor="nw", window=back_button)

        #Boton 2  (Continuar al bosque -> Encuentro Caterpillar)-----------------------------------------------------------------------------------------
        continue_button = tkinter.Button(red_path_screen, text = "Volver al bosque", font=("Gabriola",18, "bold"), padx=22,bg ="#b6e2d3", fg= "#b74153",  command = lambda: woods2("caterpillar"))
        continue_button_window = canvas_red_path_image.create_window(390,450, anchor="nw", window=continue_button)
 
#Capitulo Puerta Dorada-----------------------------------------------------------------------------------------------
def golden_gate():
        #Creación pantalla---------------------------------------------------------------------------
        golden_gate_screen = LabelFrame(window, width=712, height=540)
        golden_gate_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_golden_gate_image = tkinter.Canvas(golden_gate_screen, width = 712, height=540)
        canvas_golden_gate_image.pack(fill="both", expand=True)
        canvas_golden_gate_image.create_image(0,0, image= golden_gate_screen_image, anchor="nw")

        #Imprimir dialogo en pantalla------------------------------------------------------------
        canvas_golden_gate_image.create_image(0,0, image=dialogue_image, anchor="nw")
        golden_gate_string = "Bienvenida querida! Soy tu amigo El Picaporte. Mi cerradura es \nimpasable,a menos que cuentes con la Llave Dorada..."
        canvas_golden_gate_image.create_text(370, 370, text=golden_gate_string, font=("Calibri", 17, "bold"), fill="#1b2538")

        #Boton 1  (Usar la llave)-----------------------------------------------------------------------------------------
        key_button = tkinter.Button(golden_gate_screen, text = "Usar la llave", font=("Gabriola",18, "bold"), padx=22,bg ="#b6e2d3", fg= "#b74153", command=check_key)
        key_button_window = canvas_golden_gate_image.create_window(270,450, anchor="nw", window=key_button)

def check_key():
        golden_gate_screen = LabelFrame(window, width=712, height=540)
        golden_gate_screen.place(x=0, y=0, relheight=1, relwidth=1)
        canvas_golden_gate_image = tkinter.Canvas(golden_gate_screen, width = 712, height=540)
        canvas_golden_gate_image.pack(fill="both", expand=True)

        if golden_key["Golden Key"] == False:
                canvas_golden_gate_image.create_image(0,0, image= not_golden_gate_screen_image, anchor="nw")

                #Imprimir dialogo en pantalla------------------------------------------------------------
                canvas_golden_gate_image.create_image(0,0, image=dialogue_image, anchor="nw")
                golden_gate_string = "Es inutil! Sin la llave no iras a ningún lado!\nMejor vuelve por donde has venido y encuentra la llave!"
                canvas_golden_gate_image.create_text(350, 370, text=golden_gate_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton (Volver al bosque -> Encuentro Caterpillar)-----------------------------------------------------------------------------------------
                continue_button = tkinter.Button(golden_gate_screen, text = "Volver al bosque", font=("Gabriola",18, "bold"), padx=22,bg ="#b6e2d3", fg= "#b74153", command=lambda:woods2("caterpillar"))
                continue_button_window = canvas_golden_gate_image.create_window(240,450, anchor="nw", window=continue_button)
        else: 
                canvas_golden_gate_image.create_image(0,0, image= golden_gate_screen_image, anchor="nw")
                canvas_golden_gate_image.create_image(0,0, image= dialogue_image, anchor="nw")

                #Imprimir dialogo en pantalla------------------------------------------------------------
                golden_gate_string = "Te lo dije! Nada es imposible si lo deseas lo suficiente...\nY tienes una llave para pasar. Ten mucho cuidado alli adentro \npequeña, a la Reina le gusta Cortar Cabezas..."
                canvas_golden_gate_image.create_text(350, 370, text=golden_gate_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton (Abrir la puerta --> Encuentro con la Reina Roja)-----------------------------------------------------------------------------------------
                continue_button = tkinter.Button(golden_gate_screen, text = "Abrir la puerta", font=("Gabriola",18, "bold"),bg ="#b6e2d3", fg= "#b74153", padx=22, command=red_queen)
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
                caterpillar_string = "¿Qué es eso que ven mis ojos? Una oruga cantando? \nSe ve muy amigable, quizás pueda ayudarme a encontrar la \nLlave dorada..."
                canvas_caterpillar_image.create_text(370, 370, text=caterpillar_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton 1  (Acercarte)-----------------------------------------------------------------------------------------
                back_button = tkinter.Button(caterpillar_screen, text = "Acercarte", font=("Gabriola",18, "bold"), padx=100,bg ="#b6e2d3", fg= "#b74153", command = caterpillar_game)
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
        caterpillar1_string = "Pequeña niña! Como que buscas una Llave Dorada... \nSi quizás pueda ayudarte... pero primero debo determinar si eres \ndigna de tal honor"
        canvas_caterpillar1_image.create_text(370, 370, text=caterpillar1_string, font=("Calibri", 17, "bold"), fill="#1b2538")

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
                canvas_caterpillar_win_image.create_image(0,0, image=dialogue_image, anchor="nw")
                caterpillar_win_string = "Muy bien pequeña florecita... Sigue el camino rojo \ny ten mucho cuidado cuando cruces al otro lado... "
                canvas_caterpillar_win_image.create_text(330, 370, text=caterpillar_win_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                next_button = tkinter.Button(caterpillar_win_screen, image=next_arrow_image, borderwidth=0, command=red_path)
                next_button_window = canvas_caterpillar_win_image.create_window(590,455, anchor="nw", window=next_button)

        # --> En el caso que el resultado sumado de las preguntas sea < 6, pierde contra la oruga. Vuelta al bosque.  
        def caterpillar_loose():
                #Construccion pantalla
                caterpillar_loose_screen = LabelFrame(window, width=712, height=540)
                caterpillar_loose_screen.place(x=0, y=0, relheight=1, relwidth=1)
                
                canvas_caterpillar_loose_image = tkinter.Canvas(caterpillar_loose_screen, width = 712, height=540)
                canvas_caterpillar_loose_image.pack(fill="both", expand=True)
                canvas_caterpillar_loose_image.create_image(0,0, image= caterpillar1_screen_image, anchor="nw")

                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_caterpillar_loose_image.create_image(0,0, image=dialogue_image, anchor="nw")
                caterpillar_loose_string = "Bah! Claramente no eres digna de cargar con la Llave Dorada. \nAlejate de mi vista! "
                canvas_caterpillar_loose_image.create_text(370, 370, text=caterpillar_loose_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                next_button = tkinter.Button(caterpillar_loose_screen, image=next_arrow_image, borderwidth=0, command=lambda: woods2("cheshire_cat"))
                next_button_window = canvas_caterpillar_loose_image.create_window(590,455, anchor="nw", window=next_button)
        
        #Preguntas con puntaje
        #Pregunta 1: ¿Cuál de los siguientes colores prefieres?
        def first_question():
                #Creacion de pantalla-----------------------------------------------------------------------------------
                caterpillar_game_screen = LabelFrame(window, width=712, height=540)
                caterpillar_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
                canvas_caterpillar_game_image = tkinter.Canvas(caterpillar_game_screen, width = 712, height=540)
                canvas_caterpillar_game_image.pack(fill="both", expand=True)
                canvas_caterpillar_game_image.create_image(0,0, image= caterpillar_game_screen_image, anchor="nw")
                
                #Imprimir dialogo-pregunta en pantalla--------------------------------------------------------------------------------------
                canvas_caterpillar_game_image.create_image(0,0, image=dialogue_image, anchor="nw")
                caterpillar_game_string = "¿Cuál de los siguientes colores prefieres? "
                canvas_caterpillar_game_image.create_text(370, 370, text=caterpillar_game_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Botones de pregunta
                #Boton Azul
                blue_button = tkinter.Button(caterpillar_game_screen, text = "Bicicleta", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=35, command = lambda: command_aux(1,1))
                blue_button_window = canvas_caterpillar_game_image.create_window(70,450, anchor="nw", window=blue_button)
                 
                #Boton Rojo
                red_button = tkinter.Button(caterpillar_game_screen, text = "Oceano", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=35, command = lambda: command_aux(1,2))
                red_button_window = canvas_caterpillar_game_image.create_window(250,450, anchor="nw", window=red_button)

                #Boton Amarillo
                yellow_button = tkinter.Button(caterpillar_game_screen, text = "Cafe con Leche", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=35, command = lambda: command_aux(1,3))
                yellow_button_window = canvas_caterpillar_game_image.create_window(430,450, anchor="nw", window=yellow_button)

        #Pregunta 2: ¿Cual es tu signo zodiacal?
        def second_question():
                #Creacion de pantalla-----------------------------------------------------------------------------------
                caterpillar_game_screen = LabelFrame(window, width=712, height=540)
                caterpillar_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
                canvas_caterpillar_game_image = tkinter.Canvas(caterpillar_game_screen, width = 712, height=540)
                canvas_caterpillar_game_image.pack(fill="both", expand=True)
                canvas_caterpillar_game_image.create_image(0,0, image= caterpillar_game_screen_image, anchor="nw")

                #Imprimir dialogo-pregunta en pantalla--------------------------------------------------------------------------------------
                canvas_caterpillar_game_image.create_image(0,0, image=dialogue_image, anchor="nw")
                caterpillar_game_string = "¿Cuál es tu signo zodiacal? "
                canvas_caterpillar_game_image.create_text(370, 370, text=caterpillar_game_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Verano
                summer_button = tkinter.Button(caterpillar_game_screen, text = "Verano", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=20, command = lambda: command_aux(2,1))
                summer_button_window = canvas_caterpillar_game_image.create_window(90,450, anchor="nw", window=summer_button)
                 
                #Boton Invierno
                winter_button = tkinter.Button(caterpillar_game_screen, text = "Invierno", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=20, command = lambda: command_aux(2,2))
                winter_button_window = canvas_caterpillar_game_image.create_window(220,450, anchor="nw", window=winter_button)

                #Boton Otoño
                fall_button = tkinter.Button(caterpillar_game_screen, text = "Otoño", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=20, command = lambda: command_aux(2,4))
                fall_button_window = canvas_caterpillar_game_image.create_window(360,450, anchor="nw", window=fall_button)
                
                #Boton Primavera
                spring_button = tkinter.Button(caterpillar_game_screen, text = "Primavera", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=20, command = lambda: command_aux(2,3))
                spring_button_window = canvas_caterpillar_game_image.create_window(490,450, anchor="nw", window=spring_button)
       
       #Pregunta 3: ¿Cual es tu flor favorita?
        def third_question():
                #Creacion de pantalla---------------------------------------------------------------------------------------------
                caterpillar_game_screen = LabelFrame(window, width=712, height=540)
                caterpillar_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
                canvas_caterpillar_game_image = tkinter.Canvas(caterpillar_game_screen, width = 712, height=540)
                canvas_caterpillar_game_image.pack(fill="both", expand=True)
                canvas_caterpillar_game_image.create_image(0,0, image= caterpillar_game_screen_image, anchor="nw")

                #Imprimir dialogo-pregunta en pantalla--------------------------------------------------------------------------------------
                canvas_caterpillar_game_image.create_image(0,0, image=dialogue_image, anchor="nw")
                caterpillar_game_string = "¿Cuál es tu flor favorita? "
                canvas_caterpillar_game_image.create_text(370, 370, text=caterpillar_game_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Pop
                blue_button = tkinter.Button(caterpillar_game_screen, text = "Pop", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=35, command = lambda: command_aux(3,2))
                blue_button_window = canvas_caterpillar_game_image.create_window(150,450, anchor="nw", window=blue_button)
                 
                #Boton Jazz
                red_button = tkinter.Button(caterpillar_game_screen, text = "Jazz", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=35, command = lambda: command_aux(3,2))
                red_button_window = canvas_caterpillar_game_image.create_window(300,450, anchor="nw", window=red_button)

                #Boton Rock
                yellow_button = tkinter.Button(caterpillar_game_screen, text = "Rock", font=("Calibri",15, "bold"), bg="#f7d640", fg="#3f3955", padx=35, command = lambda: command_aux(3,2))
                yellow_button_window = canvas_caterpillar_game_image.create_window(450,450, anchor="nw", window=yellow_button)
                
        #Boton Siguiente-----------------------------------------------------------------------------------------------------------
        next_button = tkinter.Button(caterpillar1_screen, image=next_arrow_image, borderwidth=0, command=first_question)
        next_button_window = canvas_caterpillar1_image.create_window(590,455, anchor="nw", window=next_button)

#Capitulo Cheshire Cat----------------------------------------------------------------------------------------------------------------------------
def cheshire_cat():
        #Creacion Pantalla-------------------------------------------------------------------------------------------------------
        cat_encounter_screen = LabelFrame(window, width=712, height=540)
        cat_encounter_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_cat_encounter_image = tkinter.Canvas(cat_encounter_screen, width = 712, height=540)
        canvas_cat_encounter_image.pack(fill="both", expand=True)
        canvas_cat_encounter_image.create_image(0,0, image= cat_encounter_screen_image, anchor="nw")

        #Siguiente pantalla ------------------------------------------------------------------------------------------------------
        def cheshire_cat2():
                cat_and_alice_screen = LabelFrame(window, width=712, height=540)
                cat_and_alice_screen.place(x=0, y=0, relheight=1, relwidth=1)
                
                canvas_cat_and_alice_image = tkinter.Canvas(cat_and_alice_screen, width = 712, height=540)
                canvas_cat_and_alice_image.pack(fill="both", expand=True)
                canvas_cat_and_alice_image.create_image(0,0, image= cat_and_alice_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_cat_and_alice_image.create_image(0,0, image=dialogue_image, anchor="nw")
                cat_and_alice_string = "Oh! Es un gato! Hola señor Gato! Me encuentro \nsin rumbo en este bosque buscando una Llave dorada\n¿Será que podrá ayudarme Sr. Gato?"
                canvas_cat_and_alice_image.create_text(370, 370, text=cat_and_alice_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente---------------------------------------------------------------------------------------------
                next_button = tkinter.Button(cat_and_alice_screen, image=next_arrow_image, borderwidth=0, command=cheshire_cat_game)
                next_button_window = canvas_cat_and_alice_image.create_window(590,455, anchor="nw", window=next_button)

        #Boton Siguiente-----------------------------------------------------------------------------------------------------------
        next_button = tkinter.Button(cat_encounter_screen, image=next_arrow_image, borderwidth=0, command=cheshire_cat2)
        next_button_window = canvas_cat_encounter_image.create_window(590,455, anchor="nw", window=next_button)

def cheshire_cat_game():
        #Creacion Pantalla-------------------------------------------------------------------------------------------------------
        cheshire_cat_game_screen = LabelFrame(window, width=712, height=540)
        cheshire_cat_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_cheshire_cat_game_image = tkinter.Canvas(cheshire_cat_game_screen, width = 712, height=540)
        canvas_cheshire_cat_game_image.pack(fill="both", expand=True)
        canvas_cheshire_cat_game_image.create_image(0,0, image= cheshire_cat_screen_image, anchor="nw")

        #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
        canvas_cheshire_cat_game_image.create_image(0,0, image=dialogue_image, anchor="nw")
        cheshire_cat_game_string = "Sólo los locos más locos tienen el privilegio de conocer los \ncaminos detras de la puerta que abre esa llave..."
        canvas_cheshire_cat_game_image.create_text(370, 370, text=cheshire_cat_game_string, font=("Calibri", 17, "bold"), fill="#1b2538")

        def result_cheshire_cat_game(answer):
                cheshire_cat_game_screen = LabelFrame(window, width=712, height=540)
                cheshire_cat_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
                        
                canvas_cheshire_cat_game_image = tkinter.Canvas(cheshire_cat_game_screen, width = 712, height=540)
                canvas_cheshire_cat_game_image.pack(fill="both", expand=True)
                canvas_cheshire_cat_game_image.create_image(0,0, image= cheshire_cat_screen_image, anchor="nw")

                if answer == 1:
                        def result_win():
                                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                                canvas_cheshire_cat_game_image.create_image(0,0, image=dialogue_image, anchor="nw")
                                cheshire_cat_game_string = "Has ganado la llave! o has perdido con la llave... \nBueno, eso lo deberás averiguar por ti misma. "
                                canvas_cheshire_cat_game_image.create_text(310, 370, text=cheshire_cat_game_string, font=("Calibri", 17, "bold"), fill="#1b2538")
                                
                                #Se obtiene la llave
                                golden_key["Golden Key"] = True

                                #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                                next_button = tkinter.Button(cheshire_cat_game_screen, image=next_arrow_image, borderwidth=0, command=red_path)
                                next_button_window = canvas_cheshire_cat_game_image.create_window(590,455, anchor="nw", window=next_button)
                        result_win()
                elif answer == 2:
                        def result_not_win():
                                canvas_cheshire_cat_game_image.create_image(0,0, image= cat_path_screen_image, anchor="nw")

                                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                                canvas_cheshire_cat_game_image.create_image(0,0, image=dialogue_image, anchor="nw")
                                cheshire_cat_game_string = "Humm... Pues no puedo darte la llave. Pero en\n en aquella dirección encontrarás al Sombrerero Loco, \nquizás el pueda ayudarte... "
                                canvas_cheshire_cat_game_image.create_text(350, 370, text=cheshire_cat_game_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                                #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                                next_button = tkinter.Button(cheshire_cat_game_screen, image=next_arrow_image, borderwidth=0, command=lambda: woods2("hatman"))
                                next_button_window = canvas_cheshire_cat_game_image.create_window(590,455, anchor="nw", window=next_button)
                        result_not_win()
                elif answer == 3:
                        def result_loose():
                                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                                canvas_cheshire_cat_game_image.create_image(0,0, image=dialogue_image, anchor="nw")
                                cheshire_cat_game_string = "Oh niña no estas hecha para este mundo de locos!\nMejor vuelve a tu mundo antes de que te lastimes "
                                canvas_cheshire_cat_game_image.create_text(370, 370, text=cheshire_cat_game_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                                #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                                next_button = tkinter.Button(cheshire_cat_game_screen, image=next_arrow_image, borderwidth=0, command= lambda: ending("out"))
                                next_button_window = canvas_cheshire_cat_game_image.create_window(590,455, anchor="nw", window=next_button)
                        result_loose()

        #Siguiente pantalla ------------------------------------------------------------------------------------------------------
        def riddle():
                cheshire_cat_game_screen = LabelFrame(window, width=712, height=540)
                cheshire_cat_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
                canvas_cheshire_cat_game_image = tkinter.Canvas(cheshire_cat_game_screen, width = 712, height=540)
                canvas_cheshire_cat_game_image.pack(fill="both", expand=True)
                canvas_cheshire_cat_game_image.create_image(0,0, image= cheshire_cat_screen_image, anchor="nw")

                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_cheshire_cat_game_image.create_image(0,0, image=dialogue_image, anchor="nw")
                cheshire_cat_game_string = "Un pequeño acertijo: Si me sonríes, te sonrío..."
                canvas_cheshire_cat_game_image.create_text(370, 370, text=cheshire_cat_game_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Opción 1 (Correcta)---------------------------------------------------------------------------------------------
                blue_button = tkinter.Button(cheshire_cat_game_screen, text = "¿Eres un espejo?", font=("Calibri",15, "bold"), bg="#8D1586", fg="#FFFFFF", padx=35, command = lambda: result_cheshire_cat_game(1))
                blue_button_window = canvas_cheshire_cat_game_image.create_window(40,450, anchor="nw", window=blue_button)
                                
                #Boton Opción 2 (La manda al bosque con el sombrerero)------------------------------------------------------------------------
                blue_button = tkinter.Button(cheshire_cat_game_screen, text = "Sonreirle", font=("Calibri",15, "bold"), bg="#8D1586", fg="#FFFFFF", padx=35, command = lambda: result_cheshire_cat_game(2))
                blue_button_window = canvas_cheshire_cat_game_image.create_window(280,450, anchor="nw", window=blue_button)

                #Boton Opción 3 (Pierde el juego)---------------------------------------------------------------------------------------------
                blue_button = tkinter.Button(cheshire_cat_game_screen, text = "No comprendo", font=("Calibri",15, "bold"), bg="#8D1586", fg="#FFFFFF", padx=35, command = lambda: result_cheshire_cat_game(3))
                blue_button_window = canvas_cheshire_cat_game_image.create_window(460,450, anchor="nw", window=blue_button)
                
        #Boton Siguiente-----------------------------------------------------------------------------------------------------------
        next_button = tkinter.Button(cheshire_cat_game_screen, image=next_arrow_image, borderwidth=0, command=riddle)
        next_button_window = canvas_cheshire_cat_game_image.create_window(590,455, anchor="nw", window=next_button)

#Capitulo Sombrerero------------------------------------------------------------------------------------------------------------------------------
def hatman():
        #Creacion Pantalla-------------------------------------------------------------------------------------------------------
        hatman_encounter_screen = LabelFrame(window, width=712, height=540)
        hatman_encounter_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_hatman_encounter_image = tkinter.Canvas(hatman_encounter_screen, width = 712, height=540)
        canvas_hatman_encounter_image.pack(fill="both", expand=True)
        canvas_hatman_encounter_image.create_image(0,0, image= hatman_encounter_screen_image, anchor="nw")
        #Siguiente pantalla ------------------------------------------------------------------------------------------------------
        def tea_table():
                canvas_hatman_encounter_image.create_image(0,0, image= tea_table_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_hatman_encounter_image.create_image(0,0, image=dialogue_image, anchor="nw")
                tea_table_string = "♫ ♪ Feliz, feliz no cumpleaños! ♩ ♫ ♪\n ♫ ♪ Feliz, feliz no cumpleaños te dooyy ♩ a tuu ♫ ♪ !"
                canvas_hatman_encounter_image.create_text(370, 370, text=tea_table_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente---------------------------------------------------------------------------------------------
                next_button = tkinter.Button(hatman_encounter_screen, image=next_arrow_image, borderwidth=0, command=tea_table2)
                next_button_window = canvas_hatman_encounter_image.create_window(590,455, anchor="nw", window=next_button)

        def tea_table2():
                canvas_hatman_encounter_image.create_image(0,0, image= alice_tea_table_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_hatman_encounter_image.create_image(0,0, image=dialogue_image, anchor="nw")
                tea_table2_string = "♩ ♫ ¡Que canción tan divertida! Pero, lamento haber \ninterrumpido su fiesta de cumpleaños!"
                canvas_hatman_encounter_image.create_text(370, 370, text=tea_table2_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente---------------------------------------------------------------------------------------------
                next_button = tkinter.Button(hatman_encounter_screen, image=next_arrow_image, borderwidth=0, command=tea_table3)
                next_button_window = canvas_hatman_encounter_image.create_window(590,455, anchor="nw", window=next_button)

        def tea_table3():
                hatman_encounter_screen = LabelFrame(window, width=712, height=540)
                hatman_encounter_screen.place(x=0, y=0, relheight=1, relwidth=1)
                
                canvas_hatman_encounter_image = tkinter.Canvas(hatman_encounter_screen, width = 712, height=540)
                canvas_hatman_encounter_image.pack(fill="both", expand=True)

                canvas_hatman_encounter_image.create_image(0,0, image= hatman_tea_table_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_hatman_encounter_image.create_image(0,0, image=dialogue_image, anchor="nw")
                tea_table2_string = "No querida! Esto no es un no cumpleaños! \n Por que festejar sólo un día de cumpleaños cuando podemos \nfestejar 364 días de no cumpleaños! ... ¿Que hay de ti?"
                canvas_hatman_encounter_image.create_text(370, 370, text=tea_table2_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton 1 (También es mi no cumpleaños!)-----------------------------------------------------------------------------------------
                unbirthday_button = tkinter.Button(hatman_encounter_screen, text = "Hoy también es mi no cumpleaños!", font=("Gabriola",18, "bold"), padx=5, bg ="#b6e2d3", fg= "#b74153", command = unbirthday)
                unbirthday_button_window = canvas_hatman_encounter_image.create_window(40,450, anchor="nw", window=unbirthday_button)

                #Boton 2 (Hoy es mi cumpleaños!)-------------------------------------------------------------------------------------------------
                birthday_button = tkinter.Button(hatman_encounter_screen, text = "Pero... hoy es mi cumpleaños", font=("Gabriola",18, "bold"), padx=5,bg ="#b6e2d3", fg= "#b74153", command = birthday)
                birthday_button_window = canvas_hatman_encounter_image.create_window(400,450, anchor="nw", window=birthday_button)

        def birthday():
                canvas_hatman_encounter_image.create_image(0,0, image= hatman_tea_table_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla---------------------------------------------------------------------------------------------------
                canvas_hatman_encounter_image.create_image(0,0, image=dialogue_image, anchor="nw")
                tea_table2_string = "Oh... bueno... esto es incomodo...\nquizás deberías volver a tu tierra a celebrar tu cumpleaños"
                canvas_hatman_encounter_image.create_text(370, 370, text=tea_table2_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente-----------------------------------------------------------------------------------------------------------------
                next_button = tkinter.Button(hatman_encounter_screen, image=next_arrow_image, borderwidth=0, command=lambda: ending("out"))
                next_button_window = canvas_hatman_encounter_image.create_window(590,455, anchor="nw", window=next_button)

        #Boton Siguiente hatman() (Principal)-----------------------------------------------------------------------------------------------------------
        next_button = tkinter.Button(hatman_encounter_screen, image=next_arrow_image, borderwidth=0, command=tea_table)
        next_button_window = canvas_hatman_encounter_image.create_window(590,455, anchor="nw", window=next_button)

def unbirthday():
        #Creacion Pantalla--------------------------------------------------------------------------------------------------------------------
        unbirthday_screen = LabelFrame(window, width=712, height=540)
        unbirthday_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_unbirthday_image = tkinter.Canvas(unbirthday_screen, width = 712, height=540)
        canvas_unbirthday_image.pack(fill="both", expand=True)
        canvas_unbirthday_image.create_image(0,0, image= unbirthday_screen_image, anchor="nw")

        #Imprimir dialogo en pantalla---------------------------------------------------------------------------------------------------------
        canvas_unbirthday_image.create_image(0,0, image=dialogue_image, anchor="nw")
        unbirthday_cake_string = "¡Que pequeño que es este mundo! En ese caso... \n ♫ ♪ Feliz, feliz no cumpleaños! ♩ ♫ a tuu!♪"
        canvas_unbirthday_image.create_text(370, 370, text=unbirthday_cake_string, font=("Calibri", 17, "bold"), fill="#1b2538")

        #Siguiente pantalla ------------------------------------------------------------------------------------------------------
        def unbirthday_cake():
                #Recibe la llave ------------------------------------------------------------------------------------------------------------
                golden_key["Golden Key"] = True
                
                #Construccion pantalla ------------------------------------------------------------------------------------------------------
                canvas_unbirthday_image.create_image(0,0, image= hatman_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla-----------------------------------------------------------------------------------------------
                canvas_unbirthday_image.create_image(0,0, image=dialogue_image, anchor="nw")
                tea_table2_string = "Que gran celebración! Ahora querida, vuelve por el camino rojo...\nQuizás tengas un regalo de no cumpleaños en el bolsillo! "
                canvas_unbirthday_image.create_text(370, 370, text=tea_table2_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente------------------------------------------------------------------------------------------------------------
                next_button = tkinter.Button(unbirthday_screen, image=next_arrow_image, borderwidth=0, command=red_path)
                next_button_window = canvas_unbirthday_image.create_window(590,455, anchor="nw", window=next_button)

        #Boton Siguiente (unbirthday - principal)--------------------------------------------------------------------------------------------------------------------
        next_button = tkinter.Button(unbirthday_screen, image=next_arrow_image, borderwidth=0, command=unbirthday_cake)
        next_button_window = canvas_unbirthday_image.create_window(590,455, anchor="nw", window=next_button)

#Capitulo Red Queen
def red_queen():
        #Creacion Pantalla-------------------------------------------------------------------------------------------------------
        red_queen_screen = LabelFrame(window, width=712, height=540)
        red_queen_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_red_queen_image = tkinter.Canvas(red_queen_screen, width = 712, height=540)
        canvas_red_queen_image.pack(fill="both", expand=True)
        canvas_red_queen_image.create_image(0,0, image= labyrinth_screen_image, anchor="nw")

        #Siguiente pantalla ------------------------------------------------------------------------------------------------------
        def queen_gate():
                canvas_red_queen_image.create_image(0,0, image= queen_gate_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                #canvas_red_queen_image.create_image(0,0, image=dialogue_image, anchor="nw")
                #tea_table_string = "♫ ♪ Feliz, feliz no cumpleaños! ♩ ♫ ♪\n ♫ ♪ Feliz, feliz no cumpleaños te dooyy ♩ a tuu ♫ ♪ !"
                #canvas_red_queen_image.create_text(370, 370, text=tea_table_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente---------------------------------------------------------------------------------------------
                next_button = tkinter.Button(red_queen_screen, image=next_arrow_image, borderwidth=0, command=queen)
                next_button_window = canvas_red_queen_image.create_window(590,455, anchor="nw", window=next_button)

        def queen():
                canvas_red_queen_image.create_image(0,0, image= queen1_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_red_queen_image.create_image(0,0, image=dialogue_image, anchor="nw")
                tea_table2_string = "¿Y quien es esto? ¿Cómo osas caminar por mis jardines llevnado \nblanco en lugar de carmín? ... Jugarás con migo\n TODOS EN ORDEN! OBEDEZCAN A SU REINA! EN ORDEN! "
                canvas_red_queen_image.create_text(370, 370, text=tea_table2_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente---------------------------------------------------------------------------------------------
                next_button = tkinter.Button(red_queen_screen, image=next_arrow_image, borderwidth=0, command=queen_cards)
                next_button_window = canvas_red_queen_image.create_window(590,455, anchor="nw", window=next_button)

        def queen_cards():
                canvas_red_queen_image.create_image(0,0, image= queen_cards_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla--------------------------------------------------------------------------------------
                canvas_red_queen_image.create_image(0,0, image=dialogue_image, anchor="nw")
                tea_table2_string = "Eeeen orden! Son las ordenes de la Reina! \n Se jugará BLACKJACK de la realeza!"
                canvas_red_queen_image.create_text(370, 370, text=tea_table2_string, font=("Calibri", 17, "bold"), fill="#1b2538")
                
                #Boton Siguiente---------------------------------------------------------------------------------------------
                next_button = tkinter.Button(red_queen_screen, image=next_arrow_image, borderwidth=0, command=queen1)
                next_button_window = canvas_red_queen_image.create_window(590,455, anchor="nw", window=next_button)

        def queen1():
                canvas_red_queen_image.create_image(0,0, image= queen1_screen_image, anchor="nw")
                
                #Imprimir dialogo en pantalla---------------------------------------------------------------------------------------------------
                canvas_red_queen_image.create_image(0,0, image=dialogue_image, anchor="nw")
                tea_table2_string = "Jugarás un juego conmigo! Si me ganas, bueno, eso no ha pasado \nnunca... y si no, ordenare tu destierro!"
                canvas_red_queen_image.create_text(370, 370, text=tea_table2_string, font=("Calibri", 17, "bold"), fill="#1b2538")

                #Boton Siguiente-----------------------------------------------------------------------------------------------------------------
                next_button = tkinter.Button(red_queen_screen, image=next_arrow_image, borderwidth=0, command=blackjack)
                next_button_window = canvas_red_queen_image.create_window(590,455, anchor="nw", window=next_button)

        #Boton Siguiente hatman() (Principal)-----------------------------------------------------------------------------------------------------------
        next_button = tkinter.Button(red_queen_screen, image=next_arrow_image, borderwidth=0, command=queen_gate)
        next_button_window = canvas_red_queen_image.create_window(590,455, anchor="nw", window=next_button)

#Capitulo de juego final
#Creacion de clase Carta (Card) 
class Card:
        def __init__(self, image, value):
                self.image = image
                self.value = value

def blackjack():
        #Creacion de pantalla
        blackjack_screen = LabelFrame(window, width=712, height=540)
        blackjack_screen.place(x=0, y=0, relheight=1, relwidth=1)

        canvas_blackjack = tkinter.Canvas(blackjack_screen, width = 712, height=540)
        canvas_blackjack.pack(fill="both", expand=True)
        canvas_blackjack.create_image(0,0, image= queen_screen_image, anchor="nw")

        #Juego Final
        def final_game():
                #Construcción de Pantalla
                final_game_screen = LabelFrame(window, width=712, height=540)
                final_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
                        
                canvas_final_game = tkinter.Canvas(final_game_screen, width = 712, height=540)
                canvas_final_game.pack(fill="both", expand=True)
                canvas_final_game.create_image(0,0, image= queen_red_screen_image, anchor="nw")

                #Agrega puntaje
                def addScore(score, draw=None):
                        aliceScore.append(score)
                        print(score)

                        if draw == "first":
                                second_card()
                        elif draw == "second":
                                third_card()
                        elif draw == "third":
                                redqueen()

                #Funcion para elegir el valor de la carta si es un As
                def choose1or11(screen, canvas, card=None):
                        #Boton para elegir 1
                        choose1Button = tkinter.Button(screen, text = "1", font=("Gabriola",15,"bold"), padx= 75,bg ="#b6e2d3", fg= "#b74153", command = lambda: addScore(1, draw=card))
                        choose1Button_window = canvas.create_window(150,450, anchor="nw", window=choose1Button)

                        #Boton para elegir 11
                        choose11Button = tkinter.Button(screen, text = "11", font=("Gabriola",15,"bold"), padx= 75, bg ="#b6e2d3", fg= "#b74153", command = lambda: addScore(11, draw=card))
                        choose11Button_window = canvas.create_window(350,450, anchor="nw", window=choose11Button)

                def showScore(screen, canvas):
                        #canvas.create_image(0,0, image=dialogue_image, anchor="nw")
                        alice_score = 0
                        for i in aliceScore:
                                alice_score += i
                        showScore_string = (f"Tu puntaje es {alice_score}")
                        canvas.create_text(350,350, text=showScore_string, font=("Calibri", 17, "bold"), fill="#1b2538")
                        print(alice_score) #Para comprobar que se sumen correctamente los valores
                
                #Turno de ALICIA------------------------------------------------------------------------------------------------------------------
                #---PRIMER CARTA------------------------------------------------------------------------------------------------------------------
                def first_card():
                        #Creacion de pantalla
                        final_game_screen = LabelFrame(window, width=712, height=540)
                        final_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
                        
                        canvas_final_game = tkinter.Canvas(final_game_screen, width = 712, height=540)
                        canvas_final_game.pack(fill="both", expand=True)
                        canvas_final_game.create_image(0,0, image= queen_red_screen_image, anchor="nw")
                        canvas_final_game.create_image(0,0, image=dialogue_image, anchor="nw")
                        
                        #Seleccion de la primer carta
                        selectedCard = cards[random.randint(0, len(cards) - 1)]
                        #Traspaso de la carta al arreglo de cartas seleccionadas
                        selectedCards.append(selectedCard)
                        #Remocion de la carta del arreglo original
                        cards.remove(selectedCard)
                        #Muestra de la primer carta
                        selectedCard_Label =tkinter.Label(image = selectedCards[0].image)
                        selectedCard_Label.place(x=170, y=100)
                        #Espera 2 segundos
                        #time.sleep(2)
                        #Chequeo de Ases
                        if (selectedCard.value == 1):
                                blackjack_choose1or11_string = "¿Quieres contarla como 1 o como 11? "
                                canvas_final_game.create_text(315, 400, text=blackjack_choose1or11_string, font=("Calibri", 17, "bold"), fill="#1b2538")
                                choose1or11(final_game_screen, canvas_final_game, card="first")
                        
                        else:
                                addScore(10)
                        #Espera 1 segundo
                        #time.sleep(1)
                        #Muestra el puntaje
                        showScore(final_game_screen, canvas_final_game)

                        #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                        next_button = tkinter.Button(final_game_screen, image=next_arrow_image, borderwidth=0, command=second_card)
                        next_button_window = canvas_final_game.create_window(590,455, anchor="nw", window=next_button)
                
                #---SEGUNDA CARTA-----------------------------------------------------------------------------------------------------------------
                def second_card():        
                        #Creacion de pantalla
                        final_game_screen = LabelFrame(window, width=712, height=540)
                        final_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
                        
                        canvas_final_game = tkinter.Canvas(final_game_screen, width = 712, height=540)
                        canvas_final_game.pack(fill="both", expand=True)
                        canvas_final_game.create_image(0,0, image= queen_red_screen_image, anchor="nw")
                        canvas_final_game.create_image(0,0, image=dialogue_image, anchor="nw")

                        #Seleccion de la segunda carta
                        selectedCard = cards[random.randint(0, len(cards) - 1)]
                        #Traspaso de la carta al arreglo de cartas seleccionadas
                        selectedCards.append(selectedCard)
                        #Remocion de la carta del arreglo original
                        cards.remove(selectedCard)
                        #Muestra de la primer carta
                        selectedCard_Label =tkinter.Label(image = selectedCards[0].image)
                        selectedCard_Label.place(x=170, y=100)
                        #Muestra de la segunda carta
                        selectedCard_Label =tkinter.Label(image = selectedCards[1].image)
                        selectedCard_Label.place(x=300, y=100)
                        #Espera 2 segundos
                        #time.sleep(2)
                        #Chequeo de Ases
                        if (selectedCard.value == 1):
                                blackjack_choose1or11_string = "¿Quieres contarla como 1 o como 11? "
                                canvas_final_game.create_text(315, 400, text=blackjack_choose1or11_string, font=("Calibri", 17, "bold"), fill="#1b2538")
                                choose1or11(final_game_screen, canvas_final_game, card="second")
                        
                        else:
                                addScore(10)
                        #Espera 1 segundo
                        #time.sleep(1)
                        #Muestra el puntaje
                        showScore(final_game_screen, canvas_final_game)
                        #Chequear si perdió o no

                        #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                        next_button = tkinter.Button(final_game_screen, image=next_arrow_image, borderwidth=0, command=third_card)
                        next_button_window = canvas_final_game.create_window(590,455, anchor="nw", window=next_button)
                
                #---TERCER CARTA------------------------------------------------------------------------------------------------------------------
                def third_card():
                        #Creacion de pantalla
                        final_game_screen = LabelFrame(window, width=712, height=540)
                        final_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
                        
                        canvas_final_game = tkinter.Canvas(final_game_screen, width = 712, height=540)
                        canvas_final_game.pack(fill="both", expand=True)
                        canvas_final_game.create_image(0,0, image= queen_red_screen_image, anchor="nw")
                        canvas_final_game.create_image(0,0, image=dialogue_image, anchor="nw")
                        
                        #Seleccion de la tercer carta
                        selectedCard = cards[random.randint(0, len(cards) - 1)]
                        #Traspaso de la carta al arreglo de cartas seleccionadas
                        selectedCards.append(selectedCard)
                        #Remocion de la carta del arreglo original
                        cards.remove(selectedCard)
                        #Muestra de la primer carta
                        selectedCard_Label =tkinter.Label(image = selectedCards[0].image)
                        selectedCard_Label.place(x=170, y=100)
                        #Muestra de la segunda carta
                        selectedCard_Label =tkinter.Label(image = selectedCards[1].image)
                        selectedCard_Label.place(x=300, y=100)
                        #Muestra de la tercer carta
                        selectedCard_Label =tkinter.Label(image = selectedCards[2].image)
                        selectedCard_Label.place(x=430, y=100)
                        #Espera 2 segundos
                        #time.sleep(2)
                        #Chequeo de Ases
                        if (selectedCard.value == 1):
                                blackjack_choose1or11_string = "Quieres contarla como 1 o como 11? "
                                canvas_final_game.create_text(315, 400, text=blackjack_choose1or11_string, font=("Calibri", 17, "bold"), fill="#1b2538")
                                choose1or11(final_game_screen, canvas_final_game,card="third")
                        
                        else:
                                addScore(10)
                        #Espera 1 segundo
                        #time.sleep(1)
                        #Muestra el puntaje
                        showScore(final_game_screen, canvas_final_game)
                        
                        #Chequear si perdió o no

                        #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                        next_button = tkinter.Button(final_game_screen, image=next_arrow_image, borderwidth=0, command=redqueen)
                        next_button_window = canvas_final_game.create_window(590,455, anchor="nw", window=next_button)
                
                #Turno de la REINA ROJA (Computadora)----------------------------------------------------------------------------------------------
                def redqueen():
                        aliceFinalScore = 0
                        redQueenFinalScore = 0
                        redQueenCardsPlayed = 0
                        xDisplayCoordinate = 170

                        #Creacion de pantalla
                        redQueen_game_screen = LabelFrame(window, width=712, height=540)
                        redQueen_game_screen.place(x=0, y=0, relheight=1, relwidth=1)
                        
                        canvas_redQueen_game_screen = tkinter.Canvas(redQueen_game_screen, width = 712, height=540)
                        canvas_redQueen_game_screen.pack(fill="both", expand=True)
                        canvas_redQueen_game_screen.create_image(0,0, image= queen_red_screen_image, anchor="nw")

                        for i in aliceScore:
                                aliceFinalScore += i
                        while (aliceFinalScore > redQueenFinalScore) and (redQueenCardsPlayed < 3):
                                selectedCard = cards[random.randint(0, len(cards) - 1)]
                                redQueenFinalScore += selectedCard.value
                                selectedCard_Label =tkinter.Label(image = selectedCard.image)
                                selectedCard_Label.place(x=xDisplayCoordinate, y=100)
                                xDisplayCoordinate += 130
                                redQueenCardsPlayed += 1
                                cards.remove(selectedCard)
                        
                        #Imprimir puntaje final -------------------------------------------------------------
                        canvas_redQueen_game_screen.create_image(0,0, image=dialogue_image, anchor="nw")
                        showScore_string = (f"El puntaje de la Reina Roja es {redQueenFinalScore}")
                        canvas_redQueen_game_screen.create_text(370,350, text=showScore_string, font=("Calibri", 17, "bold"), fill="#1b2538")
                        print(redQueenFinalScore) #Para comprobar que se sumen correctamente los valores
                        time.sleep(2.0)
                        if (aliceFinalScore > redQueenFinalScore):
                                #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                                next_button = tkinter.Button(redQueen_game_screen, image=next_arrow_image, borderwidth=0, command=lambda: ending("win"))
                                next_button_window = canvas_redQueen_game_screen.create_window(590,455, anchor="nw", window=next_button)
                                #ending("win")
                        else:
                                #Boton Siguiente-----------------------------------------------------------------------------------------------------------
                                next_button = tkinter.Button(redQueen_game_screen, image=next_arrow_image, borderwidth=0, command=lambda: ending("lose"))
                                next_button_window = canvas_redQueen_game_screen.create_window(590,455, anchor="nw", window=next_button)

                                #ending("lose")

                first_card()
                        
        
        #Boton de aceptar y comenzar el juego
        play_button = tkinter.Button(blackjack_screen, text = "Jugar", font=("Gabriola",20, "bold"),bg ="#b6e2d3", fg= "#b74153", padx=100, command = final_game)
        play_button_window = canvas_blackjack.create_window(220,450, anchor="nw", window=play_button)
        
#Finales-------------------------------------------------------------------------------------------------------------------------------
def ending(outcome):
        #Construccion de la pantalla
        ending_screen = LabelFrame(window, width=712, height=540)
        ending_screen.place(x=0, y=0, relheight=1, relwidth=1)

        canvas_ending_image = tkinter.Canvas(ending_screen, width = 712, height=540)
        canvas_ending_image.pack(fill="both", expand=True)

        if outcome=="out":
                #-----------Imagen pantalla-----------------------------------------------------------------------------------------------------
                canvas_ending_image.create_image(0,0, image=out_screen_image, anchor="nw")
                
                 #----------Texto de Bienvenida-------------------------------------------------------------------------------------------------------
                canvas_ending_image.create_text(356, 100, text="Vuelta al mundo real... \nMejor suerte la próxima!", font=("Gabriola", 30, "bold"),fill="white")

                #-----------Boton (Volver al menu principal)-----------------------------------------------------------------------------------------
                back_button = tkinter.Button(ending_screen, text = "Volver al menu principal", font=("Gabriola",18, "bold"), padx=22, bg ="#b6e2d3", fg= "#b74153", command = welcome)
                back_button_window = canvas_ending_image.create_window(230,450, anchor="nw", window=back_button)
        
        elif outcome=="win":
                #-----------Imagen pantalla-----------------------------------------------------------------------------------------------------
                canvas_ending_image.create_image(0,0, image=win_screen_image, anchor="nw")
                                
                #----------Texto de Bienvenida-------------------------------------------------------------------------------------------------------
                canvas_ending_image.create_text(356, 320, text="Has vencido a la Reina Roja y ganado el juego! \nAhora todo el universo te pertenece... O algo asi", font=("Gabriola", 30, "bold"),fill="white")

                #Boton (Volver al menu principal))-----------------------------------------------------------------------------------------
                back_button = tkinter.Button(ending_screen, text = "Volver al menu principal", font=("Gabriola",18, "bold"), padx=22, bg ="#b6e2d3", fg= "#b74153", command = welcome)
                back_button_window = canvas_ending_image.create_window(230,450, anchor="nw", window=back_button)

        elif outcome=="lose":
                #-----------Imagen pantalla-----------------------------------------------------------------------------------------------------
                canvas_ending_image.create_image(0,0, image=loose_screen_image, anchor="nw")
                                
                #----------Texto de Bienvenida-------------------------------------------------------------------------------------------------------
                canvas_ending_image.create_text(356, 205, text="Has perdido contra la Reina Roja, que pena! \n        Pero... era todo un sueño?", font=("Gabriola", 30, "bold"),fill="white")

                #Boton (Volver al menu principal))-----------------------------------------------------------------------------------------
                back_button = tkinter.Button(ending_screen, text = "Volver al menu principal", font=("Gabriola",18, "bold"), padx=22, bg ="#b6e2d3", fg= "#b74153", command = welcome)
                back_button_window = canvas_ending_image.create_window(230,450, anchor="nw", window=back_button)

        else:
                print("Comando equivocado.")
 
#Creación de la ventana raiz y asignación propiedades----------------------------------------------------------------------------------
window = tkinter.Tk()
window.title("Alicia en el Pais de las Encrucijadas")
window.geometry("720x565")
#icono = ImageTk.PhotoImage(Image.open("Images/icono.ico"))
window.iconbitmap("Images/icono.ico") #<- Agregar iconito a la ventana

#Importación de imagenes----------------------------------------------------------------------------------------------------------------
welcome_screen_image = ImageTk.PhotoImage(Image.open("Images/home_screen.png"))
dialogue_image = ImageTk.PhotoImage(Image.open("Images/text_box.png"))
instructions_screen_image = ImageTk.PhotoImage(Image.open("Images/instructions.png"))
introduction_screen_image = ImageTk.PhotoImage(Image.open("Images/introduction.png"))
woods_screen_image = ImageTk.PhotoImage(Image.open("Images/woods.png"))
woods2_screen_image = ImageTk.PhotoImage(Image.open("Images/woods2.png"))
next_arrow_image = ImageTk.PhotoImage(Image.open("Images/next_arrow.png"))
red_path_screen_image = ImageTk.PhotoImage(Image.open("Images/red_path.png"))
golden_gate_screen_image = ImageTk.PhotoImage(Image.open("Images/golden_gate.png"))
not_golden_gate_screen_image = ImageTk.PhotoImage(Image.open("Images/not_golden_gate.png"))

#Caterpillar------------------------------------------------------------------------------------------------------------
alice_caterpillar_screen_image = ImageTk.PhotoImage(Image.open("Images/alice_caterpillar.png"))
caterpillar_screen_image = ImageTk.PhotoImage(Image.open("Images/caterpillar.png"))
caterpillar1_screen_image = ImageTk.PhotoImage(Image.open("Images/caterpillar1.png"))
caterpillar_game_screen_image = ImageTk.PhotoImage(Image.open("Images/caterpillar_game.png"))

#Cheshire Cat-----------------------------------------------------------------------------------------------------------
cat_encounter_screen_image = ImageTk.PhotoImage(Image.open("Images/cat_encounter.png"))
cheshire_cat_screen_image = ImageTk.PhotoImage(Image.open("Images/cheshire_cat.png"))
cat_and_alice_screen_image = ImageTk.PhotoImage(Image.open("Images/cat_and_alice.png"))
cat_path_screen_image = ImageTk.PhotoImage(Image.open("Images/cat_path.png"))

#Hatman-----------------------------------------------------------------------------------------------------------------
tea_table_screen_image = ImageTk.PhotoImage(Image.open("Images/tea_table.png"))
hatman_encounter_screen_image = ImageTk.PhotoImage(Image.open("Images/hatman_encounter.png"))
alice_tea_table_screen_image = ImageTk.PhotoImage(Image.open("Images/alice_tea_table.png"))
hatman_tea_table_screen_image = ImageTk.PhotoImage(Image.open("Images/hatman_tea_table.png"))

hatman_screen_image = ImageTk.PhotoImage(Image.open("Images/hatman.png"))
unbirthday_screen_image = ImageTk.PhotoImage(Image.open("Images/unbirthday.png"))

#Red Queen--------------------------------------------------------------------------------------------------------------
labyrinth_screen_image = ImageTk.PhotoImage(Image.open("Images/labyrinth.png"))
queen_gate_screen_image = ImageTk.PhotoImage(Image.open("Images/queen_gate.png"))
queen1_screen_image = ImageTk.PhotoImage(Image.open("Images/queen1.png"))
queen_cards_screen_image = ImageTk.PhotoImage(Image.open("Images/queen_cards.png"))
queen_screen_image = ImageTk.PhotoImage(Image.open("Images/queen.png"))
queen_red_screen_image = ImageTk.PhotoImage(Image.open("Images/queen_red.png"))

#Endings---------------------------------------------------------------------------------------------------------------
out_screen_image = ImageTk.PhotoImage(Image.open("Images/out.png"))
win_screen_image = ImageTk.PhotoImage(Image.open("Images/win.png"))
loose_screen_image = ImageTk.PhotoImage(Image.open("Images/loose.png"))

#Cartas----------------------------------------------------------------------------------------------------------------
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

#Creacion de arreglo de Cartas
cards = []
#Añadir cartas al arreglo con su imagen y valor respectivo
A_Pikas = Card(Apikas_image, 1)
cards.append(A_Pikas)
A_Clover = Card(Aclover_image, 1)
cards.append(A_Clover)
A_Heart = Card(Aheart_image, 1)
cards.append(A_Heart)
A_Diamond = Card(Adiam_image, 1)
cards.append(A_Diamond)
J_Pikas = Card(Jpikas_image, 10)
cards.append(J_Pikas)
J_Clover = Card(Jclover_image, 10)
cards.append(J_Clover)
J_Heart = Card(Jheart_image, 10)
cards.append(J_Heart)
J_Diamond = Card(Jdiam_image, 10)
cards.append(J_Diamond)
K_Pikas = Card(Kpikas_image, 10)
cards.append(K_Pikas)
K_Clover = Card(Kclover_image, 10)
cards.append(K_Clover)
K_Heart = Card(Kheart_image, 10)
cards.append(K_Heart)
K_Diamond = Card(Kdiam_image, 10)
cards.append(K_Diamond)
Q_Pikas = Card(Qpikas_image, 10)
cards.append(Q_Pikas)
Q_Clover = Card(Qclover_image, 10)
cards.append(Q_Clover)
Q_Heart = Card(Qheart_image, 10)
cards.append(Q_Heart)
Q_Diamond = Card(Qdiam_image, 10)
cards.append(Q_Diamond)

#Arreglo de cartas seleccionadas
selectedCards = []
#Arreglo de cartas de la Reina
redQueenCards = []
#Arreglo de puntajes de Alicia
aliceScore = []

window.mainloop()