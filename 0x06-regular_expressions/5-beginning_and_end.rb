#!/usr/bin/env ruby
puts ARGV[0].scan(/^h.n$/).join

# Matches a string starting with h and ending with n
# The string must have a character int-between h and n that is not a new line