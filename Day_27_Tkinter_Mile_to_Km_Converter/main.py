from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(400,200)
window.config(padx=20,pady=20)

def miles_to_km():
    converter = int(miles_input.get())
    kilometer=converter*1.6
    result.config(text=str(kilometer))

miles_label=Label(text="Miles",font=("Times New Roman",20))
miles_label.grid(column=5,row=0)

equal_label=Label(text="is equal to",font=("Times New Roman",20))
equal_label.grid(column=2,row=2)

kilometer_label=Label(text="Km",font=("Times New Roman",20))
kilometer_label.grid(column=5,row=2)

result=Label(text="0",font=("Times New Roman",20))
result.grid(column=4,row=2)

calculate_button=Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=4,row=4)

miles_input=Entry(width=10)
miles_input.grid(column=4,row=0)


window.mainloop()