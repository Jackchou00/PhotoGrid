import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QFileDialog, QLineEdit, QPushButton
from image_process import process_image

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): 
        self.setWindowTitle('PhotoGrid') 

        # 添加控件
        self.path_edit = QLineEdit(self)
        self.path_edit.setPlaceholderText('请选择文件夹')
        self.path_btn = QPushButton('选择文件夹', self)
        self.run_btn = QPushButton('运行程序', self)
        self.quit_btn = QPushButton('退出程序', self)
        self.num_edit = QLineEdit(self)
        self.num_edit.setPlaceholderText('每行图片数量')

        # 设置控件位置
        self.path_edit.setGeometry(10, 10, 200, 30)
        self.path_btn.setGeometry(220, 10, 100, 30)
        self.run_btn.setGeometry(10, 50, 100, 30)
        self.quit_btn.setGeometry(120, 50, 100, 30)
        self.num_edit.setGeometry(230, 50, 90, 30)

        # 连接信号与槽
        self.path_btn.clicked.connect(self.show_file_dialog)
        self.run_btn.clicked.connect(self.run_program)
        self.quit_btn.clicked.connect(QApplication.instance().quit)

        self.center()
        self.show()

    def center(self):
        """ 窗口居中显示 """
        screen = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        screen.moveCenter(center_point)
        self.move(screen.topLeft())

    def show_file_dialog(self):
        """ 显示文件选择器 """
        file_dialog = QFileDialog()
        path = file_dialog.getExistingDirectory(self, '请选择文件夹')
        if path:
            self.path_edit.setText(path)

    def run_program(self):
        """ 运行程序 """
        path = self.path_edit.text()
        num = self.num_edit.text()
        if not path or not num:
            return
        res_img = process_image(path, num)
        res_img.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())