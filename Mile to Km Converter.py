from tkinter import *

def  button_clicked():
    result = input.get()
    result = (float(result)) * 1.60934
    result_label.config(text=result)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(350, 130)
window.config(padx=30, pady=30)

input = Entry()
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 15))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 15))
equal_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 15))
km_label.grid(column=2, row=1)

button_calculate = Button(text="Calculate",  command=button_clicked, font=("Arial", 15))
button_calculate.grid(column=1, row=2)


window.mainloop()