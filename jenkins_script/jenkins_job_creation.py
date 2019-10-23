import jenkins
from jenkins import Jenkins
jenkins_server = Jenkins(url='http://18.221.129.181:8080/', username='anji', password='master')
print "-----------------------------------------------------------"
print dir(jenkins)
print "-----------------------------------------------------------"
print "Jenkins#####################################################"
print dir(jenkins_server)
print "############################################################"
#j.create_job('empty', jenkins.EMPTY_CONFIG_XML)
# Get all job in Jenkins Server
print jenkins_server.get_all_jobs()