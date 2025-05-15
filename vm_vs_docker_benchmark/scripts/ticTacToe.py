import time

def play_tic_tac_toe(rounds=100):
    # Simula rounds de juego con cálculos para que consuma CPU
    board = [' '] * 9
    players = ['X', 'O']
    for r in range(rounds):
        for i in range(9):
            board[i] = players[r % 2]
        # Simula algún cálculo
        total = sum([ord(c) for c in board])
        time.sleep(0.05)  # pausita para simular proceso
    print("Game finished")

if __name__ == "__main__":
    play_tic_tac_toe()
