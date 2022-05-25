def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
 
    left = 0                  # 探索開始位置のindex
    right = len(sorted_array) # 探索終了位置のindex
    mid = 0                   # 真ん中のindex
    
    #探索開始位置が終了位置を超えない限り探索を続ける
    while(left <= right):
        mid = int((left + right) / 2)
        
        # target_numberが見つかればそのindexを返す
        if sorted_array[mid] == target_number: 
            return mid
        
        # midより前にtarget_numberが存在しない場合、探索範囲を後半に絞る
        elif sorted_array[mid] < target_number:
            left = mid + 1
        
        # midより後ろにtarget_numberが存在しない場合、探索範囲を前半に絞る
        else:
            right = mid - 1 

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()