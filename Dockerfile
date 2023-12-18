FROM python:3.9

WORKDIR /workspace

COPY ./requirements.txt /workspace/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /workspace/requirements.txt

VOLUME /workspace/app/
#COPY ./app /workspace/app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
#--reload: faz com que o servidor restarte após mudanças no código. Usar somente durante o desenvolvimento