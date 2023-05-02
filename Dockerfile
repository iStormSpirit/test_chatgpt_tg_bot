FROM python:3.10-alpine

ENV PYTHONFAULTHANDLER=1 \
     PYTHONUNBUFFERED=1 \
     PYTHONDONTWRITEBYTECODE=1 \
     PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apk --no-cache add ffmpeg

WORKDIR /telegram_gpt_bot
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

CMD ["python3", "main.py"]