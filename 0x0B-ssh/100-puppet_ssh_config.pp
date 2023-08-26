# change ssh config with puppet
include stdlib

file_line { 'Turn off passwd auth':
path  => '/etc/ssh/ssh_config',
line  => '    PasswordAuthentication no',
match => '^#?   PasswordAuthentication'
}

file_line { 'IdentityFile':
path => '/etc/ssh/ssh_config',
line => '    IdentityFile ~/.ssh/school'
}
