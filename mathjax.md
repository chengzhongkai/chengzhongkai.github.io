
# [17.1](http://www.i.u-tokyo.ac.jp/edu/entra/pdf/archive/17math_j.pdf)
[link](http://www.i.u-tokyo.ac.jp/edu/entra/examarchive.shtml)

## Problem 1 
Suppose that three-dimensional vectors $${\begin{pmatrix}x_{n} \\y_{n}\\z_{n}\end{pmatrix} }$$ satisfy the equation 
$$\begin{pmatrix}x_{n+1} \\y_{n+1}\\z_{n+1}\end{pmatrix} =A\begin{pmatrix}x_{n} \\y_{n}\\z_{n}\end{pmatrix} (n=0,1,2,...)$$
where $x_0, y_0, z_0$ and a are real numbers, and
$$ A=\begin{pmatrix}1-2α & α & α \\α & 1-α & 0\\α&0&1-α\end{pmatrix} , 0<α<\frac{1}{3} $$
Answer the following questions.  
(1)	Express $x_n+ y_n+ z_n$ using $x_0, y_0$ and $z_0$ .  
(2)	Obtain the eigenvalues $\lambda_1$, $\lambda_2$ and $\lambda_3$, and their corresponding eigenvectors $v_1$, $v_2$ and $v_3$of the matrix A.  
(3)	Express the matrix A using $\lambda_1$, $\lambda_2$ and $\lambda_3$,$v_1$, $v_2$ and $v_3$.  
(4)	Express $$ \begin{pmatrix}x_{n} \\y_{n}\\z_{n}\end{pmatrix} $$ using $x_0, y_0$ ,$z_0$ and $\alpha$.  
(5) Obtain $$\lim_{n \rightarrow  \infty } \begin{pmatrix}x_{n} \\y_{n}\\z_{n}\end{pmatrix}$$ .  
(6) Regard $$f(x_0,y_0,z_0)=\frac{(x_n,y_n,z_n)\begin{pmatrix}x_{n+1} \\y_{n+1}\\z_{n+1}\end{pmatrix} }{(x_n,y_n,z_n)\begin{pmatrix}x_{n} \\y_{n}\\z_{n}\end{pmatrix} }$$ as a function of $x_0$, $y_0$ and $z_0$.  
Obtain the maximum and the minimum values of $f(x_0,y_0,z_0)$, where we assume that $x_0^2+y_0^2+z_0^2 \neq 0$. 
## Solution 1
(1)
$$
\begin{aligned}
\begin{bmatrix}x_{n+1} \\y_{n+1}\\z_{n+1}\end{bmatrix}&=\begin{bmatrix}1-2a & a & a \\a & 1-a & 0\\a&0&1-a\end{bmatrix} \begin{bmatrix}x_{n} \\y_{n}\\z_{n}\end{bmatrix} 
\\&=\begin{bmatrix}1-2a \\a \\a\end{bmatrix}x_{n} +
 \begin{bmatrix} a  \\ 1-a\\0\end{bmatrix} y_{n}+
 \begin{bmatrix} a \\ 0\\1-a\end{bmatrix} z_{n}
\end{aligned}
$$


$$
\begin{aligned}
x_{n+1} +y_{n+1}+z_{n+1}
 &=(1-2a+a+a)x_{n} +(a+1-a)y_{n}+(a+1-a)z_{n}
 \\& =x_{n} +y_{n}+z_{n}
 \\x_n +y_n+z_n&=x_0 +y_0+z_0
\end{aligned}
$$



(2)
$$
\begin{aligned}
det(A-\lambda I)&=\begin{vmatrix}1-2a-λ & a & a \\a & 1-a-λ & 0\\a&0&1-a-λ \end{vmatrix}
\\&=(1-2α-λ)( 1-α-λ)^2-2α^2(1-α-λ)
\\&=( 1-α-λ)[(1-2α-λ)( 1-α-λ)-2α^2]
\\&=( 1-α-λ)[(1-α-λ-a)( 1-α-λ)-2α^2]
\\&=( 1-α-λ)[( 1-α-λ)^2-a(1-α-λ)-2α^2]
\\&=( 1-α-λ)[( 1-α-λ)-2a][( 1-α-λ)+a]
\\&=( 1-α-λ)( 1-3α-λ)( 1-λ)
\end{aligned}
$$

$λ=( 1,1-α,1-3α)$

$λ=1:(A-I)x$
$$
=\begin{bmatrix}-2a & a & a \\a & -a & 0\\a&0&-a \end{bmatrix}\begin{bmatrix} x  \\ y\\z\end{bmatrix} 
=\begin{bmatrix} 0 \\ 0\\0 \end{bmatrix} $$
$v_1=k(1,1,1)$
$$k = \sqrt{1^2+1^2+1^2}=\sqrt{3} $$
$v_1=(1/\sqrt{3} ,1/\sqrt{3} ,1/\sqrt{3} )$


$λ=1-\alpha:(A-(1-\alpha)I)x$
$$
=\begin{bmatrix}1-2a-(1-\alpha) & a & a \\a & 1-a-(1-\alpha) & 0\\a&0&1-a-(1-\alpha) \end{bmatrix}\begin{bmatrix} x  \\ y\\z\end{bmatrix} $$
$$
=\begin{bmatrix}-\alpha & a & a \\a & 0 & 0\\a&0&0 \end{bmatrix}\begin{bmatrix} x  \\ y\\z\end{bmatrix} 
=\begin{bmatrix} 0 \\ 0\\0 \end{bmatrix} $$
$v_2=(0,1,-1)=(0,\frac{1}{\sqrt{2}}  ,-\frac{1}{\sqrt{2}} )$


$λ=1-3\alpha:(A-(1-3\alpha)I)x$
$$
=\begin{bmatrix}1-2a-(1-3\alpha) & a & a \\a & 1-a-(1-3\alpha) & 0\\a&0&1-a-(1-3\alpha) \end{bmatrix}\begin{bmatrix} x  \\ y\\z\end{bmatrix} $$
$$
=\begin{bmatrix}\alpha & a & a \\a & 2\alpha & 0\\a&0&2\alpha \end{bmatrix}\begin{bmatrix} x  \\ y\\z\end{bmatrix} 
=\begin{bmatrix} 0 \\ 0\\0 \end{bmatrix} $$
$v_3=(2,-1,-1)=(1,-\frac{1}{2}  ,-\frac{1}{2} )$
(3)
$$A =S\Lambda S^{-1}$$
$$A = 
\begin{bmatrix}v_1 & v_2 & v_3 \end{bmatrix}
\begin{bmatrix}\lambda_1& 0 & 0 \\0 & \lambda_2 & 0\\0&0&\lambda_3\end{bmatrix}
\begin{bmatrix}v_1 & v_2 & v_3 \end{bmatrix}^{-1}$$
$$A = 
\begin{bmatrix}1 & 0 & 2 \\1 & -1 & -1\\1&1&-1\end{bmatrix}
\begin{bmatrix}1 & 0 & 0 \\0 & 1-\alpha & 0\\0&0&1-3\alpha\end{bmatrix}
\begin{bmatrix}1 & 0 & 2 \\1 & -1 & -1\\1&1&-1\end{bmatrix}^{-1}$$
$$A = 
\begin{bmatrix}1 & 0 & 2 \\1 & -1 & -1\\1&1&-1\end{bmatrix}
\begin{bmatrix}1 & 0 & 0 \\0 & 1-\alpha & 0\\0&0&1-3\alpha\end{bmatrix}
\begin{bmatrix}\frac{1}{3} & \frac{1}{3}  & \frac{1}{3}  \\0 & -\frac{1}{2}  & \frac{1}{2} \\\frac{1}{3} &-\frac{1}{6} &-\frac{1}{6} \end{bmatrix}$$

(4)	$$ \begin{pmatrix}x_{n} \\y_{n}\\z_{n}\end{pmatrix}= 
\begin{bmatrix}1 & 0 & 2 \\1 & -1 & -1\\1&1&-1\end{bmatrix}
\begin{bmatrix}1 & 0 & 0 \\0 & (1-\alpha)^n & 0\\0&0&(1-3\alpha)^n\end{bmatrix}
\begin{bmatrix}\frac{1}{3} & \frac{1}{3}  & \frac{1}{3}  \\0 & -\frac{1}{2}  & \frac{1}{2} \\\frac{1}{3} &-\frac{1}{6} &-\frac{1}{6} \end{bmatrix} \begin{pmatrix}x_0\\y_0\\z_0\end{pmatrix}$$

(5)   
$$
\begin{aligned}
\lim_{n \rightarrow  \infty } 
\begin{pmatrix}x_{n} \\y_{n}\\z_{n}\end{pmatrix}
&=\lim_{n \rightarrow  \infty } \begin{bmatrix}1 & 0 & 2 \\1 & -1 & -1\\1&1&-1\end{bmatrix}
\begin{bmatrix}1 & 0 & 0 \\0 & (1-\alpha)^n & 0\\0&0&(1-3\alpha)^n\end{bmatrix}
\begin{bmatrix}\frac{1}{3} & \frac{1}{3}  & \frac{1}{3}  \\0 & -\frac{1}{2}  & \frac{1}{2} \\\frac{1}{3} &-\frac{1}{6} &-\frac{1}{6} \end{bmatrix} \begin{pmatrix}x_0\\y_0\\z_0\end{pmatrix}
\\&=\begin{bmatrix}1 & 0 & 2 \\1 & -1 & -1\\1&1&-1\end{bmatrix}
\begin{bmatrix}1 & 0 & 0 \\0 & 0 & 0\\0&0&0\end{bmatrix}
\begin{bmatrix}\frac{1}{3} & \frac{1}{3}  & \frac{1}{3}  \\0 & -\frac{1}{2}  & \frac{1}{2} \\\frac{1}{3} &-\frac{1}{6} &-\frac{1}{6} \end{bmatrix} \begin{pmatrix}x_0\\y_0\\z_0\end{pmatrix}
\\&=\begin{bmatrix}\frac{1}{3} & \frac{1}{3}  & \frac{1}{3}  \\ \frac{1}{3} & \frac{1}{3}  & \frac{1}{3}  \\ \frac{1}{3} & \frac{1}{3}  & \frac{1}{3}  \end{bmatrix} \begin{pmatrix}x_0\\y_0\\z_0\end{pmatrix}
\\&=\begin{pmatrix}\frac{x_0+y_0+z_0}{3}\\ \frac{x_0+y_0+z_0}{3}\\ \frac{x_0+y_0+z_0}{3}\end{pmatrix}
\end{aligned}
$$
