#!/usr/bin/env python
# coding: utf-8

# # I used the reference provided to draw the ellipse. Then I connected it's two focii by a dotted line and I also drew lines that pass through the focii. Since the number of ellipses were passed as input, i tried implementing the first draw ellipse code but then the direction of ellipses were coming same , so I wrote the second draw_ellipse function and did the required code changes in there. I pass the co-ordinates of the focii and a constant (c) as input to function . The code for drawing line that passes through the focii has been included in the draw_ellipse() function itself. 

# In[1]:


import numpy as np
import random
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # first try

# In[54]:


def draw_ellipse(num, focus1, focus2, c):
    
    count = 0
    a1 = focus1[0]
    b1 = focus1[1]
    a2 = focus2[0]
    b2 = focus2[1]
    while num:
        if count >= 1:
            h = random.randrange(2,5)
            v = random.randrange(4,7)
            a1 = a1 + h
            b1 = b1 + v
            a2 = a2 + h
            b2 = b2 + v
#             c = c + 1


        a = c / 2
        x0 = (a1 + a2)/2
        y0 = (b1 + b2)/2

        f = np.sqrt((a1 - x0)**2 + (b1 - y0)**2)
        b = np.sqrt(a**2 - f**2)
        phi = np.arctan2((b2 - b1), (a2 - a1))

        resolution = 1000
        t = np.linspace(0, 2*np.pi, resolution)
        x = x0 + a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
        y = y0 + a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)

        # Plot ellipse
        plt.plot(x, y)

        # Show focii
        plt.plot(a1, b1, 'bo')
        plt.plot(a2, b2, 'bo')
        #plot line connecting two foci
        x_ = []
        x_.append(a1)
        x_.append(a2)
        y_ = []
        y_.append(b1)
        y_.append(b2)

        for i in range(0, len(x_), 2):
            plt.plot(x_[i:i+2], y_[i:i+2], 'ro-')
        num = num -1
        count = count + 1


# In[55]:


if __name__ == "__main__" :
#     plt.xlim((-20, 20))
#     plt.ylim((-20, 20))
    # set the axis
#     ax = plt.gca()
#     # Move left y-axis and bottim x-axis to centre, passing through (0,0)
#     ax.spines['left'].set_position('center')
#     ax.spines['bottom'].set_position('center')

    # Eliminate upper and right axes
#     ax.spines['right'].set_color('none')
#     ax.spines['top'].set_color('none')
    
    draw_ellipse(5, [0,2], [6,7], 9)
#     plt.axis('equal')

    


# # second try

# In[52]:


def draw_ellipse(focus1, focus2, c):
    
    
    a1 = focus1[0]
    b1 = focus1[1]
    a2 = focus2[0]
    b2 = focus2[1]

# semi major axis
    a = c / 2
#    center x-value
    x0 = (a1 + a2) / 2
    print('x0: ', x0)
    
    # Center y-value
    y0 = (b1 + b2) / 2
    print('y0: ', y0)
# Distance from center to focus
    f = np.sqrt((a1 - x0)**2 + (b1 - y0)**2)
    # Distance from center to focus
    # check validness
    if a**2 - f**2 < 0:
        print('{} is less than {}'.format(a, f))
        print("please input a valid C value")
        return False
    # Semiminor axis
    b = np.sqrt(a**2 - f**2)
    # Angle between major axis and x-axis
    # Parametric plot in t
    phi = np.arctan2((b2 - b1), (a2 - a1))
    
    resolution = 1000
    t = np.linspace(0, 2*np.pi, resolution)
    x = x0 + a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
    y = y0 + a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)
    # Plot ellipse
    plt.plot(x, y)
    # Show foci
    point_x, point_y = [[a1, a2]], [[b1, b2]]
    for i in range(len(point_x)):
        plt.plot(point_x[i], point_y[i], linewidth=1.0, linestyle='--')
        plt.scatter(point_x[i], point_y[i], color='black')
   
        
#     plot intersecting line
    p = np.linspace(-10, 10, 1000)
    q = np.linspace(0, 0, 1000)
#     if a > b:
#     print(q + b)
#     if a1==0 or a2 == 0:
    plt.plot(q + a1, p, 'b') 
    plt.plot(q+ a2, p, 'g')
#     else : 
    plt.plot(p + a2, q, 'r') 
    
    
    finalX = [a1,x0]
    finalY = [b1,0]
    for i in range(len(finalX)):
        plt.plot(finalX[i], finalY[i], linewidth=1.0)
#         plt.scatter(finalX[i], finalY[i], color='black')
    
#         num = num -1
#         count = count + 1


# In[53]:


if __name__ == "__main__" :
    plt.xlim((-15, 15))
    plt.ylim((-15, 15))
#     set the axis
    ax = plt.gca()
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

#     Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    plt.grid()
    
    draw_ellipse([2,0], [6,7], 9)
    draw_ellipse([0,3], [3,0], 8)


# In[ ]:




