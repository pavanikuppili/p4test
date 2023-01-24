import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# Create two raw "PC" nodes
node1 = request.RawPC("node1")
node2 = request.RawPC("node2")


link1 = request.Link(members = [node1, node2])

node1.addService(rspec.Execute(shell="bash", command="pr.sh"))
node2.addService(rspec.Execute(shell="bash", command="pr.sh"))

portal.context.printRequestRSpec()
