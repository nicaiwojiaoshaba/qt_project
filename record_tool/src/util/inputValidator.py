# 入力框校验函数
def inputValidator(input_line):
    if input_line.text():
        input_line.setStyleSheet("")
        return 0
    else:
        input_line.setStyleSheet("border: 1px solid red")
        return 1
