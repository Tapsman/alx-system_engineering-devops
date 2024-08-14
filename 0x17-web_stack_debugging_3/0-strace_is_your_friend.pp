# This is a script that corrects a bad phpp to php in a file

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path	  => '/usr/local/bin/:bin/'
}
