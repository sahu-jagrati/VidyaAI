export const questions = [
  // QUANTITATIVE APTITUDE
  {
    id: 1, subject: 'Quantitative Aptitude', subjectCode: 'quant', difficulty: 'easy',
    question: 'If 25% of a number is 120, what is 60% of that number?',
    options: { A: '288', B: '256', C: '300', D: '240' },
    correct_answer: 'A', xp: 5,
    explanation: '25% = ¼, so 100% = 120 × 4 = 480. Therefore 60% of 480 = 480 × 0.6 = 288.',
  },
  {
    id: 2, subject: 'Quantitative Aptitude', subjectCode: 'quant', difficulty: 'medium',
    question: 'A train travels 360 km in 4 hours. What is its speed in m/s?',
    options: { A: '20 m/s', B: '25 m/s', C: '30 m/s', D: '15 m/s' },
    correct_answer: 'B', xp: 10,
    explanation: 'Speed = 360 ÷ 4 = 90 km/h. Convert: 90 × (1000/3600) = 25 m/s.',
  },
  {
    id: 3, subject: 'Quantitative Aptitude', subjectCode: 'quant', difficulty: 'hard',
    question: 'Compound interest on Rs. 8000 at 10% per annum for 2 years is:',
    options: { A: 'Rs. 1,600', B: 'Rs. 1,680', C: 'Rs. 1,800', D: 'Rs. 1,720' },
    correct_answer: 'B', xp: 20,
    explanation: 'CI = P[(1+r/100)ⁿ−1] = 8000[(1.1)²−1] = 8000 × 0.21 = Rs. 1,680.',
  },
  {
    id: 4, subject: 'Quantitative Aptitude', subjectCode: 'quant', difficulty: 'easy',
    question: 'What is the LCM of 12, 18, and 24?',
    options: { A: '36', B: '48', C: '72', D: '96' },
    correct_answer: 'C', xp: 5,
    explanation: '12=2²×3, 18=2×3², 24=2³×3. LCM = 2³×3² = 8×9 = 72.',
  },
  {
    id: 5, subject: 'Quantitative Aptitude', subjectCode: 'quant', difficulty: 'medium',
    question: 'A shopkeeper sells a product for Rs. 480 at a 20% profit. What is the cost price?',
    options: { A: 'Rs. 380', B: 'Rs. 400', C: 'Rs. 420', D: 'Rs. 360' },
    correct_answer: 'B', xp: 10,
    explanation: 'SP = CP × 1.2 → 480 = CP × 1.2 → CP = Rs. 400.',
  },
  // REASONING
  {
    id: 6, subject: 'Reasoning', subjectCode: 'reasoning', difficulty: 'easy',
    question: 'Complete the series: 2, 6, 12, 20, 30, __',
    options: { A: '40', B: '42', C: '44', D: '46' },
    correct_answer: 'B', xp: 5,
    explanation: 'Pattern: n(n+1) → 1×2=2, 2×3=6, 3×4=12, 4×5=20, 5×6=30, 6×7=42.',
  },
  {
    id: 7, subject: 'Reasoning', subjectCode: 'reasoning', difficulty: 'medium',
    question: 'If BOOK = 2-15-15-11, what is the code for DOOR?',
    options: { A: '4-15-15-18', B: '4-14-15-18', C: '3-15-15-18', D: '4-15-14-18' },
    correct_answer: 'A', xp: 10,
    explanation: 'Each letter = its position in alphabet. D=4, O=15, O=15, R=18.',
  },
  {
    id: 8, subject: 'Reasoning', subjectCode: 'reasoning', difficulty: 'hard',
    question: 'A is 7th from left, B is 12th from right. After swap, A is 11th from left. Total students in row?',
    options: { A: '22', B: '23', C: '24', D: '25' },
    correct_answer: 'A', xp: 20,
    explanation: 'After swap A takes B\'s original position (11 from left = 12 from right). Total = 11+12−1 = 22.',
  },
  {
    id: 9, subject: 'Reasoning', subjectCode: 'reasoning', difficulty: 'easy',
    question: 'Which is the odd one out? Apple, Mango, Carrot, Banana',
    options: { A: 'Apple', B: 'Mango', C: 'Carrot', D: 'Banana' },
    correct_answer: 'C', xp: 5,
    explanation: 'Apple, Mango, Banana are fruits. Carrot is a vegetable — the odd one out.',
  },
  {
    id: 10, subject: 'Reasoning', subjectCode: 'reasoning', difficulty: 'medium',
    question: 'A woman says "His mother is the only daughter of my mother." How is she related to him?',
    options: { A: 'Grandmother', B: 'Mother', C: 'Sister', D: 'Aunt' },
    correct_answer: 'B', xp: 10,
    explanation: '"Only daughter of my mother" = the woman herself. So his mother = the woman. She is his Mother.',
  },
  // ENGLISH
  {
    id: 11, subject: 'English', subjectCode: 'english', difficulty: 'easy',
    question: 'Choose the correct synonym of ELOQUENT:',
    options: { A: 'Silent', B: 'Articulate', C: 'Clumsy', D: 'Rude' },
    correct_answer: 'B', xp: 5,
    explanation: 'ELOQUENT means fluent and expressive in speech. ARTICULATE is its closest synonym.',
  },
  {
    id: 12, subject: 'English', subjectCode: 'english', difficulty: 'medium',
    question: 'Choose the correctly spelt word:',
    options: { A: 'Accomodation', B: 'Accommodation', C: 'Accomadation', D: 'Acomodation' },
    correct_answer: 'B', xp: 10,
    explanation: 'Correct spelling: ACCOMMODATION — double "c" and double "m".',
  },
  {
    id: 13, subject: 'English', subjectCode: 'english', difficulty: 'hard',
    question: 'Fill in: "The committee __ unable to reach a consensus."',
    options: { A: 'are', B: 'were', C: 'was', D: 'have been' },
    correct_answer: 'C', xp: 20,
    explanation: '"Committee" is a collective noun taking a singular verb. "Was" is correct.',
  },
  {
    id: 14, subject: 'English', subjectCode: 'english', difficulty: 'easy',
    question: 'Identify the antonym of BENEVOLENT:',
    options: { A: 'Generous', B: 'Kind', C: 'Malevolent', D: 'Charitable' },
    correct_answer: 'C', xp: 5,
    explanation: 'BENEVOLENT = kind and generous. Its antonym is MALEVOLENT = wishing harm.',
  },
  {
    id: 15, subject: 'English', subjectCode: 'english', difficulty: 'medium',
    question: 'Find the error: "Neither of the students have submitted their assignment."',
    options: { A: 'Neither of', B: 'have submitted', C: 'their assignment', D: 'No error' },
    correct_answer: 'B', xp: 10,
    explanation: '"Neither" is singular → correct: "Neither of the students HAS submitted..."',
  },
  // GENERAL AWARENESS
  {
    id: 16, subject: 'General Awareness', subjectCode: 'ga', difficulty: 'easy',
    question: 'Who is known as the "Iron Man of India"?',
    options: { A: 'Jawaharlal Nehru', B: 'Sardar Vallabhbhai Patel', C: 'Subhas Chandra Bose', D: 'Bhagat Singh' },
    correct_answer: 'B', xp: 5,
    explanation: 'Sardar Vallabhbhai Patel unified 562 princely states into the Indian Union, earning this title.',
  },
  {
    id: 17, subject: 'General Awareness', subjectCode: 'ga', difficulty: 'medium',
    question: 'Which Article of the Indian Constitution abolishes untouchability?',
    options: { A: 'Article 14', B: 'Article 15', C: 'Article 17', D: 'Article 21' },
    correct_answer: 'C', xp: 10,
    explanation: 'Article 17 abolishes "untouchability" and forbids its practice in any form.',
  },
  {
    id: 18, subject: 'General Awareness', subjectCode: 'ga', difficulty: 'hard',
    question: 'The Indian Constitution was adopted by the Constituent Assembly on:',
    options: { A: '15 Aug 1947', B: '26 Jan 1950', C: '26 Nov 1949', D: '2 Oct 1948' },
    correct_answer: 'C', xp: 20,
    explanation: 'The Constitution was adopted on 26 November 1949 — celebrated as Constitution Day.',
  },
  {
    id: 19, subject: 'General Awareness', subjectCode: 'ga', difficulty: 'easy',
    question: 'What is the capital of Uttarakhand?',
    options: { A: 'Dehradun', B: 'Haridwar', C: 'Nainital', D: 'Mussoorie' },
    correct_answer: 'A', xp: 5,
    explanation: 'Dehradun is the capital of Uttarakhand. Gairsain is the summer capital.',
  },
  {
    id: 20, subject: 'General Awareness', subjectCode: 'ga', difficulty: 'medium',
    question: 'Which planet is known as the "Red Planet"?',
    options: { A: 'Jupiter', B: 'Saturn', C: 'Venus', D: 'Mars' },
    correct_answer: 'D', xp: 10,
    explanation: 'Mars appears red due to iron oxide (rust) on its surface.',
  },
];

