$input = []

File.open('day_three_input.txt').each do |line|
  $input << line.chomp.split('')
end

def getSquare(x,y)
  if (x >= 0 && x < $input.length) && (y >= 0 && y < $input[x].length)
    return $input[x][y]
  else
    return "."
  end
end

def checkSquare(x,y,values)
  return (
    # TL
    values.include?(getSquare(x-1,y-1)) ||
    # TM
    values.include?(getSquare(x-1,  y)) ||
    # TR
    values.include?(getSquare(x-1,y+1)) ||
    # ML
    values.include?(getSquare(x,y-1)) ||
    # MR
    values.include?(getSquare(x,y+1)) ||
    # BL
    values.include?(getSquare(x+1,y-1)) ||
    # BM
    values.include?(getSquare(x+1,y)) ||
    # BR
    values.include?(getSquare(x+1,y+1))
  )
end

$validNumbers = []
$validCharacters = []

$input.each_with_index do |row, x|
  row.each_with_index do |column, y|
    if column[/\d/].nil? && column != "."
      $validCharacters << column
    end
  end
end

p $validCharacters.uniq

$input.each_with_index do |row, x|
  possibleNumber = ""
  validDigit = false
  row.each_with_index do |column, y|
    if !column[/\d/].nil?
      possibleNumber = possibleNumber + column
      validDigit = validDigit || checkSquare(x,y,$validCharacters)
    else
      if validDigit
        $validNumbers << possibleNumber.to_i
      end

      possibleNumber = ""
      validDigit = false
    end    
  end
  if validDigit
    $validNumbers << possibleNumber.to_i
  end
end

p $validNumbers.sort
p $validNumbers.sum