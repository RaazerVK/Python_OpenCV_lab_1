import cv2

# Запускаем вебку
cap = cv2.VideoCapture(0)

# Определяем кодек и создаем объект VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

# Отображаем дисплей
while True:
    ret, frame = cap.read()
    if ret:
        #Конвертируем все наши кадры в серый для последующей записи
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Пишем кадры в видео
        out.write(gray_frame)

        # рамка
        cv2.imshow('Webcam', gray_frame)

        #Можно прерывать по нажатию ESC
        # if cv2.waitKey(1) & 0xFF == 27:
        # Прерываем цикл по нажатию q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# "Освобождаем камеру" и закрываем все окна
cap.release()
out.release()
cv2.destroyAllWindows()

