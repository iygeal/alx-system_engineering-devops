# Install and configure nginx
package { 'nginx':
  ensure => installed,
}

class { 'nginx':
  manage_repo    => true,
  package_source => 'nginx-stable',
}

nginx::resource::server { 'default':
  listen_port      => 80,
  www_root         => '/var/www/html/',
  vhost_cfg_append => { 'rewrite' => '^/redirect_me https://www.youtube.com/@naturethrillers/videos permanent' },
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
