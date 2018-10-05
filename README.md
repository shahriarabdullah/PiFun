# PiFun
While messing around with probability stuffs, I figured out an *'exceptional way'* way to find the value of pi. This is what I did-

I drew a circle with a radius of 3 unit (it can be of any other arbitrary length) and constructed a square inscribed in the circle by connecting the vertex of horizontal and vertical diameter.

![Square inscribed in circle](https://github.com/shahriarabdullah/PiFun/blob/master/fig_final.PNG)

The area of the square is-<br/>
<a href="http://www.codecogs.com/eqnedit.php?latex=A_s=(\frac{r}{\sqrt{2}})^2=\frac{r^2}{2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?A_s=(\frac{r}{\sqrt{2}})^2=\frac{r^2}{2}" title="A_s=(\frac{r}{\sqrt{2}})^2=\frac{r^2}{2}" /></a>

<br/>The area of the circle is-<br/>
<a href="http://www.codecogs.com/eqnedit.php?latex=A_c=\pi&space;r^2" target="_blank"><img src="http://latex.codecogs.com/gif.latex?A_c=\pi&space;r^2" title="A_c=\pi r^2" /></a>

<br/>So, if we take a random point inside the circle, the probability of the point lying inside the square will be-<br/>
<a href="http://www.codecogs.com/eqnedit.php?latex=P=\frac{A_s}{A_c}=\frac{r^2/2}{\pi&space;r^2}=\frac{1}{2\pi}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?P=\frac{A_s}{A_c}=\frac{r^2/2}{\pi&space;r^2}=\frac{1}{2\pi}" title="P=\frac{A_s}{A_c}=\frac{r^2/2}{\pi r^2}=\frac{1}{2\pi}" /></a>

<br/>Which yields-<br/>
<a href="http://www.codecogs.com/eqnedit.php?latex=\pi=P/2" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\pi=P/2" title="\pi=P/2" /></a>
<br/>

I wrote a tiny program in python to generate millions of random points and tested the above approach practically and the results were so close to the actual value of pi. It was so amazing to see a real life approach to calculate pi!

Later I came to know, estimating the value of pi in a similar approach I used existed prior to my 'invention' and known as **Monte Carlo simulation**. The only difference is, the mentioned method uses a circle inscribed in a square rather than using a square inscribed in circle which obviously requires less labour to conduct the test. Nonetheless, it was really fun to figure out such a way to calculate pi.
