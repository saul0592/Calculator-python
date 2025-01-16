import pytest
import calculator_test
import tkinter as tk
from calculador import main, cal, borrar  


@calculator_test.fixture
def setup_tkinter():
    """New interaz"""
    window = tk.Tk()
    window.geometry('500x500')
    window.title("Calculadora")
    
    resultado_entry = tk.Entry(window, width=20, font=('Arial', 12), borderwidth=2, relief='solid')
    resultado_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    resultado_entry.insert(0, 'Ingresa un dato')
    
    return window, resultado_entry


def test_agregar_numero(setup_tkinter):
    
    window, resultado_entry = setup_tkinter

    # simulation of the entry has a value
    resultado_entry.insert(0, '5')

    # call the function
    main('3')

    # verify of the num is the same
    assert resultado_entry.get() == '53'


def test_calcular(setup_tkinter):
    
    window, resultado_entry = setup_tkinter

    # simulation of a entry has a expresion 
    resultado_entry.insert(0, '5+3')

    # Call the function that evaluate the expresion  
    cal()

    # verify is the answear is correct 
    assert resultado_entry.get() == '8'


def test_borrar(setup_tkinter):
   
    window, resultado_entry = setup_tkinter

    # simulation to entry a value 
    resultado_entry.insert(0, '5+3')

    # call the function of delete(borrar)
    borrar()

    # verify is the entry is empty 
    assert resultado_entry.get() == ''


@calculator_test.mark.parametrize(
    "input_val, expected_output",
    [
        ("10+5", "15"),
        ("3*3", "9"),
        ("8/4", "2"),
        ("10-3", "7"),
        ("5/0", "ERROR: Div/0")
    ]
)
def test_calcular_parametrizado(setup_tkinter, input_val, expected_output):
    window, resultado_entry = setup_tkinter

    # simulation od entry has a expression 
    resultado_entry.insert(0, input_val)

    # call the function cal 
    cal()

    # verify if it is the correct answear
    assert resultado_entry.get() == expected_output
