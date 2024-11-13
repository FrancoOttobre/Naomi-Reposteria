from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_tortas = [35000, 28000, 25000 , 40000]
precios_cupcakes = [800, 900 , 1000, 1100]
precios_masas = [800 , 650 , 600 , 550 ]


def click_boton(numero):
    global operador
    operador = operador + numero

def borrar():
    global operador
    operador = ''

# def obtener_resultado():
#     global operador
#     resultado = str(eval(operador))
#     visor_calculadora.delete(0, END)
#     visor_calculadora.insert(0, resultado)
#     operador = ''


def revisar_check():
    x = 0
    for c in cuadros_torta:
        if variables_torta[x].get() == 1:
            cuadros_torta[x].config(state=NORMAL)
            if cuadros_torta[x].get() == '0':
                cuadros_torta[x].delete(0, END)
            cuadros_torta[x].focus()
        else:
            cuadros_torta[x].config(state=DISABLED)
            texto_torta[x].set('0')
        x += 1

    x = 0
    for c in cuadros_cupcakes:
        if variables_cupcakes[x].get() == 1:
            cuadros_cupcakes[x].config(state=NORMAL)
            if cuadros_cupcakes[x].get() == '0':
                cuadros_cupcakes[x].delete(0, END)
            cuadros_cupcakes[x].focus()
        else:
            cuadros_cupcakes[x].config(state=DISABLED)
            texto_cupcakes[x].set('0')
        x += 1

    x = 0
    for c in cuadros_masas:
        if variables_masas[x].get() == 1:
            cuadros_masas[x].config(state=NORMAL)
            if cuadros_masas[x].get() == '0':
                cuadros_masas[x].delete(0, END)
            cuadros_masas[x].focus()
        else:
            cuadros_masas[x].config(state=DISABLED)
            texto_masas[x].set('0')
        x += 1


