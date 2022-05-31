from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QApplication,
    QTableWidgetItem
)

import sys, numpy as np,matplotlib.pyplot as plt
from timeit import default_timer
from app_ui import Ui_MainWindow
from Algo_genetique import genetic_algorithm

class MainWindow(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.buttons_actions()

        
    def buttons_actions(self):
        self.ui.pushButton_matrix.clicked.connect(
            self.generateMatrix
        )
        self.ui.Get_matrix_content.clicked.connect(
            self.getMatrixContent
        )
        self.ui.Random_matrix.clicked.connect(
            self.generate_random_matrix
        )
        self.ui.auto_complete.clicked.connect(
            self.auto_complete
        )


    def generateMatrix(self):
        number_of_line = int(self.ui.nbr_villes.text())
        
        for j in range(0,number_of_line):
            self.ui.tableWidget.insertColumn(j)

        for i in range(0,number_of_line):
            self.ui.tableWidget.insertRow(i)
            for j in range(0, number_of_line):
                self.ui.tableWidget.setItem(i , j, QTableWidgetItem(""))
                if i == j:
                    self.ui.tableWidget.setItem(i , j, QTableWidgetItem("0"))


    def generate_random_matrix(self): 
        number_of_line = int(self.ui.nbr_villes.text())

        for j in range(0,number_of_line):
            self.ui.tableWidget.insertColumn(j)

        for i in range(0,number_of_line):
            self.ui.tableWidget.insertRow(i)
            for j in range(0, number_of_line):
                random_number=str(np.random.randint(1,100))
                self.ui.tableWidget.setItem(i , j, QTableWidgetItem(random_number))
                self.ui.tableWidget.setItem(j , i, QTableWidgetItem(random_number))
                if i == j:
                    self.ui.tableWidget.setItem(i , j, QTableWidgetItem("0"))


    def auto_complete(self):
        count_row = self.ui.tableWidget.columnCount()
        x=1
        if self.ui.tableWidget.item(0,1).text() == "":
            for k in range (1,count_row):
                for l in range(x):
                    item = self.ui.tableWidget.item(k,l).text()
                    self.ui.tableWidget.setItem(l , k, QTableWidgetItem(item))
                x+=1           
        else:
            for k in range (1,count_row):
                for l in range(x):
                    item = self.ui.tableWidget.item(l,k).text()
                    self.ui.tableWidget.setItem(k , l, QTableWidgetItem(item))
                x+=1           


    def getMatrixContent(self):
        count_row = self.ui.tableWidget.columnCount()
        mat_distance = []
        for i in range(0,count_row):
            data=[]
            for j in range(0,count_row):
                data.append(
                    int(
                        self.ui.tableWidget.item(i,j).text()
                    )
                )
            mat_distance.append(data)    
        mat_distance=np.array(mat_distance)


        nbr_population = int(self.ui.nbr_population.text())
        nbr_iteration = int(self.ui.nbr_iterations.text())
        nbr_villes=int(self.ui.nbr_villes.text())
        villes=range(nbr_villes)


        debut=default_timer()
        (score,meilleur)= genetic_algorithm(villes,mat_distance,nbr_population,nbr_iteration)
        fin=default_timer()
        self.ui.affichage.setText(f"La meilleur solution trouvé est {meilleur} avec un score de {score}.\n\nLe temps d'execution est {fin-debut}s.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
