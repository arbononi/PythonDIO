class FiltroSQL:
    def __init__(self):
        self.clausulas = []
        self.parametros = []

    def adicionar_like(self, campo, valor):
        if valor is not None:
            self.clausulas.append(f"{campo} LIKE ?")
            self.parametros.append(f"%{valor}%")

    def adicionar_igual(self, campo, valor):
        if valor is not None:
            self.clausulas.append(f"{campo} = ?")
            self.parametros.append(valor)

    def where_clause(self):
        if self.clausulas:
            return "WHERE " + " AND ".join(self.clausulas)
        return ""

    def get_params(self):
        return self.parametros.copy()