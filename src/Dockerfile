FROM python:3.9
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r infrastructure/requirements/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
EXPOSE 8000
CMD ["python", "app.py"]