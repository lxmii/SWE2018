from rle import rle_encoder,rle_decoder
import sys

if __name__=="__main__":
    print(rle_encoder(sys.stdin.read()))

def test_simple():
    assert rle_encoder("bbbkkk") == "b3k3"
def test_advanced():
    assert rle_encoder("ffffiiiii") == "f4i5"
def test_moreadvanced():
    assert rle_encoder("k444444") == "k146"
def test_dec():
    assert rle_decoder("f4i5") == "ffffiiiii"
