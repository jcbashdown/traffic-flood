# Description

This app is intended to gather data to determine the impact of heavy rains on mobility in a given city (currently Nairobi).

The motivation was to better understand some of the impacts of the heavy rains in Nairobi in April-Early May 2024 using a much simpler approach than traditional flood risk mapping (where we would combine topographic, hydrological, remote sensing etc. data to understand flood risk.) by using a potential proxy. While traffic data may not be an ideal proxy it's much quicker and cheaper to implement using easily accessible data though there are obvious downsides:

-   Traffic data is generally much more available for major roads. Roads through the worst hit areas such as informal settlements are not covered.
-   It's heavily influenced by the quality of infrastructure. A well build road in a nevertheless vulnerable area may never show traffic effects and so any attempt to draw out statistical conclusions would be flawed in some areas. An example in Nairobi is Red Hill link road running over Peponi ridge. Peponi ridge and areas of spring valley were very badly effected by the rain but this large highway passing through the area remained largely traffic free.

# Approach

-   Gather traffic data from the API
    -   Use a local next app with rendering a map with a traffic overlay and the background map hidden
    -   Take screenshots with playwright.
    -   In large areas it's necessary to take multiple screenshots at a good zoom level and stitch them together as the map loads unreliably if you make the map area too large.
-   Filter the images to only the worse traffic (ignoring green and orange)
-   Count the pixels in the filtered image. What proportion of the image is traffic?
    -   A better approach would be to count the traffic as a proportion of the roads with traffic data. Planning this approach as a future improvement
    -   This approach is very slow but counting the area of the svg isn't working well because of double counting in my initial approach
        -   I just want to get something working quickly for now
-   Convert the PNGs of heavy traffic to svg for later use as a map overlay
-   Gather weather data from the the Visual Crossing API (because the data we need is free (the api is not great))
-   Combine weather data with traffic.
    -   Examples of the the final output are in the `final_images/svgs` directory and in `final_json/combined_data.json`

## In [the ui repo](https://github.com/jcbashdown/traffic-flood-ui)

-   Create a simple UI to display the data
    -   One sparkline for rainfall and another for traffic with a slider to move through time
    -   An openstreemap pane using leaflet with the traffic overlayed on top. The slider moved through the svgs and shows the traffic and rainfall for that time in the sparklines

# Requirements

-   Imagemagick, potrace, hugin for the smart stitch (though this doesn't currently work well)
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
rsync -avz --progress user@remote_host:/path/to/traffic-flood/output_images/* /path/to/traffic-flood/output_images/.

```

# Python setup

-   setup a virtual environment
-   run `pip install -r requirements.txt`
-   activate it

# Data processing:

Once you have the latest images

0. Ensure python is setup as above
1. Adjust the dates in `get_hourly_precip_mm.py` based on the range of traffic data you have gathered and get the rain. Note - this will give you forecast data if you set a date in the future:

```
python get_hourly_precip_mm.py <2024-05-10> <2024-05-15> hourly_precip_mm.json
```

2. Process the images to get traffic svgs and pngs:

```
./create-all-traffic-svgs.sh
```

3. Get the traffic (note, this is very slow):

```
python ./calculate_traffic_percentages_from_png.py traffic_history_full.json
```

4. Combine the data into the file in the ui repo:

```
python data_processing/combine_rain_and_traffic_data.py > /path/to/traffic-flood-ui/fixtures/combined_data.json
```

5. Copy the images to the ui repo:

```
cp -r final_images/svgs/ /path/to/traffic-flood-ui/public/
```

6. Commit the changes in that repo. Build the static export (`yarn build`) and deploy

# Python tests:

-   run `python -m pytest`

# TODO

-   Work out if precip is accumulation up to hour, 30 mins either side? after? May have to work this our from traffic effects

# TODO tidying

-   Add licence

# TODO later

-   traffic as percentage of roads - stiched but not filtered has green to calc 100%
-   Further interesting data - svgs for day of week averages. Time of day. Rainfall level. Worst roads. Analysis of the difference between rain traffic and normal traffic - which roads are most effected vs a baseline
-   dockerize
-   use .env for location of weather and traffic images

# Notes

-   I've confirmed the weather api is giving rain in mm and timestamps in local time which I'm converting to UTC
