from manim import *

class PlotPoints(Scene):
    def construct(self):
        nome_arquivo = "vertices.txt"
        points = []

        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                vertice = [float(coord) for coord in linha.strip().strip('[]').split(',')]
                points.append(tuple(vertice))
                
        nome_arquivo = "triangulos.txt"
        triangulos = []

        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                vertices_str = linha.strip().strip('[]').split('], [')
                triangulo = []
                for v_str in vertices_str:
                    v = [float(coord) for coord in v_str.strip('[]').split(', ')]
                    triangulo.append(v)
                triangulos.append(triangulo) 
        
        # coordenadas_cores = {(0, 0): '#00FF00', (0, 100): '#0000FF', (100, 100): '#FF0000', (100, 0): '#0000FF'}
        coordenadas_cores = {}
        
        
        with open("cores.txt", "r") as arquivo_cores:
            for linha in arquivo_cores:
                coordenadas_cores.update(eval(linha.strip()))
        
        max_x = max(x for x, y in points)
        max_y = max(y for x, y in points)
        min_x = min(x for x, y in points)
        min_y = min(y for x, y in points)
        
        ax = Axes(x_range=[min_x, max_x + 1, 100], y_range=[min_y, max_y + 1, 100])
        self.add(ax)
        
        manim_points = [Dot(point=ax.c2p(x, y), radius=0.1,) for x, y in points]

        for point in manim_points:
            self.add(point)

        lines = [Line(manim_points[i], manim_points[(i + 1) % len(manim_points)]) for i in range(len(manim_points))]
        
        for line in lines:
            self.add(line)

        for triangulo in triangulos:
            vertices_manim = [ax.c2p(x, y) for x, y in triangulo]
            poly = Create(Polygon(*vertices_manim, stroke_color=DARK_BLUE, fill_color=BLUE_B, fill_opacity=0.2), run_time=1)
            self.play(poly)

        manim_points2 = [Create(Dot(point=ax.c2p(x, y), color=coordenadas_cores[x, y], radius=0.1, stroke_width=0.1, stroke_color=BLACK), run_time=1) for x, y in points]
        for i, point in enumerate(manim_points2):
            self.play(point)

        self.wait(1)

# Para renderizar a cena, você pode usar o seguinte comando:
# manim -pql animacao.py PlotPoints (isso gera um vídeo rápido de qualidae 480p)
# Caso queira o vídeo mais bonito possível digite no terminal: manim animacao.py PlotPoints