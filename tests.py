import requests


def test():
    for line in requests.get("http://localhost:9102/metrics").text.splitlines():
        if line.startswith("speedtest_"):
            print(line, float(line.split()[1]))
            assert float(line.split()[1]) > 0


if __name__ == '__main__':
    test()
