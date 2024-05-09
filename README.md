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
-   Run `./loop-screenshotting.sh` or set up a crontab (recommended)

# Example crontab

```
# Run on the half hour
# m h  dom mon dow   command
0,30 * * * * cd /root/traffic-flood && /root/.nvm/versions/node/v20.12.2/bin/node ./lib/capture-screenshots.js >> /root/traffic-flood/logs/capture-screenshots.log 2>&1
#for testing
#* * * * * cd /root/traffic-flood && /root/.nvm/versions/node/v20.12.2/bin/node ./lib/capture-screenshots.js >> /root/traffic-flood/logs/capture-screenshots.log 2>&1
```

# Example pull from server:

```
rsync -avz --progress user@remote_host:/home/user/remote_directory /home/local_user/local_directory

```

# Python tests:

-   setup a virtual environment
-   run `pip install -r requirements.txt`
-   activate it
-   run `python -m pytest`

# TODO

-   Script to combine weather with traffic with image names array to json
    -   Test drive. Work out if precip is accumulation before. Assign less frequent to more frequent.
        -   Find every unique timestamp. Assign traffic and image path and then most recent previous rain
-   better/more faded background map image
-   UI (probably separate repo)

# TODO tidying

-   Move python files to data processing directory and change them to still work
-   create image processing directory and move scripts there
-   create directory for json including intermediate formats
-   remove weather api key from git history
-   use .env for api keys
-   use .env for location of weather and traffic images

# TODO later

-   traffic as percentage of roads - stiched but not filtered has green
-   dockerize

# Notes

-   I've confirmed the api is giving rain in mm
