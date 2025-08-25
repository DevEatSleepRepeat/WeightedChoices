#!/bin/bash
exec /usr/bin/osascript -e '
tell application "Terminal"
    do script "'"clear"'"
    do script "'"/Applications/WeightedChoicesBE.app/Contents/MacOS/main"'"
    activate
end tell'
