ball_1 = int(input("1-talabaning ballini kiriting: "))
ball_2 = int(input("2-talabaning ballini kiriting: "))
ball_3 = int(input("3-talabaning ballini kiriting: "))
ball_4 = int(input("4-talabaning ballini kiriting: "))
ball_5 = int(input("5-talabaning ballini kiriting: "))

max_ball = max(ball_1, ball_2, ball_3, ball_4, ball_5)
min_ball = min(ball_1, ball_2, ball_3, ball_4, ball_5)

print(f'"Eng yuqori ball: {max_ball}", "Eng past ball: {min_ball}"')