line_num = 0
value = 0
calibration_values = []
calibration_answer = 0

File.open('day_one_input.txt').each do | line |
  value = line.scan(/\d/).join('')

  if value.length > 1
    value = value[0] + value[-1,1]
  else
    value = value[0] + value[0]
  end

  calibration_values.push(value.to_i)
end

calibration_values.each { |i| calibration_answer += i }
p calibration_answer