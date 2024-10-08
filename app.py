from flask import Flask, request, render_template # type: ignore
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 从表单获取数据
        input_data = {
            'ap': float(request.form['ap']),
            'crp': float(request.form['crp']),
            'ca': float(request.form['ca']),
            'ggt': float(request.form['ggt']),
            'tp': float(request.form['tp']),
            'ab': float(request.form['ab']),
            'gc': float(request.form['gc']),
            'nab': float(request.form['nab']),
        }

        # 调用已部署的模型 API
        response = requests.post('https://nhanes-production.up.railway.app/predict', json=input_data)

        # 检查响应状态
        response.raise_for_status()

        # 获取模型预测结果
        prediction = response.json()

    except requests.exceptions.RequestException as e:
        return f"Error: {e}", 500
    except ValueError as e:
        return f"Invalid input: {e}", 400

    # 返回预测结果到页面
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
