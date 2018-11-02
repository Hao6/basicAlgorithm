# 算法设计与分析
## 算法  
- 计算指计算机物理状态的改变，而算法即是**计算的规则**  

### 算法的特性  
- *确定性(无二义性)*  
算法的每一个步骤都必须精确定义，每种情况需要执行的操作必须给出严格、无歧义的说明。
- *可行性(有效性)*  
原则上，人们可以通过纸和笔在有限的时间内准确地执行一定规模的算法。
- *有穷性*  
算法必须在执行有限步骤后终止。
- *输入*  
具有0个或者多个输入
- *输出*  
1个或者多个输出，输出指与输入有着某种关系的量，并非狭义的函数返回值。  

### 算法时间复杂度分析  
#### 非递归问题——*冒泡排序*
```Python
def swap(data,i,j):
    data[i] , data[j] = data[j] , data[i]

def bubble_sort(unsorted_data):
    """
    type unsorted_data:[int]
    rtype:[int]
    """
    if unsorted_data is None:
        return None
    lens = len(unsorted_data)
    for i in range(lens-1):
        for j in range(lens-i-1):
            if unsorted_data[j] > unsorted_data[j+1]:
                swap(unsorted_data,j,j+1)
    return unsorted_data
```
##### 时间复杂度
主要的时间来源于两层循环部分，外层循环的次数为 $n-1$ ,内层的循环次数为
$\frac{n\times(n-1)}{2}$,则总体的时间复杂度为 $O_{(n^2)}$
#### 递归问题——*汉诺塔问题*
```Python
def hanno_tower(pillar_1, pillar_2, pillar_3, n):
    """
    type pillar_1:str
    type pillar_2:str
    type pillar_3:str
    type        n:int
    """
    if n == 1:
        print "move the "+str(n) +"th dish " + "from " + pillar_1 + " to " + pillar_3
        return
    else:
        # step 1: the most top n-1's dishes were moved from pillar_1 to pillar_2
        hanno_tower(pillar_1, pillar_3, pillar_2, n-1)
        # step 2: the most bottom 1 dish were moved from pillar_1 to pillar_3
        print "move the "+str(n) +"th dish " + "from " + pillar_1 + " to " + pillar_3
        # STEP 3: the most top n-1's dishes were moved from pillar_2 to pillar_3
        hanno_tower(pillar_2, pillar_1, pillar_3, n-1)
```
##### 时间复杂度
假设当问题规模，即盘子个数为$n$时，时间复杂度可表示为$T_{n}$,且由源代码分析可得 $T_{n}=\left\{
\begin{aligned}
\cos(t) \\
\sin(t) \\
\end{aligned}
\right.$
