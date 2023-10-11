import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)


def button_click():
    mil = miles.get()
    kilometers = round(int(mil) * 1.609, 1)
    result_label['text'] = kilometers


miles = tkinter.Entry(width=10)
miles.grid(column=1, row=0)

miles_label = tkinter.Label(text='Miles', font=('Arial', 18, 'bold'))
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text='is equal to', font=('Arial', 18, 'bold'))
equal_label.grid(column=0, row=1)

km_label = tkinter.Label(text='Km', font=('Arial', 18, 'bold'))
km_label.grid(column=2, row=1)

result_label = tkinter.Label(text='0', font=('Arial', 18, 'bold'))
result_label.grid(column=1, row=1)

button = tkinter.Button(text='Calculate', command=button_click)
button.grid(column=1, row=2)

window.mainloop()
