# prepare nginx
include stdlib

exec { 'one nginx right away':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell
}

file { '/var/www/html/index.html':
  content => 'Hello World!'
}

file_line { 'where am i':
  path  => '/etc/nginx/sites-available/default',
  line  => "\nserver_name _;\n\trewrite ^/redirect_me http://www.nassera.tech permanent;",
  match => 'server_name _;',
}

exec { 'who are you':
  path  => '/etc/nginx/sites-available/default',
  line  => "listen [::]:80 default_server;\n\tadd_header X-Served-By \"${hostname}\";",
  match => 'listen [::]:80 default_server;',
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell
}
