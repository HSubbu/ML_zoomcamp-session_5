FROM  agrigorev/zoomcamp-model:3.8.12-slim
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 9696
CMD python ./predict.py