FROM frolvlad/alpine-python3
ADD ./ /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["gunicorn","-w", "4", "-b", "0.0.0.0:4000","app:app"]
