from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.Pakuri_list = []


    def get_size(self):
        return len(self.Pakuri_list)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if self.Pakuri_list:
            return [pakuri.get_species() for pakuri in self.Pakuri_list]
        else:
            return None

    def get_stats(self, species):
        for pakuri in self.Pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    def sort_pakuri(self):
        self.Pakuri_list.sort(key=lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):
        if len(self.Pakuri_list) >= self.capacity:
            return False
        for pakuri in self.Pakuri_list:
            if pakuri.get_species() == species:
                return False
        self.Pakuri_list.append(Pakuri(species))
        return True

    def evolve_species(self, species):
        for pakuri in self.Pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True

        return False