# Puppet Manifest that fixes typo stopping Apache from running

# Define the file to edit
$error_file = '/var/www/html/wp-settings.php'

# Define a command to check if the file contains "phpp"
$check_command = "grep 'phpp' ${error_file}"

# Define a command to replace "phpp" with "php"
$replace_command = "sed -i 's/phpp/php/g' ${error_file}"

# Exec resource to replace "phpp" with "php"
exec { 'replace_phpp_with_php':
  command => $replace_command,
  path    => ['/bin', '/usr/bin'], # Where to find commands used in the Manifest
  onlyif  => $check_command,
}
