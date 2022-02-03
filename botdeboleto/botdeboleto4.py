from tkinter import Tk
import unicodedata

root = Tk()


def remove_accents(b):
    normalized = unicodedata.normalize('NFKD', b)
    print(type(normalized))
    return ''.join([c for c in normalized if not unicodedata.combining(c)])


def click(event=None):
    send = 'Você: ' + a.get()
    text.insert(END, '\n' + send)
    b = a.get().lower()
    b = remove_accents(b)

    if b == 'oi':
        text.insert(END, '\n' + 'Bot: Oi, tudo bem? Sou o Bot Deboleto, espero que eu consiga te ajudar. Para continuar, digite: sim')
    elif b == 'sim':
        text.insert(END, '\n' + 'Bot: Em que posso ajudar? \n 1-Para entrar em contato? \n 2-Para encerrar.')
    elif b == '1':
        text.insert(END, '\n' + 'Bot: Para conversar com a minha criadora: deboletothatiane@gmail.com, agradeço por ter vindo até aqui. Até logo :)')
    else:
        text.insert(END, '\n' + 'Bot: Desculpe, ainda não conheço essa palavra')
    a.delete(0, 'end')


text = Text(root, bg='beige')
text.grid(row=0, column=0, columnspan=2)

a = Entry(root, width=40)

send = Button(root, text='Enviar', bg='teal', width=20,
              command=click).grid(row=1, column=1)
a.grid(row=1, column=0)

root.title('Bot Deboleto')
root.bind('<Return>', click)
root.mainloop()