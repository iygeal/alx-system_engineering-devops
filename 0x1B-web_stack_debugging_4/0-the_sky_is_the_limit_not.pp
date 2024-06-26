# This manifest increases the traffic NGINX server can handle

# Replace the ulimit value in /etc/default/nginx
exec { 'nginx_ulimit_fix':
  command => 'sed -i "s/15/4000/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/usr/bin', '/bin']
}

# Restart NGINX after changing ulimit value
exec { 'nginx_restart':
  command => 'service nginx restart',
  path    => ['/usr/sbin', '/usr/bin', '/sbin', '/bin']
}
