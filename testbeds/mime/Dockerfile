FROM debian:12
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en

RUN  apt-get update \
      && apt-get install -y sudo wget vim 

# Install php
RUN apt install -y php-cli php-zip unzip php8.2-mailparse
RUN wget -O composer-setup.php https://getcomposer.org/installer
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer

# Install dotnet
RUN wget https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb
RUN apt update && apt install -y dotnet-sdk-9.0
RUN dotnet workload update

# Install nodejs, npm 
RUN apt install nodejs npm -y

# Install python pip
RUN apt install python3-pip -y

# Install mvn
RUN apt install maven -y


ARG USER_ID=1000

RUN mkdir -p /home/user  && \
	useradd -l -u ${USER_ID} -K UMASK=0000 user

RUN	echo "user:user" | chpasswd && usermod -a -G sudo user && \
    echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN chown -R user:user /home/user

USER user
COPY --chown=user:user parsers/ /home/user/parsers/

WORKDIR /home/user/parsers

# Install parsers dependencies
RUN cd /home/user/parsers/javascript/postal-mime-parser && npm install
RUN pip install --break-system-packages standard-imghdr mail-parser flanker
RUN cd /home/user/parsers/java/apache-common-parser && mvn package
RUN cd /home/user/parsers/csharp/mimekit-parser && dotnet build
RUN cd /home/user/parsers/php/php-mime-mail-parser && composer require php-mime-mail-parser/php-mime-mail-parser


