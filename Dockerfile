FROM cloudacademydevops/ide:python37
RUN apk add --update make
WORKDIR /root/lab/
COPY src ./src
COPY test ./test
