# This a script that will change the OS configuaration
# So that it may log in with the Holberton user
# and open a file without a single error message.

exec {'Os security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
