main :: IO ()
main = do
  f <- readFile "input/input.txt"
  putStr f
