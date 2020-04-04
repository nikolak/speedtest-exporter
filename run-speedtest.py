# #!/usr/local/bin/python

import sys
from wsgiref.simple_server import make_server

import speedtest
from prometheus_client import Gauge
from prometheus_client import make_wsgi_app

s = speedtest.Speedtest()

DOWNLOAD_SPEED = Gauge('speedtest_download', 'Speedtest download', unit="kbps")
UPLOAD_SPEED = Gauge('speedtest_upload', 'Speedtest upload', unit="kbps")
PING = Gauge('speedtest_ping', 'Speedtest ping', unit="ms")

metrics_app = make_wsgi_app()


def speedtest(environ, start_fn):
    if environ['PATH_INFO'] == '/metrics':
        print("Starting speedtest")
        try:
            s.get_best_server()
            s.download()
            s.upload()
            results_dict = s.results.dict()
            DOWNLOAD_SPEED.set(results_dict["download"] / 1000)
            UPLOAD_SPEED.set(results_dict["upload"] / 1000)
            PING.set(results_dict["ping"])
        except:
            print("Unexpected error:", sys.exc_info()[0])
        return metrics_app(environ, start_fn)
    start_fn('200 OK', [])


if __name__ == '__main__':
    httpd = make_server('', 9102, speedtest)
    httpd.serve_forever()
