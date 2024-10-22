import tkinter as tk
from tkinter import font
from config import constantes as cons
from util import util_ventana as uv

class FormularioCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.construir_widgets()
        self.tema()
        
    
    def config_window(self):
        #Configuracion inicial de la ventana
        self.title("Calculadora")
        #Configurar el color de fondo y hacer transparente la ventana
        self.configure(bg=cons.COLOR_FONDO)
        self.attributes("-alpha", 0.96)
        w, h = 370, 570
        uv.centrar(self, w, h)
        
    def construir_widgets(self):
        #Etiqueta para mostrar la operacion solicitada
        self.operation_label = tk.Label(self, text = "", font=("Arial", 16), fg = cons.COLOR_TEXTO , bg = cons.COLOR_FONDO, justify="right")
        self.operation_label.grid(row = 0, column = 3, padx = 10, pady = 10) #Añadiendo column span 
        self.entry = tk.Entry(self, width=12, font=("Arial", 40), bd=0, fg=cons.COLOR_TEXTO, bg=cons.COLOR_CAJA_TEXTO, justify="right")
        self.entry.grid(row=1, column=0, columnspan = 4, padx = 10, pady=10)
        
        #Lista de Botones
        buttons = [
            "7", "8", "9", "C",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "<", "+",
            "%", "/", "="
        ]
        
        row_val = 2 #Ya utlizamos las primeras dos filas, así que lo ajustamos
        col_val = 0
        
        #Tipografia
        roboto_font = font.Font(family="Roboto", size=16)
        
        for button in buttons:
            #Fondo para los botones especiales
            if button in ["=","*","/","-","+", "C", ">", "%"]:
                color_fondo = cons.COLOR_BOTONES_ESPECIALES
                button_font = font.Font(size = 16, weight="bold")
            else:
                color_fondo = cons.COLOR_BOTONES
                button_font = roboto_font
            if button == "=":
                tk.Button(self, text = button, width=12, height=2, command= lambda b=button: self.on_button_click(b) , bg="grey", fg=cons.COLOR_TEXTO, relief=tk.FLAT, font=button_font, padx = 5, pady = 5, bd = 0, borderwidth = 0, highlightthickness=0, overrelief="flat").grid(row = row_val, column=col_val, pady=5, columnspan=2)
                    
            else:
                tk.Button(self, text = button, width=5, height=2, command= lambda b=button: self.on_button_click(b), bg=color_fondo, fg=cons.COLOR_TEXTO, relief=tk.FLAT, font=button_font, padx = 5, pady = 5, bd = 0, borderwidth = 0, highlightthickness=0, overrelief="flat").grid(row = row_val, column=col_val, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
            
    
    def on_button_click(self, value):
        
        if value == "=":
            
            try:
                expression = self.entry.get().replace("%", "/100")
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                operation = expression + " " + value
                self.operation_label.config(text=operation)                
                                
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text="")
                
        
        elif value == "C":
            self.entry.delete(0,tk.END)
            self.operation_label.config(text="")        

        elif value == "<":
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1]
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END, new_text)
                #Actualizar la etiqueta de operacion
                self.operation_label.config(text=new_text + " ")
                
                
                
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)
            
    
    def tema(self):
        self.dark_theme = True
        
        #Fuente font_awesome
        font_awesome = font.Font(family="FontAwesome", size = 12)
        self.theme_button = tk.Button(self, text = "Modo Oscuro \uf186", width=13, font=font_awesome, bd = 0, borderwidth=0, highlightthickness=0, relief=tk.FLAT, command=self.toggle_theme, bg = cons.COLOR_BOTONES_ESPECIALES_LIGHT)
        
        self.theme_button.grid(row = 0, column= 0, columnspan=2, pady = 0, padx = 0, sticky="nw")
        
    def toggle_theme(self):
        #Cambio de tema
        if self.dark_theme:
            self.configure(bg=cons.COLOR_FONDO_LIGHT)
            
            self.entry.config(fg=cons.COLOR_TEXTO_LIGHT, bg = cons.COLOR_CAJA_TEXTO_LIGHT)
            
            self.operation_label.config(fg=cons.COLOR_TEXTO_LIGHT, bg= cons.COLOR_FONDO_LIGHT)
            
            self.theme_button.configure(text= "\uf185 Modo Claro", relief=tk.SUNKEN, bg = cons.COLOR_BOTONES_ESPECIALES_LIGHT)
        else:
            self.configure(bg=cons.COLOR_FONDO)
            
            self.entry.config(fg=cons.COLOR_TEXTO, bg = cons.COLOR_CAJA_TEXTO)
            
            self.operation_label.config(fg=cons.COLOR_TEXTO, bg= cons.COLOR_FONDO)
            
            self.theme_button.configure(text= "\uf186 Modo Oscuro", relief=tk.RAISED, bg = cons.COLOR_BOTONES_ESPECIALES)
            
        self.dark_theme = not self.dark_theme