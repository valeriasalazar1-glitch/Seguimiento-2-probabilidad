# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:09:20 2026

@author: fjose
"""
import numpy as np 
import pandas as pd 
import scipy.stats as stats
from statsmodels.stats.proportion import proportions_ztest # Prueba de z de proporcines 
from statsmodels.stats.multitest import multipletests #para corrección bonferroni

#%% Para cargar los datos usamos pandas 

data = pd.read_excel('nombre_delarchivo.xlsx')


#%% slicing en un DF 

df1 = df[df["columna"]==1] # esto guardaría en df1 todos los datos del df donde la columan llamnada 'columna' sea 1

df1 = df[df["columna"]<=28]# esto guardaría en df1 todos los datos del df donde la columan llamnada 'columna' sea menor o igual a 28
#%% Z de proporciones
"""
 exitos: número de éxitos
 n: número de ensayos 
 proportion: proporcion a corroborar 
 dirección: string para la dirección de la prueba: "two-sided", "larger", "smaller"
"""

exitos =?
n= ?
proporion= ?
alternative= ?

stat, p_value = proportions_ztest(count=exitos, nobs=n, value=proportion, alternative='two-sided')

#%% Normalidad 

data = ?

#kolmogorov-smirnov
ks_stat, ks_p = stats.kstest(data, 'norm', args=(np.mean(data), np.std(data)))7
#shapito wilks
shapiro_stat, shapiro_p = stats.shapiro(data)

#%% Transformación box-cox

data=?
transformed_data, lambda_opt = stats.boxcox(data)

#%% Prueba binomial 
"""
exitos: número de éxitos
k: número de ensayos 
prop: proporcion a corroborar  
dirección: string para la dirección de la prueba: "two-sided", "less", "greater“

Result, es una estructura de resultados, el valor_p estaría en result.pvalue

"""
exitos=?
k =?
prop=?
dirección=?


result = stats.binomtest(exitos, n=k, p=prop, alternative=direccion)

#%% Prueba de signos

def sgn_test (before,after,direccion): #Prueba de Signos 
    """
    before: variable antes del tratamiento
    after: variable después del tratamiento, o mediana de comparación
    direccion: dirección de la prueba: "two-sided", "less", "greater"
    """
    #Calcular diferencias
    diff = before - after
    # Contar signos
    signos_positivos = np.sum(diff > 0)
    signos_negativos = np.sum(diff < 0)
    
    # Prueba binomial
    result = stats.binomtest(min(signos_positivos, signos_negativos), n=signos_positivos + signos_negativos, p=0.5, alternative=direccion)
return result.pvalue

#%% prueba wilcoxon compración a la mediana 

data =? 
mediana = ? 

stat, p_value = stats.wilcoxon(data-mediana)




#%% prueba wilcoxon comparación de muestras pareadas
x1 = ?
x2 = ?

stat, p_value = stats.wilcoxon(x1,x2)


#%% prueba t para dos muestras 

datos1 = ? 
datos2 = ?
t_stat, p_value = stats.ttest_ind(datos1, datos2)

#%% prueba t de comparaciones multiples
def t_test_multiple (df,tto,variable): #Prueba T de comparaciones multiples
    """
    df: dataframe, en cada columna debe estar cada variable a comparar 
    tto: string con el nombre de la columna del tratamiento
    variable: string con el nombre de la variable
    
    """    

    valores_unicos = df[tto].unique()#determinar cuales son los tratamientos posibles

    # Lista de combinaciones de pares de tratamientos
    comparaciones = list(combinations(valores_unicos, 2))
    p_values = []#lista para almacener los valores P de las comparaciones
    
    for g1, g2 in comparaciones:#extraer los datos a comparar en cada iteracion
        # Extraer datos de cada grupo
        datos1 = df[df[tto] == g1][variable]
        datos2 = df[df[tto] == g2][variable]
        
        # Prueba t para muestras independientes para cada par
        t_stat, p_value = stats.ttest_ind(datos1, datos2)
        p_values.append(p_value)
        print(f"Comparación {g1} vs {g2}: t={t_stat:.4f}, p={p_value:.4f}")
    
    # Aplicar corrección de Bonferroni
    p_corrected = multipletests(p_values, method='bonferroni')[1]
    
    print("\nP-valores corregidos con Bonferroni:")
    for i, (g1, g2) in enumerate(comparaciones):
        print(f"{g1} vs {g2}: p-corrected = {p_corrected[i]:.4f}")
#%% Prueba t de una muestra 
data = ? 
mu = ?

t_stat, p_value = stats.ttest_1samp(data, mu)


#%% Prueba U de Mann Withney 
    """
    datos1: muestra 1 a comparar
    datos 2: muestra 2 a comparar
    direccion: dirección de la prueba: "two-sided", "less", "greater"
    """
datos1 = ?
datos2 =?
direction = ?

stat,p_value=stats.mannwhitneyu(datos1,datos2,alternative=direction)

#%% Homocedasticidad 
var1 = ? 
var2 = ?

#Bartlett

bartlett_stat, bartlett_p = stats.bartlett(var1, var2)



#Levene
levene_stat, levene_p = stats.levene(var1, var2)

