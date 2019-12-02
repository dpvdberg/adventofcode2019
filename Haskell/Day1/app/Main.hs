main :: IO ()
main = do
  f <- readFile "input/input.txt"
  show (fuelCalculation 1000)
  

fuelCalculation x = floor(x / 3) + 2