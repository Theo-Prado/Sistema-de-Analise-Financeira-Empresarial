📊 SAFE - Sistema de Análise Financeira Empresarial
Um sistema de linha de comando (CLI) desenvolvido em Python para auxiliar empresas no controle e análise financeira anual. O SAFE coleta dados de vendas e despesas mês a mês, calcula o lucro bruto, compara com metas definidas pelo usuário e gera um gráfico visual interativo para facilitar a tomada de decisões.
✨ Funcionalidades
🔐 Autenticação simples para acesso ao sistema
📅 Coleta mensal de valores de vendas e despesas
🎯 Definição de metas financeira (atual e futura)
🧮 Cálculo automático de faturamento, despesas e lucro bruto
📊 Geração de gráfico de barras com matplotlib, incluindo linhas de meta
🇧🇷 Formatação de valores no padrão monetário brasileiro (R$)
💻 Interface leve via terminal
🛠️ Pré-requisitos
Python 3.7 ou superior
matplotlib
numpy
📦 Instalação
Clone o repositório:
bash
12
Crie um ambiente virtual (opcional, mas recomendado):
bash
123
Instale as dependências:
bash
1
🚀 Como Executar
bash
1
(Substitua safe.py pelo nome exato do arquivo do seu script)
O sistema guiará você pelo fluxo:
Login de acesso
Inserção dos valores de vendas (janeiro a dezembro)
Inserção dos valores de despesas (janeiro a dezembro)
Definição das metas financeiras
Exibição do relatório textual + gráfico interativo
🔐 Credenciais Padrão
Campo
Valor
Usuário
administrador
Senha
admin@544
⚠️ Nota: As credenciais estão hardcodadas para fins didáticos. Em ambientes de produção, recomenda-se implementar hash de senhas e armazenamento seguro.
📈 Visualização
Após o processamento dos dados, o SAFE exibe um gráfico contendo:
🟢 Barra Verde: Total de Vendas
🔴 Barra Vermelha: Total de Despesas
🔵 Barra Azul: Lucro Bruto
🟡 Linha Dourada (tracejada): Meta Atual
🟣 Linha Roxa (pontilhada): Próxima Meta
Os valores são exibidos automaticamente sobre as barras, formatados em R$.
💡 Melhorias Futuras (Roadmap)
Integração com banco de dados (SQLite/PostgreSQL) para persistência de dados
Exportação de relatórios para .csv ou .pdf
Autenticação com hashing de senhas (bcrypt ou hashlib)
Validação de entrada (evitar crash com textos ou valores negativos)
Gráfico de evolução mensal (linha/tempo)
Suporte a múltiplos usuários/empresas
🤝 Contribuindo
Contribuições são sempre bem-vindas! Para propor melhorias:
Faça um fork do projeto
Crie uma branch com sua feature (git checkout -b feature/nova-funcionalidade)
Commit suas mudanças (git commit -m 'feat: adiciona nova funcionalidade')
Push para a branch (git push origin feature/nova-funcionalidade)
Abra um Pull Request
📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir. Consulte o arquivo LICENSE para mais detalhes.
👤 Autor
Desenvolvido por [Seu Nome]
📧 [seu.email@exemplo.com]
🔗 [LinkedIn/GitHub]
⭐ Se este projeto foi útil para seus estudos ou trabalho, deixe uma estrela no repositório!
