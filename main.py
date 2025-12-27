import cv2
import numpy as np
import time

largura_min=80 #Largura minima do retangulo
altura_min=80 #Altura minima do retangulo

offset=6 #Erro permitido entre pixel  

# Posição da linha de contagem será calculada dinamicamente baseada na altura do frame
pos_linha_ratio = 0.6  # 60% da altura do frame

detec = []
carros = 0

def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

# Tentar inicializar captura de vídeo da câmera
# Tentar diferentes backends e índices de câmera
cap = None
camera_index = 0
max_cameras = 3

# Lista de backends para tentar (em ordem de preferência)
backends = [
    (cv2.CAP_DSHOW, "DSHOW"),
    (cv2.CAP_MSMF, "MSMF"),
    (cv2.CAP_ANY, "ANY")
]

print("Tentando inicializar a câmera...")
print("Testando diferentes backends e índices de câmera...")

# Tentar diferentes índices de câmera e backends
for idx in range(max_cameras):
    for backend_id, backend_name in backends:
        try:
            print(f"  Tentando índice {idx} com backend {backend_name}...")
            cap = cv2.VideoCapture(idx, backend_id)
            
            if cap.isOpened():
                # Tentar configurar buffer menor para evitar problemas
                cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
                
                # Dar tempo para a câmera inicializar
                time.sleep(0.5)
                
                # Testar se consegue ler frames (tentar várias vezes)
                ret = False
                test_frame = None
                for attempt in range(5):
                    ret, test_frame = cap.read()
                    if ret and test_frame is not None:
                        break
                    time.sleep(0.2)
                
                if ret and test_frame is not None:
                    camera_index = idx
                    print(f"✓ Câmera encontrada no índice {idx} com backend {backend_name}!")
                    break
                else:
                    print(f"  × Câmera no índice {idx} abriu mas não consegue ler frames")
                    cap.release()
                    cap = None
            else:
                cap = None
        except Exception as e:
            print(f"  × Erro ao tentar índice {idx} com {backend_name}: {e}")
            if cap:
                cap.release()
            cap = None
        
        if cap is not None and cap.isOpened():
            break
    
    if cap is not None and cap.isOpened():
        break

if cap is None or not cap.isOpened():
    print("\n❌ Erro: Não foi possível encontrar ou acessar nenhuma câmera!")
    print("\nSoluções possíveis:")
    print("  1. Verifique se a câmera está conectada e ligada")
    print("  2. Feche outros programas que possam estar usando a câmera (Skype, Teams, Zoom, etc.)")
    print("  3. Verifique as permissões de câmera nas configurações do Windows")
    print("  4. Tente reiniciar o computador")
    print("  5. Verifique se os drivers da câmera estão instalados corretamente")
    exit()

# Configurar propriedades da câmera (tentar, mas não falhar se não funcionar)
print("Configurando propriedades da câmera...")
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Buffer menor para reduzir latência
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30)

# Aguardar um pouco para a câmera estabilizar
print("Aguardando câmera estabilizar (isso pode levar alguns segundos)...")
for i in range(15):  # Ler mais frames para estabilizar
    ret, _ = cap.read()
    if ret:
        print(f"  Frame {i+1}/15 lido com sucesso")
    time.sleep(0.2)

# Criar o objeto de subtração de fundo
subtracao = cv2.createBackgroundSubtractorMOG2()

print("Câmera inicializada! Pressione ESC para sair.")

while True:
    ret, frame1 = cap.read()
    
    # Verificar se o frame foi lido corretamente
    if not ret:
        print("Aviso: Não foi possível ler o frame. Tentando reconectar...")
        cap.release()
        time.sleep(0.5)
        # Tentar reconectar com diferentes backends
        for backend_id, backend_name in backends:
            cap = cv2.VideoCapture(camera_index, backend_id)
            if cap.isOpened():
                cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
                ret, test_frame = cap.read()
                if ret:
                    print(f"Reconectado com sucesso usando {backend_name}")
                    break
                else:
                    cap.release()
                    cap = None
        if cap is None or not cap.isOpened():
            print("Erro: Não foi possível reconectar à câmera!")
            break
        continue
    
    # Obter dimensões do frame
    altura_frame, largura_frame = frame1.shape[:2]
    pos_linha = int(altura_frame * pos_linha_ratio)
    
    # Processar o frame
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
    contorno, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Desenhar linha de detecção (dinâmica baseada na largura do frame)
    cv2.line(frame1, (25, pos_linha), (largura_frame - 25, pos_linha), (255, 127, 0), 3)
    
    for (i, c) in enumerate(contorno):
        (x, y, w, h) = cv2.boundingRect(c)
        validar_contorno = (w >= largura_min) and (h >= altura_min)
        if not validar_contorno:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 0, 255), -1)

        for (x, y) in detec:
            if y < (pos_linha + offset) and y > (pos_linha - offset):
                carros += 1
                cv2.line(frame1, (25, pos_linha), (largura_frame - 25, pos_linha), (0, 127, 255), 3)
                detec.remove((x, y))
                print("Veículo detectado: " + str(carros))

    # Ajustar posição do texto baseado na largura do frame
    text_x = max(50, int(largura_frame / 2 - 200))
    cv2.putText(frame1, "VEHICLE COUNT : " + str(carros), (text_x, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    
    cv2.imshow("Video Original", frame1)
    cv2.imshow("Detectar", dilatada)

    # Pressionar ESC para sair
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
print("Programa encerrado. Total de veículos contados: " + str(carros))
