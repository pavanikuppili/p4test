#! /bin/sh
sudo mv prnext.sh ../../root/ && sudo apt-get update && sudo apt-get install libxml2-dev pkg-config && sudo git -C ../../root/ clone https://gitlab.flux.utah.edu/amaricq/SLANG-probed.git && sudo chmod +x ../../root/prnext.sh && sudo /../../root/prnext.sh &&  sudo -i
