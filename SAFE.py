import matplotlib.pyplot as plt
import numpy as np

vendas = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

despesas = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

valores_vendas = []
valores_despesas = []

conta = {"administrador": "admin@544"}
loop = True

print("Sistema de Análise Financeira Empresarial")
print()
print("Seja bem-vindo(a)!")
print()

while loop:
    login_nome = input("Digite o nome do usuário: ")
    login_senha = input("Digite sua senha: ")

    if login_nome == "administrador" and login_senha == conta["administrador"]:
        print("Acesso liberado!")
        break
    else:
        print("Acesso negado!")

print()

for mes in vendas:
  valor_vendas = int(input(f"Digite o valor das vendas do mês de {mes}: "))
  valores_vendas.append(valor_vendas)

print()

for mes in despesas:
 valor_despesas = int(input(f"Digite o valor das despesas do mês de {mes}: "))
 valores_despesas.append(valor_despesas)

print()

meta = int(input("Digite a meta atual: "))
meta_futura = int(input("Digite a próxima meta: "))

lucro_liquido = sum(valores_vendas)
total_despesas = sum(valores_despesas)
lucro_bruto = lucro_liquido - total_despesas
quanto_falta_meta = meta - lucro_bruto
quanto_falta_meta_futura = meta_futura - lucro_bruto

print()

if lucro_bruto >= meta_futura:
 print("Lucro de",lucro_bruto,"Todas as metas alcançadas!")
elif lucro_bruto >= meta:
 print("Lucro de",lucro_bruto,"Meta alcançada! Falta",quanto_falta_meta_futura,"para alcançar a próxima meta!")
elif lucro_bruto > 0:
 print("Lucro de",lucro_bruto,"Meta não alcançada. Falta",quanto_falta_meta,"para alcançar a meta atual!")
elif lucro_bruto == 0:
 print("Lucro nulo. Meta não alcançada. Falta",quanto_falta_meta,"para alcançar a meta atual!")
else:
 print("Prejuízo de",lucro_bruto,"Falta",quanto_falta_meta,"para alcançar a meta atual!")

labels = ['Vendas Totais', 'Despesas Totais', 'Lucro Bruto']
values = [lucro_liquido, total_despesas, lucro_bruto]
colors = ['#8fd98f', '#ff9999', '#66b3ff']

x = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x, values, color=colors, width=0.6)

ax.axhline(y=meta, color='gold', linestyle='--', label=f'Meta Atual: {meta}')
ax.axhline(y=meta_futura, color='purple', linestyle=':', label=f'Próxima Meta: {meta_futura}')

ax.set_ylabel('Valor (R$)', fontsize=12)
ax.set_title('Resumo Financeiro Anual e Metas', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=0, ha='center', fontsize=10)
ax.legend(fontsize=10)

for i, v in enumerate(values):
    ax.text(x[i], v + (max(values) * 0.02), f'R$ {v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'), ha='center', va='bottom', fontsize=9)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
