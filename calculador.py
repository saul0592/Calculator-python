import tkinter as tk


def agreag_num(num):
    if resultado_entry.get() == "Ingresa un dato":
        resultado_entry.delete(0, tk.END)

    agregar_numero = resultado_entry.get()
    resultado_entry.delete(0, tk.END) 
    resultado_entry.insert(tk.END, agregar_numero + str(num))


def cal():
    try:
        expresion = resultado_entry.get()
        result = eval(expresion)
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(tk.END, "ERROR: Div/0")
    except Exception as e:
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(tk.END, "ERROR")

def borrar():
    resultado_entry.delete(0, tk.END)
    resultado_entry.get() == "Ingresa un dato"

def focus_in(event):
    """Función para borrar el texto por defecto cuando se hace click o se selecciona el campo"""
    if resultado_entry.get() == "Ingresa un dato":
        resultado_entry.delete(0, tk.END)

    
        
#raise ValueError

window = tk.Tk()
window.geometry('500x500')
window.title("Calculadora")
window.resizable(False, False) #venana no se mueva de las dimensiones

resultado_entry = tk.Entry(window, width=20, font=('Arial', 12), borderwidth=2, relief='solid')
resultado_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
resultado_entry.insert(0, 'Ingresa un dato' )

resultado_entry.bind("<FocusIn>", focus_in)

##declaramos las variables de los numeros
botones_numeros = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]


    
for (texto, row, col) in botones_numeros:
    tk.Button(window, text=texto, width=5, height=2, font=('Arial', 14),
              command=lambda num=texto: agreag_num(num)).grid(row=row, column=col, padx=5, pady=5)


operaciones = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('=', 4, 2), ('C', 0, 3)
]




for (texto, row, col) in operaciones:
    if texto == '=':
        tk.Button(window, text=texto, width=5, height=2, font=('Arial', 14), command=cal).grid(row=row, column=col, padx=5, pady=5)
    elif texto == 'C':
        tk.Button(window, text=texto, width=5, height=2, font=('Arial', 14), command=borrar).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(window, text=texto, width=5, height=2, font=('Arial', 14),
                  command=lambda op=texto: agreag_num(op)).grid(row=row, column=col, padx=5, pady=5)


#multiplicacion_botton=tk.Button(window, text='*', command=multiplicacion)
#multiplicacion_botton.pack(pady=20)

#division_botton=tk.Button(window, text='+', command=suma)
#division_botton.pack(pady=20  )

# Iniciar el bucle de eventos de Tkinter
window.mainloop()