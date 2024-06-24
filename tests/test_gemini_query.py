from unittest import mock

from geminicli.main import query_gemini


@mock.patch("geminicli.main.genai.GenerativeModel")
def test_query_gemini(gm_mock):
    # GIVEN
    gm_mock.return_value.generate_content.return_value.text = "Hello, Gemini!"
    observer = gm_mock.return_value.generate_content

    # WHEN
    response = query_gemini("instruction: {message}", "Initial Question")

    # THEN
    observer.assert_called_once_with("instruction: Initial Question")
    assert response == "Hello, Gemini!"