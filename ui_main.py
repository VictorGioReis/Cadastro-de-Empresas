# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project-app-pyside6.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1309, 637)
        MainWindow.setStyleSheet(u"background-color:rgb(243, 243, 243)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"border: none;\n"
"}\n"
"\n"
"QLabel {\n"
"color: rrgb(74, 74, 74);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 50))
        self.label_3.setPixmap(QPixmap(u"../../vreis-logo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"  background-color: rgb(52, 55, 70);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QToolBox{\n"
"  text-align: left;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"  border-radius: 5px;\n"
"\n"
"  background-color: rgb(87, 183, 113);\n"
"  color: rgb(52, 55, 70);\n"
"  font-weight: 700;\n"
"  padding-left: 55px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMaximumSize(QSize(200, 16777215))
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"  background-color: rgb(139, 232, 158);\n"
"  color: rgb(52, 55, 70);\n"
"  font-weight: 700;\n"
"  border-top-left-radius: 10px;\n"
"  border-top-right-radius: 10px;\n"
"}")
        self.Menu = QWidget()
        self.Menu.setObjectName(u"Menu")
        self.Menu.setGeometry(QRect(0, 0, 91, 424))
        self.verticalLayout_4 = QVBoxLayout(self.Menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home = QPushButton(self.Menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(13)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastro = QPushButton(self.Menu)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMaximumSize(QSize(16777215, 30))
        self.btn_cadastro.setFont(font)
        self.btn_cadastro.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastro)

        self.btn_contato = QPushButton(self.Menu)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMaximumSize(QSize(16777215, 30))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contato)

        self.btn_sobre = QPushButton(self.Menu)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.Menu, u"Page 1")
        self.Informacoes = QWidget()
        self.Informacoes.setObjectName(u"Informacoes")
        self.Informacoes.setGeometry(QRect(0, 0, 16, 424))
        self.label_4 = QLabel(self.Informacoes)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-10, -10, 201, 571))
        self.textBrowser = QTextBrowser(self.Informacoes)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 50, 161, 181))
        self.textBrowser.setStyleSheet(u"background-color:rgb(243, 243, 243)\n"
"\n"
"")
        self.toolBox.addItem(self.Informacoes, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setStyleSheet(u"background-color:rgb(87, 183, 113);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: 700;\n"
"font-size: 20px;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.pushButton = QPushButton(self.top_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(80, 16777215))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"left: 0;")
        icon = QIcon()
        icon.addFile(u"../../../../Downloads/menu-principal (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setLayoutDirection(Qt.LeftToRight)
        self.main_frame.setAutoFillBackground(False)
        self.main_frame.setStyleSheet(u"  background-color: rgb(52, 55, 70);\n"
"  border-radius: 10px;")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_11 = QVBoxLayout(self.pg_home)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(314, 76))
        self.logo.setPixmap(QPixmap(u"../../vreis-logo.png"))
        self.logo.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.logo, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_home)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.label_7 = QLabel(self.pg_contato)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 80, 31, 31))
        self.label_7.setCursor(QCursor(Qt.ArrowCursor))
        self.label_7.setPixmap(QPixmap(u"../../../../Downloads/whatsapp (2).png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.pg_contato)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(150, 90, 201, 16))
        self.label_8.setStyleSheet(u"color: #f4f4f4;\n"
"font-weight: 700;")
        self.label_11 = QLabel(self.pg_contato)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(110, 130, 31, 31))
        self.label_11.setPixmap(QPixmap(u"../../../../Downloads/instagram (4).png"))
        self.label_11.setScaledContents(True)
        self.label_12 = QLabel(self.pg_contato)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(150, 140, 381, 16))
        self.label_12.setStyleSheet(u"color: #f4f4f4;\n"
"font-weight: 700;")
        self.label_13 = QLabel(self.pg_contato)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(150, 190, 201, 16))
        self.label_14 = QLabel(self.pg_contato)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(110, 180, 31, 31))
        self.label_14.setPixmap(QPixmap(u"../../../../Downloads/link-da-web.png"))
        self.label_14.setScaledContents(True)
        self.label_15 = QLabel(self.pg_contato)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(110, 220, 31, 31))
        self.label_15.setPixmap(QPixmap(u"../../../../Downloads/marketing-de-email.png"))
        self.label_15.setScaledContents(True)
        self.label_16 = QLabel(self.pg_contato)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(150, 230, 201, 16))
        self.Pages.addWidget(self.pg_contato)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_6 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: none;\n"
