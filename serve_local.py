from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Timer
import webbrowser


HOST = "127.0.0.1"
PORT = 8765


def open_bookshop():
    webbrowser.open(f"http://{HOST}:{PORT}/")


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"松间诗词书房已启动：http://{HOST}:{PORT}/")
    print("关闭此窗口即可停止服务。")
    Timer(0.7, open_bookshop).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
