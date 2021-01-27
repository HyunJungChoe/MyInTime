FROM python:3.6

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY pjt_MyInTime/ .

CMD ["python", "manage.py", "runserver", "0:8000"]
