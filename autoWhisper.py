import whisper
import os
from pathlib import Path

# Configuração de Caminhos
pasta_origem = r"C:\war\poc-python-tools\open-ai-whisper\src"
pasta_destino = r"C:\war\poc-python-tools\open-ai-whisper\output"
model_name = "medium"

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# 1. Carrega o modelo (isso pode demorar um pouco na primeira vez)
print(f"Carregando modelo {model_name}...")
model = whisper.load_model(model_name)

# 2. Lista todos os arquivos .mp3 na pasta src
arquivos_mp3 = [f for f in os.listdir(pasta_origem) if f.endswith(".mp3")]

if not arquivos_mp3:
    print("Nenhum arquivo .mp3 encontrado na pasta src.")
else:
    for arquivo in arquivos_mp3:
        caminho_completo_mp3 = os.path.join(pasta_origem, arquivo)
        nome_sem_extensao = Path(arquivo).stem
        
        print(f"Processando: {arquivo}...")

        # 3. Transcrição
        result = model.transcribe(
            caminho_completo_mp3,
            language="pt",
            word_timestamps=True
        )

        # 4. Salva o TXT na pasta output com o mesmo nome
        caminho_txt = os.path.join(pasta_destino, f"{nome_sem_extensao}.txt")
        
        with open(caminho_txt, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        print(f"Sucesso! Texto salvo em: {caminho_txt}")

print("\n--- Todos os arquivos foram processados ---")