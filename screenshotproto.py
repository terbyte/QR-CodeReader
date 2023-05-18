import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QCursor
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog

class ScreenshotWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.begin = QPoint()
        self.end = QPoint()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowState(Qt.WindowFullScreen)
        self.setWindowOpacity(0.3)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

    def paintEvent(self, event):
        if self.begin and self.end:
            painter = QPainter(self)
            painter.setPen(Qt.white)
            painter.setBrush(Qt.transparent)
            painter.drawRect(self.get_rect())
            


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.begin = event.pos()
            self.end = self.begin
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        rect = self.get_rect()
        if rect.width() == 0 or rect.height() == 0:
            return

        # Get the current screen
        screen = QApplication.primaryScreen()

        # Grab the screenshot of the selected area
        pixmap = screen.grabWindow(QApplication.desktop().winId(), rect.x(), rect.y(), rect.width(), rect.height())

        # Save the pixmap to a file
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", ".", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            pixmap.save(file_name)
            sys.exit()#CLOSING THE CLASS AFTER SAVING THE FILE/IMAGE


    def get_rect(self):
        return QRect(self.begin, self.end).normalized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screenshot = ScreenshotWidget()
    sys.exit(app.exec_())
