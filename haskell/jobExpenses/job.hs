import Control.Arrow
main = interact $ show . sum . map abs . filter (<0) . map (read :: String -> Integer) . tail . words
