CubeCounts = {
  "red" => 12,
  "green" => 13,
  "blue" => 14
}

$validGames = []
$invalidGames = [] 

File.open('day_two_input.txt').each do | line |
  gameCount = line.split(':')[0][/\d+/].to_i
  games = line.split(':')[1]
  $validGames.push(gameCount)

  games.split(';').each do | game |
    game.split(',').each do | draw |
      currentDrawColour = draw[/(blue|green|red)/]
      currentDrawCount = draw[/\d+/].to_i
      if $validGames.include?(gameCount) && currentDrawCount > CubeCounts[currentDrawColour]
        $invalidGames.push(gameCount)
        $validGames.delete(gameCount)
      end
    end
  end
end

p $invalidGames
p $validGames
p $validGames.sum