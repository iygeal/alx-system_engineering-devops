# Download and install Nginx web server
# and add a custom HTTP header

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Define nginx server block configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By ${facts['networking']['hostname']};
    location / {
        try_files \$uri \$uri/ =404;
    }
    if (\$request_filename ~ redirect_me){
        rewrite ^ https://www.youtube.com/@naturethrillers/videos permanent;
    }
    error_page 404 /error_404.html;
    location = /error_404.html {
        internal;
    }
}",
}

exec { 'reload nginx':
  command => 'service nginx reload',
  require => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
