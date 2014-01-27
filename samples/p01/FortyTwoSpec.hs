module Samples.P01.FortyTwoSpec where
import Test.Hspec

import Samples.FortyTwo

main :: IO ()
main = hspec spec

spec :: Spec
spec =
  describe "fortytwo" $
    it "should return 42" $
      fortytwo `shouldBe` 42
