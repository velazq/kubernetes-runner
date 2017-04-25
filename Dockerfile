FROM debian

RUN apt update && apt -y upgrade && apt install -y python3-pip curl init-system-helpers iptables libapparmor1 libltdl7 libnfnetlink0 libxtables10 nano
RUN curl https://download.docker.com/linux/debian/dists/jessie/pool/stable/amd64/docker-ce_17.03.1~ce-0~debian-jessie_amd64.deb -o /tmp/docker.deb
RUN dpkg -i /tmp/docker.deb
RUN pip3 install celery[redis] docker
RUN mkdir /tmp/data

COPY *.py /
COPY *.sh /
WORKDIR /