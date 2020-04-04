This is a very basic prometheus speedtest docker image, best used with prometheus.

Query `speedtest_exporter:9102/metrics` and speedtest gets run, which returns download/upload speed in kb/s.

The underlying speedtest is done using https://github.com/sivel/speedtest-cli