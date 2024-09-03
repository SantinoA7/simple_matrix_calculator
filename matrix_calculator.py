# import streamlit as st

# # st.title('Matriz Identidad 3x3')

# # Mostrar la matriz identidad usando LaTeX
# # st.latex(r'\begin{pmatrix}1 & 0 & 2 \\0 & 1 & 0 \\0 & 0 & 1\end{pmatrix}')
# # Título de la página
# import streamlit as st

# # Función para crear una grilla de entradas de texto
# def create_grid(rows, cols, key_prefix):
#     grid = []
#     for i in range(rows):
#         col_elements = st.columns(cols)
#         row = []
#         for j in range(len(col_elements)):
#             row.append(col_elements[j].text_input(f'{key_prefix} pos. {i+1},{j+1}', key=f'{key_prefix}_input_{i}_{j}'))
#         grid.append(row)
#     return grid

# # Título de la página
# st.title('Página de Operaciones Matriciales')

# # Crear dos columnas para las grillas
# col1, col2 = st.columns(2)

# # Primera grilla
# with col1:
#     st.subheader('Primera Grilla')
#     rows1 = st.number_input('Filas', min_value=1, max_value=3, value=3, key='rows1')
#     cols1 = st.number_input('Columnas', min_value=1, max_value=3, value=3, key='cols1')
#     create_grid(rows1, cols1, ' ')

# # Segunda grilla
# with col2:
#     st.subheader('Segunda Grilla')
#     rows2 = st.number_input('Filas', min_value=1, max_value=3, value=3, key='rows2')
#     cols2 = st.number_input('Columnas', min_value=1, max_value=3, value=3, key='cols2')
#     create_grid(rows2, cols2, '')

# # Botones de operaciones
# st.subheader('Operaciones')
# if st.button('Sumar'):
#     st.write('Has seleccionado Sumar')
# if st.button('Restar'):
#     st.write('Has seleccionado Restar')
# if st.button('Multiplicar'):
#     st.write('Has seleccionado Multiplicar')
# if st.button('Dividir'):
#     st.write('Has seleccionado Dividir')





import streamlit as st

# Función para crear una grilla de entradas de texto
def create_grid(rows, cols, key_prefix):
    grid = []
    for i in range(rows):
        col_elements = st.columns(cols)
        row = []
        for j in range(len(col_elements)):
            row.append(col_elements[j].text_input(f'{key_prefix} pos. {i+1},{j+1}', key=f'{key_prefix}_input_{i}_{j}'))
        grid.append(row)
    return grid

# Función para verificar si todas las casillas están llenas
def all_fields_filled(grid):
    for row in grid:
        for cell in row:
            if not cell or len(cell) > 7:
                return False
    return True

# Función para las operaciones
def operation():
    st.latex(r'\begin{pmatrix}1 & 0 & 2 \\0 & 1 & 0 \\0 & 0 & 1\end{pmatrix}')

# Título de la página
st.title('Página de Operaciones Matriciales')

# Crear dos columnas para las grillas
col1, col2 = st.columns(2)

# Primera grilla
with col1:
    st.subheader('Primera Grilla')
    rows1 = st.number_input('Filas', min_value=1, max_value=3, value=3, key='rows1')
    cols1 = st.number_input('Columnas', min_value=1, max_value=3, value=3, key='cols1')
    grid1 = create_grid(rows1, cols1, 'grid1')

# Segunda grilla
with col2:
    st.subheader('Segunda Grilla')
    rows2 = st.number_input('Filas', min_value=1, max_value=3, value=3, key='rows2')
    cols2 = st.number_input('Columnas', min_value=1, max_value=3, value=3, key='cols2')
    grid2 = create_grid(rows2, cols2, 'grid2')

# Botones de operaciones
st.subheader('Operaciones')
col3, col4, col5, col6 = st.columns(4)

with col3:
    if st.button('Sumar', disabled=not (all_fields_filled(grid1) and all_fields_filled(grid2))):
        operation()
with col4:
    if st.button('Restar', disabled=not (all_fields_filled(grid1) and all_fields_filled(grid2))):
        operation()
with col5:
    if st.button('Multiplicar', disabled=not (all_fields_filled(grid1) and all_fields_filled(grid2))):
        operation()
with col6:
    if st.button('Dividir', disabled=not (all_fields_filled(grid1) and all_fields_filled(grid2))):
        operation()
