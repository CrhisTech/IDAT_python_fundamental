import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.geometry('970x325')
window.wm_title('MatPlotLib Grafics')
window.minsize(width=500, height=250)

frame = tk.Frame(window, bg='red')
frame.grid(column=2, row=5, sticky='nsew')
names = ['blue', 'red', 'green', 'magenta', 'black']
colors = ['blue', 'red', 'green', 'magenta', 'black']
size = [15, 25, 10, 20, 30]

fig, axs = plt.subplots(1, 3, dpi=80, figsize =(13, 4), sharey=True, facecolor='#00f9f844')
fig.suptitle('MatPlotLib in Grafics')

# grafic bars
axs[0].bar(names, size, color=colors)
# scatter grafic
axs[1].scatter(names, size, color=colors)
# line grafic
axs[2].plot(names, size, color='m')

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=0, rowspan=3)

window.mainloop()