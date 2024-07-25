import fitz  # PyMuPDF

def split_pdf_on_term(input_pdf_path, output_pdf_path, split_term):
    input_pdf = fitz.open(input_pdf_path)
    output_pdf = fitz.open()

    for page_num in range(len(input_pdf)):
        page = input_pdf.load_page(page_num)
        page_text = page.get_text("text")
        
        notes = page_text.split(split_term)
        for i, note in enumerate(notes):
            if i > 0:
                note = split_term + note
            new_page = output_pdf.new_page(width=page.rect.width, height=page.rect.height)
            text_lines = note.split('\n')
            cursor_y = 50  
            for line in text_lines:
                new_page.insert_text((50, cursor_y), line, fontsize=11)
                cursor_y += 15  
    
    output_pdf.save(output_pdf_path)
    output_pdf.close()

input_pdf_path = ## Caminho do PDF que deseja separar as páginas
output_pdf_path = ## Caminho de saída do PDF já separado

split_term = # Inserir termo a ser localizado para fazer a quebra

split_pdf_on_term(input_pdf_path, output_pdf_path, split_term)

print("PDF split completed.")
