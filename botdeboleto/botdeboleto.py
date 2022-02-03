from tkinter import Tk

root = Tk()

def send():
    send = 'Você' + a.get()
    text.insert(END, '\n' + send)
    if(a.get() == 'oi'):
        text.insert(END, '\n' + 'Bot:Oi, tudo bem?')
    elif(a.get() == 'olá'):
        text.insert(END, '\n' + 'Bot:Olá, tudo bem?')
    elif(a.get() == 'bom dia'):
        text.insert(END, '\n' + 'Bot:Bom dia, tudo bem?')
    else:
        text.insert(END, '\n' + 'Bot:Desculpe, ainda não conheço essa palavra')       

text = Text(root, bg='white')
text.grid(row=0, column=0, columnspan=2)

a = Entry(root, width=40)

send = Button(root, text='Enviar', bg='white', width=20, command=send).grid(row=1, column=1)
a.grid(row=1, column=0)

root.title('Bot Deboleto')
root.mainloop()