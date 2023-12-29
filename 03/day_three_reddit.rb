require "set"

rows = File.open('day_three_input.txt').each_line.map(&:chomp)

syms = []
rows.each_with_index do |row,x|
  row.each_char.with_index do |char,y|
    next if char == "."
    next if char =~ /\d/
    syms << [x,y]
  end
end

number_starts = Set.new
syms.each do |(x,y)|
  [
    [-1,-1],[-1,0],[-1,1],
    [0,-1],[0,1],
    [1,-1],[1,0],[1,1]
  ].each do |(dx,dy)|
    nx = x + dx
    ny = y + dy
    if rows[nx][ny] =~ /\d/
      nny = ny
      while rows[nx][nny - 1] =~ /\d/
        nny -= 1
      end
      number_starts << [nx, nny]
    end
  end
end

results = number_starts.map do |(x,y)|
  rows[x][y..].to_i
end

p results.sort
p results.sum