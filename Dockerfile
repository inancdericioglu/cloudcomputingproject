FROM python:3.7-alpine
WORKDIR /myapp
COPY . /myapp
RUN pip install -U -r requirements.txt
RUN pip install requests
RUN pip install jsonify
EXPOSE 80
CMD ["python", "app.py"]
