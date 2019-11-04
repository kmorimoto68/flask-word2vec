FROM python:3.6

ARG project_directory
WORKDIR $project_directory

RUN pip install flask
RUN pip install flask-cors
RUN pip install gensim==3.7.0
RUN pip install numpy
