# Copyright (c) 2023 kk
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

docker compose up -d --force-recreate

# wait container ready
sleep 10

# install pip dependencies
cat ./requirements.txt | while read line; do
  docker exec chatops-opsdroid-1 pip install $line
done

docker compose restart
