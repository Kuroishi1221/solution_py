"""circle"""
def main():
    """scan"""
    radarme_x = float(input())
    radarme_y = float(input())
    russamee1 = float(input())
    radarf_x = float(input())
    radarf_y = float(input())
    russamee2 = float(input())
    total_rus = russamee2 + russamee1

    rayahang = (((radarme_x - radarf_x)**2) + ((radarme_y - radarf_y)**2))**0.5

    if total_rus == rayahang:
        print('No')
    elif total_rus > rayahang:
        print("Yes")

    else:
        print("No")

main()
