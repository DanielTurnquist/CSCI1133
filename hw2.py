import turtle, platform, math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

# cents
#==========================================
# Purpose:
#   Computes the total number of cents in US currency
# Input Parameter(s):
#   quarters - the number of quarters
#   dimes - the number of dimes
#   nickels - the number of nickels
#   pennies - the number of pennies
# Return Value:
#   The combined number of cents
#==========================================

def cents(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters*25
    total += dimes*10
    total += nickels*5
    total += pennies
    return total

# draw_M
#==========================================
# Purpose:
#   Draws the UMN 'M' logo in the turtle graphics window
# Input Parameter(s):
#   None
# Return Value:
#   None
#==========================================

def draw_M():
    turtle.delay(0)
    turtle.bgcolor("gold")
    turtle.hideturtle()
    turtle.color("maroon")
    turtle.penup()
    turtle.setpos(-200,-100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(14)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(128)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(14)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(28)
    turtle.right(60)
    turtle.forward(140)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(140)
    turtle.right(60)
    turtle.forward(28)
    turtle.left(90)
    turtle.forward(64)
    turtle.end_fill()

# Part B: star8
#==========================================
# Purpose:
#   Draws an 8-pointed star in turtle graphics window
# Input Parameter(s):
#   None
# Return Value:
#   None
#==========================================

def star8():
    turtle.forward(150)
    turtle.left(135)
    turtle.forward(150)
    turtle.left(135)
    turtle.forward(150)
    turtle.left(135)
    turtle.forward(150)
    turtle.left(135)
    turtle.forward(150)
    turtle.left(135)
    turtle.forward(150)
    turtle.left(135)
    turtle.forward(150)
    turtle.left(135)
    turtle.forward(150)
    turtle.left(135)


# Part C: trajectory
#==========================================
# Purpose:
#   prints the initial horizontal speed, initial vertical speed, and flight time of ball
# Input Parameter(s):
#    height - initial height at which the ball is thrown in meters
#    speed - initial speed at which the ball is thrown in meters/second
#    angle - angle at which the ball is thrown relative to the horizontal ground plane in degrees
# Return Value:
#   Distance traveled by ball
#==========================================

def trajectory(height, speed, angle):
    horz_speed = speed * math.cos(angle * math.pi / 180)
    print("Horizontal Speed:", round(horz_speed, 3), "m/s" )

    vert_speed = speed * math.sin(angle * math.pi / 180)
    print("Vertical Speed:", round(vert_speed, 3), "m/s")

    flight_time = (vert_speed + (math.sqrt(vert_speed ** 2 + 19.6 * height))) / 9.8
    print("Flight Time:", round(flight_time, 3), "s")
    
    return round(horz_speed * flight_time, 3)
