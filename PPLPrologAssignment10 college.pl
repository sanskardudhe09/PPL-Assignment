teacher(teacher1, course1).
teacher(teacher2, course2).
teacher(teacher3, course3).
teacher(teacher4, course4).
teacher(teacher5, course5).
teacher(teacher1, course2).
teacher(teacher2, course3).
teacher(teacher3, course4).
enrolled(sam, course1).
enrolled(sam, course2).
enrolled(robin, course3).
enrolled(robin, course4).
enrolled(peter, course1).
enrolled(peter, course2).
enrolled(peter, course3).
enrolled(jenny, course1).
enrolled(jenny, course2).
enrolled(jenny, course3).
enrolled(jenny, course4).
enrolled(jenny, course5).
teaches(P,S):-teacher(P,C),enrolled(S,C).
