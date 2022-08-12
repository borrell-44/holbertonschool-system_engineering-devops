exec { 'pkill killmenow':
  provider  => 'shell'
  # This source file will kill a process
}
