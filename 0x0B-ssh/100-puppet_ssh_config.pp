# Puppet manifest to modify SSH configuration

class ssh_config {
  file_line { 'Turn off passwd auth':
    ensure  => present,
    path    => '/home/ubuntu/.ssh/ssh_config',
    line    => 'PasswordAuthentication no',
  }

  file_line { 'Declare identity file':
    ensure  => present,
    path    => '/home/ubuntu/.ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school',
  }
}