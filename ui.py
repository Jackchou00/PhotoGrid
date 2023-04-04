import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QFileDialog, QLineEdit, QPushButton, QGridLayout
from image_process import process_image

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): 
        self.setWindowTitle('PhotoGrid') 
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        # 添加控件
        self.path_edit = QLineEdit(self)
        self.path_edit.setPlaceholderText('请选择文件夹')
        self.path_btn = QPushButton('选择文件夹', self)
        self.run_btn = QPushButton('运行程序', self)
        self.quit_btn = QPushButton('退出程序', self)
        self.num_edit = QLineEdit(self)
        self.num_edit.setPlaceholderText('每行图片数量')
        self.space_edit = QLineEdit(self)
        self.space_edit.setPlaceholderText('图片间距')

        '''
        # 设置控件位置
        self.path_edit.setGeometry(10, 10, 200, 30)
        self.path_btn.setGeometry(220, 10, 100, 30)
        self.run_btn.setGeometry(10, 50, 100, 30)
        self.quit_btn.setGeometry(120, 50, 100, 30)
        self.num_edit.setGeometry(230, 50, 90, 30) 
        '''

        self.grid.addWidget(self.path_edit, 0, 0, 1, 3)
        self.grid.addWidget(self.path_btn, 0, 3, 1, 1)
        self.grid.addWidget(self.num_edit, 1, 0, 1, 1)
        self.grid.addWidget(self.space_edit, 1, 1, 1, 1)
        self.grid.addWidget(self.run_btn, 1, 2, 1, 1)
        self.grid.addWidget(self.quit_btn, 1, 3, 1, 1)

        # 连接信号与槽
        self.path_btn.clicked.connect(self.show_file_dialog)
        self.run_btn.clicked.connect(self.run_program)
        self.quit_btn.clicked.connect(QApplication.instance().quit)
        self.show()

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
        space = self.space_edit.text()
        if not path or not num or not space:
            return
        res_img = process_image(path, num, space)
        res_img.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())