FROM kalilinux/kali-rolling

RUN apt update &&  \
    apt install -y python3.9 nmap wpscan && \
     rm -rf /var/lib/apt/lists/*
ENV URL http://localhost:8888/

WORKDIR /secu
# COPY script.py .
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]