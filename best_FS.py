graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

h = {
    "A": 7,
    "B": 5,
    "C": 3,
    "D": 8,
    "E": 6,
    "F": 4,
    "G": 0
}

def best_fs(s, g):
    open = [s]
    while open:
        best = open[0]
        for n in open:
            if h[n] < h[best]:
                best = n
        
        print("expand", best)
        if best == g:
            print("goal found:", best)
            return
        
        open.remove(best)
        open += graph[best]

best_fs("A", "G")