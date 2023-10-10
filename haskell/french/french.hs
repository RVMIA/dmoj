import Data.Char
import Control.Monad
cCount :: Char -> String -> Int
cCount _ "" = 0
cCount c (x:xs)
  | x == c = 1 + cCount c xs
  | otherwise = cCount c xs

french x
  | cCount 's' x >= cCount 't' x = "French"
  | otherwise = "English"

main = do
  times <- read <$> getLine
  lines <- replicateM times getLine
  putStrLn $ french $ map toLower $ concat lines
