FROM debian@sha256:9cc080028c43b27d2074d63a5f9caf7166d731494965616c1a6d2827a004585c
# Exact .deb versions are included in the full release, not fetched from latest.
COPY vendor/lab-debs.tar.gz /tmp/lab-debs.tar.gz
RUN mkdir /tmp/debs && tar -xf /tmp/lab-debs.tar.gz -C /tmp/debs --strip-components=1 && \
    (DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/debs/*.deb || DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/debs/*.deb || DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/debs/*.deb) && rm -rf /tmp/debs /tmp/lab-debs.tar.gz && \
    useradd -m -s /bin/bash study && mkdir -p /run/sshd /study && chown study:study /study
COPY vendor/extra-debs/ /tmp/extra-debs/
RUN dpkg -i /tmp/extra-debs/*.deb && rm -rf /tmp/extra-debs
COPY --chown=study:study . /study
USER study
WORKDIR /study
RUN python3 scripts/prepare.py
CMD ["python3", "scripts/run-suite.py", "--smoke"]
