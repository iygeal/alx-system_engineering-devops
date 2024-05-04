# Setting up my client config file
# using puppet to make changes to the default ssh config file
include stdlib

# Ensure the ssh config file exists and has correct permissions
file { '/etc/ssh/ssh_config':
  ensure => present,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

# Disable password authentication
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

# Set the identity file location
file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}