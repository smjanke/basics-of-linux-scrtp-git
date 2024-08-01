FROM ubuntu:latest
WORKDIR /pong_game


RUN apt-get update && apt-get install -y openssh-server   
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Now add umpire
RUN useradd -ms /bin/bash umpire;
RUN echo 'umpire:qwerty2000' | chpasswd
RUN chown -R umpire:umpire /pong_game;

COPY make_points.sh /pong_game

ENTRYPOINT /bin/bash /pong_game/make_points.sh