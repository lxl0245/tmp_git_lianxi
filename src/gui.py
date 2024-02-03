
# 使用pyqt5创建一个页面
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# 创建一个应用
app = QApplication(sys.argv)
# 创建一个主窗口
window = QMainWindow()
# 设置窗口标题
window.setWindowTitle("第一个PyQt5程序")
# 设置窗口大小
window.resize(400, 300)
# 显示窗口
window.show()
# 进入消息循环
sys.exit(app.exec_())
# 主程序执行结束，退出程序

