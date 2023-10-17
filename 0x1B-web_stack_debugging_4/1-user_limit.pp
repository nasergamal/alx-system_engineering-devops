# change file limit
exec {'up limit':
command  => "sed -i 's/4/10000/g; s/5/10000/g' /etc/security/limits.conf",
provider => shell
}
