# Chatbot-Inteligente

## 🚀 Como rodar o projeto localmente

1. **Clone o repositório e entre na pasta:**
   ```bash
    git clone <url-do-seu-repositorio>
    cd ChatBotpy
   
    python3 -m venv .venv
    source .venv/bin/activate

    pip install -r requirements.txt

2. **Configure o seu arquivo .env:**

    Copie o arquivo .env.example para um novo chamado .env.

    Preencha as chaves necessárias.

3.**Inicie o servidor:**
    Bash
    uvicorn app.main:app --reload