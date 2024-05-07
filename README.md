# Requirements

-   Imagemagick, potrace, hugin for the smartstich (though this doesn't currently work well)
-   Playwright, playwright dependencies - `npx playwright install-deps && npx playwright install`
-   Node > 18.something
-   tmux to run in the background
-   I needed more than 1GB of RAM to run the screenshotting script
-   I'm running with the cheapest 4GB Digital Ocean droplet. It may be possible to get away with 2GB, but I haven't tried.

# Getting started

-   Install the requirements
-   Run `yarn install`
-   Run `./background-yarn-dev.sh`
-   Run `./loop-screenshotting.sh`

# TODO

-   Script to get weather data for the period
-   Script to combine with traffic to json
-   background map image
-   UI (probably separate repo)

# TODO later

-   traffic as percentage of roads - stiched but not filtered has green

# Example crontab

```
# Run on the half hour
# m h  dom mon dow   command
0,30 * * * * cd /root/traffic-flood && /root/.nvm/versions/node/v20.12.2/bin/node ./lib/capture-screenshots.js >> /root/traffic-flood/logs/capture-screenshots.log 2>&1
#for testing
#* * * * * cd /root/traffic-flood && /root/.nvm/versions/node/v20.12.2/bin/node ./lib/capture-screenshots.js >> /root/traffic-flood/logs/capture-screenshots.log 2>&1
```
