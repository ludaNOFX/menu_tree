FROM python:3.10-buster

RUN useradd LUDA_API

WORKDIR /home/LUDA_API

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY luda_menu_tree luda_menu_tree
COPY manage.py ./

COPY boot.sh ./
RUN chmod a+x boot.sh

RUN chown -R LUDA_API:LUDA_API ./

USER LUDA_API

EXPOSE 8000

ENTRYPOINT ["./boot.sh"]