population = input().split(', ')
possible_wealth = [int(n) for n in population]
minimum_wealth = int(input())
max_wealth = possible_wealth.index(max(possible_wealth))
new_population = []
if (sum(possible_wealth) / len(possible_wealth)) < minimum_wealth:
    print('No equal distribution possible')
    exit()
for people in possible_wealth:
    if people < minimum_wealth:
        max_wealth = possible_wealth.index(max(possible_wealth))
        needed_wealth = minimum_wealth - people
        people += needed_wealth
        possible_wealth[max_wealth] -= needed_wealth
    new_population.append(people)
print(new_population)
