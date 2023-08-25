# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QDate
from PySide6.QtCore import QDateTime
from PySide6.QtCore import QLocale
from PySide6.QtCore import QMetaObject
from PySide6.QtCore import QObject
from PySide6.QtCore import QPoint
from PySide6.QtCore import QRect
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtCore import QTime
from PySide6.QtCore import QUrl
from PySide6.QtGui import QAction
from PySide6.QtGui import QBrush
from PySide6.QtGui import QColor
from PySide6.QtGui import QConicalGradient
from PySide6.QtGui import QCursor
from PySide6.QtGui import QFont
from PySide6.QtGui import QFontDatabase
from PySide6.QtGui import QGradient
from PySide6.QtGui import QIcon
from PySide6.QtGui import QImage
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QLinearGradient
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPalette
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QRadialGradient
from PySide6.QtGui import QTransform
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMenu
from PySide6.QtWidgets import QMenuBar
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QStatusBar
from PySide6.QtWidgets import QTabWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class Ui_FurPatternGenerator(object):
    def setupUi(self, FurPatternGenerator):
        if not FurPatternGenerator.objectName():
            FurPatternGenerator.setObjectName(u"FurPatternGenerator")
        FurPatternGenerator.resize(754, 406)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FurPatternGenerator.sizePolicy().hasHeightForWidth())
        FurPatternGenerator.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(12)
        FurPatternGenerator.setFont(font)
        FurPatternGenerator.setTabShape(QTabWidget.Rounded)
        self.actionOpen = QAction(FurPatternGenerator)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave_as = QAction(FurPatternGenerator)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionSave = QAction(FurPatternGenerator)
        self.actionSave.setObjectName(u"actionSave")
        self.central_widget = QWidget(FurPatternGenerator)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setMinimumSize(QSize(0, 0))
        self.central_widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.central_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.main_vertical_layout = QVBoxLayout()
        self.main_vertical_layout.setObjectName(u"main_vertical_layout")
        self.upper_layout = QHBoxLayout()
        self.upper_layout.setObjectName(u"upper_layout")
        self.image_layout = QVBoxLayout()
        self.image_layout.setObjectName(u"image_layout")
        self.image_label = QLabel(self.central_widget)
        self.image_label.setObjectName(u"image_label")
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QSize(1, 1))
        self.image_label.setAlignment(Qt.AlignCenter)

        self.image_layout.addWidget(self.image_label)

        self.line_4 = QFrame(self.central_widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.image_layout.addWidget(self.line_4)

        self.resolution_layout = QHBoxLayout()
        self.resolution_layout.setObjectName(u"resolution_layout")
        self.lb_x = QLabel(self.central_widget)
        self.lb_x.setObjectName(u"lb_x")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_x.sizePolicy().hasHeightForWidth())
        self.lb_x.setSizePolicy(sizePolicy1)

        self.resolution_layout.addWidget(self.lb_x)

        self.input_res_x = QLineEdit(self.central_widget)
        self.input_res_x.setObjectName(u"input_res_x")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_res_x.sizePolicy().hasHeightForWidth())
        self.input_res_x.setSizePolicy(sizePolicy2)
        self.input_res_x.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.resolution_layout.addWidget(self.input_res_x)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.resolution_layout.addItem(self.horizontalSpacer)

        self.lb_y = QLabel(self.central_widget)
        self.lb_y.setObjectName(u"lb_y")
        sizePolicy1.setHeightForWidth(self.lb_y.sizePolicy().hasHeightForWidth())
        self.lb_y.setSizePolicy(sizePolicy1)

        self.resolution_layout.addWidget(self.lb_y)

        self.input_res_y = QLineEdit(self.central_widget)
        self.input_res_y.setObjectName(u"input_res_y")
        sizePolicy2.setHeightForWidth(self.input_res_y.sizePolicy().hasHeightForWidth())
        self.input_res_y.setSizePolicy(sizePolicy2)
        self.input_res_y.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.resolution_layout.addWidget(self.input_res_y)

        self.bt_apply = QPushButton(self.central_widget)
        self.bt_apply.setObjectName(u"bt_apply")

        self.resolution_layout.addWidget(self.bt_apply)

        self.bt_randomize = QPushButton(self.central_widget)
        self.bt_randomize.setObjectName(u"bt_randomize")

        self.resolution_layout.addWidget(self.bt_randomize)


        self.image_layout.addLayout(self.resolution_layout)


        self.upper_layout.addLayout(self.image_layout)

        self.line_2 = QFrame(self.central_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.upper_layout.addWidget(self.line_2)

        self.property_layout = QVBoxLayout()
        self.property_layout.setObjectName(u"property_layout")
        self.fur_color_layout = QGridLayout()
        self.fur_color_layout.setObjectName(u"fur_color_layout")
        self.fur_color_layout.setHorizontalSpacing(6)
        self.lb_fur_color = QLabel(self.central_widget)
        self.lb_fur_color.setObjectName(u"lb_fur_color")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lb_fur_color.sizePolicy().hasHeightForWidth())
        self.lb_fur_color.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.lb_fur_color.setFont(font1)

        self.fur_color_layout.addWidget(self.lb_fur_color, 0, 0, 1, 1)

        self.label = QLabel(self.central_widget)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fur_color_layout.addWidget(self.label, 1, 0, 1, 1)

        self.bt_base = QPushButton(self.central_widget)
        self.bt_base.setObjectName(u"bt_base")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.bt_base.sizePolicy().hasHeightForWidth())
        self.bt_base.setSizePolicy(sizePolicy5)
        self.bt_base.setCheckable(False)

        self.fur_color_layout.addWidget(self.bt_base, 1, 1, 1, 1)

        self.label_5 = QLabel(self.central_widget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fur_color_layout.addWidget(self.label_5, 2, 0, 1, 1)

        self.bt_pattern = QPushButton(self.central_widget)
        self.bt_pattern.setObjectName(u"bt_pattern")
        sizePolicy5.setHeightForWidth(self.bt_pattern.sizePolicy().hasHeightForWidth())
        self.bt_pattern.setSizePolicy(sizePolicy5)

        self.fur_color_layout.addWidget(self.bt_pattern, 2, 1, 1, 1)


        self.property_layout.addLayout(self.fur_color_layout)

        self.line_3 = QFrame(self.central_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.property_layout.addWidget(self.line_3)

        self.generator_layout = QGridLayout()
        self.generator_layout.setObjectName(u"generator_layout")
        self.lb_generator = QLabel(self.central_widget)
        self.lb_generator.setObjectName(u"lb_generator")
        sizePolicy3.setHeightForWidth(self.lb_generator.sizePolicy().hasHeightForWidth())
        self.lb_generator.setSizePolicy(sizePolicy3)
        self.lb_generator.setFont(font1)

        self.generator_layout.addWidget(self.lb_generator, 0, 0, 1, 1)

        self.label_2 = QLabel(self.central_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.generator_layout.addWidget(self.label_2, 1, 0, 1, 1)

        self.input_activator_radius = QLineEdit(self.central_widget)
        self.input_activator_radius.setObjectName(u"input_activator_radius")
        self.input_activator_radius.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.generator_layout.addWidget(self.input_activator_radius, 1, 1, 1, 1)

        self.label_3 = QLabel(self.central_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.generator_layout.addWidget(self.label_3, 2, 0, 1, 1)

        self.input_inhibitor_radius = QLineEdit(self.central_widget)
        self.input_inhibitor_radius.setObjectName(u"input_inhibitor_radius")
        self.input_inhibitor_radius.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.generator_layout.addWidget(self.input_inhibitor_radius, 2, 1, 1, 1)

        self.label_4 = QLabel(self.central_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.generator_layout.addWidget(self.label_4, 3, 0, 1, 1)

        self.input_inhibitor_weight = QLineEdit(self.central_widget)
        self.input_inhibitor_weight.setObjectName(u"input_inhibitor_weight")
        self.input_inhibitor_weight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.generator_layout.addWidget(self.input_inhibitor_weight, 3, 1, 1, 1)

        self.bt_generate = QPushButton(self.central_widget)
        self.bt_generate.setObjectName(u"bt_generate")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.bt_generate.sizePolicy().hasHeightForWidth())
        self.bt_generate.setSizePolicy(sizePolicy6)
        self.bt_generate.setCheckable(False)

        self.generator_layout.addWidget(self.bt_generate, 4, 1, 1, 1)


        self.property_layout.addLayout(self.generator_layout)


        self.upper_layout.addLayout(self.property_layout)


        self.main_vertical_layout.addLayout(self.upper_layout)

        self.line = QFrame(self.central_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.main_vertical_layout.addWidget(self.line)

        self.lower_layout = QHBoxLayout()
        self.lower_layout.setObjectName(u"lower_layout")
        self.bt_open = QPushButton(self.central_widget)
        self.bt_open.setObjectName(u"bt_open")
        self.bt_open.setCheckable(False)

        self.lower_layout.addWidget(self.bt_open)

        self.bt_save_as = QPushButton(self.central_widget)
        self.bt_save_as.setObjectName(u"bt_save_as")
        self.bt_save_as.setCheckable(False)

        self.lower_layout.addWidget(self.bt_save_as)

        self.bt_save = QPushButton(self.central_widget)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setCheckable(False)

        self.lower_layout.addWidget(self.bt_save)


        self.main_vertical_layout.addLayout(self.lower_layout)


        self.verticalLayout_6.addLayout(self.main_vertical_layout)

        FurPatternGenerator.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(FurPatternGenerator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 754, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        FurPatternGenerator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FurPatternGenerator)
        self.statusbar.setObjectName(u"statusbar")
        FurPatternGenerator.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.input_res_x, self.input_res_y)
        QWidget.setTabOrder(self.input_res_y, self.bt_apply)
        QWidget.setTabOrder(self.bt_apply, self.bt_base)
        QWidget.setTabOrder(self.bt_base, self.bt_pattern)
        QWidget.setTabOrder(self.bt_pattern, self.input_activator_radius)
        QWidget.setTabOrder(self.input_activator_radius, self.input_inhibitor_radius)
        QWidget.setTabOrder(self.input_inhibitor_radius, self.input_inhibitor_weight)
        QWidget.setTabOrder(self.input_inhibitor_weight, self.bt_generate)
        QWidget.setTabOrder(self.bt_generate, self.bt_open)
        QWidget.setTabOrder(self.bt_open, self.bt_save_as)
        QWidget.setTabOrder(self.bt_save_as, self.bt_save)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave)

        self.retranslateUi(FurPatternGenerator)

        QMetaObject.connectSlotsByName(FurPatternGenerator)
    # setupUi

    def retranslateUi(self, FurPatternGenerator):
        FurPatternGenerator.setWindowTitle(QCoreApplication.translate("FurPatternGenerator", u"Fur-Pattern-Generator (FPG)", None))
        self.actionOpen.setText(QCoreApplication.translate("FurPatternGenerator", u"Open", None))
        self.actionSave_as.setText(QCoreApplication.translate("FurPatternGenerator", u"Save as...", None))
        self.actionSave.setText(QCoreApplication.translate("FurPatternGenerator", u"Save", None))
        self.image_label.setText("")
        self.lb_x.setText(QCoreApplication.translate("FurPatternGenerator", u"x:", None))
#if QT_CONFIG(tooltip)
        self.input_res_x.setToolTip(QCoreApplication.translate("FurPatternGenerator", u"<html><head/><body><p>the resolution x</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_y.setText(QCoreApplication.translate("FurPatternGenerator", u"y:", None))
#if QT_CONFIG(tooltip)
        self.input_res_y.setToolTip(QCoreApplication.translate("FurPatternGenerator", u"<html><head/><body><p>the resolution y</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_apply.setText(QCoreApplication.translate("FurPatternGenerator", u"Apply", None))
        self.bt_randomize.setText(QCoreApplication.translate("FurPatternGenerator", u"Randomize", None))
        self.lb_fur_color.setText(QCoreApplication.translate("FurPatternGenerator", u"Fur-Color:", None))
        self.label.setText(QCoreApplication.translate("FurPatternGenerator", u"Base-Color:", None))
#if QT_CONFIG(tooltip)
        self.bt_base.setToolTip(QCoreApplication.translate("FurPatternGenerator", u"<html><head/><body><p>the base fur color</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_base.setText("")
        self.label_5.setText(QCoreApplication.translate("FurPatternGenerator", u"Pattern-Color:", None))
#if QT_CONFIG(tooltip)
        self.bt_pattern.setToolTip(QCoreApplication.translate("FurPatternGenerator", u"<html><head/><body><p>the pattern fur color (hence the melanocyte cells)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_pattern.setText("")
        self.lb_generator.setText(QCoreApplication.translate("FurPatternGenerator", u"Generator:", None))
        self.label_2.setText(QCoreApplication.translate("FurPatternGenerator", u"Activator radius [px]:", None))
#if QT_CONFIG(tooltip)
        self.input_activator_radius.setToolTip(QCoreApplication.translate("FurPatternGenerator", u"<html><head/><body><p>the activator radius A</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("FurPatternGenerator", u"Inhibitor radius [px]:", None))
#if QT_CONFIG(tooltip)
        self.input_inhibitor_radius.setToolTip(QCoreApplication.translate("FurPatternGenerator", u"<html><head/><body><p>the inhibitor radius I</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("FurPatternGenerator", u"w:", None))
#if QT_CONFIG(tooltip)
        self.input_inhibitor_weight.setToolTip(QCoreApplication.translate("FurPatternGenerator", u"<html><head/><body><p>the inhibitor weight w</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_generate.setText(QCoreApplication.translate("FurPatternGenerator", u"Generate", None))
        self.bt_open.setText(QCoreApplication.translate("FurPatternGenerator", u"Open", None))
        self.bt_save_as.setText(QCoreApplication.translate("FurPatternGenerator", u"Save as ...", None))
        self.bt_save.setText(QCoreApplication.translate("FurPatternGenerator", u"Save", None))
        self.menuFile.setTitle(QCoreApplication.translate("FurPatternGenerator", u"File", None))
    # retranslateUi

