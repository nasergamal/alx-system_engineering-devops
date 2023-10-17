# change file limit
exec {'up limit':
command  => "sed -i 's/15/20000/g' /etc/default/nginx",
provider => shell
}

exec { 'restart':
command  => 'sudo service nginx restart',
provider => shell
}
