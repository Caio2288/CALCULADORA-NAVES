from tkinter import *

# 🎨 CORES
cor_fundo = "#000000"    # fundo preto
cor_display = "#1C1C1C"  # cinza escuro para o display
cor_botao = "#2E2E2E"    # cinza médio para botões
cor_operador = "#FF9500" # laranja para operadores
cor_texto = "#FFFFFF"    # texto branco

# 🖥️ JANELA
janela = Tk()
janela.title('Calculadora Naves')  # 🔥 alterado o título aqui!
janela.geometry("300x450")
janela.config(bg=cor_fundo)

# 🔳 FRAME DO DISPLAY
frame_tela = Frame(janela, width=300, height=60, bg=cor_display)
frame_tela.grid(row=0, column=0)

# 🔲 FRAME DO CORPO
frame_corpo = Frame(janela, width=300, height=400, bg=cor_fundo)
frame_corpo.grid(row=1, column=0)

# 📟 VARIÁVEL DO DISPLAY
valor_texto = StringVar()

# 📟 LABEL DO DISPLAY
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2,
                  padx=7, relief=FLAT, anchor="e",
                  bg=cor_display, fg=cor_texto, font=('ivy 18 bold'))
app_label.place(x=0, y=0)

# 🛠️ FUNÇÕES
todos_valores = ""

def entrar_valores(valor):
    """Adiciona valores ao display."""
    global todos_valores
    todos_valores += str(valor)
    valor_texto.set(todos_valores)

def calcular():
    """Calcula o resultado."""
    global todos_valores
    try:
        resultado = str(eval(todos_valores))
        valor_texto.set(resultado)
        todos_valores = resultado
    except:
        valor_texto.set("Erro")
        todos_valores = ""

def limpar_tela():
    """Limpa o display."""
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# 🔲 TAMANHO PADRÃO DOS BOTÕES
btn_w = 7
btn_h = 3

# 🔳 LINHA 1
Button(frame_corpo, text="C", command=limpar_tela, width=btn_w*2, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=0, y=0, width=150, height=75)
Button(frame_corpo, text="%", command=lambda: entrar_valores('%'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=150, y=0, width=75, height=75)
Button(frame_corpo, text="/", command=lambda: entrar_valores('/'), width=btn_w, height=btn_h,
       bg=cor_operador, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=225, y=0, width=75, height=75)

# 🔳 LINHA 2
Button(frame_corpo, text="7", command=lambda: entrar_valores('7'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=0, y=75, width=75, height=75)
Button(frame_corpo, text="8", command=lambda: entrar_valores('8'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=75, y=75, width=75, height=75)
Button(frame_corpo, text="9", command=lambda: entrar_valores('9'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=150, y=75, width=75, height=75)
Button(frame_corpo, text="*", command=lambda: entrar_valores('*'), width=btn_w, height=btn_h,
       bg=cor_operador, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=225, y=75, width=75, height=75)

# 🔳 LINHA 3
Button(frame_corpo, text="4", command=lambda: entrar_valores('4'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=0, y=150, width=75, height=75)
Button(frame_corpo, text="5", command=lambda: entrar_valores('5'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=75, y=150, width=75, height=75)
Button(frame_corpo, text="6", command=lambda: entrar_valores('6'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=150, y=150, width=75, height=75)
Button(frame_corpo, text="-", command=lambda: entrar_valores('-'), width=btn_w, height=btn_h,
       bg=cor_operador, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=225, y=150, width=75, height=75)

# 🔳 LINHA 4
Button(frame_corpo, text="1", command=lambda: entrar_valores('1'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=0, y=225, width=75, height=75)
Button(frame_corpo, text="2", command=lambda: entrar_valores('2'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=75, y=225, width=75, height=75)
Button(frame_corpo, text="3", command=lambda: entrar_valores('3'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=150, y=225, width=75, height=75)
Button(frame_corpo, text="+", command=lambda: entrar_valores('+'), width=btn_w, height=btn_h,
       bg=cor_operador, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=225, y=225, width=75, height=75)

# 🔳 LINHA 5
Button(frame_corpo, text="0", command=lambda: entrar_valores('0'), width=btn_w*2, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=0, y=300, width=150, height=75)
Button(frame_corpo, text=".", command=lambda: entrar_valores('.'), width=btn_w, height=btn_h,
       bg=cor_botao, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=150, y=300, width=75, height=75)
Button(frame_corpo, text="=", command=calcular, width=btn_w, height=btn_h,
       bg=cor_operador, fg=cor_texto, font=('ivy 13 bold'), relief=FLAT).place(x=225, y=300, width=75, height=75)

janela.mainloop()
