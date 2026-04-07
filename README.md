# Auto Whisper Transcriber

Um script simples e automático em Python para realizar a transcrição em lote de arquivos de áudio utilizando o [Whisper](https://github.com/openai/whisper) da OpenAI.

## 🎙️ O que este app faz?

Este programa lê todos os arquivos de áudio (formato `.mp3`) presentes na pasta `src/`, transcreve o conteúdo deles otimizado para o idioma Português (`pt`), e automaticamente salva um arquivo de texto equivalente (`.txt`) com a transcrição final na pasta `output/`.

**Configurações Atuais:**
- **Modelo:** `medium` (garante alta capacidade de precisão em português mantendo velocidade de execução razoável).
- **Processamento em lote:** Transcreve automaticamente todos os mídias da pasta sem precisar executar de um em um.

## 📂 Estrutura de Pastas

```text
open-ai-whisper/
├── src/               # 📥 Pasta de Entrada: Coloque seus arquivos .mp3 aqui
├── output/            # 📤 Pasta de Saída: Os arquivos .txt transcritos serão salvos aqui
├── autoWhisper.py     # ⚙️ O script principal de execução
└── .gitignore         # 🚫 Ignora arquivos de sistema e outputs para o git
```

## 🚀 Como usar

### 1. Pré-requisitos

Para utilizar este projeto, é necessário possuir no sistema:
- **Python 3.8+**
- **[FFmpeg](https://ffmpeg.org/)** instalado (necessário para o Whisper processar o áudio)

E instalar as dependências de biblioteca no seu ambiente virtual (`venv`):

```bash
pip install -U openai-whisper
```

### 2. Executando o Script

1. Cole os seus arquivos `.mp3` desejados dentro da pasta `src/`.
2. Em seu terminal, execute o script:
   
   ```bash
   python autoWhisper.py
   ```
   
4. Aguarde o final do processo (na primeira execução pode demorar um pouco pois o modelo `medium` será baixado). 
5. Acesse seus textos prontos na pasta `output/`!
