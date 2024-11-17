def check_days(m):
    match m:
        case "January":
            return "31";
        case "Febuary":
            return "28/29"
        case _:
            return "wrong output"

res=check_days("ssry")
print(res)