# Use an official Apache HTTPD image as the base
FROM httpd:latest

# install nodejs
RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_20.x  | bash -
RUN apt-get -y install nodejs

# mount the frontend & copy all files
WORKDIR /fe
COPY ../../frontend/stanafra/ /fe/

# build the web app
RUN npm install
RUN npm run build

# copy distribution files to apache loc
RUN cp -r dist/* /usr/local/apache2/htdocs/

# port 80
EXPOSE 80


CMD ["httpd", "-D", "FOREGROUND"]