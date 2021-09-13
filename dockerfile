FROM python:3.8
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt true_sphere/requirements.txt
WORKDIR /true_sphere
RUN pip install -r requirements.txt
COPY . /true_sphere
ENTRYPOINT [ "python3" ]
CMD [ "gradient_testing.py" ]