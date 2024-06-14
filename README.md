# OpenAI: ChatBot de um e-commerce fictício de produtos ecológicos

Este é um projeto codificado em Python acessando a API da OpenAI para uso da inteligência artificial GPT.
Aprendizado:
- Criação de assistente IA
- Upload de arquivos de contexto ao assistente
- Prompt para definição de persona do assistente (comportamentos)
- Function Calling associada ao assistente
- Envio de imagem para análise do assistente

## 🔐 API Key

É necessário a criação de uma API key na plataforma da OpenAI. (https://platform.openai.com/api-keys)
Após criar sua API KEY, informe ela dentro do arquivo .env deste repositório e **atente-se para não compartilhá-lo**.

## ⚙️ Configuração do Ambiente

### Criando e Ativando o Ambiente Virtual

**Windows:**
```bash
python -m venv IA_GPT-OpenAI
IA_GPT-OpenAI\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv IA_GPT-OpenAI
source IA_GPT-OpenAI/bin/activate
```

### Instalação das Bibliotecas

```bash
pip install numpy openai python-dotenv tiktoken flask opencv-python
```

## 📚 Referências de Leitura

- [Documentação Whisper](https://openai.com/research/whisper)
- [Documentação Dall-E](https://openai.com/research/dall-e)
- [Preços OpenAI](https://openai.com/pricing)
- [Áudios Longos](https://platform.openai.com/docs/guides/speech-to-text/prompting)

