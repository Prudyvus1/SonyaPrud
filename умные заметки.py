import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QMessageBox


class SmartNotesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        

        # Создаем основное окно
        self.setWindowTitle("Умные заметки")
        self.setGeometry(100, 100, 400, 300)


        # Создаем текстовое поле для заметок
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(100, 160, 200, 40)


        # Создаем кнопку для сохранения заметок
        save_button = QPushButton("Сохранить", self)
        save_button.setGeometry(150, 220, 100, 30)
        save_button.clicked.connect(self.save_notes)


        # Создаем кнопку для удаление заметок
        delite_all_button = QPushButton("Удалить всё", self)
        delite_all_button.setGeometry(275, 220, 100, 30)
        delite_all_button.clicked.connect(self.delite_notes)


        # Создаем кнопку для удаление текста заметок
        delite_button = QPushButton("Удалить", self)
        delite_button.setGeometry(25, 220, 100, 30)
        delite_button.clicked.connect(self.delite_text)


        # Создаем кнопку для читание текста заметок
        txt_button = QPushButton("", self)
        txt_button.setGeometry(80, 25, 250, 130)
        txt_button.clicked.connect(self.show_json)
        

    def show_json(self):
        try:
            # Загружаем данные из JSON файла и отображаем их в поле
            with open('notes.json', 'r') as file:
                json_notes = json.load(file)
                self.json_display.setPlainText(json.dumps(json_notes, indent=4))
        except FileNotFoundError:
            self.json_display.setPlainText('JSON файл не найден.')
        except Exception as e:
            self.json_display.setPlainText('Ошибка при загрузке данных из JSON файла: {}'.format(e))

    
    def delite_notes(self):
        try:
            # Очищаем содержимое JSON файла
            with open('notes.json', 'w') as file:
                file.write('')
            QMessageBox.information(self, 'Удалено', 'Текст в JSON файле успешно удален.')
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', 'Произошла ошибка при удалении текста в JSON файле: {}'.format(e))


    def delite_text(self):
        self.text_edit.clear()


    def save_notes(self):
        text = self.text_edit.toPlainText()
        if text:
            # Загружаем существующие данные из JSON файла
            with open('notes.json', 'r') as file:
                notes = json.load(file)
            # Добавляем новый текст в список
            notes.append(text)

            # Сохраняем обновленные данные в JSON файл
            with open('notes.json', 'w') as file:
                json.dump(notes, file, indent=4)

            QMessageBox.information(self, 'Сохранено', 'Текст успешно сохранен в JSON файле.')


def main():
    app = QApplication(sys.argv)
    window = SmartNotesApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()