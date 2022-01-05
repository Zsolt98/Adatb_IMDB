import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter.ttk import Label
import gui_szinesz
import gui_mufaj
import gui_film
import gui_szereplesek
import gui_rendezesek
import gui_film_mufajok
import gui_rendezo
import gui_nemzetek

if __name__ == '__main__':
    root = tk.Tk()
    root.title("IMDb")
    root.geometry("960x640")

    class Logostyle:
        def __init__(self, master) -> None:
            self.master = master
            self.style = Font(self.master, size=25, family='Impact', weight='bold')
            Label(self.master, text="IMDb", font=self.style).pack(pady=5)

    titleLabel = Logostyle(root)

    mainFrame = ttk.Notebook(root)
    mainFrame.pack()

    szineszek_tab = ttk.Frame(mainFrame, width=800, height=600)
    filmek_tab = ttk.Frame(mainFrame, width=800, height=600)
    mufajok_tab = ttk.Frame(mainFrame, width=800, height=600)
    szereplesek_tab = ttk.Frame(mainFrame, width=800, height=600)
    rendezesek_tab = ttk.Frame(mainFrame, width=800, height=600)
    film_mufajok_tab = ttk.Frame(mainFrame, width=800, height=600)
    rendezok_tab = ttk.Frame(mainFrame, width=800, height=600)
    nemzetek_tab = ttk.Frame(mainFrame, width=800, height=600)

    mainFrame.add(nemzetek_tab, text="Nemzetek")
    mainFrame.add(szineszek_tab, text="Színészek")
    mainFrame.add(rendezok_tab, text="Rendezők")
    mainFrame.add(mufajok_tab, text="Műfajok bevitele")
    mainFrame.add(filmek_tab, text="Filmek")
    mainFrame.add(szereplesek_tab, text="Szereplések ")
    mainFrame.add(rendezesek_tab, text="Rendezések")
    mainFrame.add(film_mufajok_tab, text="Film műfajok")

    mainFrame.pack(fill="both", expand=1)

    root.grid_rowconfigure(0, weight=1, pad=10)
    root.grid_columnconfigure(0, weight=1, pad=10)

    root.maxsize(1920, 1080)
    root.minsize(960, 640)

    windowWidth = root.winfo_width()
    #windowHeight = root.winfo_height()

    gui_nemzetek.init_gui(nemzetek_tab, windowWidth)
    gui_szinesz.init_gui(szineszek_tab, windowWidth)
    gui_rendezo.init_gui(rendezok_tab, windowWidth)
    gui_mufaj.init_gui(mufajok_tab, windowWidth)
    gui_film.init_gui(filmek_tab, windowWidth)
    gui_szereplesek.init_gui(szereplesek_tab, windowWidth)
    gui_rendezesek.init_gui(rendezesek_tab, windowWidth)
    gui_film_mufajok.init_gui(film_mufajok_tab, windowWidth)


    root.mainloop()
