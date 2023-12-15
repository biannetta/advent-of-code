$replacement_map = {
  'one'  => '1',
  'two'  => '2',
  'three'=> '3',
  'four' => '4',
  'five' => '5',
  'six'  => '6',
  'seven'=> '7',
  'eight'=> '8',
  'nine' => '9'
}

value = ''
calibration_values = []
calibration_answer = 0

def findFirstNumber(combinedValue, remainingString)
  match = $replacement_map[combinedValue[/(one|two|three|four|five|six|seven|eight|nine)/]]
  firstLetter = remainingString[0]

  if match != nil
    return match
  elsif firstLetter[/\d/] != nil
    return firstLetter
  else
    return findFirstNumber(combinedValue + firstLetter, remainingString[1,remainingString.length])
  end
end

def findLastNumber(combinedValue, remainingString)
  match = $replacement_map[combinedValue[/(one|two|three|four|five|six|seven|eight|nine)/]]
  lastLetter = remainingString[-1,1]

  if match != nil
    return match
  elsif lastLetter[/\d/] != nil
    return lastLetter
  else
    return findLastNumber(lastLetter + combinedValue, remainingString[0,remainingString.length - 1])
  end
end

File.open('day_one_input.txt').each do | line |
  # p line
  value = findFirstNumber('', line) + findLastNumber('',line)
  calibration_values.push(value.to_i)
end

# p calibration_values
calibration_values.each { |i| calibration_answer += i }
p calibration_answer