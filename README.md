# internet-speed
[![license](https://img.shields.io/badge/license-GPL3-brightgreen.svg)](https://github.com/asonnino/internet-speed/blob/master/LICENSE)

Automatically measure and plot average internet speed. 

## Install & Run
First, install [speedtest-cli](https://github.com/sivel/speedtest-cli) as described [here](https://github.com/sivel/speedtest-cli#installation), and give appropriate permissions to the script `speedtest.sh`:
```
$ chmod +x speedtest.sh
```
Set a `cron` job to regularly trigger the script. For instance, if your script is located in `/root` and you want to trigger it hourly, you can add the following line to your crontab:
```
@hourly bash /root/speedtest.sh
```
Data will be collected in a file called `speedtest.json` in the same directory as the script.

## Plot the average speed
You can run the Matlab script `script.mlx` to plot the average internet speed versus the hours of the day. You can edit the script to set the theoretical download & upload speed as below:
```
% download theoretical speed
th_download = 20;
% upload theoretical speed
th_upload = 1;
```

## License
[The GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html)