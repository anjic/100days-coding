import jenkins

jenkins_server = jenkins.Jenkins('http://18.221.129.181:8080', username='anji', password='master')
user = jenkins_server.get_whoami()
version = jenkins_server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'],version))

#creating job
try:
	jenkins_server.create_job('empty', jenkins.EMPTY_CONFIG_XML)

except NameAlreadyExits:
	print "Given name already exists. Please try with New one"

else:
	print "Creating new job......"
	my_job = jenkins_server.create_job('cool-job')
	#print(my_job) 
my_job = server.get_job_config('cool-job')

# prints XML configuration
#jenkins_server.build_job('empty')
#jenkins_server.disable_job('empty')
#jenkins_server.copy_job('empty', 'empty_copy')
#jenkins_server.enable_job('empty_copy')
#jenkins_server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)