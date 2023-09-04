import random

class Carta:
    def __init__(self, pinta, valor):
        self.pinta = pinta
        self.valor = valor

class Baraja:
    def __init__(self):
        self.cartas = [Carta(pinta, valor) for pinta in ['Corazón', 'Trebol', 'Diamante', 'Esparada'] for valor in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]
        random.shuffle(self.cartas)
    
    def repartir_carta(self):
        return self.cartas.pop()

class Mano:
    def __init__(self):
        self.cartas = []
    
    def agregar_carta(self, carta):
        self.cartas.append(carta)
    
    def calcular_valor(self):
        valor = 0
        ases = 0
        
        for carta in self.cartas:
            if carta.valor in ['J', 'Q', 'K']:
                valor += 10
            elif carta.valor == 'A':
                ases += 1
            else:
                valor += int(carta.valor)
        
        for _ in range(ases):
            if valor + 11 <= 21:
                valor += 11
            else:
                valor += 1
        
        return valor

class Jugador:
    def __init__(self, nombre, fichas=100):
        self.nombre = nombre
        self.fichas = fichas
        self.mano = Mano()
    
    def realizar_apuesta(self):
        while True:
            apuesta = int(input(f'{self.nombre}, Tienes {self.fichas} fichas.\nRealiza tu apuesta: '))
            if apuesta <= self.fichas:
                return apuesta
            else:
                print('No tienes suficientes fichas para esa apuesta.\n')
    
    def mostrar_mano(self):
        print(f'Mano de {self.nombre}: {[f"{carta.valor} de {carta.pinta}" for carta in self.mano.cartas]}\n')

class Blackjack:
    def __init__(self):
        self.baraja = Baraja()
        self.jugador = Jugador(input('Ingresa tu nombre: '))
    
    def Menu(self):
        while self.jugador.fichas > 0:
            self.jugador.mano = Mano()
            self.casa = Jugador('Casa', fichas=0)
            
            apuesta = self.jugador.realizar_apuesta()
            
            
            self.jugador.mano.agregar_carta(self.baraja.repartir_carta())
            self.jugador.mano.agregar_carta(self.baraja.repartir_carta())
            self.casa.mano.agregar_carta(self.baraja.repartir_carta())
            self.casa.mano.agregar_carta(self.baraja.repartir_carta())
            
           
            self.jugador.mostrar_mano()
            print(f'Una de las cartas de la casa: {self.casa.mano.cartas[0].valor} de {self.casa.mano.cartas[0].pinta}\n')
            
            
            while self.jugador.mano.calcular_valor() < 21:
                opcion = input('¿Quieres una nueva carta (1) o parar (2)? \n').upper()
                if opcion == '1':
                    nueva_carta = self.baraja.repartir_carta()
                    self.jugador.mano.agregar_carta(nueva_carta)
                    self.jugador.mostrar_mano()
                elif opcion == '2':
                    break
            
            
            while self.casa.mano.calcular_valor() < 17:
                nueva_carta = self.baraja.repartir_carta()
                self.casa.mano.agregar_carta(nueva_carta)
            
            
            self.jugador.mostrar_mano()
            print(f'Mano de la casa: {[f"{carta.valor} de {carta.pinta}" for carta in self.casa.mano.cartas]}\n')
            
            
            if self.jugador.mano.calcular_valor() > 21:
                print(f'{self.jugador.nombre}, te has pasado de 21. Pierdes {apuesta} fichas.\n')
                self.jugador.fichas -= apuesta
            elif self.casa.mano.calcular_valor() > 21 or self.jugador.mano.calcular_valor() > self.casa.mano.calcular_valor():
                print(f'{self.jugador.nombre}, ganas {apuesta} fichas!\n')
                self.jugador.fichas += apuesta
            elif self.jugador.mano.calcular_valor() == self.casa.mano.calcular_valor():
                print('Empate. Recibes de vuelta tu apuesta.\n')
            else:
                print(f'{self.jugador.nombre}, pierdes {apuesta} fichas.')
                self.jugador.fichas -= apuesta
            
            continuar = input('¿Quieres seguir con la partida (Y/N)? \n').upper()
            if continuar != 'Y':
                break
        
        print(f'Juego finalizado, {self.jugador.nombre}.\nTienes {self.jugador.fichas} fichas restantes.\n')


if __name__ == "__main__":
    juego = Blackjack()
    juego.Menu()