export const dailyQuestions = [
  questions[0],  // Quant easy
  questions[6],  // Reasoning medium
  questions[11], // English easy
  questions[16], // GA easy
  questions[2],  // Quant hard
];

export const leaderboardData = [
  { rank: 1,  name: 'Priya Sharma',   xp: 4850, streak: 42, accuracy: 89, city: 'Delhi',     avatar: 'PS' },
  { rank: 2,  name: 'Amit Kumar',     xp: 4620, streak: 38, accuracy: 85, city: 'Mumbai',    avatar: 'AK' },
  { rank: 3,  name: 'Sneha Patel',    xp: 4410, streak: 35, accuracy: 88, city: 'Ahmedabad', avatar: 'SP' },
  { rank: 4,  name: 'Rohit Verma',    xp: 3980, streak: 29, accuracy: 81, city: 'Lucknow',   avatar: 'RV' },
  { rank: 5,  name: 'Ananya Singh',   xp: 3750, streak: 27, accuracy: 79, city: 'Patna',     avatar: 'AS' },
  { rank: 6,  name: 'Vikram Gupta',   xp: 3520, streak: 24, accuracy: 77, city: 'Jaipur',    avatar: 'VG' },
  { rank: 7,  name: 'Kavya Reddy',    xp: 3290, streak: 22, accuracy: 82, city: 'Hyderabad', avatar: 'KR' },
  { rank: 8,  name: 'Arjun Nair',     xp: 3100, streak: 19, accuracy: 76, city: 'Kochi',     avatar: 'AN' },
  { rank: 9,  name: 'Pooja Mishra',   xp: 2940, streak: 17, accuracy: 74, city: 'Bhopal',    avatar: 'PM' },
  { rank: 10, name: 'Nikhil Jain',    xp: 2780, streak: 15, accuracy: 72, city: 'Surat',     avatar: 'NJ' },
  { rank: 11, name: 'Swati Yadav',    xp: 2560, streak: 14, accuracy: 70, city: 'Agra',      avatar: 'SY' },
  { rank: 12, name: 'Deepak Tiwari',  xp: 2340, streak: 12, accuracy: 68, city: 'Varanasi',  avatar: 'DT' },
  { rank: 13, name: 'Nisha Kumari',   xp: 2100, streak: 11, accuracy: 71, city: 'Ranchi',    avatar: 'NK' },
  { rank: 14, name: 'Rajesh Pandey',  xp: 1890, streak: 9,  accuracy: 66, city: 'Allahabad', avatar: 'RP' },
  { rank: 52, name: 'Rahul Sharma',   xp: 1240, streak: 14, accuracy: 73, city: 'Pune',      avatar: 'RS', isCurrentUser: true },
];

