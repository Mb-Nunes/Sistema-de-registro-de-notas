# 🎓 Sistema de Cadastro de Notas FATEC

Projeto desenvolvido em Python para cadastro de alunos, cálculo de médias e armazenamento de dados utilizando SQLite3.

O sistema funciona via terminal e permite registrar:

- 👤 Nome do aluno
- 📝 Nota N1
- 📝 Nota N2
- 📊 Média final
- ✅ Situação do aluno (Aprovado/Reprovado)

---

# 🚀 Tecnologias utilizadas

- 🐍 Python
- 🗄️ SQLite3

---

# 📁 Estrutura do projeto

```txt
CálculoNota/
│
├── main.py
├── clientes.py
├── database.py
├── README.md
│
└── data/
```

---

# ⚙️ Funcionalidades

- ✅ Cadastro de alunos
- ✅ Entrada de notas
- ✅ Cálculo automático da média
- ✅ Verificação de aprovação
- ✅ Armazenamento dos dados em banco SQLite

---

# 📊 Como funciona a média

A média é calculada utilizando os pesos:

- 📝 N1 = 40%
- 📝 N2 = 60%

Fórmula:

```python
media = (n1 * 0.4) + (n2 * 0.6)
```

---

# 🧩 Organização dos arquivos

## 📌 `main.py`

Responsável pelo fluxo principal do sistema:
- coleta de informações
- cálculo da média
- exibição dos resultados
- salvamento no banco de dados

---

## 📌 `clientes.py`

Contém as funções relacionadas à lógica do sistema:
- entrada de dados
- cálculo da média
- resultado do aluno

---

## 📌 `database.py`

Responsável pela conexão com o banco SQLite:
- criação da tabela
- inserção dos dados dos alunos

---

# 🗄️ Banco de Dados

O projeto utiliza SQLite3 para armazenar os dados localmente.

Tabela utilizada:

```sql
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    n1 REAL,
    n2 REAL,
    media REAL,
    situacao TEXT
)
```

---

# ▶️ Como executar o projeto

### 1️⃣ Instale o Python

Baixe em:
https://www.python.org/

---

### 2️⃣ Baixe os arquivos do projeto

---

### 3️⃣ Execute o sistema

```bash
python main.py
```

---

# 📚 Objetivo do projeto

Este projeto foi desenvolvido com foco em aprendizado de:

- 🧠 Funções
- 🧩 Modularização
- 🗄️ SQLite3
- 📂 Organização de código
- ⚙️ Estruturação de projetos Python
- 💾 Manipulação de dados

---

# 🔮 Melhorias futuras

- 🎨 Interface gráfica
- 📋 Listagem de alunos cadastrados
- ✏️ Edição e remoção de alunos
- 🔒 Validação avançada de notas
- 📤 Exportação de dados
- 🌐 Integração com interfaces web

---

# 👨‍💻 Autor

**Murilo Beluci Nunes**
