FROM python:3.10

WORKDIR /financeapp

COPY financeapp/ .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM node:23 AS frontend-build

WORKDIR /frontend

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install

COPY frontend ./

RUN npm run build

EXPOSE 8000 3000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000 & cd /frontend && npm start"]
