from processo import split_case_number, build_datajud_alias, has_valid_check_digit

EXAMPLE = "0000832-35.2018.4.01.3202"

def test_check_digit():
    assert has_valid_check_digit(split_case_number(EXAMPLE))
    assert not has_valid_check_digit(split_case_number("0000832-36.2018.4.01.3202"))

def test_punctuation():
    punctuation_data = split_case_number(EXAMPLE)
    no_punctuation_data = split_case_number("00008323520184013202")
    assert punctuation_data == no_punctuation_data

def test_invalid_inputs():
    assert split_case_number("0000832-35.2018.4.01.32") is None
    assert split_case_number("000083A-35.2018.4.01.3202") is None

def test_builds_trf_and_trt_aliases():
    assert build_datajud_alias(split_case_number(EXAMPLE)) == "api_publica_trf1"
    assert build_datajud_alias(split_case_number("0000832-35.2018.5.12.3202")) == "api_publica_trt12"
    assert build_datajud_alias(split_case_number("0000832-35.2018.5.00.3202")) == "api_publica_tst"
    assert build_datajud_alias(split_case_number("0000832-35.2018.6.00.3202")) is None
