from unittest import mock

import pytest
from geminicli.main import main


@mock.patch("getpass.getuser")
@mock.patch("geminicli.main.typer")
@mock.patch("geminicli.main.query_gemini")
def test_main_with_interactive(qg_mock, typer_mock, getuser_mock):
    # GIVEN
    question = "Any question?"
    response = "Hello, Gemini!"
    interactive_mode = True
    qg_mock.return_value = response
    getuser_mock.return_value = "user Z"
    typer_mock.prompt.side_effect = [KeyboardInterrupt]

    # WHEN
    with pytest.raises(KeyboardInterrupt):
        main(question, interactive=interactive_mode)

    # THEN
    print(typer_mock.style.call_args_list)
    typer_mock.style.assert_any_call(f" {response}\n", fg=typer_mock.colors.BRIGHT_GREEN)
    typer_mock.style.assert_any_call(f"\n{getuser_mock.return_value}:", bold=True, fg=typer_mock.colors.BRIGHT_CYAN)
    typer_mock.style.assert_any_call(f"\n Algo mais {getuser_mock.return_value}?  (CTRL + C para encerrar)\n", bold=True, fg=typer_mock.colors.BRIGHT_GREEN)


@mock.patch("getpass.getuser")
@mock.patch("geminicli.main.typer")
@mock.patch("geminicli.main.query_gemini")
def test_main_wo_interactive(qg_mock, typer_mock, getuser_mock):
    # GIVEN
    question = "Any question?"
    response = "Hello, Gemini!"
    interactive_mode = False
    qg_mock.return_value = response
    getuser_mock.return_value = "user Z"

    # WHEN
    main(question, interactive=interactive_mode)

    # THEN
    print(typer_mock.style.call_args_list)
    typer_mock.style.assert_any_call(f" {response}\n", fg=typer_mock.colors.BRIGHT_GREEN)
    typer_mock.style.assert_any_call(f"\n{getuser_mock.return_value}:", bold=True, fg=typer_mock.colors.BRIGHT_CYAN)
    typer_mock.prompt.assert_not_called()