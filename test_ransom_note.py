from ransom_note import can_construct

def test_can_construct():
    assert can_construct("a", "b") == False
    assert can_construct("aa", "ab") == False
    assert can_construct("aa", "aab") == True
    assert can_construct("abc", "cba") == True
    assert can_construct("aabbcc", "abcabc") == True
    assert can_construct("aabbcc", "aabbc") == False


def test_longer_cases():

    assert can_construct("hiddenclue", "the quick fox had no idea a clue was hidden nearby") == True
    assert can_construct("pythoncode", "coding in java and python should be fun and concise") == True
    assert can_construct("impossible", "simple string without enough matching letters") == False
    assert can_construct("helloworld", "hold water well, re-do logic and end up low") == True
    assert can_construct("missingletter", "all missive notes are later retrieved") == False
    assert can_construct("findthekey", "they knew the key was left behind in the drawer") == True
    assert can_construct("mapthesecrets", "some great mysteries are mapped across sectors") == True
    assert can_construct("notavailable", "none of the values align or balance in later events") == False


if __name__ == "__main__":
    test_can_construct()
    test_longer_cases()
    print("All tests passed!")
