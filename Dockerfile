FROM busybox:1.31.1
WORKDIR /root/lab/
COPY src ./src
COPY test ./test
