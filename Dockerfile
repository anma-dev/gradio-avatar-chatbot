FROM python:3.10-slim
WORKDIR /code
RUN pip install gradio, base64
CMD ["python", "-u", "app.py"]
