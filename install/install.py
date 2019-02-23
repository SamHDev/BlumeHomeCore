import subprocess

text = """
[Unit]
Description=BlumeIOT Device Daemon
Wants=network-online.target
After=network.target

[Service]
Type=simple
ExecStart=/home/blume/

StandardOutput=console

[Install]
WantedBy=multi-user.target
"""

f = open("/etc/systemd/system/blume.service","w")
f.write(text)
f.close()