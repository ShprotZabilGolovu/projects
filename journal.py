class Journal:
    
    
    def __init__(self, klass):
        self.klass = klass
        self.journal = {}
        
    
    def add_subject(self, subject):
        for subject in self.journal:
            self.journal[subject] = {}
            
         
    def add_student(self, students):
        for stud in self.journal:
            self.journal[stud][students] = []


    def rate_students(self, subject, students, mark):
        self.journal[subject][students].append(mark)


if __name__ == '__main__':
    journal_1 = Journal('10 Б')
    journal_1.add_student(['Пётр Васин', 'Вовочка', 'Антон'])
    journal_1.add_subject('Анuлийский')
    journal_1.add_subject('Програмирование')
    journal_1.rate_students('Програмирование', 'Вовочка', 5)
    journal_1.rate_students('Английский', 'Антон', 2)
    print(journal_1.journal)            
            