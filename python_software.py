import json
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.categories = set()

    def add_category(self, category):
        """Adiciona uma nova categoria para transações."""
        self.categories.add(category)

    def add_transaction(self, amount, category, transaction_type, date=datetime.now().strftime("%Y-%m-%d")):
        """Registra uma nova transação financeira."""
        if category not in self.categories:
            print(f"Categoria '{category}' não existe. Adicione a categoria primeiro.")
            return
        self.transactions.append({
            'amount': amount,
            'category': category,
            'type': transaction_type,
            'date': date
        })

    def get_balance(self):
        """Calcula o saldo atual."""
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'revenue')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        return income - expenses

    def generate_report(self):
        """Gera um relatório detalhado de transações."""
        df = pd.DataFrame(self.transactions)
        return df.groupby(['date', 'category', 'type']).sum()

    def plot_expenses(self):
        """Gera gráficos de despesas por categoria."""
        df = pd.DataFrame(self.transactions)
        if not df.empty:
            expense_data = df[df['type'] == 'expense'].groupby('category').sum()
            expense_data.plot(kind='bar', y='amount', legend=False)
            plt.title('Despesas por Categoria')
            plt.ylabel('Valor (R$)')
            plt.xlabel('Categorias')
            plt.show()
        else:
            print("Não há despesas registradas para gerar gráfico.")

    def set_financial_goal(self, goal):
        """Define uma meta financeira."""
        self.financial_goal = goal
        print(f"Meta financeira definida: R$ {{self.financial_goal:.2f}}")

    def check_alerts(self):
        """Verifica e exibe alertas sobre pagamentos próximos."""
        print("Verifique seus pagamentos próximos!")

# Uso do FinanceManager
def main():
    fm = FinanceManager()

    # Adicionando categorias
    fm.add_category('Alimentação')
    fm.add_category('Transporte')
    fm.add_category('Lazer')

    # Adicionando transações
    fm.add_transaction(2000, 'Salário', 'revenue')
    fm.add_transaction(300, 'Alimentação', 'expense')
    fm.add_transaction(100, 'Transporte', 'expense')
    fm.add_transaction(150, 'Lazer', 'expense')

    # Cálculo do saldo atual
    current_balance = fm.get_balance()
    print(f'Saldo atual: R$ {{current_balance:.2f}}')

    # Geração de relatório de transações
    report = fm.generate_report()
    print("\nRelatório de Transações:")
    print(report)

    # Gerar gráfico de despesas
    fm.plot_expenses()

    # Definindo uma meta financeira
    fm.set_financial_goal(1500)

    # Checando alertas
    fm.check_alerts()

if __name__ == "__main__":
    main()