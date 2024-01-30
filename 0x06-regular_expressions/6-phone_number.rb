#!/usr/bin/env ruby
puts ARGV[0].scan(/^\d{10}$/).join

# Macthes any digits; must be exactly 10 digits