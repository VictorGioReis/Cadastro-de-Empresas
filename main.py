from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
import pandas as pd
import openpyxl
import sqlite3
import sys
from ui_functions import consulta_cnpj
from database import Data_base


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("VR Tech - Sistema de Cadastro de Empresas")
        appIcon = QIcon(u"assets/images/vr.png")
        self.setWindowIcon(appIcon)

        #Toggle Button
        self.pushButton.clicked.connect(self.LeftMenu)

        #Páginas do Sistema
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrar))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))

        #Botão consulta dados do CNPJ
        self.txt_cnpj.editingFinished.connect(self.consult_api)

        #Botão para salvar cadastro
        self.btn_cadastrar.clicked.connect(self.cadastrar_empresas)

        self.btn_alterar.clicked.connect(self.updata_company)

        self.btn_excel.clicked.connect(self.gerar_excel_bd)

        self.btn_excluir.clicked.connect(self.delete_company)

        self.buscar_empresas()

    def LeftMenu(self):
        width = self.left_container.width()

        if width == 9:
            newwidth = 200
        else:
            newwidth = 9

        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def consult_api(self):
        campos = consulta_cnpj(self.txt_cnpj.text())

        self.txt_nome.setText(campos[0])
        self.txt_logradouro.setText(campos[1])
        self.txt_numero.setText(campos[2])
        self.txt_complemento.setText(campos[3])
        self.txt_bairro.setText(campos[4])
        self.txt_mucipio.setText(campos[5])
        self.txt_uf.setText(campos[6])
        self.txt_cep.setText(campos[7].replace('.', '').replace('-', ''))
        self.txt_telefone.setText(campos[8].replace('(', '').replace(')', '').replace('-', ''))
        self.txt_email.setText(campos[9])

    def cadastrar_empresas(self):
        db = Data_base()
        db.connect()

        fullDataSet = (

            self.txt_cnpj.text(), self.txt_nome.text(), self.txt_logradouro.text(), self.txt_numero.text(),
            self.txt_complemento.text(), self.txt_bairro.text(), self.txt_mucipio.text(), self.txt_uf.text(),
            self.txt_cep.text(), self.txt_telefone.text().strip(), self.txt_email.text()
        )

        #CADASTRAR NO BANCO DE DADOS
        resp = db.register_company(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Casdastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            self.txt_cnpj.clear()
            self.txt_nome.clear()
            self.txt_logradouro.clear()
            self.txt_numero.clear()
            self.txt_complemento.clear()
            self.txt_bairro.clear()
            self.txt_mucipio.clear()
            self.txt_uf.clear()
            self.txt_cep.clear()
            self.txt_telefone.clear()
            self.txt_email.clear()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente, ou se o Fornecedor já foi cadastrado!")
            msg.exec()
            db.close_connection()
            self.txt_cnpj.clear()
            self.txt_nome.clear()
            self.txt_logradouro.clear()
            self.txt_numero.clear()
            self.txt_complemento.clear()
            self.txt_bairro.clear()
            self.txt_mucipio.clear()
            self.txt_uf.clear()
            self.txt_cep.clear()
            self.txt_telefone.clear()
            self.txt_email.clear()
            return

    def buscar_empresas(self):

        db = Data_base()
        db.connect()
        result = db.select_all_companies()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.close_connection()

    def updata_company(self):

        dados = []
        update_dados = []

        for row in range(self.tableWidget.rowCount()):
           for column in range(self.tableWidget.columnCount()):
               dados.append(self.tableWidget.item(row, column).text())
           update_dados.append(dados)
           dados = []

        db = Data_base()
        db.connect()

        for emp in update_dados:
            db.update_company(tuple(emp))

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização cadastral")
        msg.setText("Atualização Realizada com sucesso")
        msg.exec()

        self.tableWidget.reset()
        self.buscar_empresas()

    def gerar_excel(self):
        dados = []
        all_dados = []

        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                dados.append(self.tableWidget.item(row, column).text())
            
            all_dados.append(dados)
            dados = []

        columns = ['CNPJ','NOME','LOGRADOURO','NUMERO','COMPLEMENTO','BAIRRO','MUNICIPIO',
        'UF','CEP','TELEFONE','EMAIL']

        empresas = pd.DataFrame(all_dados, columns=columns)
        empresas.to_excel("relat/Empresas.xlsx", sheet_name='empresas-cadastradas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()
    
    def gerar_excel_bd(self):
        consulta = sqlite3.connect("system.db")

        columns = ['CNPJ','NOME','MUNICIPIO',
        'UF','TELEFONE','EMAIL']

        empresa = pd.read_sql_query(""" SELECT * FROM Empresas""", consulta)

        empresas = pd.DataFrame(empresa, columns=columns)
        empresas.to_excel("assets/relatorios/Empresas-sql.xlsx", sheet_name='empresas-cadastradas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    def delete_company(self):
        db = Data_base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir cadastro")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Tem certeza que deseja excluir o cadastro?")
        msg.setStandardButtons(QMessageBox.Yes  | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_companies(cnpj)
            self.buscar_empresas()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Excluir")
            msg.setText(result)
            msg.exec()


        db.close_connection()
        
if __name__ == "__main__":

    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()