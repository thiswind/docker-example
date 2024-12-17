# 使用官方的Python基础镜像
FROM python:3

# 设置工作目录
WORKDIR /app

# 复制本地的src目录到镜像中
COPY ./src /app/src

# 安装依赖
RUN pip install --no-cache-dir -r /app/src/requirements.txt

# 暴露端口
EXPOSE 5000

# 运行Flask应用
CMD ["python", "/app/src/app.py"]