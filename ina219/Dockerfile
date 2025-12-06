FROM alpine:3.19

# Устанавливаем python, pip и поддержку i2c
RUN apk add --no-cache python3 py3-pip i2c-tools linux-headers build-base

# Создаём виртуальное окружение и устанавливаем smbus2 внутри него
RUN python3 -m venv /opt/venv \
    && /bin/sh -c "source /opt/venv/bin/activate && pip install --upgrade pip smbus2"

# Добавляем путь venv в PATH, чтобы Python из venv использовался по умолчанию
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY ina219.py /app/ina219.py
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]