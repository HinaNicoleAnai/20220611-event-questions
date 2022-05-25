from turtle import right


def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    left = 0                # 左から探索用
    right = len(array) - 1  # 右から探索用
    temp = 0                # 値交換用
    
    while(1):
        # pivot以上を左側から探索
        while(array[left] < pivot):
            left += 1
        
        # pivot未満を右側から探索
        while(pivot < array[right]):
            right -= 1
        
        # 先頭と末端の検索がぶつかったら処理終了
        if left >= right:
            break
        
        # 値の入れ替え
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
    
    #基準値以上と基準値未満のグループに分ける
    array[:left + 1] = sort(array[:left + 1]) #pivotの左側をソート
    array[left + 1:] = sort(array[left + 1:]) #pivotから右側をソート
    
    return array

    # ここまで記述

if __name__ == '__main__':
    main()