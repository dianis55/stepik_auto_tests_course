def test_substring(stdout, stdin):
    # ваша реализация, напишите assert и сообщение об ошибке
     assert stdin in stdout, f"expected '{stdin}' to be substring of '{stdout}'"
