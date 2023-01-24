import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# Create two raw "PC" nodes
node1 = request.RawPC("node1")
node2 = request.RawPC("node2")


link1 = request.Link(members = [node1, node2])

node1.addService(rspec.Execute(shell="sh", command="sudo mv prnext.sh ../../root/ && sudo apt-get update && sudo apt-get install libxml2-dev pkg-config && sudo git -C ../../root/ clone https://gitlab.flux.utah.edu/amaricq/SLANG-probed.git && sudo chmod +x ../../root/prnext.sh && sudo /../../root/prnext.sh &&  sudo -i"))
node2.addService(rspec.Execute(shell="sh", command="sudo mv prnext.sh ../../root/ && sudo apt-get update && sudo apt-get install libxml2-dev pkg-config && sudo git -C ../../root/ clone https://gitlab.flux.utah.edu/amaricq/SLANG-probed.git && sudo chmod +x ../../root/prnext.sh && sudo /../../root/prnext.sh &&  sudo -i"))

portal.context.printRequestRSpec()
