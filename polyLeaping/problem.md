Paul the polygon leaper is practicing his polygon leaping skills. He stands on the top side of a convex polgyon (i.e. no dips, so it could be a square/pentagon/hexagon, etc), and the polygon starts spinning. While in the air, Paul is able to jump $j$ faces clockwise from the current side he is on of the polygon. 

Given a convex polygon with $n$ sides, and being able to leap $j$ faces at a time, determine how many faces of the polygon Paul did not land on when he returns to the side that he started on.

For example, if $n$ is 4 and $j$ is 2:
![image](https://s3.amazonaws.com/hr-assets/0/1602272768-c76093a756-square2.png)

The sides on the left and right in this picture are never hit, so the answer 2 (2 sides were never hit.)

As another example: $n$ is 5 and $j$ is 4:

![image](https://s3.amazonaws.com/hr-assets/0/1602274245-a155f8f5fa-smallerPentagons.png)

Paul landed on every side before coming back to his starting side, so the answer is 0 (0 sides were untouched)

