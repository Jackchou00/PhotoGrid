import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QPushButton
from image_process import process_image

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
       
        # 添加控件
        self.path_edit = QLineEdit(self)
        self.path_btn = QPushButton('选择文件夹', self)

        # 设置控件位置
        self.path_edit.setGeometry(10, 10, 200, 30)
        self.path_btn.setGeometry(220, 10, 100, 30)

        # 连接信号与槽
        self.path_btn.clicked.connect(self.show_file_dialog)
        self.run_btn = QPushButton('运行程序', self)
        self.run_btn.setGeometry(10, 50, 100, 30)
        self.run_btn.clicked.connect(self.run_program)

    def show_file_dialog(self):
        """ 显示文件选择器 """
        file_dialog = QFileDialog()
        path = file_dialog.getExistingDirectory(self, '请选择文件夹')
        if path:
            self.path_edit.setText(path)

    def run_program(self):
        """ 运行程序 """
        path = self.path_edit.text()
        if not path:
            return
        res_img = process_image(path)
        res_img.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())