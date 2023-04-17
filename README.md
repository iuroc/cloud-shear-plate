# 云剪切板

> 多用户，全匿名，自动保存

- 作者：欧阳鹏
- 开发日期：2023 年 4 月 18 日

## 功能展示

- 使用 SQLite3 存储数据，简单方便
- 为剪切板分配 ID，可大量创建剪切板
- 记录 Cookie，让每台设备保持固定 ID
- 采用节流算法，优化前后端交互
- 采用深色背景，舒适护眼
- 增大行距和字间距，优化阅读体验
- 自动保存，并实时提示“保存成功”
- 后端使用 Python + Flask，部署简单便捷
- 支持 Docker 部署

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
    docker run -p 5000:5000 -d cloud-shear-plate
    rm -rf cloud-shear-plate
    ```

部署成功后，可以通过 5000 端口进行访问。