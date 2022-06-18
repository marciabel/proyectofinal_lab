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
import tkinter
from tkinter.font import BOLD
from tkinter.ttk import LabelFrame
from turtle import bgpic
from PIL import ImageTk, Image

#Ver Instrucciones
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
        back_button = tkinter.Button(instructions_screen, text = "Volver al menú", font=("Gabriola",20,"bold"), command = welcome)
        back_button_window = canvas_instructions_image.create_window(500,430, anchor="nw", window=back_button)

#Capitulo Introduccion al juego
def introduction():
        #Creación pantalla-------------------------------------------------------------------------------
        introduction_screen = LabelFrame(window, width=712, height=540)
        introduction_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_introduction_image = tkinter.Canvas(introduction_screen, width = 712, height=540)
        canvas_introduction_image.pack(fill="both", expand=True)
        canvas_introduction_image.create_image(0,0, image=introduction_screen_image, anchor="nw")


        #Imagen con dialogo------------------------------------------------------------------------------
        canvas_introduction_image.create_image(0,0, image=dialogue_image, anchor="nw")
        
        #Boton 1 (No seguir al conejo)-----------------------------------------------------------------------------------------
        back_button = tkinter.Button(introduction_screen, text = "No seguir al Conejo", font=("Gabriola",18, "bold"), padx=22, command = welcome)
        back_button_window = canvas_introduction_image.create_window(130,450, anchor="nw", window=back_button)

        #Boton 2 (Seguir al conejo)-----------------------------------------------------------------------------------------
        continue_button = tkinter.Button(introduction_screen, text = "Seguir al Conejo", font=("Gabriola",18, "bold"), padx=22, command = woods)
        continue_button_window = canvas_introduction_image.create_window(370,450, anchor="nw", window=continue_button)

#Capitulo Bosque
def woods():
        #Creación pantalla---------------------------------------------------------------------------
        woods_screen = LabelFrame(window, width=712, height=540)
        woods_screen.place(x=0, y=0, relheight=1, relwidth=1)
        
        canvas_woods_image = tkinter.Canvas(woods_screen, width = 712, height=540)
        canvas_woods_image.pack(fill="both", expand=True)
        canvas_woods_image.create_image(0,0, image= woods_screen_image, anchor="nw")

        #Imprimir instrucciones en pantalla------------------------------------------------------------
        canvas_woods_image.create_image(0,0, image=dialogue_image, anchor="nw")
        
        #Boton 1  (Seguir el camino Rojo -> Puerta Dorada)-----------------------------------------------------------------------------------------
        back_button = tkinter.Button(woods_screen, text = "Tomar el Camino Rojo", font=("Gabriola",18, "bold"), padx=22, command = golden_gate)
        back_button_window = canvas_woods_image.create_window(100,450, anchor="nw", window=back_button)

        #Boton 2  (Continuar al bosque -> Encuentro Caterpillar)-----------------------------------------------------------------------------------------
        continue_button = tkinter.Button(woods_screen, text = "Continuar al bosque", font=("Gabriola",18, "bold"), padx=22)
        continue_button_window = canvas_woods_image.create_window(360,450, anchor="nw", window=continue_button)


#Capitulo Puerta Dorada
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
        if golden_key == False:
                golden_gate_screen = LabelFrame(window, width=712, height=540)
                golden_gate_screen.place(x=0, y=0, relheight=1, relwidth=1)
                canvas_golden_gate_image = tkinter.Canvas(golden_gate_screen, width = 712, height=540)
                canvas_golden_gate_image.pack(fill="both", expand=True)

                canvas_golden_gate_image.create_image(0,0, image= not_golden_gate_screen_image, anchor="nw")
                canvas_golden_gate_image.create_image(0,0, image=dialogue_image, anchor="nw")

                #Boton (Volver al bosque -> Encuentro Caterpillar)-----------------------------------------------------------------------------------------
                continue_button = tkinter.Button(golden_gate_screen, text = "Volver al bosque", font=("Gabriola",18, "bold"), padx=22, command=woods)
                continue_button_window = canvas_golden_gate_image.create_window(270,450, anchor="nw", window=continue_button)


'''
#Capitulo CaterPillar
def caterpillar():
        #ventana

        #preguntas con puntaje
        puntaje = 0

        #print texto en la ventana
        #recibir puntaje 


        #Si el puntaje alcanza if
                golden_key = True
        

#Capitulo Cheshire Cat


#Capitulo Red Queen
'''


#Creación de la ventana raiz y asignación propiedades.
window = tkinter.Tk()
window.title("Alicia en el Pais de las Encrucijadas")
window.geometry("720x565")
#window.iconbitmap() <- Agregar iconito a la ventana

#Exportación de imagenes
welcome_screen_image = ImageTk.PhotoImage(Image.open("Images/home_screen.png"))
dialogue_image = ImageTk.PhotoImage(Image.open("Images/text_box.png"))
instructions_screen_image = ImageTk.PhotoImage(Image.open("Images/instructions.png"))
introduction_screen_image = ImageTk.PhotoImage(Image.open("Images/introduction.gif"))
woods_screen_image = ImageTk.PhotoImage(Image.open("Images/woods.png"))
golden_gate_screen_image = ImageTk.PhotoImage(Image.open("Images/golden_gate.png"))
not_golden_gate_screen_image = ImageTk.PhotoImage(Image.open("Images/not_golden_gate.png"))

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
        start_button = tkinter.Button(welcome_screen, text = "Comenzar", font=("Gabriola",15,"bold"), padx= 75, command = introduction)
        start_button_window = canvas_welcome_image.create_window(100,430, anchor="nw", window=start_button)

        #----------Boton Instrucciones-------------------------------------------------------------------------------------------------------
        howto_button = tkinter.Button(welcome_screen, text = "Instrucciones", font=("Gabriola",15,"bold"), padx= 75, command = open_how_to, )
        howto_button_window = canvas_welcome_image.create_window(350,430, anchor="nw", window=howto_button)

welcome()


#Llave dorada 
golden_key = False










window.mainloop()
