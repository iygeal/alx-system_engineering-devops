# Puppet manifest to kill a process named "killmenow" using pkill
exec { 'kill':
command =>  'pkill -f killmenow',
path    =>  '/usr/bin/',

}