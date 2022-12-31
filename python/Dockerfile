FROM python:3

#Upgrade pip
RUN pip install --upgrade pip

#コンテナで/codeディレクトリ作成
RUN mkdir /code
#作業ディレクトリ
WORKDIR /code

#requirements.txtをコンテナにコピー
COPY requirements.txt /code/

#requirements.txtに書かれているパッケージをインストール
RUN pip install -r requirements.txt

# opencv-devのインストール
RUN apt-get update -y && apt-get install -y libopencv-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*




