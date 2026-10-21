# 🚀 Uso do AgentScope 2.0 com Python

Um projeto com exemplos de execução de código utilizando o framework **AgentScope** na versão 2.0.6, com o objetivo de ser um tutorial.

## 🎯 Objetivo

Este projeto fornece exemplos do AgentScope para:

- ⚙️ Padronizar criação de código
- 🛠️ Criar ferramentas
- 🤖 Criar agentes
- 🧪 Facilitar experimentos e benchmarks


---

## 🧰 Requisitos

- Python **3.11.8**
- LM Studio
---

## ⚙️ Setup do Ambiente

Siga os passos abaixo para configurar e executar o ambiente do projeto:

```bash
# Criar ambiente virtual
python -m venv venv

# Atualizar o pip
pip install --upgrade pip

# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Verificar se o AgentScope está na versão esperada (2.0.6)
pip show agentscope

# Executar o código
python main.py

# Para sair do ambiente virtual
deactivate