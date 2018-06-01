In general, we use upper case letters to denote constants, such as $C, K, M, N, T$, etc. We use lower case letters as dummy indexes of the appropriate range, such as $c=1:C$ to index classes, $i=1:M$ to index data cases, $j=1:N$ to index input features, $k=1:K$ to index states or clusters, $t=1:T$ to index time, etc.

We use $x$ to represent an observed data vector. In a supervised problem, we use $y$ or ${y}$ to represent the desired output label. We use ${z}$ to represent a hidden variable. Sometimes we also use $q$ to represent a hidden discrete variable.


Symbol|Meaning

$C$ | Number of classes
$D$ | Dimensionality of data vector (number of features)
$N$ | Number of data cases
$N_c$ | Number of examples of class $c$,$N_c=\sum_{i=1}^{N}\mathbb{I}(y_i=c)$
$R$ | Number of outputs (response variables)
$\mathcal{D}$ | Training data $\mathcal{D}=\left\{({x}_i,y_i) | i=1:N\right\}$
$\mathcal{D}_{test}$ | Test data
$\mathcal{X}$ | Input space
$\mathcal{Y}$ | Output space
$K$ | Number of states or dimensions of a variable (often latent)
$k(x,y)$ | Kernel function
${K}$ | Kernel matrix
$\mathcal{H}$ | Hypothesis space
$L$ | Loss function 
$J({\theta})$ | Cost function
$f({x})$ | Decision function
$P(y|{x})$ | Conditional probability
$\lambda$ | Strength of $\ell_2$ or $\ell_1 regularizer$
$\phi(x)$ | Basis function expansion of feature vector ${x}$
$\Phi$ | Basis function expansion of design matrix ${X}$
$q()$ | Approximate or proposal distribution
$Q({\theta},{\theta}_{old})$ | Auxiliary function in EM
$T$ | Length of a sequence
$T(\mathcal{D})$ | Test statistic for data
${T}$ | Transition matrix of Markov chain
${\theta}$ | Parameter vector
${\theta}^{(s)}$ | $s$'th sample of parameter vector
$\hat{{\theta}}$ | Estimate (usually MLE or MAP) of ${\theta}$
$\hat{{\theta}}_{MLE}$ | Maximum likelihood estimate of ${\theta}$
$\hat{{\theta}}_{MAP}$ | MAP estimate of ${\theta}$
$\bar{{\theta}}$ | Estimate (usually posterior mean) of  ${\theta}$
${w}$ | Vector of regression weights (called ${\beta}$ in statistics)
b | intercept (called $\varepsilon$ in statistics)
${W}$ | Matrix of regression weights
$x_{ij}$ | Component (i.e., feature) $j$ of data case $i$ ,for $i=1:N ,j=1:D$
${x}_i$ | Training case, $i=1:N$
${X}$ | Design matrix of size $N \times D$
$\bar{{x}}$ | Empirical mean $\bar{{x}}=\dfrac{1}{N}\sum_{i=1}^{N} {x}_i$
$\tilde{{x}}$ | Future test case
${x}_*$ | Feature test case
${y}$ | Vector of all training labels ${y} =(y_1,...,y_N)$
$z_{ij}$ | Latent component $j$ for case $i$
