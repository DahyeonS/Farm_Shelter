#%%
# 패키지 불러오기
import pathlib
import matplotlib.pyplot as plt
from PIL import Image

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#%%
# 전체 데이터 수
data_dir = pathlib.Path("./cheese")
len(list(data_dir.glob('*/*')))

#%%
# 파일 로드
fresh = list(data_dir.glob('fresh/*'))
Image.open(str(fresh[1]))

#%%
# 이미지 크기 설정
batch_size = 32
img_height = 256
img_width = 256

#%%
# 데이터셋 분리(훈련)
train_ds = keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.3,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

#%%
# 데이터셋 분리(검증)
val_ds = keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.3,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

#%%
# 라벨 추출
class_names = train_ds.class_names
print(class_names)

#%%
# 모델링 전 시각화
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")

#%%
# 전처리 레이어 생성
normalization_layer = tf.keras.layers.Rescaling(
    1./255, input_shape=(img_height, img_width, 3))

#%%
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal_and_vertical"),
    layers.RandomRotation(0.2),
])

#%%
# 모델링 성능 개선
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

#%%
# 모델링
num_classes = len(class_names)

model = tf.keras.Sequential([
  normalization_layer,
  data_augmentation,
  tf.keras.layers.Conv2D(16, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(2),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(2),
  tf.keras.layers.Conv2D(64, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  layers.Dropout(0.4),
  tf.keras.layers.Dense(num_classes)
])

#%%
model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

#%%
# 모델 적용
epochs = 20
history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)

#%%
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(1, epochs+1)

plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

#%%
test_ds = keras.utils.image_dataset_from_directory(
  data_dir,
  image_size=(img_height, img_width),
  batch_size=batch_size)

#%%
model.summary()

#%%
model.evaluate(test_ds) # loss: 0.5024 - accuracy: 0.8083

#%%
model.save('cheese.h5')