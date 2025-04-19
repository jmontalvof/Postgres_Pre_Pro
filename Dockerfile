FROM python:3.11-slim

# Establecer entorno no interactivo para evitar prompts
ENV DEBIAN_FRONTEND=noninteractive

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar solo lo necesario, limpiar caché y paquetes temporales
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-client \
        git \
        curl \
    && apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de ficheros
COPY . .

# Comando por defecto (puede ser sobreescrito por GitHub Actions)

FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

RUN apt-get update &&     apt-get install -y --no-install-recommends         postgresql-client         git         curl &&     apt-get autoremove -y &&     apt-get clean &&     rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["bash"]
