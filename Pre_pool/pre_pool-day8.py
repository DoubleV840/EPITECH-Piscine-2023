# # -*- coding: utf-8 -*-
# #Created by Willipatafoul at 11:02 on 20/09/2023
# #

# # ---------- matplotlib and numpy Task 01 ---------- #

# import numpy as np
# x_min = 10
# x_max = 20
# x_values = np.linspace(x_min, x_max, 100)
# print(x_values)

# # ---------- matplotlib and numpy Task 02 ---------- #

# #(0; 12), (1; 32), (2; 42) and (3; 52)

# import numpy as np
# import matplotlib.pyplot as plt

# plt.plot([0, 1, 2, 3], [12, 32, 42, 52], 'r.:')
# plt.show()

# # ---------- matplotlib and numpy Task 03 ---------- #

# import numpy as np
# import matplotlib.pyplot as plt

# liste_abssisses = []
# liste_ordonnees = []
# i = 1
# for i in range(4):
#     abssisses = float(input(f"Entrez le point {i+1} en abssisses : "))
#     liste_abssisses.append(abssisses)
# for i in range(4):
#     ordonnees = float(input(f"Entrez le point {i+1} en ordonnees : "))
#     liste_ordonnees.append(ordonnees)

# plt.plot(liste_abssisses, liste_ordonnees, 'r.:')
# plt.show()

# # ---------- matplotlib and numpy Task 04 ---------- #

# import numpy as np
# import matplotlib.pyplot as plt
# import math

# def plot_fct(func, x_min, x_max):
#     x = np.linspace(x_min, x_max, 1000) 
#     y = func(x)
#     plt.plot(x, y)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Function Plot')
#     plt.grid(True)
#     plt.show()

# def f(x):
#     return x**2 + x*3 + 2

# plot_fct(math.sin, 0, 50) 
# plot_fct(f, -100, 200) 
# plot_fct(lambda x: x**2, -10, 10) 
# plot_fct(lambda x: 1/x, -100, 100)

# ---------- Tkinter Task 01 ---------- #

import tkinter as tk

window = tk.Tk()
def button_click():
    label.config(text="Button Clicked!")
    
button = tk.Button(window, text="Click Me", command=button_click)
label = tk.Label(window, text="Hello, Tkinter!")
window.title("FENEEEEEEEEETRE")
window.geometry("1000x500")
label.pack()
button.pack()

window.mainloop()
