
# Documentação do FinanceManager

## Introdução
O `FinanceManager` é um software para gerenciamento financeiro pessoal, permitindo que os usuários registrem suas transações, categorizem despesas e receitas, gerem relatórios e visualizem gráficos de consumo por categoria.

## Instalação
Para instalar o `FinanceManager`, siga os passos abaixo:
1. **Requisitos:**
   - Python 3.6 ou superior
   - Bibliotecas: `matplotlib`, `pandas`

2. **Instalação das dependências:**
   ```
   pip install matplotlib pandas
   ```

## Uso
Para utilizar o `FinanceManager`, você pode seguir o exemplo abaixo, que demonstra suas principais funcionalidades:

```python
from FinanceManager import FinanceManager

# Criação de uma instância do gerenciador financeiro
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
print(f'Saldo atual: R$ {current_balance:.2f}')

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
```

## Referência de API
### Classe FinanceManager
- `__init__(self)`: Inicializa a instância com uma lista vazia de transações e um conjunto de categorias.
- `add_category(self, category)`: Adiciona uma nova categoria para transações.
- `add_transaction(self, amount, category, transaction_type, date)`: Registra uma nova transação financeira.
- `get_balance(self)`: Calcula o saldo atual com base nas transações registradas.
- `generate_report(self)`: Gera um relatório detalhado de transações agrupadas por data, categoria e tipo.
- `plot_expenses(self)`: Gera gráficos de despesas por categoria.
- `set_financial_goal(self, goal)`: Define uma meta financeira.
- `check_alerts(self)`: Verifica e exibe alertas sobre pagamentos próximos.

## Contribuição
Para contribuir com o `FinanceManager`, siga estas etapas:
1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça suas modificações e teste.
4. Submeta um pull request.

### Estilo de Código
Siga as diretrizes PEP 8 para formatação de código Python.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.