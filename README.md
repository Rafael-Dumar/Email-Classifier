# Email-Classifier
# 🤖 Analisador de Emails com IA

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers-yellow?style=for-the-badge)](https://huggingface.co/docs/transformers/index)

> Um projeto full-stack que utiliza Processamento de Linguagem Natural (NLP) para classificar emails em "Produtivos" ou "Improdutivos" e sugerir respostas adequadas, otimizando o fluxo de trabalho e a gestão de caixas de entrada.

---

## 🚀 Acesso à Aplicação

**A aplicação está no ar! Acesse e teste em:** [**[COLE O SEU LINK DO RENDER AQUI]**]([COLE O SEU LINK DO RENDER AQUI])

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido como uma solução para automatizar a triagem de um alto volume de emails. A aplicação web permite que o usuário cole o texto de um email ou faça o upload de um arquivo (`.txt` ou `.pdf`) e, utilizando um modelo de IA da Hugging Face, classifica o conteúdo em duas categorias:

* **Produtivo:** Emails que exigem uma ação ou resposta específica (solicitações, dúvidas, etc.).
* **Improdutivo:** Emails que não necessitam de uma ação imediata (agradecimentos, felicitações, informativos).

Com base na classificação, o sistema sugere uma resposta padrão, ajudando a agilizar a comunicação e a liberar o tempo da equipe.

## ✨ Funcionalidades

* **Análise de Texto e Arquivos:** Processa tanto texto colado diretamente quanto arquivos `.txt` e `.pdf`.
* **Interface Intuitiva:** UI limpa com suporte a "Arrastar e Soltar" (Drag and Drop) para uma melhor experiência do usuário.
* **Classificação com IA:** Utiliza um modelo de classificação **Zero-Shot** para entender a intenção do email sem a necessidade de treinamento prévio em um dataset específico.
* **Sugestão de Resposta:** Fornece respostas pré-definidas e contextuais baseadas na classificação do email.

## 🛠️ Tecnologias Utilizadas

O projeto foi construído com as seguintes tecnologias:

* **Backend:**
    * **Python 3.11**
    * **Flask:** Micro-framework para o servidor web e a API.
* **Inteligência Artificial:**
    * **Hugging Face Transformers:** Para o pipeline de classificação (`zero-shot-classification`).
    * **PyMuPDF:** Para a extração de texto de arquivos PDF.
* **Frontend:**
    * **HTML**
    * **CSS**.
    * **JavaScript (ES6):** Para interatividade, manipulação do DOM e comunicação com a API via `fetch`.
* **Deploy:**
    * **Render:** Plataforma de nuvem para a hospedagem da aplicação.

## ⚙️ Como Executar Localmente

Para executar este projeto na sua máquina local, siga os passos abaixo:

# 1. Clone o repositório
git clone [https://github.com/Rafael-Dumar/Email-Classifier)]

# 2. Crie e ative um ambiente virtual
python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação Flask
flask run

Agora, abra seu navegador e acesse `http://127.0.0.1:5000`.

## 👨‍💻 Autor

Desenvolvido por **Rafael Dumar**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafaeldumar/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Rafael-Dumar)