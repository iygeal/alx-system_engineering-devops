# Puppet manifest to configure limits for the holberton user

# Increase hard file limit for user holberton
exec { 'holberton_nofile_hard':
  command => 'sed -i "s/^holberton hard nofile [0-9]\\+/holberton hard nofile 70000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
}

# Increase soft file limit for user holberton
exec { 'holberton_nofile_soft':
  command => 'sed -i "s/^holberton soft nofile [0-9]\\+/holberton soft nofile 70000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
}
