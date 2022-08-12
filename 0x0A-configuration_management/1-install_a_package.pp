  # require   => Package['python-pip']
  # This source file will install flask from pip3
package {'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',

}
