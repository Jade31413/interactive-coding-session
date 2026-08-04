# 这里的内容需要复习 - 上课一点没听，
# 记得找老师要录像来重新学习一下这里的内容（课程录像大约30分钟左右吧
# Start at Jul 30, around 11:10这样

# if 语句 (if statements) 是用来控制"某段代码要不要运行"的
# control flow(控制流) 决定的是代码 when(什么时候)，whether(要不要)，how often(运行几次)
# if 语句负责的是 whether(要不要运行)

# 先来看最基本的 if 语句结构：
my_gender = "Male"
my_name = "Quentin"

if my_gender == 'Male':  # if 关键字 + 一个逻辑判断(logical test) + 冒号
    print("Hello Mr. " + my_name)  # 缩进的代码块，只有条件为 True 才会执行

# 逻辑判断(logical test) 是任何一个结果为 True 或 False 的表达式
# 如果条件是 False，Python 会直接跳过这个缩进块，不会报错，也不会执行

# ------------------------------------------------------------
# elif 和 else: 谁先是 True，谁就赢 (first True wins)
# ------------------------------------------------------------
# if 后面可以跟 0 个或多个 elif，最后最多跟 1 个 else

my_gender = "Female"
if my_gender == 'Male':
    print("Hello Mr. " + my_name)
elif my_gender == 'Female':   # elif 只有在：自己的条件是True，并且上面所有条件都是False时，才会运行
    print("Hello Ms. " + my_name)
else:                          # else 没有条件，只有上面全部是False，才会运行
    print("How should I address you?")

# 规则(the rule)：Python 是按顺序检查条件的，一旦遇到第一个 True 就停止
# 也就是说，一个 if/elif/else 结构里，最多只有一个代码块会被执行

# ------------------------------------------------------------
# 顺序很重要 —— 一个常见的坑 (order matters, the gotcha)
# ------------------------------------------------------------
# 因为 Python 遇到第一个 True 就会停止，所以如果把"范围大"的条件写在前面，
# 会导致下面"范围小、更精确"的条件永远不会被检查到

def status_checker(age):
    if age >= 13:
        print("You are a teenager")
    elif age >= 18:      # 这一行永远不会被执行到！ (never reached)
        print("You are an adult")

status_checker(39)   # 打印结果是 "You are a teenager"，这是一个bug！

# 为什么？因为 39 >= 13 已经是 True 了，Python在这里就直接停止判断了，
# 根本不会再去看 age >= 18 这个条件

# 解决方法：永远把"最严格 / 最难满足"的条件放在最前面
# 正确顺序应该是：先判断 >= 18，再判断 >= 13，最后判断 >= 4

def status_checker_fixed(age):
    if age >= 18:
        print("You are an adult")
    elif age >= 13:
        print("You are a teenager")
    else:
        print("You are a child")

status_checker_fixed(39)   # 现在正确打印 "You are an adult"

# ------------------------------------------------------------
# 嵌套 (nesting)
# ------------------------------------------------------------
# 一个 if 代码块里面可以再嵌套一个 if，每一层嵌套都需要自己的缩进

def can_legally_drink(country, age):
    if country == "USA":
        if age >= 21:
            return True
        else:
            return False
    elif country == 'Canada':
        if age >= 19:
            return True
        else:
            return False
    else:
        return "Don't know"

print(can_legally_drink("USA", 25))     # True
print(can_legally_drink("Canada", 18))  # False
print(can_legally_drink("France", 30))  # "Don't know"

# 追踪一下这个函数 (tracing)：
# can_legally_drink("USA", 25)
# 第一步：country == "USA" ? True，进入这个分支
# 第二步：age >= 21 ? 25 >= 21 是 True，所以 return True

# ------------------------------------------------------------
# 技巧 1：三元运算符 (ternary operator)
# ------------------------------------------------------------
# 当一个 if/else 唯一的作用就是"给一个变量赋值"时，可以写成一行

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"

# 结构是: VALUE_IF_TRUE if TEST else VALUE_IF_FALSE
# 效果和下面这个4行版本完全一样：
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# 注意：三元运算符只适合"赋值"这种简单场景，
# 如果逻辑比较复杂，还是老老实实写成 if/elif/else，可读性更好

# ------------------------------------------------------------
# 技巧 2：用字典代替很长的 if 链 (dictionary beats a long chain)
# ------------------------------------------------------------
# 当每一个分支判断的都是"同一个变量"，并且只是"返回另一个值"，
# 这其实不是一个判断(decision)，而是一个查找(lookup)

country_currency = {
    "USA": "US Dollars",
    "Canada": "Canadian Dollars",
    "France": "Euros",
    "Japan": "Yen",
}

print(country_currency["France"])   # 'Euros'

# 注意：这和 if 链并不完全等价！
# if 链有 else 来处理"未知输入"的情况，但是普通的字典查找没有

# print(country_currency["Iran"])   # 会报错！KeyError

# 用 .get() 加一个默认值(fallback)，就可以恢复"else"的效果：
print(country_currency.get("Iran", "Country not found"))  # 'Country not found'

# ------------------------------------------------------------
# 写 if 链时要检查的几个点 (checklist)
# ------------------------------------------------------------
# 1. 条件顺序：从"最难满足"排到"最容易满足"，避免上面的经典bug
# 2. 多个独立的 if 语句 vs elif 链：不是一回事！
#    独立的 if 会把每个条件都单独检查一遍（可能有多个代码块运行）
#    elif 链只要遇到第一个 True 就停止（最多只有一个代码块运行）
# 3. 字典查找默认没有 else，记得用 .get(key, default)
# 4. 三元运算符只用来做简单赋值，不要塞太复杂的逻辑进去

# ------------------------------------------------------------
# 练习：自己 trace 一遍这个函数
# ------------------------------------------------------------
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print(grade(85))
# 问题：
# 1. 第一个被检查的条件是什么？结果是 True 还是 False？
# 2. 真正触发的是哪一个 elif？
# 3. 这个函数最终打印出什么？
# 4. 如果把条件顺序换成先判断 score >= 70，会发生什么？(联系上面的坑)