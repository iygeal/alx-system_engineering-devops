#This manifest increases the traffic NGINX server can handle

# Replace the ulimit value in /etc/default/nginx
exec { 'nginx-fix':
  command => 'sed -i "s/ULIMIT=\"-n [0-9]*\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => '/bin:/usr/bin',
}

# Restart NGINX after changing ulimit value
exec { 'nginx-restart':
  command => 'service nginx reload',
  path    => ['/sbin', '/usr/sbin', '/bin', '/usr/bin'],
}