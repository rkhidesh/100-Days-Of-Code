from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    output_label.config(text=f"{km}")


#window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)
# #label
miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()    