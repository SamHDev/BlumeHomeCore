import subprocess

text = """
[Unit]
Description=BlumeHome Daemon
Wants=network-online.target
After=network.target

[Service]
Type=simple
ExecStart=/home/blume/

StandardOutput=console

[Install]
WantedBy=multi-user.target
"""