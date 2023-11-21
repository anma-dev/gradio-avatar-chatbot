FROM python:3.10-slim
WORKDIR /code
RUN pip install gradio
CMD ["python", "-u", "app.py"]
