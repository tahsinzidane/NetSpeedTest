from flask import Flask, jsonify
from flask_cors import CORS
import speedtest

app = Flask(__name__)
CORS(app)  

@app.route('/api/speed-test', methods=['GET'])
def check_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  
    upload_speed = st.upload() / 1_000_000      
    ping = st.results.ping

    # Return the results as JSON
    return jsonify({
        'download_speed': f"{download_speed:.2f} Mbps",
        'upload_speed': f"{upload_speed:.2f} Mbps",
        'ping': f"{ping} ms"
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
