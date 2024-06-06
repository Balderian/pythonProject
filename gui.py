import tkinter as tk
from tkinter import ttk
from estonian_people_analyzer import EstonianPeopleAnalyzer

class GUI:
    def __init__(self, data):
        self.analyzer = EstonianPeopleAnalyzer(data)
        self.root = tk.Tk()
        self.root.title("Eesti Inimeste Analüsaator")

        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=('value'), show='tree')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.column('#0', width=800, stretch=True)
        self.tree.column('value', width=800, stretch=True)

        self.populate_data()

    def populate_data(self):
        results = self.analyzer.analyze_data()

        self.tree.insert('', 'end', text=f'Isikute koguarv: {results["total_count"]}', values=())
        self.tree.insert('', 'end', text=f'Kõige pikem nimi: {results["longest_name"][0]} (Pikkus: {results["longest_name"][1]})', values=())
        self.tree.insert('', 'end', text=f'Kõige vanem elav: {results["oldest_alive"][0]} (Vanus: {results["oldest_alive"][1]}, Sünniaeg: {results["oldest_alive"][2]})', values=())
        self.tree.insert('', 'end', text=f'Kõige vanem surnud: {results["oldest_deceased"][0]} (Vanus: {results["oldest_deceased"][1]}, Sünniaeg: {results["oldest_deceased"][2]}, Surmaaeg: {results["oldest_deceased"][3]})', values=())
        self.tree.insert('', 'end', text=f'Näitlejate arv: {results["actors_count"]}', values=())
        self.tree.insert('', 'end', text=f'Sündinud aastal 1997: {results["born_in_1997_count"]}', values=())
        self.tree.insert('', 'end', text=f'Erinevate ametite arv: {results["unique_roles_count"]}', values=())
        self.tree.insert('', 'end', text=f'Rohkem kui kahe nimega isikute arv: {results["more_than_two_names_count"]}', values=())
        self.tree.insert('', 'end', text=f'Sama sünni- ja surmakuupäevaga isikute arv: {results["same_birth_and_death_day_count"]}', values=())
        self.tree.insert('', 'end', text=f'Elus: {results["alive_count"]}', values=())
        self.tree.insert('', 'end', text=f'Surnud: {results["deceased_count"]}', values=())

    def run(self):
        self.root.mainloop()