def total():
    sub_total_tortas = 0
    p = 0
    for cantidad in texto_torta:
        sub_total_tortas = sub_total_tortas + (float(cantidad.get()) * precios_tortas[p])
        p += 1

    sub_total_cupcakes = 0
    p = 0
    for cantidad in texto_cupcakes:
        sub_total_cupcakes = sub_total_cupcakes + (float(cantidad.get()) * precios_cupcakes[p])
        p += 1

    sub_total_masas = 0
    p = 0
    for cantidad in texto_masas:
        sub_total_masas = sub_total_masas + (float(cantidad.get()) * precios_masas[p])
        p += 1

    sub_total = sub_total_tortas + sub_total_cupcakes + sub_total_masas
    impuestos = sub_total * 0.10
    total = sub_total + impuestos

    var_costo_tortas.set(f'$ {round(sub_total_tortas, 2)}')
    var_costo_cupcakes.set(f'$ {round(sub_total_cupcakes, 2)}')
    var_costo_masas.set(f'$ {round(sub_total_masas, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for torta in texto_torta:
        if torta.get() != '0':
            texto_recibo.insert(END, f'{lista_tortas[x]}\t\t{torta.get()}\t'
                                     f'$ {int(torta.get()) * precios_tortas[x]}\n')
        x += 1

    x = 0
    for cupcake_alf in texto_cupcakes:
        if cupcake_alf.get() != '0':
            texto_recibo.insert(END, f'{lista_cupcakes_alfajores[x]}\t\t{cupcake_alf.get()}\t'
                                     f'$ {int(cupcake_alf.get()) * precios_cupcakes[x]}\n')
        x += 1

    x = 0
    for masa in texto_masas:
        if masa.get() != '0':
            texto_recibo.insert(END, f'{lista_masas[x]}\t\t{masa.get()}\t'
                                     f'$ {int(masa.get()) * precios_masas[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Total de las Tortas: \t\t\t{var_costo_tortas.get()}\n')
    texto_recibo.insert(END, f' Total Cupcakes/alf: \t\t\t{var_costo_cupcakes.get()}\n')
    texto_recibo.insert(END, f' Total Masas: \t\t\t{var_costo_masas.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Sub-total (Efectivo): \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Recargo ( 10%): \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total (Tarjeta): \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_masas:
        texto.set('0')
    for texto in texto_cupcakes:
        texto.set('0')
    for texto in texto_masas:
        texto.set('0')

    for cuadro in cuadros_cupcakes:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_cupcakes:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_masas:
        cuadro.config(state=DISABLED)

    for v in variables_torta:
        v.set(0)
    for v in variables_cupcakes:
        v.set(0)
    for v in variables_masas:
        v.set(0)

    var_costo_tortas.set('')
    var_costo_cupcakes.set('')
    var_costo_masas.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1248x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title("Repostería Artesanal Naomi - Sistema de Facturacion")

# color de fondo de la ventana
aplicacion.config(bg='#F6EBE7')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Dosis', 58), bg='#F6EBE7', width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_tortas = LabelFrame(panel_izquierdo, text='Tortas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_tortas.pack(side=LEFT)

# panel bebidas
panel_cupcakes_alfajores = LabelFrame(panel_izquierdo, text='Cupcakes/Alfajores', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_cupcakes_alfajores.pack(side=LEFT)

# panel postres
panel_masas = LabelFrame(panel_izquierdo, text='Variedad de Masas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_masas.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
# panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
# panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# lista de productos
lista_tortas = ['Selva Negra', 'Carrot Cake', 'Lemon Pie', 'Imperial Ruso']
lista_cupcakes_alfajores = ['Vainilla', 'Oreo', 'Relleno ddl', 'Coco']
lista_masas = ['Donas','Churros','Galletas','Scones']

# generar items tortas
variables_torta = []
cuadros_torta = []
texto_torta = []
contador = 0
for torta in lista_tortas:
    # crear checkbutton
    variables_torta.append('')
    variables_torta[contador] = IntVar()
    torta = Checkbutton(panel_tortas,
                         text=torta.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_torta[contador],
                         command=revisar_check)

    torta.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_torta.append('')
    texto_torta.append('')
    texto_torta[contador] = StringVar()
    texto_torta[contador].set('0')
    cuadros_torta[contador] = Entry(panel_tortas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_torta[contador])
    cuadros_torta[contador].grid(row=contador,
                                  column=1)
    contador += 1

# generar items bebida
variables_cupcakes = []
cuadros_cupcakes = []
texto_cupcakes = []
contador = 0
for cupcake in lista_cupcakes_alfajores:
    # crear checkbutton
    variables_cupcakes.append('')
    variables_cupcakes[contador] = IntVar()
    cupcake = Checkbutton(panel_cupcakes_alfajores,
                         text=cupcake.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_cupcakes[contador],
                         command=revisar_check)
    cupcake.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_cupcakes.append('')
    texto_cupcakes.append('')
    texto_cupcakes[contador] = StringVar()
    texto_cupcakes[contador].set('0')
    cuadros_cupcakes[contador] = Entry(panel_cupcakes_alfajores,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_cupcakes[contador])
    cuadros_cupcakes[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items postres
variables_masas = []
cuadros_masas = []
texto_masas = []
contador = 0
for masa in lista_masas:
    # crear checkbutton
    variables_masas.append('')
    variables_masas[contador] = IntVar()
    masa = Checkbutton(panel_masas,
                          text=masa.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_masas[contador],
                         command=revisar_check)
    masa.grid(row=contador,
                 column=0,
                 sticky=W)

    # crear los cuadros de entrada
    cuadros_masas.append('')
    texto_masas.append('')
    texto_masas[contador] = StringVar()
    texto_masas[contador].set('0')
    cuadros_masas[contador] = Entry(panel_masas,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_masas[contador])
    cuadros_masas[contador].grid(row=contador,
                                   column=1)
    contador += 1


# variables
var_costo_tortas = StringVar()
var_costo_cupcakes = StringVar()
var_costo_masas = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada
etiqueta_costo_torta = Label(panel_costos,
                              text='Costo Tortas',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_torta.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_tortas)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_cupcakes = Label(panel_costos,
                              text='Costo Cupcakes/Alf',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_cupcakes.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_cupcakes)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postres = Label(panel_costos,
                              text='Costo Masas',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_masas)
texto_costo_postres.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal (Efectivo)',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                              text='Recargo (Tarjeta 10%)',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                              text='Total (Tarjeta)',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

# # calculadora
# visor_calculadora = Entry(panel_calculadora,
#                           font=('Dosis', 16, 'bold'),
#                           width=32,
#                           bd=1)
# visor_calculadora.grid(row=0,
#                        column=0,
#                        columnspan=4)

# botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
#                        '1', '2', '3', 'x', 'R', 'B', '0', '/']
# botones_guardados = []

# fila = 1
# columna = 0
# for boton in botones_calculadora:
#     boton = Button(panel_calculadora,
#                    text=boton.title(),
#                    font=('Dosis', 16, 'bold'),
#                    fg='white',
#                    bg='azure4',
#                    bd=1,
#                    width=8)

#     botones_guardados.append(boton)

#     boton.grid(row=fila,
#                column=columna)

#     if columna == 3:
#         fila += 1

#     columna += 1

#     if columna == 4:
#         columna = 0

# botones_guardados[0].config(command=lambda : click_boton('7'))
# botones_guardados[1].config(command=lambda : click_boton('8'))
# botones_guardados[2].config(command=lambda : click_boton('9'))
# botones_guardados[3].config(command=lambda : click_boton('+'))
# botones_guardados[4].config(command=lambda : click_boton('4'))
# botones_guardados[5].config(command=lambda : click_boton('5'))
# botones_guardados[6].config(command=lambda : click_boton('6'))
# botones_guardados[7].config(command=lambda : click_boton('-'))
# botones_guardados[8].config(command=lambda : click_boton('1'))
# botones_guardados[9].config(command=lambda : click_boton('2'))
# botones_guardados[10].config(command=lambda : click_boton('3'))
# botones_guardados[11].config(command=lambda : click_boton('*'))
# botones_guardados[12].config(command=obtener_resultado)
# botones_guardados[13].config(command=borrar)
# botones_guardados[14].config(command=lambda : click_boton('0'))
# botones_guardados[15].config(command=lambda : click_boton('/'))



# evitar que la pantalla se cierre
aplicacion.mainloop()