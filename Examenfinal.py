from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
          # Initializations
        
        #ancho
        ancho = 800
        
        #alto
        alto = 600

        # Asigna un color de fondo a la ventana. Si se omite
        window.configure(bg = 'green')

          # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

  #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('Aplicación De Validación De Numeros')

         # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Variables')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

         # creamos un etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)

         #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)

         # creamos un etiqueta
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)

         #creamos un input donde ingresar valores
        self.var2 = Entry(frame)
        self.var2.focus()
        self.var2.grid(row = 2, column = 1)

        # creamos un etiqueta
        Label(frame, text = 'tercer numero: ').grid(row = 3, column = 0)

         #creamos un input donde ingresar valores
        self.var3 = Entry(frame)
        self.var3.focus()
        self.var3.grid(row = 3, column = 1)


    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var1.get()) != 0

   # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var2.get()) != 0 and len(self.var2.get()) != 0

           # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var3.get()) != 0 and len(self.var3.get()) != 0


        #validamos si estamos en la aplicación inicial
if __name__ == '__main__':

    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()