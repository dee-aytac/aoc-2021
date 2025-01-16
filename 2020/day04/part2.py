
def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    valid_passport = 0
    passport_data = dict()
    idx = 0
    hex_digits = "0123456789abcdef"
    for line in content:
        if line == "":
            if len(passport_data.keys()) == 8 or (len(passport_data.keys()) == 7 and "cid" not in passport_data.keys()):
                byr_valid = int(passport_data["byr"]) >= 1920 and int(passport_data["byr"]) <= 2002
                iyr_valid = int(passport_data["iyr"]) >= 2010 and int(passport_data["iyr"]) <= 2020
                eyr_valid = int(passport_data["eyr"]) >= 2020 and int(passport_data["eyr"]) <= 2030
                hgt_valid = True
                if "cm" in passport_data["hgt"]:
                    height = int(passport_data["hgt"][0:len(passport_data["hgt"])-2])
                    if height < 150 or height > 193:
                        hgt_valid = False
                if "in" in passport_data["hgt"]:
                    height = int(passport_data["hgt"][0:len(passport_data["hgt"])-2])
                    if height < 59 or height > 76:
                        hgt_valid = False
                hcl_valid = is_hex(passport_data["hcl"][1:])
                if len(passport_data["hcl"]) != 7 or passport_data["hcl"][0] != "#":
                    hcl_valid = False
                ecl_valid = passport_data["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                pid_valid = True
                if len(passport_data["pid"]) != 9 or not passport_data["pid"].isdigit():
                    pid_valid = False
                if byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid:
                    valid_passport += 1
            passport_data = dict()
            idx += 1
            continue
        fields = line.split(' ')
        for field in fields:
            key, val = field.split(':')
            passport_data[key] = val

    return valid_passport

if __name__ == "__main__":
    print(solution('input.txt')) 
