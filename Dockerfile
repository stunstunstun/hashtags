FROM python:3
LABEL maintainer="stunstunstun <minhyeok.jung85@gmail.com>"

COPY . /nicolas
WORKDIR /nicolas

RUN pip install pipenv
RUN pipenv install --deploy --dev

ENV SHELL=/bin/bash
ENTRYPOINT ["pipenv", "run"]
CMD [ "python", "-m", "unittest" ]
