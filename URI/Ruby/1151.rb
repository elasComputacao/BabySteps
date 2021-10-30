amount = gets.chomp.to_i
two_last = [0,1]
def fibonacci(amount, two_last)

  if amount == 1
    puts(0)
    return 0
  end

  if amount == 2
    puts("0 1")
    return 0
  end

  (amount-2).times do
    two_last.push(two_last[two_last.length-1] + two_last[two_last.length-2])
  end
  puts(two_last.join(' '))

end

fibonacci(amount, two_last)