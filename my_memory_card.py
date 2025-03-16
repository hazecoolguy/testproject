from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint
#приложение и главное окно
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,300)

main_win.score = 0
main_win.total = 0

#создание вижетов
lbl_Stat = QLabel('Статистика')


lbl_question = QLabel('Вопрос')
RadioGroup = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Ответ 1')
rbtn_2 = QRadioButton('Ответ 2')
rbtn_3 = QRadioButton('Ответ 3')
rbtn_4 = QRadioButton('Ответ 4')
btn_ok = QPushButton('Ответить')

AnswerGroup = QGroupBox('Результат')
lbl_result = QLabel('Верно/неверно')
lbl_correct = QLabel('Правильный ответ')

ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rbtn_1)
ButtonGroup.addButton(rbtn_2)
ButtonGroup.addButton(rbtn_3)
ButtonGroup.addButton(rbtn_4)


answ = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


#привязка элементов к 'layout'
row1 = QHBoxLayout()
row1.addWidget(rbtn_1)
row1.addWidget(rbtn_2)
row2 = QHBoxLayout()
row2.addWidget(rbtn_3)
row2.addWidget(rbtn_4)

col = QVBoxLayout()
col.addLayout(row1)
col.addLayout(row2)

RadioGroup.setLayout(col)

col1 = QVBoxLayout()
col1.addWidget(lbl_result, alignment=Qt.AlignLeft)
col1.addWidget(lbl_correct, alignment=Qt.AlignCenter)
AnswerGroup.setLayout(col1)
AnswerGroup.hide()

main_layout = QVBoxLayout()
main_layout.setSpacing(15)

main_layout.addWidget(lbl_question, alignment=Qt.AlignCenter, stretch= 1)
main_layout.addWidget(RadioGroup, stretch= 2)
main_layout.addWidget(AnswerGroup, stretch= 2)
main_layout.addWidget(btn_ok)
main_layout.addWidget(lbl_Stat, stretch= 2)

main_win.setLayout(main_layout)




class Question():
    def __init__(self, q, r, w1, w2, w3):
        self.question = q
        self.r_answer = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3


question_list = []
q = Question('В каком году создали windows?', '1985', '1986', '1967', '1974')
question_list.append(q)
q = Question('Кто создал windows?', 'Билл Гейтс', 'Стив Джобс', 'Рональд Уэйн', 'Стив Возняк')
question_list.append(q)
q = Question('Какого windows никогда не существовало?', '9', '8', 'XP', '10')
question_list.append(q)
q = Question('Какая версия windows была вместо 9 версии?', '8.1', '8.5', 'никакая', 'xp')
question_list.append(q)


def ShowResult():
    RadioGroup.hide()
    AnswerGroup.show()
    btn_ok.setText('Следующий вопрос')


def ShowQuestion():
    num = randint(0, len(question_list)-1)
    ask(question_list[num])
    RadioGroup.show()
    AnswerGroup.hide()
    btn_ok.setText('Ответить')
    ButtonGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    ButtonGroup.setExclusive(True)





def ask(q):
    shuffle(answ)
    lbl_question.setText(q.question)
    lbl_correct.setText(q.r_answer)
    answ[0].setText(q.r_answer)
    answ[1].setText(q.wrong1)
    answ[2].setText(q.wrong2)
    answ[3].setText(q.wrong3)
    main_win.total+=1

def checkAnswer():
    if btn_ok.text() == 'Ответить':
        if answ[0].isChecked():
            lbl_result.setText('Совершенно верно!')
            main_win.score+=1
        else:
            lbl_result.setText('Неверно!')
        ShowResult()
        lbl_Stat.setText('Статистика:\nВсего вопросов:'+str(main_win.total)+'\nПравильных ответов:'+str(main_win.score)+'\nНеправильных ответов:'+str(main_win.total-main_win.score))
    else:
        ShowQuestion()

        

num = randint(0, len(question_list)-1)
ask(question_list[num])

btn_ok.clicked.connect(checkAnswer)



#запуск приложения
main_win.show()
app.exec_()






