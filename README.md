# Chat Deep - Aplicativo Streamlit com DeepSeek

## Descrição
Este é um aplicativo de chat baseado em [Streamlit](https://streamlit.io/) que utiliza o modelo `deepseek-r1-distill-llama-70b` da [LangChain Groq](https://python.langchain.com/docs/integrations/llms/groq). O objetivo é permitir a interação com o modelo de linguagem de maneira simples e intuitiva.

## Recursos
- Interface minimalista criada com Streamlit.
- Persistência do histórico de mensagens na sessão.
- Oculta elementos padrão da interface do Streamlit para um design mais limpo.
- Integração com o modelo de IA via LangChain Groq.

## Requisitos
- Python 3.8+
- Dependências listadas no arquivo `requirements.txt`:
  ```txt
  streamlit
  python-dotenv
  langchain_groq
  ```

## Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/seuusuario/chat-deep.git
   cd chat-deep
   ```
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` e defina sua chave de API do Groq:
   ```ini
   GROQ_API_KEY=seu_api_key_aqui
   ```

## Uso
Para iniciar o aplicativo, execute:
```sh
streamlit run app.py
```

## Estrutura do Código
- **dotenv**: Carrega variáveis de ambiente do arquivo `.env`.
- **Streamlit**: Gera a interface de chat.
- **LangChain Groq**: Integração com o modelo de linguagem.
- **Histórico de mensagens**: Gerenciado via `st.session_state`.

## Personalização
- Para alterar o modelo de IA utilizado, modifique a linha:
  ```python
  llm = ChatGroq(model="novo-modelo", api_key="sua_chave")
  ```
- Para modificar a interface, edite a seção `st.markdown()` que oculta o menu e rodapé.

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
