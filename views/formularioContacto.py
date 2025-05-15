import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from models.Contacto import Contacto
from controllers.ctrlContacto import guardarContacto

def crearVentana():
    #Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Mi formulario de contacto")
    ventana.geometry("700x600")
    
    #Label de informacion
    titulo = tk.Label(ventana, text="FORMULARIO DE CONTACTO")
    titulo.pack()
    
    #Label de nombre
    labelNombre = tk.Label(ventana, text="Ingrese si nombre: ")
    labelNombre.pack() 
    #Entrada de texto
    EntradaNombre = tk.Entry(ventana)
    EntradaNombre.pack()
    
    #Label de apellido
    labelApellido = tk.Label(ventana, text="Ingrese su apellido: ")
    labelApellido.pack()
    #Entrada de apellido
    entradaApellido = tk.Entry(ventana)
    entradaApellido.pack()
    
    #Entrada de correo
    labelCorreo = tk.Label(ventana, text="Ingrese su correo electronico: ")
    labelCorreo.pack()
    entradaCorreo = tk.Entry(ventana)
    entradaCorreo.pack()
    
    #Entrada de telefono
    labelTelefono = tk.Label(ventana, text="Ingrese su telefono: ")
    labelTelefono.pack()
    entradaTelefono = tk.Entry(ventana)
    entradaTelefono.pack()
    
    #Seleccionar pais
    labelPais = tk.Label(ventana, text="Selecciona su pais: ")
    labelPais.pack()
    #Seleccion de pais
    paises = ["Perú", "Ecuador", "Venezuela", "Bolivia", "Brasil", "Chile", "Colombia", "Argentina", "Uruguay", "Paraguay"]
    seleccionPais = ttk.Combobox(ventana, values=paises)
    seleccionPais.current(0)
    seleccionPais.pack(pady=10)
    
    
    #Funcion del boton nuevo contacto
    def agregarContacto():
        nombre = EntradaNombre.get()
        apellido = entradaApellido.get()
        correo = entradaCorreo.get()
        telefono = entradaTelefono.get()
        pais = seleccionPais.get()
        
        if nombre and apellido and correo and telefono and pais:
            nuevoContacto = Contacto(nombre, apellido, correo, telefono, pais)
            guardarContacto(nuevoContacto)
            messagebox.showinfo("Exito", "Se registro correctamente")
            EntradaNombre.delete(0, tk.END)
            entradaApellido.delete(0, tk.END)
            entradaCorreo.delete(0, tk.END)
            entradaTelefono.delete(0, tk.END)
            seleccionPais.current(0)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
    
    #boton agregar nuevo contacto
    btnAgregarContacto = tk.Button(ventana, text="Agregar nuevo contacto", command=agregarContacto, bg="green", fg="white")
    btnAgregarContacto.pack(pady=10)
    
    
    
    #boton eliminar contacto
    
    #boton actualizar contacto
    #boton buscar contacto
    
    #iniciar la interfaz
    ventana.mainloop()
    
    
#Llamos a la funcion de crear ventana
crearVentana()