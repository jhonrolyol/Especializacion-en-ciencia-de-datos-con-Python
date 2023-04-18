import numpy as np
def poisson_process(val_lambda,val_t):
    val_0 = np.random.exponential(1/val_lambda,1)[0]
    W_t = val_0
    rng_valx = list([0,val_0])
    while W_t <= val_t:
    val = np.random.exponential(1/val_lambda,1)[0]
    W_t += val
    if W_t <= val_t: rng_valx.append(val)
    rng_ejex = list(np.cumsum(rng_valx))
    N_t = len(rng_ejex)
    rng_ejey = list(np.arange(N_t))
    rng_ejey.append(N_t-1)
    rng_ejex.append(val_t)
    print('Cantidad de realizaciones : ',N_t-1)
    print('Tiempos de interllegadas : ',np.round(rng_ejex[1:-1],3))
    plt.step(x=rng_ejex,y=rng_ejey,where='post',color='blue')
    plt.title('Proceso de poisson (lambda = ' + str(val_lambda) + ')',
    fontdict={'fontname': 'Times New Roman', 'fontsize': 19}, y=1.03)
    plt.ylim(0)
    plt.ylabel('N(t)')
    plt.xlim([0,val_t])
    plt.show()
