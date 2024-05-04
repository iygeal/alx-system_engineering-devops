# Puppet manifest to modify SSH configuration

class ssh_config(
  # Description: Configure SSH client to use private key
  # and refuse password authentication
  # Parameters: None
  # Dependencies: None
) {
  file { '/home/ubuntu/.ssh/config':
    ensure  => present,
    content => "
Host *
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0600',
  }
}