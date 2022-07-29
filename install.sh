# /usr/bin/bash
if [ -e /etc/systemd/system/analyze-corner.service ]; then
    sudo rm -r /etc/systemd/system/analyze-corner.service
fi

if [ -e /opt/AnalyzeCorner ]; then
    sudo rm -r /opt/AnalyzeCorner/
fi

sudo cp -r . /opt/AnalyzeCorner
sudo cp ./analyze-corner.service /etc/systemd/system/

sudo chmod 755 /opt/AnalyzeCorner/app.py

sudo systemctl enable analyze-corner.service
