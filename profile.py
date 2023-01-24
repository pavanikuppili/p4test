# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node1 = request.RawPC("node1")
node2 = request.RawPC("node2")

link = request.Link(members = [node1, node2])

# Install and execute a script that is contained in the repository.
node1.addService(pg.Execute(shell="sh", command="sudo apt-get update -y && sudo apt-get install libxml2-dev pkg-config -y && sudo git -C /root/ clone https://gitlab.flux.utah.edu/amaricq/SLANG-probed.git && sudo autoreconf -i /root/SLANG-probed/ && (sudo bash -c "cd /root/SLANG-probed ; ./configure && make")"))
node2.addService(pg.Execute(shell="sh", command="sudo apt-get update -y && sudo apt-get install libxml2-dev pkg-config -y && sudo git -C /root/ clone https://gitlab.flux.utah.edu/amaricq/SLANG-probed.git && sudo autoreconf -i /root/SLANG-probed/ && (sudo bash -c "cd /root/SLANG-probed ; ./configure && make")")) 

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)



