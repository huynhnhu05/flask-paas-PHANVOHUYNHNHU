from flask import Flask
import datetime
import platform

app = Flask(__name__)


@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Flask PaaS Demo</title>
        <style>
            body {{
                font-family: Arial;
                max-width: 640px;
                margin: 60px auto;
            }}

            .box {{
                background: #DEAEF1;
                border-left: 5px solid #F14E79;
                padding: 24px;
                border-radius: 8px;
            }}

            h1 {{
                color: #4F46E5;
            }}
        </style>
    </head>

    <body>
        <h1>Ứng dụng Flask trên PaaS - phiên bản 2</h1>

        <div class="box">
            <p><b>Sinh viên:</b>PHAN VO HUYNH NHU - 233404050199</p>
            <p><b>Môn học:</b> Điện toán Đám mây</p>
            <p><b>Mô hình:</b> PaaS - Platform as a Service</p>
            <p><b>Python:</b> {platform.python_version()}</p>
            <p><b>Thời gian server:</b> {datetime.datetime.now()}</p>
        </div>

        <p>
            Developer chỉ viết code – PaaS lo build, deploy,
            HTTPS, scaling!
        </p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)