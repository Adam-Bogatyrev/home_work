from docx import Document

def create_word_file(text):
    document = Document()
    document.add_paragraph(text)
    document.save('output.docx')

if __name__ == "__main__":
    text = input("Введите текст для сохранения в Word-файле: ")
    create_word_file(text)
    print("Word-файл успешно создан!")
