FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app/backend

# Copia los archivos necesarios
COPY backend /app/backend

# Instala dependencias
RUN pip install -r requirements.txt

