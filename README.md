# YouTube_Resumo_Bot [LEGADO]

Um bot analisador simples em Python que analisa os videos do youtube, criar um script que seja capaz de criar um resumo de um video do youtube, recebendo a URL do video (``observação: o programa analisa apenas 1 video por vez``). Ideal para estudantes, pesquisadores, criadores de conteúdo e qualquer pessoa que queira entender rapidamente o conteúdo de um vídeo sem precisar assisti-lo por completo.

# Funcionalidades

- 🔗 Recebe uma URL de vídeo do YouTube
- 🎙️ Extrai o áudio do vídeo
- 📝 Transcreve o áudio para texto - Modelo Markdown
- 🧠 Resume o conteúdo automaticamente com IA (OpenAI GPT)
- 💾 Salva o resumo em um arquivo `.txt`

---

# Tecnologias Utilizadas

- Python 3.12+
- [pytubefix](https://pypi.org/project/pytubefix/) — Para baixar vídeos do YouTube
- [ffmpeg](https://ffmpeg.org/) — Para converter áudio
- [openai](https://pypi.org/project/openai/) — Para gerar resumos com IA
- [whisper](https://github.com/openai/whisper) (opcional) — Para transcrição de áudio com alta precisão

---

# Pré-requisitos

Antes de rodar o projeto, certifique-se de ter instalado:

- Python 3.12 ou superior
- ffmpeg (instalado e no PATH do sistema)
- Uma conta na [OpenAI](https://platform.openai.com/signup) e sua `API Key`

---

# Instalação

```bash
# Clone este repositório
git clone https://github.com/Saulodtarso06/YouTube_Resumo_Bot.git

# Acesse a pasta do projeto
cd YouTube_Resumo_Bot

# Instale as dependências
pip install -r requirements.txt

```
# Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

# Contato
Desenvolvido por Saulo de Tarso — dev jr fullstack  
📧 Email: saulo.detarso06@yahoo.com.br
🔗 GitHub: @Saulodtarso06

