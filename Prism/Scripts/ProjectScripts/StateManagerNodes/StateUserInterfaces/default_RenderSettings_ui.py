# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default_RenderSettings.ui'
#
# Created: Tue Jul 28 08:56:40 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_wg_RenderSettings(object):
    def setupUi(self, wg_RenderSettings):
        wg_RenderSettings.setObjectName("wg_RenderSettings")
        wg_RenderSettings.resize(340, 449)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wg_RenderSettings.sizePolicy().hasHeightForWidth())
        wg_RenderSettings.setSizePolicy(sizePolicy)
        wg_RenderSettings.setMinimumSize(QtCore.QSize(340, 0))
        wg_RenderSettings.setMaximumSize(QtCore.QSize(340, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(wg_RenderSettings)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.f_name = QtGui.QWidget(wg_RenderSettings)
        self.f_name.setObjectName("f_name")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.f_name)
        self.horizontalLayout_4.setContentsMargins(9, 0, 18, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.l_name = QtGui.QLabel(self.f_name)
        self.l_name.setObjectName("l_name")
        self.horizontalLayout_4.addWidget(self.l_name)
        self.e_name = QtGui.QLineEdit(self.f_name)
        self.e_name.setObjectName("e_name")
        self.horizontalLayout_4.addWidget(self.e_name)
        self.l_class = QtGui.QLabel(self.f_name)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_class.setFont(font)
        self.l_class.setObjectName("l_class")
        self.horizontalLayout_4.addWidget(self.l_class)
        self.verticalLayout.addWidget(self.f_name)
        self.gb_general = QtGui.QGroupBox(wg_RenderSettings)
        self.gb_general.setObjectName("gb_general")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gb_general)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.w_load_3 = QtGui.QWidget(self.gb_general)
        self.w_load_3.setObjectName("w_load_3")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.w_load_3)
        self.horizontalLayout_12.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.chb_editSettings = QtGui.QCheckBox(self.w_load_3)
        self.chb_editSettings.setObjectName("chb_editSettings")
        self.horizontalLayout_12.addWidget(self.chb_editSettings)
        self.verticalLayout_2.addWidget(self.w_load_3)
        self.w_presetOption = QtGui.QWidget(self.gb_general)
        self.w_presetOption.setObjectName("w_presetOption")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.w_presetOption)
        self.horizontalLayout_13.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.l_presetOption = QtGui.QLabel(self.w_presetOption)
        self.l_presetOption.setObjectName("l_presetOption")
        self.horizontalLayout_13.addWidget(self.l_presetOption)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.cb_presetOption = QtGui.QComboBox(self.w_presetOption)
        self.cb_presetOption.setObjectName("cb_presetOption")
        self.horizontalLayout_13.addWidget(self.cb_presetOption)
        self.verticalLayout_2.addWidget(self.w_presetOption)
        self.w_loadCurrent = QtGui.QWidget(self.gb_general)
        self.w_loadCurrent.setObjectName("w_loadCurrent")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.w_loadCurrent)
        self.horizontalLayout_11.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.b_loadCurrent = QtGui.QPushButton(self.w_loadCurrent)
        self.b_loadCurrent.setObjectName("b_loadCurrent")
        self.horizontalLayout_11.addWidget(self.b_loadCurrent)
        self.b_loadPreset = QtGui.QPushButton(self.w_loadCurrent)
        self.b_loadPreset.setObjectName("b_loadPreset")
        self.horizontalLayout_11.addWidget(self.b_loadPreset)
        self.verticalLayout_2.addWidget(self.w_loadCurrent)
        self.w_addSetting = QtGui.QWidget(self.gb_general)
        self.w_addSetting.setObjectName("w_addSetting")
        self.horizontalLayout = QtGui.QHBoxLayout(self.w_addSetting)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_addSetting = QtGui.QComboBox(self.w_addSetting)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_addSetting.sizePolicy().hasHeightForWidth())
        self.cb_addSetting.setSizePolicy(sizePolicy)
        self.cb_addSetting.setEditable(True)
        self.cb_addSetting.setMaxVisibleItems(30)
        self.cb_addSetting.setObjectName("cb_addSetting")
        self.horizontalLayout.addWidget(self.cb_addSetting)
        self.verticalLayout_2.addWidget(self.w_addSetting)
        self.gb_settings = QtGui.QGroupBox(self.gb_general)
        self.gb_settings.setObjectName("gb_settings")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gb_settings)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.te_settings = QtGui.QTextEdit(self.gb_settings)
        self.te_settings.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.te_settings.setObjectName("te_settings")
        self.verticalLayout_3.addWidget(self.te_settings)
        self.verticalLayout_2.addWidget(self.gb_settings)
        self.w_save = QtGui.QWidget(self.gb_general)
        self.w_save.setObjectName("w_save")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.w_save)
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_resetSettings = QtGui.QPushButton(self.w_save)
        self.b_resetSettings.setObjectName("b_resetSettings")
        self.horizontalLayout_2.addWidget(self.b_resetSettings)
        self.b_applySettings = QtGui.QPushButton(self.w_save)
        self.b_applySettings.setEnabled(True)
        self.b_applySettings.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_applySettings.setObjectName("b_applySettings")
        self.horizontalLayout_2.addWidget(self.b_applySettings)
        self.verticalLayout_2.addWidget(self.w_save)
        self.w_load = QtGui.QWidget(self.gb_general)
        self.w_load.setObjectName("w_load")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.w_load)
        self.horizontalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.b_savePreset = QtGui.QPushButton(self.w_load)
        self.b_savePreset.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_savePreset.setObjectName("b_savePreset")
        self.horizontalLayout_10.addWidget(self.b_savePreset)
        self.verticalLayout_2.addWidget(self.w_load)
        self.verticalLayout.addWidget(self.gb_general)

        self.retranslateUi(wg_RenderSettings)
        QtCore.QMetaObject.connectSlotsByName(wg_RenderSettings)

    def retranslateUi(self, wg_RenderSettings):
        wg_RenderSettings.setWindowTitle(QtGui.QApplication.translate("wg_RenderSettings", "Render Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.l_name.setText(QtGui.QApplication.translate("wg_RenderSettings", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_class.setText(QtGui.QApplication.translate("wg_RenderSettings", "RenderSettings", None, QtGui.QApplication.UnicodeUTF8))
        self.gb_general.setTitle(QtGui.QApplication.translate("wg_RenderSettings", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_editSettings.setText(QtGui.QApplication.translate("wg_RenderSettings", "Edit settings", None, QtGui.QApplication.UnicodeUTF8))
        self.l_presetOption.setText(QtGui.QApplication.translate("wg_RenderSettings", "Preset:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_loadCurrent.setText(QtGui.QApplication.translate("wg_RenderSettings", "Get current settings", None, QtGui.QApplication.UnicodeUTF8))
        self.b_loadPreset.setText(QtGui.QApplication.translate("wg_RenderSettings", "Load preset...", None, QtGui.QApplication.UnicodeUTF8))
        self.gb_settings.setTitle(QtGui.QApplication.translate("wg_RenderSettings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.b_resetSettings.setText(QtGui.QApplication.translate("wg_RenderSettings", "Apply default settings", None, QtGui.QApplication.UnicodeUTF8))
        self.b_applySettings.setText(QtGui.QApplication.translate("wg_RenderSettings", "Apply preset", None, QtGui.QApplication.UnicodeUTF8))
        self.b_savePreset.setText(QtGui.QApplication.translate("wg_RenderSettings", "Save new preset...", None, QtGui.QApplication.UnicodeUTF8))

