![GitHub](https://img.shields.io/github/license/nikolak/speedtest-exporter)
[![Build Status](https://travis-ci.org/nikolak/speedtest-exporter.svg?branch=master)](https://travis-ci.org/nikolak/speedtest-exporter)
![Docker Pulls](https://img.shields.io/docker/pulls/nikolak/speedtest-exporter)


This is a very basic prometheus speedtest docker image, best used with prometheus.

Query `speedtest_exporter:9102/metrics` and speedtest gets run, which returns download/upload speed in kb/s.

The underlying speedtest is done using https://github.com/sivel/speedtest-cli

Docker compose example:

```yaml
version: "2.4"

services:
  speedtest_exporter:
    image: nikolak/speedtest-exporter:latest
    container_name: speedtest_exporter
    restart: unless-stopped
```

And the prometheus scrape config:

```yaml
  - job_name: "speedtest_exporter"
    scrape_interval: 3m
    scrape_timeout: 1m
    metrics_path: /metrics
    static_configs:
      - targets: ["speedtest_exporter:9102"]
```