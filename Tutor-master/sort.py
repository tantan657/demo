def insertion_sort(arr):
    #插入排序
    # 第一层for表示循环插入的遍数
    for i in range(1, len(arr)):
        # 设置当前需要插入的元素
        current = arr[i]
        # 与当前元素比较的比较元素
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            # 当比较元素大于当前元素则把比较元素后移
            arr[pre_index + 1] = arr[pre_index]
            # 往前选择下一个比较元素
            pre_index -= 1
        # 当比较元素小于当前元素，则将当前元素插入在 其后面
        arr[pre_index + 1] = current
    return arr


def selection_sort(arr):
    #选择排序
    # 第一层for表示循环选择的遍数
    for i in range(len(arr) - 1):
        # 将起始元素设为最小元素
        min_index = i
        # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
        # 查找一遍后将最小元素与起始元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def bubble_sort(arr):
    #冒泡排序
    # 第一层for表示循环的遍数
    for i in range(len(arr) - 1):
        # 第二层for表示具体比较哪两个元素
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # 如果前面的大于后面的，则交换这两个元素的位置
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]

                t = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = t
    return arr



def quick_sort(arr):
  if len(arr) < 2:
    # 基线条件：为空或只包含一个元素的数组是“有序”的
    return arr
  else:
    # 递归条件
    pivot = arr[0]
    # 由所有小于基准值的元素组成的子数组
    less = [i for i in arr[1:] if i <= pivot]
    # 由所有大于基准值的元素组成的子数组
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


# print(quick_sort([10, 5, 2, 3]))


def merge_sort(arr):
    #归并排序
    if len(arr) == 1:
        return arr
    # 使用二分法将数列分两个
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 使用递归运算
    return marge(merge_sort(left), merge_sort(right))


def marge(left, right):
    #排序合并两个数列
    result = []
    # 两个数列都有值
    while len(left) > 0 and len(right) > 0:
        # 左右两个数列第一个最小放前面
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 只有一个数列中还有值，直接添加
    result += left
    result += right
    return result


def shell_sort(arr):
    #希尔排序
    # 取整计算增量（间隔）值
    gap = len(arr) // 2
    while gap > 0:
        # 从增量值开始遍历比较
        for i in range(gap, len(arr)):
            j = i
            current = arr[i]
            # 元素与他同列的前面的每个元素比较，如果比前面的小则互换
            while j - gap >= 0 and current < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current
        # 缩小增量（间隔）值
        gap //= 2
    return arr


def RadixSort(list, d):
    for k in range(d):#d轮排序
        # 每一轮生成10个列表
        s=[[] for i in range(10)]#因为每一位数字都是0~9，故建立10个桶
        for i in list:
            # 按第k位放入到桶中
            s[i//(10**k)%10].append(i)
        # 按当前桶的顺序重排列表
        list=[j for i in s for j in i]
    return list


def Conuting_Sort(A):
    k = max(A)          # A的最大值，用于确定C的长度
    C = [0]*(k+1)       # 通过下表索引，临时存放A的数据
    B = (len(A))*[0]    # 存放A排序完成后的数组
    for i in range(0, len(A)):
        C[A[i]] += 1    # 记录A有哪些数字，值为A[i]的共有几个
    for i in range(1, k+1):
        C[i] += C[i-1]  # A中小于i的数字个数为C[i]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i] # C[A[i]]的值即为A[i]的值在A中的次序
        C[A[i]] -= 1    # 每插入一个A[i]，则C[A[i]]减一
    return B


def sift_down(arr, node, end):
    root = node
    #print(root,2*root+1,end)
    while True:
        # 从root开始对最大堆调整
        child = 2 * root +1  #left child
        if child  > end:
            #print('break',)
            break
        print("v:",root,arr[root],child,arr[child])
        print(arr)
        # 找出两个child中交大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]: #如果左边小于右边
            child += 1 #设置右边为大
        if arr[root] < arr[child]:
            # 最大堆小于较大的child, 交换顺序
            tmp = arr[root]
            arr[root] = arr[child]
            arr[child]= tmp
            # 正在调整的节点设置为root
            #print("less1:", arr[root],arr[child],root,child)
            root = child #
            #[3, 4, 7, 8, 9, 11, 13, 15, 16, 21, 22, 29]
            #print("less2:", arr[root],arr[child],root,child)
        else:
            # 无需调整的时候, 退出
            break
    #print(arr)
    print('-------------')


def heap_sort(arr):
    # 从最后一个有子节点的孩子还是调整最大堆
    first = len(arr) // 2 -1
    for i in range(first, -1, -1):
        sift_down(arr, i, len(arr) - 1)
    #[29, 22, 16, 9, 15, 21, 3, 13, 8, 7, 4, 11]
    print('--------end---',arr)
    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(arr) -1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
        #print(arr)


#桶排序
def bucket_sort(the_list):
    #设置全为0的数组
    all_list = [0 for i in range(100)]
    last_list = []
    for v in the_list:
        all_list[v] = 1 if all_list[v]==0 else all_list[v]+1
    for i,t_v in enumerate(all_list):
        if t_v != 0:
            for j in range(t_v):
                last_list.append(i)
    return last_list


a = [10, 5, 2, 3, 7, 4, 8, 1, 6, 9]
print(bucket_sort(a))
