-- RunTwice :: (a -> a) -> a -> a
-- RunTwice f x = f (f x)
  
removeNonUppercase :: [Char] -> [Char]  
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]   
:t removeNonUppercase

  