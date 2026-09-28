import requests
import streamlit as st


st.title("Conversor de unidades")
unidades = {
    "Moedas": ["USD", "EUR", "BRL"],
    "Temperatura": ["Celsius", "Fahrenheit", "Kelvin"],
    "Distância": ["Metros", "Quilômetros", "Milhas"],
}
option = st.radio(
    "Escolha o que deseja converter:", list(unidades.keys()), horizontal=True
)
col1, col2 = st.columns(2)
origem = col1.selectbox("Escolha a unidade de origem:", unidades[option])
destino = col2.selectbox("Escolha a unidade de destino:", unidades[option])

match option:
    case "Moedas":
        valor = st.number_input("Digite o valor a ser convertido:")
        if st.button("Converter"):
            if origem == destino:
                st.warning("Escolha moedas diferentes para conversão.")
            else:
                url = f"https://economia.awesomeapi.com.br/json/last/{origem}-{destino}"
                response = requests.get(url)
                data = response.json()
                taxa = float(data[f"{origem}{destino}"]["bid"])
                resultado = valor * taxa
                st.metric(
                    f"{valor} {origem} é igual a:", f"{resultado:.2f} {destino}"
                )

    case "Temperatura":
        valor = st.number_input("Digite o valor a ser convertido:")
        if st.button("Converter"):
            if origem == destino:
                st.warning("Escolha unidades diferentes para conversão.")
            else:
                if origem == "Celsius":
                    if destino == "Fahrenheit":
                        resultado = (valor * 9 / 5) + 32
                    elif destino == "Kelvin":
                        resultado = valor + 273.15
                elif origem == "Fahrenheit":
                    if destino == "Celsius":
                        resultado = (valor - 32) * 5 / 9
                    elif destino == "Kelvin":
                        resultado = (valor - 32) * 5 / 9 + 273.15
                elif origem == "Kelvin":
                    if destino == "Celsius":
                        resultado = valor - 273.15
                    elif destino == "Fahrenheit":
                        resultado = (valor - 273.15) * 9 / 5 + 32
                st.metric(
                    f"{valor} {origem} é igual a:", f"{resultado:.2f} {destino}"
                )

    case "Distância":
        valor = st.number_input("Digite o valor a ser convertido:")
        if st.button("Converter"):
            if origem == destino:
                st.warning("Escolha unidades diferentes para conversão.")
            else:
                if origem == "Metros":
                    if destino == "Quilômetros":
                        resultado = valor / 1000
                    elif destino == "Milhas":
                        resultado = valor / 1609.34
                elif origem == "Quilômetros":
                    if destino == "Metros":
                        resultado = valor * 1000
                    elif destino == "Milhas":
                        resultado = valor / 1.60934
                elif origem == "Milhas":
                    if destino == "Metros":
                        resultado = valor * 1609.34
                    elif destino == "Quilômetros":
                        resultado = valor * 1.60934
                st.metric(
                    f"{valor} {origem} é igual a:", f"{resultado:.2f} {destino}"
                )
