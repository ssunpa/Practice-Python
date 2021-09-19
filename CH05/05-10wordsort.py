word = list('삶꿈정')
word.extend('봄빛')
print(word)
word.sort()
print(word)

fruit = ['복숭아', '자두', '골드키위', '오렌지']
print(fruit)
fruit.sort(reverse=True)
print(fruit)

mix = word + fruit
print(sorted(mix))
print(sorted(mix, reverse=True))
