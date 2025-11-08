import subprocess, sys, textwrap

def run_game(inputs: str):
    p = subprocess.run(
        [sys.executable, "app/treasure.py"],
        input=inputs.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True
    )
    return p.stdout.decode()

def test_happy_path():
    out = run_game("left\nwait\nyellow\n")
    assert "You found the treasure!!!" in out

def test_bad_turn():
    out = run_game("right\n")
    assert "You fell into the hole!" in out