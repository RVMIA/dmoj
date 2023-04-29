grades n
  | n < 60 = 0
  | n < 70 = 1
  | n < 80 = 2
  | n < 90 = 3
  | otherwise = 4

same (a:b:_)
  | a == b = "Same"
  | otherwise = "Different"
main = do
  line' <- getLine
  let line = (same . map grades . map read . words) (line')
  putStrLn line
  
  
  
