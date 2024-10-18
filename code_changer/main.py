from keystone import Ks, KS_ARCH_X86, KS_MODE_64
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.md = Cs(CS_ARCH_X86, CS_MODE_64)
        self.ks = Ks(KS_ARCH_X86, KS_MODE_64)


        grid = QGridLayout()
        self.setLayout(grid)
        self.assembly_code_edit = QLineEdit()
        self.assembly_result_label = QLineEdit('test')
        self.assembly_result_label.setReadOnly(1)
        self.assembly_copy_btn = QPushButton('Copy')

        self.mnemonic_code_edit = QLineEdit()
        self.mnemonic_result_label = QLineEdit('test')
        self.mnemonic_result_label.setReadOnly(1)
        self.mnemonic_copy_btn = QPushButton('Copy')

        grid.addWidget(QLabel('Assembly Code:'), 0, 0)
        grid.addWidget(self.assembly_code_edit, 0, 1)
        grid.addWidget(self.assembly_copy_btn, 1, 0)
        grid.addWidget(self.assembly_result_label, 1, 1)

        grid.addWidget(QLabel('Mnemonic Code:'), 2, 0)
        grid.addWidget(self.mnemonic_code_edit, 2, 1)
        grid.addWidget(self.mnemonic_copy_btn, 3, 0)
        grid.addWidget(self.mnemonic_result_label, 3, 1)

        self.assembly_code_edit.textChanged.connect(self.a2m)
        self.mnemonic_code_edit.textChanged.connect(self.m2a)
        self.assembly_copy_btn.clicked.connect(self.copyAssembly)
        self.mnemonic_copy_btn.clicked.connect(self.copyMnemonic)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 100)
        self.show()

    def copyAssembly(self):
        cb = QApplication.clipboard()
        cb.setText(self.assembly_result_label.text())

    def copyMnemonic(self):
        cb = QApplication.clipboard()
        cb.setText(self.mnemonic_result_label.text())

    # assembly to mnemonic
    # form : 00 11 22 33 44
    def a2m(self):
        try:
            text = self.assembly_code_edit.text().split(' ')
            assembly_code = bytearray()
            for c in text:
                assembly_code.append(int(c,16))

            result = []

            for instruction in self.md.disasm(assembly_code, 0x0):

                result.append(instruction.mnemonic + ' ' + instruction.op_str)

            self.assembly_result_label.setText(','.join(result))
        except Exception as e:
            self.mnemonic_result_label.setText('Invalid assembly code')

    # mnemonic to assembly
    def m2a(self):
        try:
            encoding, count = self.ks.asm(self.mnemonic_code_edit.text())
            result = []
            for i in range(len(encoding)):
                result.append(hex(encoding[i])[2:])
            self.mnemonic_result_label.setText(' '.join(result))
        except Exception as e:
            self.mnemonic_result_label.setText('Invalid mnemonic')
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())