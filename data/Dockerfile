FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/migration

COPY ../doc.txt /usr/src/doc.txt
RUN pip install -r /usr/src/doc.txt

COPY .. /usr/src/migration

EXPOSE 5432
EXPOSE 3306
CMD ["python", "Test_migration.py"]