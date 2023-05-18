import wave

def estereo2mono(ficEste, ficMono, canal = 2):
    # Lee el fichero ficEste y lo guarda en la variable wav_in
    wav_in = wave.open(ficEste, 'rb')

    #Obtener los parámetros del archivo de entrada
    params = wav_in.getparams()

    #Comprovamos que el archivo de entrada és estéreo
    if params.nchannels != 2:
        print("El archivo NO es estéreo!!!")
        return

    # Creamos el archivo de salida 
    wav_out = wave.open(ficMono, 'wb')

    # Establecemos los parámetros del archivo de salida
    wav_out.setparams(params)

    # Leemos las muestras del archivo de entrada
    frames = wav_in.readframes(params.nframes)

    #Convertir los datos de las muestras en una lista de enteros
    samples = list(wave.struct.unpack(f"{params.nframes * params.nchannels}h", frames))

    # Crear una lista para almacenar las muestras del canal seleccionado
    mono_samples = []

    # Obtener las muestras del canal seleccionado
    if canal == 0:
        # Canal Izquierdo
        mono_samples = samples[::2]
    elif canal == 1:
        # Canal Derecho
        mono_samples = samples[1::2]
    elif canal == 2:
        # Semisuma (L+R)/2
        for i in range(0, len(samples), 2):
            mono_samples.append((samples[i] + samples[i + 1]) // 2)
            