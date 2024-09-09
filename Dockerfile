# 使用Python官方的轻量镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . .

# 安装依赖
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 暴露Flask默认的运行端口
EXPOSE 5000

# 启动Flask应用
CMD ["flask", "run", "--host=0.0.0.0"]
