# Python-un yüngül versiyasını seçirik
FROM python:3.11-slim

# İşçi qovluğunu təyin edirik
WORKDIR /app

# Lazımi kitabxanaları quraşdırırıq
RUN pip install --no-cache-dir fastapi uvicorn psutil

# Kodlarımızı konteynerə köçürürük
COPY . .

# API-ın işləyəcəyi portu açırıq
EXPOSE 8000

# Serveri başladırıq
CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "8000"]