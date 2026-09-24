JUDICIARY_BRANCH_BY_CODE = {"1": "Supremo Tribunal Federal", "2": "Conselho Nacional de Justiça",
            "3": "Superior Tribunal de Justiça", "4": "Justiça Federal",
            "5": "Justiça do Trabalho", "6": "Justiça Eleitoral",
            "7": "Justiça Militar da União", "8": "Justiça dos Estados e do Distrito Federal e Territórios",
            "9": "Justiça Militar Estadual"}

def split_case_number(case_number):
    clean = case_number.replace(".", "").replace("-", "")
    if clean.isdigit() and len(clean) == 20:
        return {"sequential_number": clean[:7],
                "check_digit": clean[7:9],
                "year": clean[9:13],
                "judiciary_branch": clean[13:14],
                "court_code": clean[14:16],
                "origin_unit": clean[16:]}
    return None

def describe_case(parts):
    branch = JUDICIARY_BRANCH_BY_CODE.get(parts["judiciary_branch"])
    return branch

def build_datajud_alias(parts):
    branch = parts["judiciary_branch"]
    if parts["court_code"] == "00" and branch == "5":
        return "api_publica_tst"

    number = parts["court_code"].lstrip("0")
    if branch == "4":
        return  f"api_publica_trf{number}"
    elif branch == "5":
        return f"api_publica_trt{number}"
    return None

def has_valid_check_digit(parts):
    check_digit = int(parts["check_digit"])
    number_case = int(((parts["sequential_number"]) +
                   (parts["year"]) +
                   (parts["judiciary_branch"]) +
                   (parts["court_code"]) +
                   (parts["origin_unit"]) + "00"))

    expected_check_digit = 98 - (number_case % 97)
    return expected_check_digit == check_digit

if __name__ == "__main__":
    case_number = input("Número do processo: ").strip()
    parts = split_case_number(case_number)

    if parts:
        print(parts)
        print(describe_case(parts))
        print(build_datajud_alias(parts))
        print(has_valid_check_digit(parts))
    else:
        print("Número de processo inválido")

