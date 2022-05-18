import os

import pytest
from typer.testing import CliRunner

from compose_viz import cli

runner = CliRunner()


@pytest.mark.parametrize(
    "file_number",
    [
        "000001",
        "000010",
        "000011",
        "000100",
        "000101",
        "000110",
        "000111",
        "001000",
        "001001",
        "001010",
        "001011",
        "001100",
        "001101",
        "001110",
        "001111",
        "010000",
        "010001",
        "010010",
        "010011",
        "010100",
        "010101",
        "010110",
        "010111",
        "011000",
        "011001",
        "011010",
        "011011",
        "011100",
        "011101",
        "011110",
        "011111",
        "100000",
        "100001",
        "100010",
        "100011",
        "100100",
        "100101",
        "100110",
        "100111",
        "101000",
        "101001",
        "101010",
        "101011",
        "101100",
        "101101",
        "101110",
        "101111",
        "110000",
        "110001",
        "110010",
        "110011",
        "110100",
        "110101",
        "110110",
        "110111",
        "111000",
        "111001",
        "111010",
        "111011",
        "111100",
        "111101",
        "111110",
        "111111",
    ],
)
def test_cli(file_number: str) -> None:
    input_path = f"tests/in/{file_number}.yaml"
    output_path = f"{file_number}.png"
    result = runner.invoke(cli.app, ["-o", output_path, input_path])

    assert result.exit_code == 0
    assert f"Successfully parsed {input_path}\n" in result.stdout
    assert os.path.exists(output_path)

    os.remove(output_path)
