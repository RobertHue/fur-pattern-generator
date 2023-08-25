import sys

import numpy as np

from fpg.generator import NP_RGBA_DTYPE
from fpg.generator import Cells
from fpg.generator import RGB_Color
from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtGui import QDoubleValidator
from PySide6.QtGui import QImage
from PySide6.QtGui import QIntValidator
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QColorDialog
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtWidgets import QMainWindow
from window import Ui_FurPatternGenerator


def pixmap_to_numpy(pixmap: QPixmap) -> np.ndarray:
    qimage = pixmap.toImage()
    width = qimage.width()
    height = qimage.height()
    # channel_count = qimage.depth() // 8  # Calculate bytes per channel
    buffer = qimage.bits().tobytes()  # Get the raw bytes from QImage
    shape = (height, width)
    return np.frombuffer(buffer, dtype=NP_RGBA_DTYPE).reshape(shape).copy()


def numpy_to_pixmap(numpy_array: np.ndarray) -> QPixmap:
    height, width = numpy_array.shape
    qimage = QImage(numpy_array.data, width, height, QImage.Format_RGBA8888)
    return QPixmap.fromImage(qimage)


def set_scene_resolution(
    scene: QGraphicsScene, width: int, height: int
) -> None:
    # Update the size of the scene's items
    for item in scene.items():
        if isinstance(item, QGraphicsRectItem):
            item.setRect(
                item.rect().x(),
                item.rect().y(),
                item.rect().width() * width / scene.width(),
                item.rect().height() * height / scene.height(),
            )
    # Update the scene's bounding rectangle
    scene.setSceneRect(0, 0, width, height)


def generate_random(res_x: int, res_y: int) -> QImage:
    numpy_image = np.random.randint(0, 256, (res_x, res_y, 3), dtype=np.uint8)
    return QImage(
        numpy_image.data,
        numpy_image.shape[1],
        numpy_image.shape[0],
        QImage.Format_RGBA8888,
    )


