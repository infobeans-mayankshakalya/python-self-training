students={'john': ['Java', 'Python', 'C++'],
          'doe': ['JavaScript', 'HTML', 'CSS'],
          'jane': ['Ruby', 'Go', 'Swift'],
          'smith': ['PHP', 'Perl', 'Rust'],
          'alice': ['Kotlin', 'Scala', 'Haskell']}

keys = students.keys()
for eachKey in keys:
    print(f"Student: {eachKey}, Subjects: {students[eachKey]}")