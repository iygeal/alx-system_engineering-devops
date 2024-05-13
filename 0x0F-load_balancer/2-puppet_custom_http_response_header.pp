# 2-puppet_custom_http_response_header.pp

# Ensure nginx is installed
package { 'nginx':
  ensure => installed,
}

# Allow traffic through port 80
firewall { 'Nginx HTTP':
  dport  => 80,
  proto  => 'tcp',
  action => 'accept',
}

# Define nginx server block configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
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

# Restart nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
