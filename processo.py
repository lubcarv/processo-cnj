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


case_number = input("Número do processo: ").strip()
parts = split_case_number(case_number)

if parts:
    print(parts)
else:
    print("Número de processo inválido")
