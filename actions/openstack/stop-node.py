from novaclient.v1_1 import client
nt = client.Client('admin', 'labstack', 'demo', 'http://150.165.85.110:5000/v2.0', service_type='compute')
search_opts = {'host': 'openstack-VirtualBox'}
server_list = nt.servers.list(search_opts=search_opts)
for one_server in server_list:
	one_server.force_delete()


