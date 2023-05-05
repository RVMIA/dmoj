import Data.Char
zip' :: [Int] -> [(Int,Int)]
zip' n = zip n [1..]
mod10 n
  | mod n 10 == 0 = 10
  | otherwise = mod n 10
poweri (a,b) = a^b
--main = interact $ show $ sum (map mod10 (map (sum . map poweri) (map poweritself ((map (map (sub96 . ord . toLower) ) . words)))))

