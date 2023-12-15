CubeCounts = {
  "red" => 12,
  "green" => 13,
  "blue" => 14
}

$validGames = []
$invalidGames = [] 
$totalGames = []

File.open('day_two_input.txt').each do | line |
  gameCount = line.split(':')[0][/\d+/].to_i
  games = line.split(':')[1]
  $validGames.push(gameCount)

  draws = { "red" => 0, "blue" => 0, "green" => 0 }

  games.split(';').each do | game |
    game.split(',').each do | draw |
      currentDrawColour = draw[/(blue|green|red)/]
      currentDrawCount = draw[/\d+/].to_i

      if draws[currentDrawColour] < currentDrawCount
        draws[currentDrawColour] = currentDrawCount
      end
      
      if $validGames.include?(gameCount) && currentDrawCount > CubeCounts[currentDrawColour]
        $invalidGames.push(gameCount)
        $validGames.delete(gameCount)
      end

    end
  end

  $totalGames.push(draws)

end

p $validGames.sum

sum = 0
$totalGames.each { | game |
  product = 1
  game.each { | key, value |
    product *= value
  }
  sum += product
}
p sum