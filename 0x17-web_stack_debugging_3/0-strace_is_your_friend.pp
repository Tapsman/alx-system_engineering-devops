# This is a script that corrects a bad phpp to php in a file
# And once the issue is found, it may be fixed
exec {'/etc/php5/apache2/php.ini':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/display_errors = off/display_errors = On/g' /etc/php5/apache2/php.ini",
}

exec { '/var/www/html/wp-setting.php':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}

exec {'/etc/init.d/apache2':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => '/etc/init.d/apache2 restart',
}
