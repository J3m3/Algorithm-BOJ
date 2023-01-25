def fractal_stars(n):
    if n == 1:
        return ['*']

    stars = fractal_stars(n // 3)
    result = []

    for star in stars:
        result.append(star * 3)
    for star in stars:
        result.append(star + ' ' * (n // 3) + star)
    for star in stars:
        result.append(star * 3)

    return result

print('\n'.join(fractal_stars(int(input()))))