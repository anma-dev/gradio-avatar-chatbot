FROM python:3.10-slim
RUN pip install gradio
CMD ["python", "-u", "app.py"]
