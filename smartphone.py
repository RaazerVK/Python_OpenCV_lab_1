import cv2

# Запускаем вебку

#Вместо cap = cv2.VideoCapture(0) пишем:
cap = cv2.VideoCapture("<camera_url>")
#где <camera_url> URL ссылка на камеру. Правда нужно установить подходящее приложение на телефон.

# Проверяем успешнный захват камеры
if not cap.isOpened():
    print("Не удается получить доступ к камере")
    exit()

# создаем видео из кадров
while True:
    # читаем кадры с камеры
    ret, frame = cap.read()

    # Прерываем цикл, если неправильно захвачен кадр
    if not ret:
        break

    # Отображаем окошко
    cv2.imshow("SmartPhon", frame)

    # Прерываем цикл по нажатию q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# "Освобождаем" камеру и закрываем окна
cap.release()
cv2.destroyAllWindows()
