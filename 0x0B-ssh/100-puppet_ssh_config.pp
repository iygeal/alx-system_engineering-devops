# Seting up my client config file
class ssh_config() {
  # Puppet manifest to configure SSH client to connect without password

  file { '/home/ubuntu/.ssh/config':
    ensure  => present,
    content => "
Host *
  SendEnv LANG LC_*
  HashKnownHosts yes
  GSSAPIAuthentication yes
  GSSAPIDelegateCredentials no
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
  }
}
