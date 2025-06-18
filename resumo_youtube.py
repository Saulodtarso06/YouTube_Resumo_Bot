import os
import sys
from pytubefix import YouTube
import subprocess
import openai

from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Certifique-se de definir sua chave da OpenAI como variável de ambiente / Cria cliente OpenAI
import openai
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# Verifica se a chave foi carregada corretamente
if not api_key:
    print("ERRO: Variável OPENAI_API_KEY não encontrada.")
    exit(1)

# Verifica se a URL foi passada como argumento
if len(sys.argv) < 2:
    print("Uso: python main.py <URL do vídeo>")
    sys.exit(1)

# Parâmetros iniciais
url = sys.argv[1]
filename = "audio.wav"

# Baixa o vídeo e obtém o link do stream
yt = YouTube(url)
stream_url = yt.streams.filter(only_audio=True).first().url

# Converte o stream para WAV com ffmpeg
subprocess.run([
    "ffmpeg", "-y", "-i", stream_url,
    "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", filename
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Transcreve o áudio com Whisper
with open(filename, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    ).text

# Gera resumo com GPT-4o-mini
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": (
                "Você é um assistente que resume vídeos do YouTube de forma clara e estruturada. "
                "Responda com formatação Markdown."
            )
        },
        {
            "role": "user",
            "content": f"Transcrição do vídeo:\n{transcript}\n\nAgora, faça um resumo detalhado."
        }
    ]
)

# Salva o resumo em um arquivo .md
os.makedirs("output", exist_ok=True)
with open("output/resumo.md", "w", encoding="utf-8") as md_file:
    md_file.write(completion.choices[0].message.content)

print("✅ Resumo salvo em 'output/resumo.md'")
