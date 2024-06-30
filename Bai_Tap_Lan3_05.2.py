def chon(player):
    choise = input(f"mmời người chơi {player}chọn kéo, búa, bao :").strip().lower()
    if choise in ['keo', 'bua', 'bao']:
        return choise
    else:
        print("không hợp lệ mời nhập lại!")

def winner(choise1, choise2):
    if choise1 == choise2:
        return None
    elif (choise1 == 'keo' and choise2 == 'bao') or (choise1 == 'bua' and choise2 == 'keo') or (choise1 == 'bao' and choise2 == 'bua'):
        return 1
    else:
        return 2

def main():
    while True:
        choise1 = chon(1)
        choise2 = chon(2)
        winners = winner(choise1, choise2)
        if winner is None:
            print("Hoa")
        else:
            print(f"Người chơi {winners} thắng! ({choise1 if winners == 1 else choise2} đánh bại {choise2 if winners == 1 else choise1}).")
if __name__ == "__main__":
    main()