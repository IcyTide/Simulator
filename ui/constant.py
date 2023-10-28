def embed_cof(level):
    if level > 6:
        return (level * 0.65 - 3.2) * 1.3
    else:
        level * 0.195


def strength_cof(level):
    return level * (0.7 + 0.3 * level) / 200

