import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageSequence, ImageOps
import random
import binascii
from bitarray import bitarray

from err_generator import generate_noice, generate_spaces
from correct import correct, load_model

from resize_gif_img import transform_image

gif_filename = r'chimuelo-toothless.gif'
sg.theme('DarkAmber')

generate_layout = [  [sg.Text('  incert input file path:', font='Roboto', size=25), sg.InputText(default_text='input.txt', font='Roboto', size=25)],
            [sg.Text('  incert output file path:', font='Roboto', size=25), sg.InputText(default_text='output.txt',font='Roboto', size=25)],
            [sg.Text('  incert spaces file path:', font='Roboto', size=25), sg.InputText(default_text='spaces.txt',font='Roboto', size=25)],
            [sg.Button('generate spaces', font='Roboto', size=25), sg.Button('generate errors', font='Roboto', size=25)],
            [sg.Text('                      error percent:', font='Roboto', size=25), sg.Slider(orientation ='horizontal', key='stSlider',expand_x = 1, range=(0,100), resolution =0.1)],
            [sg.Multiline(' Первоначальные данные\n', size=(50, 8), key='-ML1-', font='Roboto')],
            [sg.Multiline(' Битый вывод\n', size=(50, 8), key='-ML2-', font='Roboto')],
            [sg.Image(key='-IMAGE1-'),sg.Image(key='-IMAGE2-'),sg.Image(key='-IMAGE3-'),sg.Image(key='-IMAGE4-'),sg.Image(key='-IMAGE5-'),sg.Image(key='-IMAGE6-')]]

correct_layout = [  [sg.Text(' Correct input', font='Roboto', size=25), sg.Button('load model', font='Roboto', size=25)],
                    [sg.Text('  iterate:', font='Roboto', size=25), sg.Button('correct', font='Roboto', size=25)],
                    [sg.Multiline(' Финальный вывод\n', size=(50,8), key='-ML3-', font='Roboto')]]

layout = [[sg.Column(generate_layout, element_justification='c', grab=True),
           sg.VSeperator(),
           sg.Column(correct_layout, element_justification='c')]]

#layout = [  [sg.Text('  Jamspell correct:', font='Roboto', size=25), sg.InputText(font='Roboto', size=25), sg.Push()],
#            [sg.Text('  incert output file path:', font='Roboto', size=25), sg.InputText(font='Roboto', size=25), sg.Push()],
#            [sg.Text('  incert spaces file path:', font='Roboto', size=25), sg.InputText(font='Roboto', size=25), sg.Push()],
#            [sg.Button('generate spaces', font='Roboto', size=25), sg.Button('generate errors', font='Roboto', size=25), sg.Push()],
#            [sg.Text('  error percent:', font='Roboto', size=25), sg.Slider(orientation ='horizontal', key='stSlider', range=(1,100)), sg.Push()],
#            [sg.Multiline(' Первоначальные данные\n', size=(80,10), key='-ML1-', font='Roboto')],
#            [sg.Multiline(' Битый вывод\n', size=(80, 10), key='-ML2-', font='Roboto')],
#            [sg.Image(key='-IMAGE1-'),sg.Image(key='-IMAGE2-'),sg.Image(key='-IMAGE3-'),sg.Image(key='-IMAGE4-'),sg.Image(key='-IMAGE5-'),sg.Image(key='-IMAGE6-'),sg.Image(key='-IMAGE7-')]]

# Create the Window
window = sg.Window('NeuroCorrect', layout, element_justification='c', margins=(1,1), element_padding=(1,1), finalize=True)
#window.Maximize()
turbo_gif=Image.open(gif_filename)


interframe_duration = turbo_gif.info['duration']     # get how long to delay between frames
#turbo_gif=ImageOps.scale(turbo_gif, 0.5, resample=Image.Resampling.BICUBIC)
turbo_gif=transform_image(turbo_gif, 100, 100)

mline1:sg.Multiline = window['-ML1-']
mline2:sg.Multiline = window['-ML2-']
mline3:sg.Multiline = window['-ML3-']


while True:
    for frame in turbo_gif:
        event, values = window.read(timeout=interframe_duration)
        if event == sg.WIN_CLOSED:
            exit(0)
        if event == 'generate errors':
            err_inp, s_inp = generate_noice(values[0], values[1], values['stSlider'])
            mline1.print(s_inp)
            mline2.print(err_inp)

            print("Generated")
        if event == 'generate spaces':
            generate_spaces(values[0], values[2])
            print("Generated")

        if event == 'load model':
            global jsp
            global spell
            jsp, spell, str_o= load_model(values[0], values[2])
            mline2.print(str_o)
            print("loaded")
        if event == 'correct':
            str_out, str_t=correct(values[1], values[1], values[2])
            mline3.print(str_out)
            mline3.print(str_t)
            print("corrected")

        #print(values[3])
        window['-IMAGE1-'].update(data=ImageTk.PhotoImage(frame))
        window['-IMAGE2-'].update(data=ImageTk.PhotoImage(frame))
        window['-IMAGE3-'].update(data=ImageTk.PhotoImage(frame))
        window['-IMAGE4-'].update(data=ImageTk.PhotoImage(frame))
        window['-IMAGE5-'].update(data=ImageTk.PhotoImage(frame))
        window['-IMAGE6-'].update(data=ImageTk.PhotoImage(frame))

window.close()


