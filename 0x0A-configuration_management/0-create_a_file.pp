# Puppet manifest to create the file /tmp/school with given permissions
file { '/tmp/school':
ensure => 'file',
mode => '0744',
owner => 'www-data',
group => 'www-data',
content => 'I love Puppet',
}