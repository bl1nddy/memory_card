from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)
from random import randint, shuffle


class Question()
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3)
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(
    Question('Official language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
question_list.append(
    Question('Which color is NOT on Russian flag', 'Green', 'Red', 'White', 'Blue'))
question_list.append(
    Question('National yakut hut', 'Urasa', 'Urt', 'Igloo', 'Hata'))

app = QApplication([])

button_OK = QPushButton('Answer')
label_Question = QLabel('Hardest question in the world!')

RadioGroupBox = QGroupBox('Answer options')

radiobutton_1 = QRadioButton('Option 1')
radiobutton_2 = QRadioButton('Oprion 2')
radiobutton_3 = QRadioButton('Option 3')
radiobutton_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(radiobutton_1)
RadioGroup.addButton(radiobutton_2)
RadioGroup.addButton(radiobutton_3)
RadioGroup.addButton(radiobutton_4)

layout_answer_1 = QHBoxLayout()
layout_answer_2 = QVBoxLayout()
layout_answer_3 = QVBoxLayout()
layout_answer_2.addWidget(radiobutton_1)
layout_answer_2.addWidget(radiobutton_2)
layout_answer_3.addWidget(radiobutton_3)
layout_answer_3.addWidget(radiobutton_4)

layout_answer_1.addLayout(layout_answer_2)
layout_answer_1.addLayout(layout_answer_3)

RadioGroupBox.setLayout(layout_answer_1)
AnswerGroupBox = QGroupBox('Test result')

Label_Result = QLabel('Are you right or not')
Label_Correct = QLabel('Answer will be here!')

layout_res = QVBoxLayout()
layout_res.addWidget(Label_Result, alignment=(Qt.AlignLeft  Qt.AlignTop))
layout_res.addWidget(Label_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnswerGroupBox.setLayout(layout_res)
layout_line_1 = QHBoxLayout()
layout_line_2 = QHBoxLayout()
layout_line_3 = QHBoxLayout()

layout_line_3.addStretch(1)
layout_line_3.addWidget(button_OK, stretch=2)
layout_line_3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line_1, stretch=2)
layout_card.addLayout(layout_line_2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line_3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result()
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    button_OK.setText('Next question')

def show_question()
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    button_OK.setText('Answer')
    RadioGroup.setExclusive(False)
    radiobutton_1.setChecked(False)
    radiobutton_2.setChecked(False)
    radiobutton_3.setChecked(False)
    radiobutton_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [radiobutton_1, radiobutton_2, radiobutton_3, radiobutton_4]

def ask(q Question)
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label_Question.setText(q.question)
    Label_Correct.setText(q.right_answer)
    show_question()

def show_correct(res)
    Label_Result.setText(res)
    show_result()

def check_answer()
    if answers[0].isChecked()
        show_correct('Correct!')
        window.score += 1
        print('Statisticsn-Amount of questions ', window.total, 'n-Correct answers', window.score)
        print('Rating ', (window.scorewindow.total100), '%')
    else
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked()
            show_correct('Incorrect!')
            print('Rating ', (window.scorewindow.total100), '%')

def next_question()
    window.total += 1
    print('Statisticsn-Amount of questions ', window.total, 'n-Correct answers ', window.score)
    current_question = randint(0, len(question_list) - 1)
    q = question_list[current_question]
    ask(q)
def click_ON()
    if button_OK.text() == 'Answer'
        check_answer()
    else
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

button_OK.clicked.connect(click_ON)

window.score = 0
window.total = 0
next_question()
window.resize(400,300)
window.show()
app.exec()
