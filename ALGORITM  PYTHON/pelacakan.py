from collections import deque

peta = {
    'A': ['B','C'],
    'B': ['A', 'D', 'E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','F']
}

def pelacakan_buta(graph, titikAwal, tujuan):
    dikunjungi = set()
    antrean = deque([(titikAwal, [titikAwal])])

    while antrean:
        titik_sekarang, rute = antrean.popleft()

        if titik_sekarang == tujuan:
            return rute
        
        if titik_sekarang not in dikunjungi:
            dikunjungi.add(titik_sekarang)

            for tetangga in graph[titik_sekarang]:
                if tetangga not in dikunjungi:
                    antrean.append((tetangga, rute + [tetangga]))

    return "Jalur tidak ditemukan" 

awal = 'A'
target = 'F'

print(f"AI sedang mencari jalan dari {awal} ke {target}...")
rute_ditemukan = pelacakan_buta(peta, awal, target)

print("Berhasil! Rute terpendek ditemukan:", rute_ditemukan)


