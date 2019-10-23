# from pyVim.connect import SmartConnect
from pyVim import connect
# from pyVmomi.VmomiSupport.v
import ssl
import re

cer = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
cer.verify_mode = ssl.CERT_NONE
# cert_ssl = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

# cert_ssl.verify_mode = ssl.CERT_NONE
'Connecting to Host'
# print help(connect)
si = connect.SmartConnect(host='172.30.60.89', user='root', pwd='p@ssw0rd',sslContext=cer)
# print type(si)
# print dir(si)

# print si._version
# print si.content
' Vcenter or Host inventory'
# inventory_cont = si.content
inventory = si.RetrieveContent()
# print "RetrieveContent:\n",inventory
# print "#############################"
# print "Content:\n",inventory_cont
# print type(inventory)
'Retrieve Datacenter '
dc1 = inventory.rootFolder.childEntity[0]
# print len(dc1)
print dc1.name
# print type(dc1)
# print dir(inventory.rootFolder)
'Here it gives vms as a object'
vms = dc1.vmFolder.childEntity
# print dir(dc1.vmFolder)
# print dir(dc1.vmFolder.childEntity)

print type(vms)
for vm in vms:
    # print vm.name
    # print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    ''' To Getting each VM states '''
    print "VM Name:{0} and power status of:{1} ".format(vm.name, vm.runtime.powerState)
    f = open("vm_summary.txt","r+")
    
    # vm.PowerOff()
    print "VM Name: {0} | power status: {1} | Fullname: {2} | VM path:{3} | UUID:{4}".format(vm.name, vm.runtime.powerState,vm.summary.config.guestFullName,vm.summary.config.vmPathName,vm.summary.config.uuid)
    if vm.name == 'UDS Server':
        ''' We can make poweroff/on vm '''
        # t = vm.PowerOn()
        vm.PowerOff()
        # print "############################################################"
        print "Vm is going to",vm.runtime.powerState
        # print "############################################################"
        print "VM going to Powerstatus: ",vm.runtime.powerState
        print "\nTemplate :",vm.summary.config.template
        print "\nVirtual Disk:",vm.summary.config.numVirtualDisks
        print "\nMemory: ",vm.summary.config.memorySizeMB
        print "\n We are going to template...",vm.summary.vm
   

        # pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        # s = str(vm.summary)
        # f.write(s)
        # filecontent = f.read()
        # print filecontent
        # pat = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        # pat = re.compile("^((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        # result= re.findall(pat,filecontent)
        # f1 = open('1.txt','w')
        # print type(result)
        # f1.write(str(result))
        # f.vm.summary
    # print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    # print "guestFullName: \n, NAme:\n", dir(vm.summary.config.guestFullName)
    # print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    # print "Vm path:\n", dir(vm.summary.config.vmPathName)
    # print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    # print "VM UUID:\n", dir(vm.summary.config.uuid)
    # print dir(vm)
    # print type(vm)