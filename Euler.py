import matplotlib.pyplot as plt

def function(x, y):
    return x + y

def Euler(x0, y0, h, nombre_etapes):
    x_values = [x0]
    y_values = [y0]

    for i in range(nombre_etapes):
        x = x_values[-1]
        y = y_values[-1]

        pente = function(x, y)
        y = y + h * pente
        x = x + h

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

if __name__ == "__main__":
    x0 = float(input("Entrez la valeur initiale de x: "))
    y0 = float(input("Entrez la valeur initiale de y: "))
    h = float(input("Entrez la taille du pas h: "))
    nombre_etapes = int(input("Entrez le nombre d'étapes: "))

    x_values, y_values = Euler(x0, y0, h, nombre_etapes)

    # Tracer la courbe
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Méthode d\'Euler')
    plt.show()