"border-radius: 10px;")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frm_cadastro = QFrame(self.widget)
        self.frm_cadastro.setObjectName(u"frm_cadastro")
        self.frm_cadastro.setStyleSheet(u"QFrame{\n"
"  background-color:rgb(248, 250, 251);\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"  background-color: rgb(243, 243, 243);\n"
"  font: 10pt;\n"
"}")
        self.frm_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frm_cadastro.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frm_cadastro)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_logradouro = QLineEdit(self.frm_cadastro)
        self.txt_logradouro.setObjectName(u"txt_logradouro")

        self.gridLayout.addWidget(self.txt_logradouro, 2, 0, 1, 2)

        self.txt_cnpj = QLineEdit(self.frm_cadastro)
        self.txt_cnpj.setObjectName(u"txt_cnpj")

        self.gridLayout.addWidget(self.txt_cnpj, 1, 0, 1, 1)

        self.txt_nome = QLineEdit(self.frm_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")

        self.gridLayout.addWidget(self.txt_nome, 1, 1, 1, 1)

        self.txt_cep = QLineEdit(self.frm_cadastro)
        self.txt_cep.setObjectName(u"txt_cep")

        self.gridLayout.addWidget(self.txt_cep, 5, 0, 1, 1)

        self.txt_mucipio = QLineEdit(self.frm_cadastro)
        self.txt_mucipio.setObjectName(u"txt_mucipio")

        self.gridLayout.addWidget(self.txt_mucipio, 4, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frm_cadastro)
        self.txt_complemento.setObjectName(u"txt_complemento")

        self.gridLayout.addWidget(self.txt_complemento, 3, 0, 1, 1)

        self.txt_numero = QLineEdit(self.frm_cadastro)
        self.txt_numero.setObjectName(u"txt_numero")

        self.gridLayout.addWidget(self.txt_numero, 3, 1, 1, 1)

        self.txt_uf = QLineEdit(self.frm_cadastro)
        self.txt_uf.setObjectName(u"txt_uf")

        self.gridLayout.addWidget(self.txt_uf, 5, 1, 1, 1)

        self.txt_bairro = QLineEdit(self.frm_cadastro)
        self.txt_bairro.setObjectName(u"txt_bairro")

        self.gridLayout.addWidget(self.txt_bairro, 4, 1, 1, 1)

        self.txt_telefone = QLineEdit(self.frm_cadastro)
        self.txt_telefone.setObjectName(u"txt_telefone")

        self.gridLayout.addWidget(self.txt_telefone, 6, 0, 1, 2)

        self.txt_email = QLineEdit(self.frm_cadastro)
        self.txt_email.setObjectName(u"txt_email")

        self.gridLayout.addWidget(self.txt_email, 7, 0, 1, 2)

        self.lbl_title = QLabel(self.frm_cadastro)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(57, 181))
        self.lbl_title.setMaximumSize(QSize(16777215, 200))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.lbl_title.setFont(font2)
        self.lbl_title.setStyleSheet(u"color: rgb(61, 158, 90);")

        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 2, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frm_cadastro)

        self.btn_cadastrar = QPushButton(self.widget)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(160, 30))
        self.btn_cadastrar.setMaximumSize(QSize(160, 30))
        font3 = QFont()
        font3.setPointSize(12)
        self.btn_cadastrar.setFont(font3)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(61, 158, 90);\n"
"  border: 1px solid rgb(40, 42, 54);\n"
"  border-radius: 10px;\n"
"  color: #f4f4f4;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: rgb(152, 255, 187);\n"
"  color: rgb(40, 42, 54);\n"
"  border: 1px solid rgb(61, 158, 90);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_cadastrar, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(421, 16777215))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_5)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"  background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"  background-color: rgb(139, 232, 158);\n"
"  font: 9pt \"MS Shell Dlg 2\";\n"
"  font-weight: 600;\n"
"  color: #282a36;\n"
"  margin: 2px;\n"
"  border-radius: 5px; \n"
"  \n"
"}")

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.horizontalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(120, 0))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_excel = QPushButton(self.frame_6)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 30))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(33, 115, 70);\n"
"  color: #f4f4f4;\n"
"  border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: rgb(54, 191, 116);\n"
"  color: #f4f4f4;\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_excel)

        self.btn_excluir = QPushButton(self.frame_6)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(222, 60, 47);\n"
"  color: #f4f4f4;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 82, 53);\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_excluir)

        self.btn_alterar = QPushButton(self.frame_6)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(0, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(255, 119, 7);\n"
"  color: #f4f4f4;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: rgb(255, 152, 7);\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_alterar)


        self.horizontalLayout_6.addWidget(self.frame_6, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_9 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.pg_sobre)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setPointSize(21)
        font4.setBold(True)
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"font-weight: 700;\n"
"color: #f4f4f4;\n"
"")

        self.verticalLayout_9.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.pg_sobre)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(700, 0))
        self.label_10.setStyleSheet(u"color: #8be89e;")
        self.label_10.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_sobre)

        self.horizontalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #343746;\n"
"font-weight: 700;\n"
"font-size: 20px;")

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Menu), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_4.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Usu\u00e1rio:  </span><span style=\" font-size:12pt;\"> VR Tech</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Sistema:   </span><span style=\" font-size:12pt;\">Cadastro</span></p>\n"
"<p style=\" margin-top:0px; m"
                        "argin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Status:       </span><span style=\" font-size:12pt;\">Ativo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                  </p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Informacoes), QCoreApplication.translate("MainWindow", u"Page 2", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Sistema de Cadastro</span></p></body></html>", None))
        self.logo.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"(11) 93315-1724", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://instagram.com/vitooreis?igshid=MzMyNGUyNmU2YQ==\"><span style=\" text-decoration: underline; color:#00b294;\">Instagram</span></a></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://victorgioreis.github.io/\"><span style=\" text-decoration: underline; color:#00b294;\">VR Tech Solutions</span></a></p></body></html>", None))
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"victorgrsantos@gmail.com\"><span style=\" text-decoration: underline; color:#00b294;\">Email</span></a></p></body></html>", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RAZ\u00c3O SOCIAL", None))
        self.txt_cep.setText("")
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_mucipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE EMPRESAS", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#005500;\">Empresas Cadastradas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u" COMPLEMENTO ", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Este sistema faz consulta do CNPJ utilizando API da receita federal, e faz o cadastro em um banco de dados SQLite3. Objetivo desse sistema e ensinar como utilizar Python e o Qt Designer.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9VR Tech Solutions", None))
    # retranslateUi

