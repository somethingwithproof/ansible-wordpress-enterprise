# Development controller for supported Ubuntu and Rocky Linux targets.
ARG BASE_IMAGE=ubuntu:24.04
# Docker CLI 29.8.2, pinned by digest.
FROM docker@sha256:b1805116a6a86cc591b5d5f60a910a0715cdcc9d18d866ad68b1457ead25c35c AS docker-cli
FROM ${BASE_IMAGE}

LABEL maintainer="Thomas Vincent <thomasvincent@users.noreply.github.com>"
LABEL description="WordPress Enterprise Ansible development controller"
ENV DEBIAN_FRONTEND=noninteractive LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH="/opt/ansible/bin:$PATH"

# Molecule's community.docker.docker connection runs the Docker CLI.
COPY --from=docker-cli /usr/local/bin/docker /usr/local/bin/docker
COPY requirements.lock requirements.yml /tmp/dependencies/
RUN if [ -f /etc/debian_version ]; then \
        apt-get update && apt-get install -y --no-install-recommends \
            ca-certificates curl git gnupg lsb-release python3-apt python3.12 \
            python3.12-venv sudo systemd systemd-sysv wget && \
        rm -rf /var/lib/apt/lists/*; \
    elif [ -f /etc/redhat-release ]; then \
        dnf install -y ca-certificates curl-minimal git python3.12 python3.12-pip sudo systemd wget && \
        dnf clean all; \
    else exit 1; fi && \
    python3.12 -m venv /opt/ansible && \
    python -m pip install --no-cache-dir --require-hashes --only-binary=:all: \
        -r /tmp/dependencies/requirements.lock && \
    ansible-galaxy collection install -r /tmp/dependencies/requirements.yml \
        -p /usr/share/ansible/collections && \
    useradd -m -s /bin/bash ansible && \
    echo "ansible ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ansible && \
    chmod 0440 /etc/sudoers.d/ansible && \
    mkdir -p /workspace && chown ansible:ansible /workspace

WORKDIR /workspace
COPY --chown=ansible:ansible defaults/ defaults/
COPY --chown=ansible:ansible handlers/ handlers/
COPY --chown=ansible:ansible meta/ meta/
COPY --chown=ansible:ansible molecule/ molecule/
COPY --chown=ansible:ansible tasks/ tasks/
COPY --chown=ansible:ansible templates/ templates/
COPY --chown=ansible:ansible tests/ tests/
COPY --chown=ansible:ansible vars/ vars/
COPY --chown=ansible:ansible requirements.txt requirements.lock requirements.yml .ansible-lint .yamllint /workspace/
USER ansible
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python --version && ansible --version || exit 1
CMD ["/bin/bash"]
