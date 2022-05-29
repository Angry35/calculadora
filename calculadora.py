# En este caso no voy a usar el tema de ttk ya que todos los botones que voy a agregar
# seran directamente con la libreria estandar de tkinter esto lo hago para poder personalizar los botones
import tkinter as tk
from tkinter import messagebox


# definimos nuestra clase
class Calculadora(tk.Tk):
    # Definimos nuestro metodo init
    def __init__(self):
        # llamamos al constructor de la clase padre, de esta manera cuando creemos un objeto de esta}
        # clase y llamemos el metodo mainloop no vamos a tener problemas para que se visualize nuestra aplicacion
        super().__init__()
        self.geometry('320x325')
        # especificamos que no se pueda modificar
        self.resizable(0, 0)
        # Ponemos el titulo de la ventana llamando el metodo title
        self.title('CALCULADORA')
        self.iconbitmap('calculadora.ico')
        # Atributos de Clase
        self.expresion = ''
        # caja de texto (input)
        self.entrada = None
        # StringVar lo utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # creamos los componentes
        self._creacion_componentes()

    # Metodos de clase
    # metodo para crear los componentes
    # Creamos nuestro metodo protegido
    # devido a que es un metodo de nuestra clase recibe el parametro self
    def _creacion_componentes(self):
        # creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        # debido que es un frame lo visualizamos con el metodo pack
        entrada_frame.pack(side=tk.TOP)
        # caja de Texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable=self.entrada_texto, width=24,
                           justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)
        # Creamos  otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        # Usamos el metodo pack sin ningunn parametro puesto que solo quiero que se visualize
        botones_frame.pack()

        # ASIGNACION Y VISUALIZACION DE BOTONES
        # Primer reglon (C,/)
        boton_Limpiar = tk.Button(botones_frame, text='C', width='32', height=3,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=self._Evento_Limpiar)
        # El metodo grid se usa para visualizar

        boton_Limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        # Agregar boton de division
        # Lambda lo usamos para dar una funcion anonima
        boton_dividir = tk.Button(botones_frame, text='/', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                                  command=lambda: self._evento_click('/'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)

        # Segundo reglon (7,8,9,*)

        boton_siete = tk.Button(botones_frame, text='7', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click(7))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)

        boton_ocho = tk.Button(botones_frame, text='8', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_click(8))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)

        boton_nueve = tk.Button(botones_frame, text='9', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click(9))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)

        boton_multiplicacion = tk.Button(botones_frame, text='*', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                                         command=lambda: self._evento_click('*'))
        boton_multiplicacion.grid(row=1, column=3, padx=1, pady=1)

        # Tercer reglon (4,5,6,-)

        boton_cuatro = tk.Button(botones_frame, text='4', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                                 command=lambda: self._evento_click(4))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)

        boton_cinco = tk.Button(botones_frame, text='5', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click(5))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)

        boton_seis = tk.Button(botones_frame, text='6', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_click(6))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)

        boton_menos = tk.Button(botones_frame, text='-', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._evento_click('-'))
        boton_menos.grid(row=2, column=3, padx=1, pady=1)

        # Cuarto reglon (1,2,3,+)

        boton_uno = tk.Button(botones_frame, text='1', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                              command=lambda: self._evento_click(1))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)

        boton_dos = tk.Button(botones_frame, text='2', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                              command=lambda: self._evento_click(2))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)

        boton_tres = tk.Button(botones_frame, text='3', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_click(3))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)

        boton_mas = tk.Button(botones_frame, text='+', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                              command=lambda: self._evento_click('+'))
        boton_mas.grid(row=3, column=3, padx=1, pady=1)

        # quinto reglon (0,.,eliminar,=)

        boton_cero = tk.Button(botones_frame, text='0', width=21, height=3, bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_click(0))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        boton_punto = tk.Button(botones_frame, text='.', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._evento_click('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)

        boton_evaluar = tk.Button(botones_frame, text='=', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                                command=self._evento_evaluar)
        boton_evaluar.grid(row=4, column=3, padx=1, pady=1)

    def _evento_evaluar(self):
        #eval evalua la expresion str como una expresion aritmetica
        try:
            resultado = str(eval(self.expresion))
            self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
        finally:
            self.expresion=''

    def _Evento_Limpiar(self):
        # El valor que voy a almacenar lo almaceno en la variable expresion
        self.expresion = ''
        # cada que presione limpiar/c  se limpiara todo lo que hallamos escrito
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento ala expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)




if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()

