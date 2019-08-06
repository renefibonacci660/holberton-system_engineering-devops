# Kills a process by filename
exec { 'pkill killmenow':
  path    => '/usr/bin',
  command => 'pkill killmenow',
}
