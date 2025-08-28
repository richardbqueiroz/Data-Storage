# 📈 Data Storage: Sistema de Gerenciamento de Estoque

## 📜 Sobre o Projeto

Data Storage é um Sistema de Gerenciamento de Estoque (SGE) desenvolvido como um projeto de conclusão de curso. A sua principal missão é solucionar a desorganização e a falta de controle de produtos em estoques, um problema comum que afeta a eficiência de pequenas e médias empresas.

O sistema substitui métodos de gestão manuais ou inadequados, que frequentemente levam a perdas por excesso de estoque (overstock) ou perda de vendas por falta de produtos (stockout). Através de uma interface simples e prática, o Data Storage automatiza o controle de mercadorias e centraliza as informações, transformando dados operacionais em insights estratégicos para a tomada de decisão

# 🚀 Funcionalidades

## ✨ Telas Principais

- Painel de Controle (Dashboard)
- Uma visão geral e consolidada do estado do estoque, com os principais Indicadores de Desempenho (KPIs) para uma análise rápida e eficaz.


## 📝 Cadastro de Produtos

- Formulário intuitivo para registrar novos produtos, editar informações existentes e manter a base de itens sempre atualizada.


## ✅ Funcionalidades Principais

- 📦 Módulo de Cadastros: Gerenciamento completo de Produtos, Fornecedores, Categorias e Marcas.


- ↔️ Controle de Transações: Registro simplificado de entradas e saídas de produtos, com atualização automática do inventário.


- 👤 Gestão de Usuários: Sistema de controle de acesso com diferentes níveis de permissão para garantir a segurança dos dados.



- 📊 Dashboard Inteligente: Painel visual com KPIs essenciais, como valor do estoque, produtos com baixa quantidade, itens mais movimentados e gráficos de desempenho.


- 📄 Módulo de Relatórios: Geração de relatórios gerenciais detalhados em PDF sobre a movimentação do estoque, inventário atual e mais.


## 🛠️ Tecnologias e Arquitetura
- O projeto foi construído utilizando tecnologias modernas e consolidadas, seguindo o padrão de arquitetura 

- MVT (Model-View-Template), nativo do Django. Uma API RESTful foi implementada para garantir a comunicação segura e desacoplada entre o back-end e o front-end.

## ⚙️ Instalação e Execução

- Clone o repositório:

```bash
  git clone https://github.com/richardbqueiroz/Data-Storage.git
  cd Data-Storage
```

- Crie e ative um ambiente virtual:

```bash
  # Para Windows
  python -m venv venv
  .\venv\Scripts\activate

  # Para Linux/Mac
  python3 -m venv .venv
  source venv/bin/activate
```

 - Instale as dependências do projeto:

```bash
  pip install -r requirements.txt
```

- Execute as migrações do banco de dados:

```bash
  python manage.py migrate
```

- Crie um superusuário para acessar o painel de administrador:

```bash
  python manage.py createsuperuser
```

- Inicie o servidor de desenvolvimento:

```bash
  python manage.py runserver
```

Acesse a aplicação em http://127.0.0.1:8000.

## 👨‍💻 Autor

- Richard Bonafin Queiroz 

- LinkedIn: linkedin.com/in/richardbqueiroz

- GitHub: @richardbqueiroz


## 📄Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
