FROM ubuntu:latest
WORKDIR /pong_game


RUN apt-get update && apt-get install -y openssh-server   
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config


COPY create_users.sh /pong_game
# loop to add 20 players in team 1&2 and umpire
RUN bash create_users.sh

ENTRYPOINT /bin/bash