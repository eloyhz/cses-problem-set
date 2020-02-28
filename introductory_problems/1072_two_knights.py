def knights(k):
    return (
            k * k * (k * k - 1)         # All possible combinations to put two knights
            - 4 * 2                     # Four corners attack 2 squares
            - 8 * 3                     # Squares next to corners attack 3 squares
            - (k - 4) * 4 * 4           # Each other square on the border attack 4 squares by 4 sides
                                        # (k - 4) because 2 corners and 2 next-to-corners squares already counted
            - 4 * 4                     # Four corners second layer attack 4 squares
            - (k - 4) * 4 * 6           # Squares next to corners on second layer attack 6 squares
            - (k - 4) * (k - 4) * 8     # The center squares
            ) // 2                      # Divided by two because doesn't matter the knights order


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(knights(i + 1))
