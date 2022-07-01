FROM python:3.7.2-alpine3.9
RUN apk add --no-cache \
    jq \
    curl \
    git \
    python
RUN apk add --no-cache python3-dev libstdc++ && \
    apk add --no-cache g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip3 install medium 


WORKDIR /app
ADD ./src /app
RUN chmod +x /app/app.py
ENTRYPOINT ["/app/app.py"]
