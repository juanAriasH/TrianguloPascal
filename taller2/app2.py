from flask import Flask, render_template, redirect, request
contador = 1
app = Flask(__name__)


def pascal(n):
    vector = [[1],[1,1]]

    for i in range(1,n):
        linea = [1]

        for j in range(0,len(vector[i])-1):
            linea.extend([vector[i][j] + vector[i][j+1]])
            
        linea += [1]
        vector.append(linea)
    return vector


@app.route('/')
def index():
    titulo = "Triangulo de pascal"
    return render_template('index.html', titulo=titulo, titulo_body=titulo)

@app.route('/aumentar', methods=['POST'])
def aumentar():
    global contador
    print("\n -----------------------------------------\n")
    print(" ---->Entró en aumentar")

    if contador < 9 :
        print(" El contador está en:",contador+1,"\n")
        
        res = pascal(contador)

        for i in range(0,len(res)):
            print(res[i])

        contador +=1
        print("\n -----------------------------------------\n")
        return redirect('/')
           
    else:
        print(" ---->Pasó de 9")
        return render_template('reiniciar.html')
     

    
    

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    global contador
    contador = 1
    print("\n -----------------------------------------\n")
    print(" ---->Entró en reiniciar")

    print(" El contador está en:",contador+1,"\n")
    

    print("\n -----------------------------------------\n")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')