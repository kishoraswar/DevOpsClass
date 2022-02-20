FROM centos:latest
MAINTAINER kishor aswar
RUN yum install –y httpd\
      zip \
      unzip
ADD https://www.free-css.com/assets/files/free-css-templates/download/page274/arizona.zip /var/www/html
WORKDIR /var/www/html
RUN unzip Arizona.zip 
RUN cp –rvf Arizona/* .
RUN rm –rf Arizona.zip
CMD [“/usr/sbin/httpd”, “-D”, “FOREGROUND”]
EXPOSE 80



