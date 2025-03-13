import sys
import os
import markdown
import re
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWebEngineWidgets import QWebEngineView
from UI import Ui_NoteViewer

class NoteViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NoteViewer()
        self.ui.setupUi(self)

        # Replace placeholder frame with a web view.
        self.webView = QWebEngineView(self)
        self.ui.horizontalLayout.replaceWidget(self.ui.PLACEHOLDER_FRAME, self.webView)
        self.ui.PLACEHOLDER_FRAME.deleteLater()

        # Menu actions.
        self.ui.actionOpen.triggered.connect(self.open_file_dialog)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout_this_program.triggered.connect(self.about_program)
        self.ui.actionAbout_the_creator.triggered.connect(self.about_creator)
        self.ui.actionOtw_rz_pomoc.triggered.connect(self.open_help)
        self.ui.show_toc.triggered.connect(self.toggle_toc)
        self.ui.toc.clicked.connect(self.toc_item_clicked)

        # Theming variables.
        self.text_color = "white"          # "white" or "black"
        self.background_color = "#2a2e32"    # App background color

        self.current_file = None
        self.markdown_content = ""
        self.md_toc_tokens = None

        # Show placeholder text.
        self.show_placeholder()

    def show_placeholder(self):
        placeholder = (
            "# Witaj w Note Viewer!\n"
            "> Aby otworzyć plik, kliknij \"Plik\" i \"Otwórz\" gdzie wybierzesz swój plik *markdown*!"
        )
        md = markdown.Markdown(extensions=['extra', 'nl2br', 'toc'],
                                 extension_configs={'toc': {'permalink': True}})
        html = md.convert(placeholder)
        self.md_toc_tokens = md.toc_tokens
        self.webView.setHtml(self.wrap_html_with_css(html))
        self.build_placeholder_toc()

    def open_file_dialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Otwórz plik Markdown", "", "Pliki tekstowe (*.md *.py *.json *.css *.txt);;Wszystkie pliki (*.*)")
        if fileName:
            self.open_file_path(fileName)

    def open_file_path(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        valid_extensions = {'.md', '.py', '.json', '.css', '.txt'}

        # If not a valid text extension, show error.
        if ext not in valid_extensions:
            QMessageBox.critical(self, "Błąd", "Program nie może otworzyć tego pliku, ponieważ nie jest to dokument tekstowy ani plik Markdown.")
            return

        # If it's a text file but not markdown, warn the user.
        if ext != ".md":
            reply = QMessageBox.question(
                self, "Ostrzeżenie",
                "Wybrany plik nie jest plikiem Markdown. Czy mimo to chcesz go otworzyć?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply != QMessageBox.Yes:
                return

        self.current_file = file_path
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.markdown_content = f.read()
        except Exception as e:
            QMessageBox.critical(self, "Błąd", f"Nie udało się otworzyć pliku:\n{str(e)}")
            return

        md = markdown.Markdown(extensions=['extra', 'nl2br', 'toc'],
                                 extension_configs={'toc': {'permalink': True}})
        html = md.convert(self.markdown_content)
        self.md_toc_tokens = md.toc_tokens
        self.webView.setHtml(self.wrap_html_with_css(html))
        self.build_toc_tokens()

    def wrap_html_with_css(self, html):
        # CSS: use the app's background color, system font, set text color,
        # style blockquotes with a left border, and adjust code styling.
        css = f"""
        <style>
            body {{
                background-color: {self.background_color};
                color: {self.text_color};
                font-family: system-ui, sans-serif;
                margin: 10px;
            }}
            blockquote {{
                border-left: 3px solid #555;
                margin-left: 0;
                padding-left: 10px;
                color: #aaa;
            }}
            /* Inline code outside of pre */
            :not(pre) > code {{
                background-color: #2d2d2d;
                color: {self.text_color};
                border: 1px solid #555;
                border-radius: 3px;
                padding: 2px;
            }}
            /* Code blocks */
            pre {{
                background-color: #2d2d2d;
                color: {self.text_color};
                border: 1px solid #555;
                border-radius: 3px;
                padding: 5px;
                overflow: auto;
            }}
            /* Remove inline code styling inside pre blocks */
            pre code {{
                border: none;
                background: transparent;
                padding: 0;
            }}
            .headerlink {{ display: none; }}
        </style>
        """
        return f"{css}{html}"

    def build_toc_tokens(self):
        model = QStandardItemModel()
        rootItem = model.invisibleRootItem()

        if self.current_file:
            root_name = os.path.splitext(os.path.basename(self.current_file))[0]
        else:
            root_name = "Dokument"
        root = QStandardItem(root_name)
        root.setData("", Qt.UserRole + 1)
        root.setEditable(False)
        rootItem.appendRow(root)

        def add_tokens(tokens, parent):
            for token in tokens:
                name = token.get("name", "")
                anchor = token.get("id", "")
                item = QStandardItem(name)
                item.setData(anchor, Qt.UserRole + 1)
                item.setEditable(False)
                parent.appendRow(item)
                if token.get("children"):
                    add_tokens(token["children"], item)

        if self.md_toc_tokens:
            add_tokens(self.md_toc_tokens, root)
        self.ui.toc.setModel(model)
        self.ui.toc.expandAll()

    def build_placeholder_toc(self):
        model = QStandardItemModel()
        root = QStandardItem("Witaj")
        root.setData("", Qt.UserRole + 1)
        root.setEditable(False)
        model.invisibleRootItem().appendRow(root)
        self.ui.toc.setModel(model)
        self.ui.toc.expandAll()

    def toc_item_clicked(self, index):
        anchor = index.data(Qt.UserRole + 1)
        if anchor:
            js = f"var el = document.getElementById('{anchor}'); if(el) el.scrollIntoView();"
            self.webView.page().runJavaScript(js)

    def about_program(self):
        QMessageBox.information(self, "O programie", "To jest przykład przeglądarki Markdown.")

    def about_creator(self):
        QMessageBox.information(self, "O twórcy", "Stworzone przez dobrego starego przyjaciela.")

    def open_help(self):
        QMessageBox.information(self, "Pomoc", "Program otwiera pliki Markdown, konwertuje je na HTML i generuje spis treści z nagłówków.\nDaj znać, jeśli potrzebujesz instrukcji jak to zrobić.")

    def toggle_toc(self):
        visible = self.ui.show_toc.isChecked()
        self.ui.dockWidget_2.setVisible(visible)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = NoteViewer()
    viewer.setWindowTitle("Note Viewer")

    # If a file is passed as a command line argument, try opening it.
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            viewer.open_file_path(file_path)
        else:
            QMessageBox.critical(viewer, "Błąd", "Podany plik nie istnieje.")

    viewer.show()
    sys.exit(app.exec())
