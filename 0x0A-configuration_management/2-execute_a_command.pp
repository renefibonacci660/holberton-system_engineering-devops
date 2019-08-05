# Kills a process by filename
exec { 'pkill killmenow':
  command => 'pkill killmenow',
}
