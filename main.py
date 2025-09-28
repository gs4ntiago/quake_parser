
def contarKills(aruivoTeste):
    placar = dict()
    try:
        with open(aruivoTeste, 'r', encoding="utf-8") as arquivo:
            for linhas in arquivo:
                linhas = linhas.strip()
                if "killed" not in linhas:
                    continue


                try:
                    partes = linhas.split()
                    idxKilled = partes.index("killed")
                    idxBy = partes.index("by")
                    killer = " ".join(partes[5:idxKilled ])
                    victim = " ".join(partes[idxKilled + 1:idxBy])

                    if victim not in placar:
                        placar[victim] = 0
                    if killer == "<world>" or killer == victim:
                        placar[victim] -= 1
                    else:
                        if killer not in placar:
                            placar[killer] = 0
                        placar[killer] += 1

                except ValueError:
                    continue
        return placar
    except FileNotFoundError:
        print("o arquivo nao foi encontrado")
        return {}


totalKills = contarKills("games.txt")
print("\n=====Scoreboard=====")
for player, score in sorted(totalKills.items(), key=lambda x: x[1], reverse=True):
    print(f"{player}: {score}")
