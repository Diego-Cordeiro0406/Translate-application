FROM python:3-alpine3.17

WORKDIR /translate-project

COPY *requirements.txt ./

RUN apk update && apk add git
RUN python3 -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

ARG FLASK_ENV
RUN if [ "$FLASK_ENV" = "dev" ] ; then pip install --no-cache-dir -r dev-requirements.txt  ; fi

COPY . .

CMD ["python3", "src/app.py"]
