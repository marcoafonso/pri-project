### Page Rank Exercise

## Evaluations Exercise
### Ter em conta que:

## Algoritmo PageRank:

#### - E[u,v]= 1 se o link de u para v existir, caso contrario e 0

### - $`N_u = \sum_{v} E[u,v] `$ 

### - $`\rho_{0}[v] = initial\ prestige\ vector`$

### - $`\rho_{i+1}[v] =\frac{d}{N}+(1-d) \sum_{(u,v)\in E} \frac{ \rho_i\ [u]}{N_u} `$

### 5.2)

![](./graph.PNG)

**1º calcular $`N_u`$**:

$`N_A = A->B+A->C+A->D= 1+0+1=2`$

$`N_B = B->A+B->C+B->D= 0+1+1=2`$

$`N_C = C->A+C->B+C->D= 0+0+1=1`$

$`N_D = D->A+D->B+D->C+D->A= 0+0+0=0`$

**2º calcular $`\rho_{0}[v]`$**

$`\rho_{0}[A]=\frac{1}{numero\ de\ paginas}=\frac{1}{4}`$

$`\rho_{0}[B]=\frac{1}{numero\ de\ paginas}=\frac{1}{4}`$

$`\rho_{0}[C]=\frac{1}{numero\ de\ paginas}=\frac{1}{4}`$

$`\rho_{0}[D]=\frac{1}{numero\ de\ paginas}=\frac{1}{4}`$

**Nesta altura ja temos uma tabela deste genero**

|i |     A          |      B          |     C           |      D           |
|--|----------------|-----------------|-----------------|------------------|
|-1|$`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$  |

**1ªiteracao para i=0**

### - $`\rho_{1}[A] =\frac{0.1}{4}+(1-0.1) \sum_{(u,A)\in E} \frac{ \rho_0\ [u]}{N_u}=\frac{0.1}{4}+(1-0.1)0=\frac{0.1}{4}=0.025 `$ o sumatorio e zero pq nao existe links de u para A.

### - $`\rho_{1}[B] =\frac{0.1}{4}+(1-0.1) \sum_{(u,B)\in E} \frac{ \rho_0\ [u]}{N_u}=\frac{0.1}{4}+(1-0.1)*(\frac{\rho_0\ [A]}{N_A})=\frac{0.1}{4}+(1-0.1)*(\frac{\frac{1}{4}}{2})=0.1375 `$

### - $`\rho_{1}[C] =\frac{0.1}{4}+(1-0.1) \sum_{(u,C)\in E} \frac{ \rho_0\ [u]}{N_u} =\frac{0.1}{4}+(1-0.1) (\frac{ \rho_0\ [B]}{N_B})=\frac{0.1}{4}+(1-0.1)*(\frac{\frac{1}{4}}{2})=0.1375`$

### - $`\rho_{1}[D] =\frac{0.1}{4}+(1-0.1) \sum_{(u,D)\in E} \frac{ \rho_0\ [u]}{N_u} =\frac{0.1}{4}+(1-0.1) (\frac{ \rho_0\ [A]}{N_A}+\frac{ \rho_0\ [B]}{N_B}+\frac{ \rho_0\ [C]}{N_C})=\frac{0.1}{4}+(1-0.1)*(\frac{\frac{1}{4}}{2}+\frac{\frac{1}{4}}{2}+\frac{\frac{1}{4}}{1})=0.475`$

**Nesta altura temos uma tabela deste genero**

|i |     A          |      B          |     C           |      D           |
|--|----------------|-----------------|-----------------|------------------|
|-1|$`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$  |
|0 |     0.025      |     0.1375      |       0.1375    |      0.475       |

**1ªiteracao para i=1**

### - $`\rho_{2}[A] =\frac{0.1}{4}+(1-0.1) \sum_{(u,A)\in E} \frac{ \rho_1\ [u]}{N_u}=\frac{0.1}{4}+(1-0.1)0=\frac{0.1}{4}=0.025 `$ o sumatorio e zero pq nao existe links de u para A.

### - $`\rho_{2}[B] =\frac{0.1}{4}+(1-0.1) \sum_{(u,B)\in E} \frac{ \rho_1\ [u]}{N_u}=\frac{0.1}{4}+(1-0.1)*(\frac{\rho_1\ [A]}{N_A})=\frac{0.1}{4}+(1-0.1)*(\frac{0.025}{2})=0.03625 `$

### - $`\rho_{2}[C] =\frac{0.1}{4}+(1-0.1) \sum_{(u,C)\in E} \frac{ \rho_1\ [u]}{N_u} =\frac{0.1}{4}+(1-0.1) (\frac{ \rho_1\ [B]}{N_B})=\frac{0.1}{4}+(1-0.1)*(\frac{0.1375}{2})=0.086875`$

### - $`\rho_{2}[D] =\frac{0.1}{4}+(1-0.1) \sum_{(u,D)\in E} \frac{ \rho_1\ [u]}{N_u} =\frac{0.1}{4}+(1-0.1) (\frac{ \rho_1\ [A]}{N_A}+\frac{ \rho_1\ [B]}{N_B}+\frac{ \rho_1\ [C]}{N_C})=\frac{0.1}{4}+(1-0.1)*(\frac{0.025}{2}+\frac{0.1375}{2}+\frac{0.1375}{1})=0.221875`$

