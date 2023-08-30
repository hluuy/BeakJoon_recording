plates = input()
height =10
setting = []
for i in range(len(plates)):
    setting.append(plates[i])
    if len(setting) > 1:
        if plates[i] == setting[i - 1]:
            height += 5
        else:
            height += 10
print(height)