from _pytest.capture import CaptureFixture

from learning_buddy import main


def test_main_prints_greeting(capsys: CaptureFixture[str]) -> None:
    main()

    captured = capsys.readouterr()

    assert captured.out == "Hello from learning-buddy!\n"
