from tkinter import * 
from tkinter import messagebox


class CalculadoraFinanceira:
    def __init__(self, master=None):
        self.master = master
        master.title("Calculadora Financeira Pessoal")
        master.geometry("400x400")
        master.configure(bg='#f0f0f0')
        self.frame_principal = Frame(master, bg='#f0f0f0')
        self.frame_principal.pack(pady=20)
        self.titulo = Label(self.frame_principal,
                            text="Controle de Gastos Mensais",
                            font=("Arial", 14, "bold"),
                            bg='#f0f0f0')
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)
        self.criar_campo("Renda Mensal (R$):", 1)
        self.criar_campo("Gastos Necessários (R$):", 2)
        self.criar_campo("Gastos Imprevistos (R$):", 3)
        self.criar_campo("Gastos Desnecessários (R$):", 4)
        self.btn_calcular = Button(self.frame_principal,
                                   text="Calcular",
                                   font=("Arial", 10),
                                   command=self.calcular,
                                   bg='#4CAF50',
                                   fg='white')
        self.btn_calcular.grid(row=5, column=0, columnspan=2, pady=15, ipadx=50)
        self.frame_resultados = Frame(master, bg='#f0f0f0')
        self.frame_resultados.pack(pady=10)
        self.label_resultado = Label(self.frame_resultados,
                                     text="",
                                     font=("Arial", 12),
                                     bg='#f0f0f0')
        self.label_resultado.pack()

        self.label_percentual = Label(self.frame_resultados,
                                      text="",
                                      font=("Arial", 10),
                                      bg='#f0f0f0')
        self.label_percentual.pack()
        
        def criar_campo(self, texto, linha):
            Label = Label(self.frame_principal,
                          text=texto,
                          font=("Arial", 10),
                          bg='#f0f0f0',
                          anchor='w')
            Label.grid(row=linha, column=0, sticky='w', padx=10, pady=5)
            entry = Entry(self.frame_principal, font=("Arial", 10))
            entry.grid(row=linha, column=1, padx=10, pady=5)

            if "Renda" in texto:
                self.renda_entry = entry
            elif "Necessários" in texto:
                self.necessarios_entry = entry
            elif "Imprevistos" in texto:
                self.imprevistos_entry = entry
            elif "Desnecessários" in texto:
                self.desnecessarios_entry = entry         
        
def calcular(self): 
    try:
    renda = float(self.renda_entry.get() or 0)
    necessarios = float(self.necessarios_entry.get() or 0)
    imprevistos = float(self.imprevistos_entry.get() or 0)
    desnecessarios = float(self.desnecessarios_entry.get() or 0)
    
if renda == 0:
    messagebox.showwarning("Aviso", "A renda mensal não pode ser zero!")

saldo = renda - necessarios - imprevistos - desnecessarios
percentual = (desnecessarios / renda) * 100

resultado_texto = f"Saldo Disponível: R$ {saldo:.2f}"
percentual_texto = f"Percentual gasto desnecessariamente: {percentual:.2f}%"

if saldo >= 0:
    self.label_resultado.config(text=resultado_texto, fg='green')
else:
    self.label_resultado.config(text=f"Déficit: R$ {abs(saldo):.2f}", fg='red')

self.label_percentual.config(text=percentual_texto)

except ValueError:
    messagebox.showerror("Erro", "Por favor, insira apenas números nos campos. \nUse ponto para decimais (ex: 1000.50)")

root = Tk()
app = CalculadoraFinanceira(root) 
root.mainloop()