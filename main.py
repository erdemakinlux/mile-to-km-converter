from tkinter import *

def miles_to_km(miles_in):
    if len(miles_in) > 0:
        miles = float(miles_in)
        km = miles * 1.609
        km_result_label.config(text=f"{km}")
    else:
        km_result_label.config(text="{km}")



window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

km_label = Label(text='km')
km_label.grid(column=2,row=1)

miles_label = Label(text='miles')
miles_label.grid(column=2,row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0,row=1)

km_result_label = Label(text='0')
km_result_label.grid(column=1,row=1)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)

calculate_button = Button(text="Calculate", command=miles_to_km(miles_input.get()))
calculate_button.grid(column=1,row=2)



window.mainloop()
