# prepare nginx
include stdlib

exec { 'one nginx right away':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell,
  before => File_line['who are you']
}

file_line { 'who are you':
  path  => '/etc/nginx/sites-available/default',
  line  => "\tlocation / {\n\t\tadd_header X-Served-By \"${hostname}\";",
  match => "^\tlocation / {",
  before => Exec['restart']
}

exec {'restart':
  command  => '/usr/sbin/service nginx restart',
  provider => shell
}
