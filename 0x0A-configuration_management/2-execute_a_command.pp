exec { 'killmenow':
command => 'pkill -f killmenow',
onlyif  => 'pgrep -f killmenow',
path    => '/usr/bin'
}
