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
node1.addService(pg.Execute(shell="sh", command="mkdir /local/repository/HELLO"))
node2.addService(pg.Execute(shell="sh", command="mkdir /local/repository/HELLO"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
