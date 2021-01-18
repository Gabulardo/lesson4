subj = {}
with open('lesson5-6.txt', 'r') as les:
    for line in les:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
print(f'Общее количество часов по предмету: \n {subj}')
