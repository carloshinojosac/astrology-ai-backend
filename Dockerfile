FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./ /app

EXPOSE 80
EXPOSE 8000

RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install tensorflow
RUN python3 -m pip install gpt-2-simple
RUN python3 -m pip install uvicorn
RUN python3 -m pip install fastapi

CMD ["uvicorn", "run_model:app", "--host", "0.0.0.0", "--port", "8000"]