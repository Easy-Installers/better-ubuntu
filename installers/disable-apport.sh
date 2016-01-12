#!/bin/bash

sudo sh -c 'echo "# set this to 0 to disable apport, or to 1 to enable it
# you can temporarily override this with
# sudo service apport start force_start=1
enabled=0" >> /etc/default/apport'
