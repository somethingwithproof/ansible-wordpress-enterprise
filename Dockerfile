# Dockerfile for testing Ansible WordPress Enterprise role
# Supports both Ubuntu and RHEL-based distributions

ARG BASE_IMAGE=ubuntu:22.04
FROM ${BASE_IMAGE}

LABEL maintainer="Thomas Vincent <thomasvincent@users.noreply.github.com>"
LABEL description="Docker image for testing WordPress Enterprise Ansible role"
LABEL version="1.0.0"

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Install system dependencies based on OS family
RUN if [ -f /etc/debian_version ]; then \
        apt-get update && \
        apt-get install -y --no-install-recommends \
            python3 \
            python3-pip \
            python3-apt \
            sudo \
            systemd \
            systemd-sysv \
            curl \
            wget \
            ca-certificates \
            gnupg \
            lsb-release \
            openssh-server && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*; \
    elif [ -f /etc/redhat-release ]; then \
        yum install -y \
            python3 \
            python3-pip \
            sudo \
            systemd \
            curl \
            wget \
            ca-certificates \
            openssh-server && \
        yum clean all; \
    fi

# Install Ansible and required collections
RUN pip3 install --no-cache-dir \
        'ansible>=2.15' \
        ansible-lint \
        molecule \
        molecule-plugins[docker] \
        pytest \
        pytest-testinfra \
        yamllint

# Install Ansible collections
RUN ansible-galaxy collection install community.general && \
    ansible-galaxy collection install community.mysql && \
    ansible-galaxy collection install ansible.posix

# Create ansible user with sudo privileges
RUN useradd -m -s /bin/bash ansible && \
    echo "ansible ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ansible && \
    chmod 0440 /etc/sudoers.d/ansible

# Setup SSH for testing
RUN mkdir -p /var/run/sshd && \
    ssh-keygen -A

# Create workspace
WORKDIR /workspace

# Copy role files
COPY . /workspace/

# Set proper permissions
RUN chown -R ansible:ansible /workspace

# Switch to ansible user
USER ansible

# Set working directory
WORKDIR /workspace

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python3 --version && ansible --version || exit 1

CMD ["/bin/bash"]
