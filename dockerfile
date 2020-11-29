FROM python:3.6-slim-stretch

LABEL THE SIMPLE COMPANY <sales@simplecompany.io>

ENV CHROME_DRIVER_VERSION 2.42
ENV CHROME_DRIVER_TARBALL http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip

RUN \
    echo "==> [1/5] Instalando actualizaciones faltantes: (python:3.6-slim-stretch) ... "   && \
    apt-get update            && \
    apt-get install -y --no-install-recommends \
        gnupg   \
        dirmngr \
        wget    \
        ca-certificates               && \
        rm -rf /var/lib/apt/lists/*   && \
    \
    \
    echo "==> [2/5] Descargando Google Chrome ... "  && \
    wget -q -O- https://dl.google.com/linux/linux_signing_key.pub | apt-key add -  && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google.list  && \
    \
    \
    echo "==> [3/5] Instalando dependencias ... "   && \
    apt-get update            && \
    apt-get install -y --no-install-recommends \
        python3-dev              \
        python3-pip              \
        google-chrome-stable  && \
    \
    \
    echo "==> [4/5] Instalando Chromedriver ... "  && \
    wget -qO- $CHROME_DRIVER_TARBALL | zcat > /usr/local/bin/chromedriver  && \
    chown root:root /usr/local/bin/chromedriver  && \
    chmod 0755 /usr/local/bin/chromedriver       && \
    \
    echo "==> [5/5] Finalizando  :) "      && \
    rm -rf /var/lib/apt/lists/*


ENV PATH /usr/lib/chromium/:$PATH

WORKDIR    /behave
ENV        REQUIREMENTS_PATH  /behave/features/steps/requirements.txt

COPY . .
ENTRYPOINT ["./main.sh"]
