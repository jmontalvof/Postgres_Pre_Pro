
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

RUN apt-get update &&     apt-get install -y --no-install-recommends         postgresql-client         git         curl &&     apt-get autoremove -y &&     apt-get clean &&     rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["bash"]
