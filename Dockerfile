FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY inmation_script.py .
EXPOSE 8000

CMD ["python", "inmation_script.py"]