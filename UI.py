# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledWfXsdh.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTreeView,
    QWidget)

class Ui_NoteViewer(object):
    def setupUi(self, NoteViewer):
        if not NoteViewer.objectName():
            NoteViewer.setObjectName(u"NoteViewer")
        NoteViewer.resize(800, 600)
        NoteViewer.setDocumentMode(False)
        self.actionOpen = QAction(NoteViewer)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(NoteViewer)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(NoteViewer)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionExit = QAction(NoteViewer)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout_this_program = QAction(NoteViewer)
        self.actionAbout_this_program.setObjectName(u"actionAbout_this_program")
        self.actionAbout_the_creator = QAction(NoteViewer)
        self.actionAbout_the_creator.setObjectName(u"actionAbout_the_creator")
        self.show_toc = QAction(NoteViewer)
        self.show_toc.setObjectName(u"show_toc")
        self.show_toc.setCheckable(True)
        self.show_toc.setChecked(True)
        self.actionOtw_rz_pomoc = QAction(NoteViewer)
        self.actionOtw_rz_pomoc.setObjectName(u"actionOtw_rz_pomoc")
        self.centralwidget = QWidget(NoteViewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PLACEHOLDER_FRAME = QFrame(self.centralwidget)
        self.PLACEHOLDER_FRAME.setObjectName(u"PLACEHOLDER_FRAME")
        self.PLACEHOLDER_FRAME.setFrameShape(QFrame.Shape.StyledPanel)
        self.PLACEHOLDER_FRAME.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.PLACEHOLDER_FRAME)

        NoteViewer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NoteViewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuPlik = QMenu(self.menubar)
        self.menuPlik.setObjectName(u"menuPlik")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuPomoc = QMenu(self.menubar)
        self.menuPomoc.setObjectName(u"menuPomoc")
        self.menuWidok = QMenu(self.menubar)
        self.menuWidok.setObjectName(u"menuWidok")
        NoteViewer.setMenuBar(self.menubar)
        self.dockWidget_2 = QDockWidget(NoteViewer)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.gridLayout = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toc = QTreeView(self.dockWidgetContents_2)
        self.toc.setObjectName(u"toc")

        self.gridLayout.addWidget(self.toc, 0, 0, 1, 1)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        NoteViewer.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget_2)
        self.statusbar = QStatusBar(NoteViewer)
        self.statusbar.setObjectName(u"statusbar")
        NoteViewer.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuPomoc.menuAction())
        self.menubar.addAction(self.menuWidok.menuAction())
        self.menuPlik.addAction(self.actionOpen)
        self.menuPlik.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_this_program)
        self.menuAbout.addAction(self.actionAbout_the_creator)
        self.menuPomoc.addAction(self.actionOtw_rz_pomoc)
        self.menuWidok.addAction(self.show_toc)

        self.retranslateUi(NoteViewer)

        QMetaObject.connectSlotsByName(NoteViewer)
    # setupUi

    def retranslateUi(self, NoteViewer):
        NoteViewer.setWindowTitle(QCoreApplication.translate("NoteViewer", u"Note Viewer", None))
        self.actionOpen.setText(QCoreApplication.translate("NoteViewer", u"Otw\u00f3rz", None))
        self.actionSave.setText(QCoreApplication.translate("NoteViewer", u"Zapisz", None))
        self.actionSave_as.setText(QCoreApplication.translate("NoteViewer", u"Zapisz jako...", None))
        self.actionExit.setText(QCoreApplication.translate("NoteViewer", u"Wyjd\u017a", None))
        self.actionAbout_this_program.setText(QCoreApplication.translate("NoteViewer", u"O tym programie", None))
        self.actionAbout_the_creator.setText(QCoreApplication.translate("NoteViewer", u"O tw\u00f3rcy", None))
        self.show_toc.setText(QCoreApplication.translate("NoteViewer", u"Spis tre\u015bci", None))
        self.actionOtw_rz_pomoc.setText(QCoreApplication.translate("NoteViewer", u"Otw\u00f3rz pomoc", None))
        self.menuPlik.setTitle(QCoreApplication.translate("NoteViewer", u"Plik", None))
        self.menuAbout.setTitle(QCoreApplication.translate("NoteViewer", u"Info", None))
        self.menuPomoc.setTitle(QCoreApplication.translate("NoteViewer", u"Pomoc", None))
        self.menuWidok.setTitle(QCoreApplication.translate("NoteViewer", u"Widok", None))
    # retranslateUi

