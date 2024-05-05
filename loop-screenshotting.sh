#!/bin/bash
# loop-screenshotting.sh

tmux new-session -d -s screenshotSession 'while true; do node ./lib/capture-screenshots.js; sleep 1800; done'

#re-attach with tmux attach-session -t screenshotSession
#detach with ctrl+b d
