replaceSemis :: String -> String
replaceSemis "" = ""
replaceSemis (x:xs)
  | x == ';' = ' ': replaceSemis xs
  | otherwise = x:replaceSemis xs

toRange x
  | '-' `notElem` x = [read x :: Int]
  | otherwise = [a..b]
  where a = read $ fst c
        b = read $ tail $ snd c
        c = break (== '-') x



main = do
  p <- getLine
  print $ length $ concatMap toRange $ words $ replaceSemis p
