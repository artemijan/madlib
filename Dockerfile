FROM python:3.10-slim

LABEL owner="Artem Fedorov"
LABEL author.name="Artem Fedorov"
LABEL authot.email="lineartem@gmail.com"
LABEL version="1.0"

ARG USERNAME=app
ARG USER_UID=1000
ARG USER_GID=$USER_UID


# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME


USER $USERNAME
RUN mkdir -p /home/$USERNAME/app
WORKDIR /home/$USERNAME/app
ENV PORT=8080
COPY ./requirements.txt $WORK_DIR/

RUN pip install --no-cache-dir -r $WORK_DIR/requirements.txt

COPY . $WORK_DIR


EXPOSE $PORT



CMD ["python","-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
