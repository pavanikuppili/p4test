import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# Create two raw "PC" nodes
node1 = request.RawPC("node1")
node2 = request.RawPC("node2")


link1 = request.Link(members = [node1, node2])

node1.addService(rspec.Install(url="https://github.com/PavaniKRao/p4test/blob/main/pr.sh", path="/root"))
node2.addService(rspec.Install(url="https://github.com/PavaniKRao/p4test/blob/main/pr.sh", path="/root"))
#node1.addService(rspec.Execute(shell="sh", command="/local/repository/pr.sh"))
#node2.addService(rspec.Execute(shell="sh", command="/local/repository/pr.sh"))

portal.context.printRequestRSpec()
