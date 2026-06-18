year = 0
zi = ['신', '유', '술', '해', '자', '축', '인', '묘', '진', '사', '오', '미']
gan = ['경', '신', '임', '계', '갑', '을', '병', '정', '무', '기']

def gantoyear(year_gty):
    ani = ['원숭이', '닭', '개', '돼지', '쥐', '소', '범', '토끼', '용', '뱀', '말', '양']
    print(f"{year_gty}년은 {gan[year_gty % 10]}{zi[year_gty % 12]}년({ani[year_gty % 12]}) 입니다.")

def yeartogan(year_ytg):
    num_gan, num_zi = 0, 0
    century = (int(input("세기> ")) - 1) * 100
    if century < 0:
        print("음수의 연도는 계산할 수 없습니다.")
        return
    for num_gan in range(10):
        if year_ytg[0] == gan[num_gan]:
            century += num_gan
            num_gan = 0
            century1 = century
            break
        
    for num_zi in range(12):
        if year_ytg[-1] == zi[num_zi]:
            while century1 % 12 != num_zi:
                century1 += 10
                if century1 > century + 100:
                    print("올바르지 않은 육십갑자")
                    return
            break
    if year_ytg[-1] != zi[num_zi]:
        print("올바르지 않은 육십갑자")
        return
    
    print(f"{century1}, {century1 + 60}")

while(year != "-1"):
    try:
        print("-----종료를 원한다면 -1 을 입력-----")
        year = input("육십갑자 / 년도 : ")
        if year == "-1":
            continue
        elif year[0] == "-":
            print("음수의 연도는 계산할 수 없습니다.")
            continue
        if year.isdigit():
            gantoyear(int(year))
        else:
            yeartogan(year)
            
    except Exception as error:
        print("알 수 없는 오류 발생")
        exit(error)

    finally:
        print("")