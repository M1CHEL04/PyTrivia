import csv

def leer_dataset (file_path): #agregar excepcion
    """
      This function receives a csv file and returns its header and data separated
    """
    try:
        with open(file_path,"r",encoding="UTF-8",newline='\n')as file:
            csv_reader=csv.reader(file,delimiter=",")
            header=next(csv_reader)
            data=list(csv_reader)
    except FileNotFoundError:
        print("No se encontró el archivo.")
    return header,data

def escribir_dataset(file_path,header,data):
    """
        This function writes in a new file the header and data received from the parameters
    """
    try:
        with open(file_path,"w",encoding="UTF-8", newline='\n')as file_out:
            writer=csv.writer(file_out)
            writer.writerow(header)
            writer.writerows(data)
    except FileNotFoundError:
        print("No se encontró el archivo.")

def eliminar_tilde_texto(text):
    """
        This function removes the accent marks from the string received    
    """
    vowels_with_accent_marks={'á':'a',
                       'é':'e',
                       'í':'i',
                       'ó':'o',
                       'ú':'u',
                       'Á':'A',
                       'É':'E',
                       'Í':'I',
                       'Ó':'O',
                       'Ú':'U'}
    copy_text=text
    for accent_mark,without_accent_mark in vowels_with_accent_marks.items():
        copy_text=copy_text.replace(accent_mark,without_accent_mark)
    return copy_text

def sin_tildes_csv(dataset):
    """
        This function removes the accent marks from the dataset received by parameter    
    """
    header,data=leer_dataset(dataset)
    #Creo una lista para eliminar el encabezado sin tildes
    clean_header=[]
    for col in header:
        clean_text=eliminar_tilde_texto(col)
        clean_header.append(clean_text)

    #Creo una lista para eliminar los datos sin tildes
    clean_data=[]
    for row in data:
        #Creo una lista para eliminar las filas sin tildes
        clean_row=[]
        for cell in row:
            clean_text=eliminar_tilde_texto(cell)
            clean_row.append(clean_text)
        clean_data.append(clean_row)

    escribir_dataset(dataset,clean_header,clean_data)