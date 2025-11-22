class Journal:
    
    
    def __init__(self, klass):
        self.klass = klass
        self.journal = {}
    
    
    def add_subjects(self, subject):      
        for subj in self.journal:
            self.journal[subj][subject] = []
            
    
    def add_student(self, students):
        for student in students:
            self.journal[students] = {}
            
    
    def rate_students(self, stundents, subject, mark):
        self.journal[students][subject].append(mark)
        

if __name__ == '__main__':
    journal_1 = Journal('10 Б')
    journal_1.add_student(['Пётр Васин', 'Вовочка', 'Антон'])
    journal_1.add_subjects('Английский язык')
    journal_1.add_subjects('Программирование')
    journal_1.add_subjects('Программирование')
    journal_1.rate_students('Вовочка', 'Программирование', 4)
    journal_1.rate_students('Вовочка', 'Программирование', 5)
    journal_1.rate_students('Вовочка', 'Английский язык', 3)
    journal_1.rate_students('Вовочка', 'Программирование', 5)
    journal_1.rate_students('Вовочка', 'Английский язык', 5)
    journal_1.rate_students('Вовочка', 'Программирование', 1)
    print(journal_1.journal)