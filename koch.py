# Python program to print complete Koch Curve. 
import turtle

t = turtle.Turtle()
t.shape("turtle")  
t.pen(pencolor='dark violet')
  
# function to create koch snowflake or koch curve 
def snowflake(lengthSide, levels): 
    if levels == 0: 
        t.forward(lengthSide) 
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1) 
    t.left(60) 
    snowflake(lengthSide, levels-1) 
    t.right(120) 
    snowflake(lengthSide, levels-1) 
    t.left(60) 
    snowflake(lengthSide, levels-1) 
  
# main function 
if __name__ == "__main__": 
    # defining the speed of the turtle 
    t.speed(9999)                    
    length = 300.0   
            
    t.penup()                      
  
    t.backward(length/2.0) 
          
    t.pendown()            
    for i in range(3):     
        snowflake(length, 4) 
        t.right(120) 
   