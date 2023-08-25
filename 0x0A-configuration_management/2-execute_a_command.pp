# kill process killmenow
exec { 'killmenow':
command => 'pkill -f killmenow',
onlyif  => 'pgrep -f killmenow',
path    => '/usr/bin'
}
