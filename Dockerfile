FROM python
ADD . /src
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install flask
WORKDIR /src
CMD ["flask", "run", "--host=0.0.0.0"]