from chatbot import get_response

def test_get_response():
    assert "Hello" in get_response("hi")
    assert "Bye" in get_response("bye")
    assert "幫到你" in get_response("help")
    assert "唔明" in get_response("random stuff")

if __name__ == "__main__":
    test_get_response()
    print("All tests passed!")