**Nesta altura temos uma tabela deste genero**

|i |     A          |      B          |     C           |      D           |
|--|----------------|-----------------|-----------------|------------------|
|-1|$`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$  |
|0 |     0.025      |     0.1375      |       0.1375    |      0.475       |
|1 |     0.025      |     0.03625     |       0.086875  |      0.221875    |

**3ªiteracao para i=2**

### - $`\rho_{3}[A] =\frac{0.1}{4}+(1-0.1) \sum_{(u,A)\in E} \frac{ \rho_2\ [u]}{N_u}=\frac{0.1}{4}+(1-0.1)0=\frac{0.1}{4}=0.025 `$ o valor mantem-se.

### - $`\rho_{3}[B] =\frac{0.1}{4}+(1-0.1) \sum_{(u,B)\in E} \frac{ \rho_2\ [u]}{N_u}=\frac{0.1}{4}+(1-0.1)*(\frac{\rho_2\ [A]}{N_A})=\frac{0.1}{4}+(1-0.1)*(\frac{0.025}{2})=0.03625 `$ o valor mantem-se.

### - $`\rho_{3}[C] =\frac{0.1}{4}+(1-0.1) \sum_{(u,C)\in E} \frac{ \rho_2\ [u]}{N_u} =\frac{0.1}{4}+(1-0.1) (\frac{ \rho_2\ [B]}{N_B})=\frac{0.1}{4}+(1-0.1)*(\frac{0.03625}{2})=0.0413125`$

### - $`\rho_{3}[D] =\frac{0.1}{4}+(1-0.1) \sum_{(u,D)\in E} \frac{ \rho_2\ [u]}{N_u} =\frac{0.1}{4}+(1-0.1) (\frac{ \rho_2\ [A]}{N_A}+\frac{ \rho_2\ [B]}{N_B}+\frac{ \rho_2\ [C]}{N_C})=\frac{0.1}{4}+(1-0.1)*(\frac{0.025}{2}+\frac{0.03625}{2}+\frac{0.086875}{1})=0.13075`$

**Nesta altura temos uma tabela deste genero**

|i |     A          |      B          |     C           |      D           |
|--|----------------|-----------------|-----------------|------------------|
|-1|$`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$  |
|0 |     0.025      |     0.1375      |       0.1375    |      0.475       |
|1 |     0.025      |     0.03625     |       0.086875  |      0.221875    |
|2 |     0.025      |     0.03625     |       0.0413125 |      0.13075     |

**4ªiteracao para i=3**

### - $`\rho_{4}[A] =\frac{0.1}{4}+(1-0.1) \sum_{(u,A)\in E} \frac{ \rho_3\ [u]}{N_u}=\frac{0.1}{4}+(1-0.1)0=\frac{0.1}{4}=0.025 `$ o valor mantem-se.

### - $`\rho_{4}[B] =\frac{0.1}{4}+(1-0.1) \sum_{(u,B)\in E} \frac{ \rho_3\ [u]}{N_u}=\frac{0.1}{4}+(1-0.1)*(\frac{\rho_3\ [A]}{N_A})=\frac{0.1}{4}+(1-0.1)*(\frac{0.025}{2})=0.03625 `$ o valor mantem-se.

### - $`\rho_{4}[C] =\frac{0.1}{4}+(1-0.1) \sum_{(u,C)\in E} \frac{ \rho_3\ [u]}{N_u} =\frac{0.1}{4}+(1-0.1) (\frac{ \rho_3\ [B]}{N_B})=\frac{0.1}{4}+(1-0.1)*(\frac{0.03625}{2})=0.0413125`$ o valor mantem-se.

### - $`\rho_{4}[D] =\frac{0.1}{4}+(1-0.1) \sum_{(u,D)\in E} \frac{ \rho_3\ [u]}{N_u} =\frac{0.1}{4}+(1-0.1) (\frac{ \rho_3\ [A]}{N_A}+\frac{ \rho_3\ [B]}{N_B}+\frac{ \rho_3\ [C]}{N_C})=\frac{0.1}{4}+(1-0.1)*(\frac{0.025}{2}+\frac{0.03625}{2}+\frac{0.0413125}{1})=0.086875`$

**Nesta altura temos uma tabela deste genero**

|i |     A          |      B          |     C           |      D           |
|--|----------------|-----------------|-----------------|------------------|
|-1|$`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$ | $`\frac{1}{4}`$  |
|0 |     0.025      |     0.1375      |       0.1375    |      0.475       |
|1 |     0.025      |     0.03625     |       0.086875  |      0.221875    |
|2 |     0.025      |     0.03625     |       0.0413125 |      0.13075     |
|3 |     0.025      |     0.03625     |       0.0413125 |      0.086875    |

**5ªiteracao para i=4**

Ja nao entra pois mais nenhum valor vai mudar! 
