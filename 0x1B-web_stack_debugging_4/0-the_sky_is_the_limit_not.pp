# This is a script that will finx Nginx so it accepts and serve more requests
# So that it can stop getting failed requests

exec {'modify max open files to limit settings':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/usr/games:/usr/local/games',
}
