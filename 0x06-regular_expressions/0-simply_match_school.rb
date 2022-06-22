#!/usr/bin/env ruby
arr = ARGV[0]
pat = arr.scan(/School/)
for i in pat do
  print i

end
puts
