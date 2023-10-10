import Data.List
import Control.Monad

main = do
  times <- read <$> getLine
  arr <- unlines . map show . sort . map (toInteger . read) <$> replicateM times getLine
  putStrLn arr