export const badges = [
  { id: 'warrior7',  label: '7-Day Warrior',   icon: '⚔️',  desc: 'Maintained a 7-day streak',     earned: true  },
  { id: 'master30',  label: '30-Day Master',    icon: '👑',  desc: 'Maintained a 30-day streak',    earned: false },
  { id: 'quant',     label: 'Quant Master',     icon: '🔢',  desc: 'Solved 50 Quant questions',     earned: true  },
  { id: 'fast',      label: 'Fast Solver',      icon: '⚡',  desc: 'Solved 10 questions in < 20s',  earned: true  },
  { id: 'accuracy',  label: 'Accuracy King',    icon: '🎯',  desc: '80%+ accuracy for a week',      earned: false },
  { id: 'century',   label: 'Century Club',     icon: '💯',  desc: 'Solved 100 questions total',    earned: false },
];

export const mockUser = {
  id: 1,
  name: 'Rahul Sharma',
  email: 'rahul@example.com',
  xp: 1240,
  current_streak: 14,
  highest_streak: 21,
  total_questions: 287,
  accuracy: 73,
  rank: 52,
  target_exam: 'SSC CGL',
  joined: 'January 2025',
  subjectStats: {
    'Quant':    { accuracy: 68, solved: 89,  total: 130 },
    'Reasoning':{ accuracy: 82, solved: 95,  total: 116 },
    'English':  { accuracy: 71, solved: 63,  total: 89  },
    'GA':       { accuracy: 65, solved: 40,  total: 62  },
  },
};
