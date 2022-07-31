import pipe
import joblib
from tkinter import *
from tkinter import messagebox

model = joblib.load('dados/my_model.pkl')

window = Tk()
window.title('Modelo')

label1 = Label(text='Preencha os campos')
label1.grid(column=1, row=0)

i = 1
entries = []

for n in [n for n in range(16) if n != 4]:
    label = Label(text=f"Feature{n}:")
    label.grid(column=0, row=i)
    entry = Entry(width=32)
    entry.grid(column=1, row=i)
    entries.append(entry)
    i += 1

def get_features():
    lista = []
    for e in entries:
        try:
            float(e.get())
        except ValueError:
            messagebox.showwarning(
                title='Erro',
                message='Preencha todos os campos com valores numéricos'
            )
            return
        else:
            lista.append(float(e.get()))
    result = pipe.transform(lista)

    l = Label(text=f'Resultado previsto pelo modelo: {model.predict(result)}')
    l.grid(column=1, row=i)

    for e in entries:
        e.delete(0, END)

botao = Button(text='Prever resultado', command=get_features)
botao.grid(column=0, row=i)

window.mainloop()
