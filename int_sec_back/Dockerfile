FROM ubuntu:22.04
RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker
RUN DEBIAN_FRONTEND=noninteractive && \
  apt-get update && \
  apt-get install -y python3 && \
  apt-get install -y pip && \
  apt-get install -y iputils-ping && \ 
  apt-get install -y openssh-server  && \
  apt-get install -y net-tools && \
  apt-get install -y dnsutils

WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]