# Internet Speed Test Web App

This is a simple web application that allows users to check their internet speed. It fetches speed data from a server and displays the download speed, upload speed, and ping. The app uses a Python backend to serve the speed test results.

## Features
- Check internet speed by clicking a button.
- Displays download speed, upload speed, and ping.
- Button disables while fetching data and re-enables once the test completes.
- Error handling in case of network issues.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript (Async/Await, Fetch API)
- **Backend**: Python (Flask)
- **Speed Test Library**: `speedtest-cli` (for Python)

## Setup

### 1. Frontend Setup

Clone the repository and open `index.html` in your browser to view the app:

```bash
git clone https://github.com/tahsinzidane/NetSpeedTest.git
```

Make sure the frontend is served from a web server or opened directly in your browser. Ensure that the frontend's fetch request URL points to the correct backend server.

### 2. Backend Setup (Python Server)

To run the Python backend, you need Python installed on your system. Follow the steps below to set up and run the server.

#### Step 1: Install Python and Dependencies

Ensure Python is installed on your system (preferably Python 3.6+). Then, install the required libraries.

1. **Install Flask**:
   ```bash
   pip install flask
   ```

2. **Install speedtest-cli**:
   ```bash
   pip install speedtest-cli
   ```

#### Step 2: Create the Backend Server

Create a new Python file (e.g., `app.py`) with the following content to set up the backend:

```python
from flask import Flask, jsonify
import speedtest

app = Flask(__name__)

@app.route('/api/speed-test', methods=['GET'])
def speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert from bits to megabits
        upload_speed = st.upload() / 1_000_000  # Convert from bits to megabits
        ping = st.results.ping
        return jsonify({
            'download_speed': round(download_speed, 2),
            'upload_speed': round(upload_speed, 2),
            'ping': ping
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

This Flask app provides an API endpoint (`/api/speed-test`) that uses the `speedtest-cli` library to fetch the current internet speed and returns it in JSON format.

#### Step 3: Run the Server

To start the backend server, run the following command in your terminal:

```bash
python app.py
```

The server will start running on `http://127.0.0.1:5000`. Make sure that the frontend app is configured to fetch data from this URL.

### 3. Running the Full Application

- Ensure the Python server is running (`python app.py`).
- Open the frontend `index.html` in your browser or host it on any web server.
- Click the "Check Speed" button to initiate the speed test and view the results.

## Example API Response
```json
{
  "download_speed": 50.12,
  "upload_speed": 10.45,
  "ping": 20
}
```

## License
This project is open-source and available under the MIT License.