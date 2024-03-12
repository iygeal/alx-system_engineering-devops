#!/usr/bin/env ruby

# ARGV[0]: Retrieves the first command-line argument passed to the script.
# .scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/):
#   - Uses regular expressions to search for patterns in the log entry.
#   - \[from:(.*?)\]: Matches the 'from' part and captures content
#	inside the brackets non-greedily (using ? means it matches as fewer as possible).
#   - \[to:(.*?)\]: Matches the 'to' part and captures content
#	inside the brackets non-greedily.
#   - \[flags:(.*?)\]: Matches the 'flags' part and captures
#	content inside the brackets non-greedily.
# .join(","): Joins the matched results using commas and prints the final result.
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")

