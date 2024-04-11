#!/usr/bin/env bash

gitlab_host="http://10.0.0.102"
gitlab_token="CiscoAutomationUser"
runner_name="runner1"
runner_token="sandboxrunners"
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

echo ""
printf "Removing any stale runners..."
RUNNERS=$(/usr/bin/curl --silent \
            --request GET \
            --header "PRIVATE-TOKEN: ${gitlab_token}" \
            ${gitlab_host}/api/v4/runners/all | \
            /usr/bin/jq '.[].id')

for RUNNER in ${RUNNERS}; do
    /usr/bin/curl --request DELETE \
        --header "PRIVATE-TOKEN: ${gitlab_token}" \
        ${gitlab_host}/api/v4/runners/${RUNNER}
done
success

printf "Getting runner container name..."
runner_container=$(/usr/bin/docker compose ps --no-trunc --format=json | \
                       jq -s ".[] | select(.Service == \"${runner_name}\") | .Name" | \
                       tr -d '"')
success

printf "Registering CICD Runner..."
/usr/bin/docker exec -d ${runner_container} /usr/bin/gitlab-runner register \
  --url ${gitlab_host} \
  -r ${runner_token}
sleep 5
/usr/bin/docker exec -d ${runner_container} /usr/bin/gitlab-runner verify \
  --url ${gitlab_host} \
  -n ${runner_name} \
  --delete
success

printf "Waiting for runner to start..."
health_check_result=$(/usr/bin/curl --silent \
                          --request GET \
                          --header "PRIVATE-TOKEN: ${gitlab_token}" \
                          ${gitlab_host}/api/v4/runners/all | \
                          /usr/bin/jq '.[].status')

until [ $health_check_result = '"online"' ]; do
    health_check_result=$(/usr/bin/curl --silent \
                            --request GET \
                            --header "PRIVATE-TOKEN: ${gitlab_token}" \
                            ${gitlab_host}/api/v4/runners/all | \
                            /usr/bin/jq '.[].status')
    printf '.'
    sleep 10
done
success
