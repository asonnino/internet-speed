#!/bin/bash
speedtest-cli --share --json --secure  >> ./speedtest.json
echo ',' >> ./speedtest.json