def main():
    with open('archivo_creado.txt', 'x') as f:
        f.write('Archivo creado\n')

    with open('archivo_creado.txt', 'a') as f:
        f.write('Se ha anexado este texto al final del archivo\n')

if __name__ == '__main__':
    main()