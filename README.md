# 云剪切板

> 多用户，全匿名，自动保存

- 作者：欧阳鹏
- 开发日期：2023 年 4 月 18 日

## 安装部署

- 普通方式

    ```bash
    git clone https://github.com/oyps/cloud-shear-plate
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    pip install flask
    flask run --host=0.0.0.0
    ```
- Docker 方式

    ```
    git clone https://github.com/oyps/cloud-shear-plate
    docker build -t cloud-shear-plate cloud-shear-plate
    docker run -p 3005:5000 cloud-shear-plate
    ```