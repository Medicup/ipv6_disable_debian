#!/usr/bin/env python3
import subprocess

#open sysctl.conf file to append
file = open('/etc/sysctl.conf','a')

#append to disable ipv6
file.write('\n')
file.write('net.ipv6.conf.all.disable_ipv6 = 1\n')
file.write('net.ipv6.conf.default.disable_ipv6 = 1\n')
file.write('net.ipv6.conf.lo.disable_ipv6 = 1\n')
file.close()

#force the update
subprocess.call(['sysctl', '-p'])
subprocess.call(["echo", "Finished" ])
