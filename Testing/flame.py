# Copyright 2019 The University of Texas at Austin
#
# For licensing information see
#                http://www.cs.utexas.edu/users/flame/license.html
#
# Programmed by: Name of author
#                Email of author

# import flame
import numpy as np


def Dot_unb(alpha, x, y):

    xT, \
        xB = flame.part_2x1(x,
                            0, 'TOP')

    yT, \
        yB = flame.part_2x1(y,
                            0, 'TOP')

    while xT.shape[0] < x.shape[0]:

        x0,   \
            chi1, \
            x2 = flame.repart_2x1_to_3x1(xT,
                                         xB,
                                         1, 'BOTTOM')

        y0,   \
            psi1, \
            y2 = flame.repart_2x1_to_3x1(yT,
                                         yB,
                                         1, 'BOTTOM')

        #------------------------------------------------------------#

        alpha = chi1 * psi1 + alpha;

        #------------------------------------------------------------#

        xT, \
            xB = flame.cont_with_3x1_to_2x1(x0,
                                            chi1,
                                            x2,
                                            'TOP')

        yT, \
            yB = flame.cont_with_3x1_to_2x1(y0,
                                            psi1,
                                            y2,
                                            'TOP')

x = np.array()
print(Dot_unb(0,x,y))
