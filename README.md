# 📚 Painel de Controle de Treinamentos

Este sistema foi desenvolvido para auxiliar na **gestão e visualização de treinamentos corporativos**, permitindo registrar, exibir e controlar treinamentos de forma eficiente, com uma interface visual moderna.

---

## 🚀 Funcionalidades

- ✅ Cadastro de treinamentos com título, data e participantes
- 📅 Visualização em painel dinâmico
- 🗂 Registro de usuários com níveis de acesso
- 🖥 Interface desenvolvida com `CustomTkinter` e `Tkinter`
- 🧠 Armazenamento local usando arquivos JSON
- 📈 Destaque automático para o próximo treinamento agendado

---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- CustomTkinter
- Tkinter
- JSON (armazenamento)
- Pillow (para imagens)
- pyautogui (automatização, se aplicável)

---

## 📂 Estrutura do Projeto

projeto_treinamento/
├── main.py # Arquivo principal da aplicação
├── interface/ # Interface visual do sistema
│ └── painel.py
├── helpers/ # Funções auxiliares
│ ├── dados.py
│ └── imagens.py
├── data/ # Base de dados local (JSON)
│ └── treinamentos.json
├── imagens/ # Logos, ícones, fundos
│ ├── logo.png
│ └── fundo.jpg
└── requisitos.txt # Dependências do sistema
