"""Ce projet est l'implémentation d'une calculatrice avec le module Tkinter"""

import tkinter as tk
import re

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.equation = tk.Entry(width=40, borderwidth=2)
        self.equation.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        
        self.create_buttons()

    def add_button(self, value):
        """
        Permet d'ajouter un boutton à l'interface

        1 2 3 4 5 6 7 8 9 0 + - * / c =
        
        """
        
        return tk.Button(self, text=value, width=10, height=3, command=lambda: self.click_button(str(value)))

    def click_button(self, value):
        """Fonction qui permet d'effectuer les actions sur les bouttons"""

        current_eq = self.equation.get()

        # Verify the equation
        if current_eq in ["#DIV/0", "#Error"]:
            current_eq = "" 

        
        if value == 'C':
            self.equation.delete(-1, tk.END)
        elif value == '=':
            try:
                if not re.match('^[0-9\+\-\*\/\(\)]*$', current_eq):
                    result = "#Error"
                else:
                    result = str(eval(current_eq))
            except ZeroDivisionError:
                result = "#DIV/0"

            except:
                result = "#Error"

            self.equation.delete(-1, tk.END)
            self.equation.insert(0, result)
        else:
            self.equation.delete(-1, tk.END)
            self.equation.insert(0, current_eq + value)


    def create_buttons(self):
        buttons = {
            '0': self.add_button(0),
            '1': self.add_button(1),
            '2': self.add_button(2),
            '3': self.add_button(3),
            '4': self.add_button(4),
            '5': self.add_button(5),
            '6': self.add_button(6),
            '7': self.add_button(7),
            '8': self.add_button(8),
            '9': self.add_button(9),
            'mult': self.add_button('*'),
            'add': self.add_button('+'),
            'sub': self.add_button('-'),
            'div': self.add_button('/'),
            'equal': self.add_button('='),
            'clear': self.add_button('C'),
        }

        rows = [
            [ buttons['7'], buttons['8'], buttons['9'], buttons['add']],
            [ buttons['4'], buttons['5'], buttons['6'], buttons['sub']],
            [ buttons['1'], buttons['2'], buttons['3'], buttons['mult']],
            [ buttons['clear'], buttons['equal'], buttons['0'], buttons['div']],
        ]

        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                button = row[j]

                button.grid(row=i+1, column=j+1, columnspan=1)





if __name__ == "__main__":
    app = Calculator()
    app.title("Calculatrice")
    app.mainloop()
