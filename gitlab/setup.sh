#!/usr/bin/env bash

gitlab_host="http://10.0.0.102"
gitlab_wait_time=45
# prints colored text
success () {
    COLOR="92m"; # green
    STARTCOLOR="\e[$COLOR";
    ENDCOLOR="\e[0m";
    printf "$STARTCOLOR%b$ENDCOLOR" "done\n";
}

echo ""
printf "Launching Gitlab CE..."
/usr/bin/docker compose up -d 2> gitlab_setup.log
success

printf "Waiting for Gitlab CE to become available..."

until $(curl --output /dev/null --silent --head --fail ${gitlab_host}); do
    printf '.'
    sleep 10
done
success
