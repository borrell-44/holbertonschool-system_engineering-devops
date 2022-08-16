# This source file will kill a process
exec {'pkill killmenow':
  provider  => 'shell'
}
