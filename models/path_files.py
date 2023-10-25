import os


class PathFiles:
    def __init__(self):
        self.path_default = 'W:\\Pessoal\\Fechamento de folha automatizado\\Automação Folha'

    def found_folder_config(self, config, competencia):
        for path in os.listdir(self.path_default):
            if config in path:
                if competencia in os.listdir(os.path.join(self.path_default, path)):
                    competencia = [compet for compet in os.listdir(
                        os.path.join(self.path_default, path)) if compet == competencia][0]
                    self.path_found = os.path.join(
                        self.path_default, path, competencia)

                    return self.path_found


# path = PathFiles()
# path = path.found_folder_config('3', '082023')

# print(path)
