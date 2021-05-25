from click import testing
from hello import hello
from click.testing import CliRunner

def test_hello():
    runner = CliRunner()
    result = runner.invoke(hello, ["--name", "Thor", "--color", "blue"])
    assert "Thor" in result.output
