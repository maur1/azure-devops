from click import testing
from hello import hello
from click.testing import CliRunner

def if_present_in_input_then__prensent_in_output():
    runner = CliRunner()
    result = runner.invoke(hello, ["--name", "Thor", "--color", "blue"])
    assert "Thor" in result.output
