# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define Nginx server configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
}

# Define the Nginx server configuration template
file { '/etc/nginx/sites-available/default.erb':
  ensure => present,
  source => 'puppet:///modules/nginx/default.erb',
}

# Ensure Nginx is listening on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80;
    server_name _;
    location / {
        return 301 https://www.youtube.com/@naturethrillers/videos;
    }
}",
  notify  => Service['nginx'],
}