class FPG_MainWindow(QMainWindow, Ui_FurPatternGenerator):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # Set Defaults (here: the model)
        self.base_color = QColor(255, 100, 0, 255)  # orange
        self.pattern_color = QColor(0, 0, 0, 255)  # black
        self.res_x = 64
        self.res_y = 64
        self.activator_radius = 3
        self.inhibitor_radius = 6
        self.inhibitor_weight = 0.42
        # convert from QColor to RGB_Color
        self.d_color = RGB_Color(
            self.pattern_color.red(),
            self.pattern_color.green(),
            self.pattern_color.blue(),
            self.pattern_color.alpha(),
        )
        self.u_color = RGB_Color(
            self.base_color.red(),
            self.base_color.green(),
            self.base_color.blue(),
            self.base_color.alpha(),
        )

        # add new random image
        self.label.setAlignment(Qt.AlignCenter)
        logger.debug(f"{self.image_label.size()=}")
        qimage = generate_random(self.res_x, self.res_y)
        self.pixmap = QPixmap.fromImage(qimage)
        self.apply_pixmap_to_label(self.pixmap)

        # Set the validator to allow only integer input
        int_validator = QIntValidator()
        double_validator = QDoubleValidator()
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        double_validator.setRange(0.0, 100.0)
        self.input_res_x.setValidator(int_validator)
        self.input_res_y.setValidator(int_validator)
        self.input_activator_radius.setValidator(int_validator)
        self.input_inhibitor_radius.setValidator(int_validator)
        # self.input_inhibitor_weight.setValidator(double_validator)

        # apply defaults to view
        self.update_view()

        # connect the buttons with functionality...
        self.bt_base.clicked.connect(self.set_bt_base_color)
        self.bt_pattern.clicked.connect(self.set_bt_pattern_color)
        self.input_res_x.textChanged.connect(self.update_res_x)
        self.input_res_y.textChanged.connect(self.update_res_y)
        self.bt_apply.clicked.connect(self.apply)
        self.bt_randomize.clicked.connect(self.randomize)
        self.bt_generate.clicked.connect(self.generate)
        self.bt_open.clicked.connect(self.open_image)
        self.bt_save_as.clicked.connect(self.save_image)
        self.bt_save.clicked.connect(self.save_image)

    def apply_pixmap_to_label(self, pixmap):
        new_size = self.image_label.size()
        expanded_pixmap = pixmap.scaled(
            new_size.width(),
            new_size.height(),
            Qt.KeepAspectRatio,
            Qt.FastTransformation,
        )
        self.image_label.setPixmap(expanded_pixmap)

    def resizeEvent(self, event):
        logger.debug(f"{self.image_label.size()=}")
        self.apply_pixmap_to_label(self.pixmap)

    def randomize(self):
        logger.info("clicked randomize")
        res = (self.res_x, self.res_y)
        cells = Cells(d_color=self.d_color, u_color=self.u_color, res=res)
        cells.randomize()
        self.pixmap = numpy_to_pixmap(cells.data)
        self.apply_pixmap_to_label(self.pixmap)

    def generate(self):
        logger.info("clicked generate")
        self.activator_radius = int(self.input_activator_radius.text())
        self.inhibitor_radius = int(self.input_inhibitor_radius.text())
        self.inhibitor_weight = float(self.input_inhibitor_weight.text())
        numpy_arr = pixmap_to_numpy(self.pixmap)
        cells = Cells(
            d_color=self.d_color, u_color=self.u_color, ndarray=numpy_arr
        )
        logger.info(
            f"generate with {self.activator_radius=} | {self.inhibitor_radius=} | {self.inhibitor_weight=}"
        )
        cells.develop(
            self.activator_radius, self.inhibitor_radius, self.inhibitor_weight
        )
        self.pixmap = numpy_to_pixmap(cells.data)
        self.apply_pixmap_to_label(self.pixmap)

    def update_res_x(self, new_value):
        self.res_x = int(new_value)

    def update_res_y(self, new_value):
        self.res_y = int(new_value)

    def apply(self):
        logger.info("clicked apply")
        qimage = generate_random(self.res_x, self.res_y)
        self.pixmap = QPixmap.fromImage(qimage)
        self.apply_pixmap_to_label(self.pixmap)

    def get_style(self, color: QColor) -> str:
        style = (
            f"background-color: rgba({color.red()}, {color.green()}, "
            f"{color.blue()}, {color.alpha()});"
        )
        logger.info(style)
        return style

    def update_view(self):
        style_base = self.get_style(self.base_color)
        self.bt_base.setStyleSheet(style_base)
        style_pattern = self.get_style(self.pattern_color)
        self.bt_pattern.setStyleSheet(style_pattern)
        self.input_res_x.setText(str(self.res_x))
        self.input_res_y.setText(str(self.res_y))
        self.input_activator_radius.setText(str(self.activator_radius))
        self.input_inhibitor_radius.setText(str(self.inhibitor_radius))
        self.input_inhibitor_weight.setText(str(self.inhibitor_weight))

    def set_bt_base_color(self):
        color = self.pick_color(self.base_color)
        self.base_color = color
        logger.debug(f"{self.base_color}")
        style_sheet_color = self.get_style(color)
        self.bt_base.setStyleSheet(style_sheet_color)
        # convert from QColor to RGB_Color
        self.u_color = RGB_Color(
            self.base_color.red(),
            self.base_color.green(),
            self.base_color.blue(),
            self.base_color.alpha(),
        )

    def set_bt_pattern_color(self):
        color = self.pick_color(self.pattern_color)
        self.pattern_color = color
        style_sheet_color = self.get_style(color)
        self.bt_pattern.setStyleSheet(style_sheet_color)
        # convert from QColor to RGB_Color
        self.d_color = RGB_Color(
            self.pattern_color.red(),
            self.pattern_color.green(),
            self.pattern_color.blue(),
            self.pattern_color.alpha(),
        )

    def open_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Images (*.png *.jpg *.bmp);;All Files (*)",
            options=options,
        )
        if file_path:
            pixmap = QPixmap(file_path)
            self.image = pixmap.toImage()
            self.update_view()

    def save_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Image",
            "",
            "Images (*.png *.jpg *.bmp);;All Files (*)",
            options=options,
        )
        if file_path:
            # Save the image logic here
            self.pixmap.save(file_path)

    def pick_color(self, current_color: QColor) -> QColor:
        # Show the color dialog and get the selected color
        selected_color = QColorDialog.getColor(
            current_color, self  # , options=QColorDialog.ShowAlphaChannel
        )
        if not selected_color.isValid():
            raise RuntimeError(
                f"Selected color {selected_color.name()} is not valid~"
            )
        return selected_color


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FPG_MainWindow()
    window.show()
    window.resize(640, 480)
    sys.exit(app.exec())
