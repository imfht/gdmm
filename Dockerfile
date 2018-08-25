FROM frolvlad/alpine-python3
RUN pip3 install flask gunicorn
COPY ./ /app
CMD ["gunicorn","-w 4 -b 0.0.0.0:4000","app:app"]
