We use boldface lower-case to denote vectors, such as $\vec{x}$, and boldface upper-case to denote matrices, such as $\vec{X}$. We denote entries in a matrix by non-bold upper case letters, such as $X_{ij}$. 

Vectors are assumed to be column vectors, unless noted otherwise. We use $(x_1,\cdots,x_D)$ to denote a column vector created by stacking $D$ scalars. If we write $\vec{X}=(\vec{x}_1,\cdots,\vec{x}_n)$, where the left hand side is a matrix, we mean to stack the $\vec{x}_i$ along the columns, creating a matrix. 


Symbol|Meaning
--|--
$X \succ 0$ | $X$ is a positive definite matrix
$tr(X)$ | Trace of a matrix
$det(X)$ | Determinant of matrix $X$|
$\lvert X \rvert$ | Determinant of matrix $X$|
$X^{-1}$ | Inverse of a matrix|
$X^{\dagger}$ | Pseudo-inverse of a matrix|
$X^T$ | Transpose of a matrix|
$x^T$ | Transpose of a vector|
$\mathrm{diag}(x)$ | Diagonal matrix made from vector $x$|
$\mathrm{diag}(X)$ | Diagonal vector extracted from matrix ${X}$|
$I$ or $I_d$ | Identity matrix of size $d \times d$ (ones on diagonal, zeros of)|
$\vec{1}$ or $\vec{1}_d$ | Vector of ones (of length $d$)|
$\vec{0}$ or $\vec{0}_d$ | Vector of zeros (of length $d$)|
$\lvert\lvert\vec{x}\rvert\rvert=\lvert\lvert\vec{x}\rvert\rvert_2$ | Euclidean or $\ell_2$ norm $\sqrt{\sum\limits_{j=1}^{d} x_j^2}$|
$\lvert{\lvert{\vec{x}}}_1\rvert\rvert$ | $\ell_1$ norm $\sum\limits_{j=1}^{d} \lvert{x_j}\rvert$|
${X}_{:,j}$ | j'th column of matrix|
${X}_{i,:}$ | transpose of $i$'th row of matrix (a column vector)|
${X}_{i,j}$ | Element $(i,j)$ of matrix ${X}$ |
$\vec{x} \otimes \vec{y}$ | Tensor product of $\vec{x}$ and $\vec{y}$|
