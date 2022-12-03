#!/usr/bin/env python3

import subprocess
import json

all_apps_cmd = '''
yabai -m query --windows --space | jq '.[] | {app: .app, pid: .pid, index: ."stack-index", sticky: ."is-sticky"} | select(.sticky == false)' | jq -s 'sort_by(.index)'
'''
apps = subprocess.run(all_apps_cmd, capture_output=True, shell=True, text=True).stdout
apps = json.loads(apps)

current_pid_cmd = '''
yabai -m query --windows --window | jq '.pid'
'''
current_pid = subprocess.run(current_pid_cmd, capture_output=True, shell=True, text=True)
current_pid = int(current_pid.stdout)

display = []
for (idx, app) in enumerate(apps):
    app_name = app["app"]
    if app["pid"] == current_pid:
        app_name = '*' + app_name
    display.append(app_name)

labels = ' | '.join(display)
subprocess.run('sketchybar -m --set title label="{}"'.format(labels), shell=True)
