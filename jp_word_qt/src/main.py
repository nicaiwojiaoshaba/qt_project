import sys
import yaml
import copy

from util.random_numbers import generate_unique_random_numbers
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QIcon
from Main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 设定单选按钮默认选项
        self.chinaRadioButton.setChecked(True)
        # 画面初始化时禁用翻译按钮
        self.translateButton.setEnabled(False)
        # 画面初始化时禁用全部翻译按钮
        self.translateAllButton.setEnabled(False)
        # 点击提问按钮
        self.questionButton.clicked.connect(self.questionButtonClicked)
        # 点击翻译按钮
        self.translateButton.clicked.connect(self.translateButtonClicked)
        # 点击全部翻译
        self.translateAllButton.clicked.connect(self.translateAllButtonClicked)
        # 更改翻译内容
        self.translateText.textChanged.connect(self.translateTextChanged)
        # 单选按钮变更
        self.chinaRadioButton.toggled.connect(self.init_tool)
        self.kanaRadioButton.toggled.connect(self.init_tool)
        self.japanRadioButton.toggled.connect(self.init_tool)

    def init_tool(self):
        # 清空提问区
        self.questionView.setModel(QtCore.QStringListModel([]))
        # 禁用翻译按钮
        self.translateButton.setEnabled(False)
        # 禁用全部翻译按钮
        self.translateAllButton.setEnabled(False)
        # 清空翻译入力框
        self.translate_value.setText("")
        # 清空翻译区域内容
        self.translateText.setText("")

    def questionButtonClicked(self):
        try:
            '''
              获取元素的值
                _book:      书册
                _class:     课
                _count:     听写个数
                _wordType:  听写类型
            '''
            self._book = self.bookComboBox.currentText()
            self._class = self.classComboBox.currentText()
            self._count = self.countComboBox.currentText()
            self._wordType = self.typeComboBox.currentText()
            self.yaml_dict = {}

            # 读取对应yaml文件内容
            self.yaml_data = load_yaml(f"./question_word/{self._book}/{self._class}.yaml")
            # 激活翻译按钮
            self.translateButton.setEnabled(True)
            # 激活全部翻译按钮
            self.translateAllButton.setEnabled(True)
            # 判断当前选择的提问类型
            if self.chinaRadioButton.isChecked():
                self.questionType = '汉译'
                # self.questionView.setModel(QtCore.QStringListModel([]))
            elif self.kanaRadioButton.isChecked():
                self.questionType = '假名'
            else:
                self.questionType = '日本字'
            # 获取单词提问列表
            self.question_list = make_question_list(self.yaml_data, int(self._count), self.questionType, self._wordType)
            model = QtCore.QStringListModel(self.question_list)
            # 设定提问列表到提问区
            self.questionView.setModel(model)
        except KeyError:
            QMessageBox.information(self, "提示", "本课没有该类型单词,请重新选择")

    # 点击翻译按钮事件
    def translateButtonClicked(self):
        # 读取对应yaml文件中内容写入translate_dict字典
        if not self.yaml_dict:
            for item in self.yaml_data.values():
                self.yaml_dict.update(item)
        translate_dict = copy.deepcopy(self.yaml_dict)
        # 循环translate_dict字典
        for _, value in translate_dict.items():
            # 判断当前单词组是否包含入力框的内容
            if self.translateText.toPlainText().strip() in value.values():
                # 如果yaml文件中假名和日本字相同，表示该单词没有日本字，删除
                if value['假名'] == value['日本字']:
                    del value['日本字']
                # 拼接列表元素
                self.translate_value.setText("    ".join(value.values()))
                # 设置翻译字体颜色
                self.translate_value.setStyleSheet("color:blue")
        # 如果翻译内容不存在，给出提示
        if self.translate_value.text() == "":
            self.translate_value.setText("请问点我会的东西,没问的话不要瞎点")
            self.translate_value.setStyleSheet("color:red")

    # 翻译入力框值变更时，清空翻译内容
    def translateTextChanged(self):
        self.translate_value.setText("")

    # 翻译全部提问单词
    def translateAllButtonClicked(self):
        # 定义全部翻译列表
        translate_list = []
        # 判断yaml文件内容是否已被读取过，*点击翻译按钮时也会作成这一步
        if not self.yaml_dict:
            for item in self.yaml_data.values():
                self.yaml_dict.update(item)
        # 深拷贝作成的yaml_dict
        translate_all_dict = copy.deepcopy(self.yaml_dict)
        # 循环提问区列表
        for item in self.question_list:
            # 循环作成的yaml字典
            for _, value in translate_all_dict.items():
                # 判断当前提问单词是否在单词组中
                if item in value.values():
                    # 在单词组中删除提问单词，删除原因位提问单词想要放在第一个显示，所有后面会手动拼接到最前面
                    if item == value[self.questionType]:
                        del value[self.questionType]
                    # 如果当前提问类型是汉译，全部翻译格式为，汉译+假名+（日本字）
                    if self.questionType == '汉译':
                        translate_list.append(item.ljust(16) + list(value.values())[0] + "（" + list(value.values())[1] + "）")
                    # 否则格式为 当前提问单词+汉译
                    else:
                        translate_list.append(item.ljust(16) + list(value.values())[1])
        model = QtCore.QStringListModel(translate_list)
        # 重新给提问区赋值
        self.questionView.setModel(model)


# 读取yaml文件内容
def load_yaml(path):
    with open(path, "r", encoding="utf-8") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        return yaml_data


# 作成提问列表
def make_question_list(yaml_data, count, questionType, wordType="ALL"):
    try:
        new_data = {}
        question_list = []
        # 如果听写类型是ALL的场合，讲所有类型单词合并为一个字典
        if wordType == "ALL":
            for type in yaml_data:
                new_data.update(yaml_data[type])
        else:
            new_data = yaml_data[wordType]
        # 如果选择的听写类型的单词数量少于听写个数,那么听写个数按照实际单词设定
        if len(new_data) < count:
            count = len(new_data)
        # 定义听写起始位置
        min_num = next(iter(new_data))
        # 定义听写结束位置
        max_num = next(reversed(new_data))
        # 生成随机数列表
        random_list = generate_unique_random_numbers(min_num, max_num, count)
        # 作成单词提问列表
        for item in random_list:
            question_list.append(new_data[item][questionType])
        return question_list
    except KeyError:
        raise


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("jp_word_qt")
    win.setWindowIcon(QIcon(r"src\resource\favicon.ico"))
    # 显示主窗口
    win.show()
    app.exit(app.exec())
