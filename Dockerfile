FROM centos:6.9
LABEL maintainer vasanth3g@gmail.com
RUN yum install httpd  epel-release wget zip unzip php php-mysql php-mbstring php-mcrypt curl pip soap php-devel php-gd php-soap php-mcrypt  cakephp -y
ENTRYPOINT ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
EXPOSE 80


