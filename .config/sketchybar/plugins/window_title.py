#!/usr/bin/env python3

import subprocess
import json

all_apps_cmd = '''
yabai -m query --windows --space \
| jq '.[] | {app: .app, id: .id, index: ."stack-index", sticky: ."is-sticky", minimized: ."is-minimized" } \
| select(.sticky == false and .minimized == false)' | jq -s 'sort_by(.index)'
'''
apps = subprocess.run(all_apps_cmd, capture_output=True, shell=True, text=True).stdout
apps = json.loads(apps)

current_id_cmd = '''
yabai -m query --windows --window | jq '.id'
'''
current_id = subprocess.run(current_id_cmd, capture_output=True, shell=True, text=True)
current_id = int(current_id.stdout)

display = []
for (idx, app) in enumerate(apps):
    app_name = app["app"]
    if app["id"] == current_id:
        app_name = '*' + app_name
    display.append(app_name)

labels = ' | '.join(display)
subprocess.run('sketchybar -m --set title label="{}"'.format(labels), shell=True)
