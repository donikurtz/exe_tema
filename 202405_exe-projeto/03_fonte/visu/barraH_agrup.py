import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import ceil

def plot_barraHagrup(df,var,num_cols):
    sns.set(style="white")


    # Lista de todas as colunas que deseja plotar
    todas_colunas = df.dtypes[(df.dtypes == 'object')&(df.dtypes.index != 'customerID')&(df.dtypes.index != var)].index

    max_categories = 0
    for colunas in todas_colunas:
        max_categories = max(df[colunas].nunique(),max_categories)

    # Criando a figura e os subplots (eixos) com duas linhas e três colunas
    fig, ax = plt.subplots(nrows=ceil(len(todas_colunas)/num_cols), ncols=num_cols, figsize=(15, 15))

    # Iterando sobre todas as colunas e criando um gráfico para cada uma
    for i, coluna in enumerate(todas_colunas):
        row = i // num_cols  # Determina a linha atual
        col = i % num_cols   # Determina a coluna atual

        df_cat = pd.DataFrame(index=df[var].value_counts().index)

        for categ in df[coluna].unique():
            df_cat = df_cat.join(pd.DataFrame(df[var][df[coluna]==categ].value_counts(normalize=True))).rename(columns={'proportion':categ})

        df_melted = df_cat.reset_index().melt(id_vars=var, var_name='cat', value_name='Proportion')

        cate = (df[coluna].nunique() / max_categories) * 0.8
        sns.barplot(data=df_melted, y=var, x='Proportion', hue='cat', orient='h', ax=ax[row, col], width=cate)

        # Obtendo a altura de cada barra, que é necessária para calcular a posição y do texto
        bar_height = ax[row, col].patches[0].get_height() / 2

        # Loop sobre as barras para adicionar os rótulos de texto
        for bar in ax[row, col].patches:
            # Apenas adicionar texto se a largura da barra (o valor) for maior que zero
            if bar.get_width() > 0:
                # O valor a ser impresso como rótulo
                value = f'{bar.get_width() * 100:.1f}%'.replace('.', ',')
                
                # Coordenadas x e y para o texto
                x = bar.get_width()
                y = bar.get_y() + bar_height
                
                # Adicionando o texto ao gráfico
                ax[row, col].text(x + 0.01, y, value, va='center')

        # Ajustando a legenda
        ax[row, col].legend(title='', loc='lower right')
        ax[row, col].set_xlim(0, 1.5)
        ax[row, col].set_title(coluna)
        ax[row, col].set_ylabel('')
        ax[row, col].set_xlabel('')
        ax[row, col].get_xaxis().set_visible(False)

    # Adicionando um título geral acima de todos os subplots
    fig.suptitle(f'{var} Segmentado pelas Características de Clientes', fontsize=16, fontweight='bold')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Ajusta o layout para dar espaço para o suptitle
    plt.show()