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

-   SVG is more than 10000x10000
-   Loop for screenshot stitching, converting to svg and worst traffic png
-   Script for calculating number of traffic pixels per 30 mins
-   Script to get weather data for the period
-   Script to combine to json
-   background map image
-   UI (probably separate repo)
